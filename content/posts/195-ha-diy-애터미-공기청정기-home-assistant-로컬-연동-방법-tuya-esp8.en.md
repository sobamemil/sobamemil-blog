---
title: "[Smart Home / DIY] How to Integrate Atomy Air Purifier into Home Assistant Locally (Tuya ESP8266 TLS Patch & Bypass)"
date: 2026-08-06T16:55:41+09:00
draft: false
categories: ["Smart Home DIY", "Home Assistant IoT"]
tags: ["ESP8266", "Home Assistant", "IoT", "OpenSSL", "Smart Home", "Atomy Air Purifier", "Tuya"]
description: "A complete guide on reviving an abandoned Atomy Air Purifier (AAP-KR19W) into Home Assistant via local Tuya MQTT provisioning and custom OpenSSL TLS patch."
---

# Successful Home Assistant Local Integration for Abandoned Atomy Air Purifier

I recently brought home an Atomy air purifier (`AAP-KR19W`) that was sitting unused at my parents' house. The hardware performance and filter condition were still great, so I decided to integrate it into my Home Assistant smart home setup for automated air quality control.

However, when I tried connecting to its official app, it completely failed. After contacting Atomy Customer Service, I received a surprising response: **"The third-party vendor responsible for developing the app and managing the cloud servers went out of business, so service support is permanently discontinued."** Looking up the app store confirmed that the iOS app was completely removed, with only an unofficial Android APK floating around the internet.

Rather than abandoning functional hardware, I decided to disconnect it from the dead official cloud entirely and resurrect it as a 100% local Home Assistant (HA) device. After two days of deep technical debugging, here is the full story of how I brought it back to life.

---

### 1st Attempt: Choosing Software Bypass Over Hardware UART Soldering

Initially, I considered disassembling the unit, soldering a USB-to-TTL adapter to the mainboard's **UART serial communication pins (TX/RX/GND/3V3)**, and flashing custom firmware like ESPHome or Tasmota.

However, ordering a serial adapter and waiting for delivery would take days, and I wanted to get it working tonight. Instead of disassembling a working PCB and soldering wires, I chose a non-destructive software bypass method to seize local control while keeping the original hardware intact.

---

### 2nd Attempt: APK Reverse Engineering & Hidden Provisioning APIs

I decompiled the salvaged Atomy Smart Home Android APK using the JADX decompiler to analyze the app's internal communication logic.

Source code analysis revealed that the air purifier used a **Tuya-based ESP8266 chipset**.  
Holding down the device's Wi-Fi button puts it into SoftAP mode (`Atomy_Air_Purifier`), exposing an internal HTTP web server (`192.168.4.1:789`) with three hidden RESTful Provisioning APIs:

```cpp
1. Set MQTT Broker Address: http://192.168.4.1:789/setbroker?url=[HA_IP]&port=1885
2. Inject Home Wi-Fi Credentials: http://192.168.4.1:789/provision?ssid=[SSID]&passwd=[PW]
3. Complete Provisioning Command: http://192.168.4.1:789/endprovision
```

Using these hidden APIs allowed me to forcibly redirect the device's MQTT Broker address from the dead Atomy server to my local Home Assistant OS IP without any hardware disassembly or soldering!

---

### The Wall of Difficulty: ESP8266 Non-Standard TLS 1.2 Handshake Failure

After pointing the Broker address to my HA OS IP and attempting a connection, the TLS Handshake failed instantly at HA's TLS relay port, dropping the connection:

```cpp
SSL3 alert read:fatal:unexpected message (Alert number 10)
SSL_accept(): error:0A00006E:SSL routines::bad extension
```

#### Root Cause Analysis

1. **Legacy Cipher Requirement**: Due to ESP8266 hardware constraints, it only supports legacy Ciphers (`AES128-SHA256`).
2. **Non-Compliant TLS Extension**: When the ESP8266 firmware sends a `ClientHello`, it transmits the `max_fragment_length` Extension option as 2 bytes (`0x00 0x02`) instead of the standard 1-byte TLS specification.
3. **Strict Validation in OpenSSL 3.x**: Modern Linux kernels and OpenSSL 3.x in HA OS flag this as a non-standard malformed packet and immediately reject (`bad extension`) the handshake, closing the session.

---

### Solution: Patching OpenSSL 3.6.3 C Source Code & Custom Addon Build

Since I could not modify the device's compiled firmware directly, I decided to download OpenSSL's C source code on the HA OS side and patch the validation logic to bypass the check.

In OpenSSL 3.6.3 source file `ssl/statem/extensions_srvr.c`, I injected an early success return (`return 1;`) at the entry of `tls_parse_ctos_maxfragmentlen`:

```cpp
# patch.py - OpenSSL TLS Extension Validation Bypass
path = "/build/openssl/ssl/statem/extensions_srvr.c"
text = open(path).read()

idx = text.find("tls_parse_ctos_maxfragmentlen")
brace = text.find("{", idx)

# Inject early return 1; at function entry to bypass validation
patched = text[:brace+1] + "\n    (void)s; (void)pkt; (void)context; return 1;\n" + text[brace+1:]
open(path, "w").write(patched)
```

Using this patched OpenSSL binary inside an Alpine Linux container, I built a custom Docker Addon (`local_atomy_bridge`).

The final communication architecture is:  
`[Air Purifier] --(TLS 1.2 / Port 1885)--> [socat TLS Decryptor] --(Plaintext MQTT / Port 11883)--> [Local Mosquitto] --(Bridge)--> [HA Core]`

---

### Protocol Inversion: Discovering 1-Minute Polling Requirement

After establishing a successful connection, sensor data was not automatically arriving. Analyzing packet structures revealed the reason:

The air purifier does **not** stream sensor values continuously. Instead, it uses a **Request-Response Polling architecture** where it only replies when the app sends a query packet.

By registering a 1-minute polling automation in Home Assistant's `automations.yaml` to publish `'{"1":11}'` to `aircleaner/app/[MAC]`, real-time temperature (`27.1°C`), humidity (`68.1%`), and PM1.0/PM2.5/PM10 particle data began streaming reliably every minute! *(Note: The built-in PMS9003M laser sensor accurately reports PM1.0 via DP 11, PM2.5 via DP 10, and PM10 via DP 9. An `expire_after: 120` option was added to correctly mark them as Unavailable when powered off).*

---

### Final Verified Configuration Code (`configuration.yaml` & `automations.yaml`)

#### 1. `configuration.yaml` (MQTT Entity Definitions)

```yaml
mqtt:
  fan:
    - name: "Atomy Air Purifier"
      unique_id: atomy_air_purifier
      state_topic: "aircleaner/device/A1B2C3D4E5F6"
      command_topic: "aircleaner/app/A1B2C3D4E5F6"
      command_template: >-
        {% if value == "ON" %}{"1":2,"2":2}
        {% elif value == "OFF" %}{"1":2,"2":1}
        {% endif %}
      payload_on: "ON"
      payload_off: "OFF"
      state_value_template: >-
        {% set power = value_json.get('2') or (value_json.get('19', {}).get('2')) %}
        {% if power == 2 %}ON{% elif power == 1 %}OFF{% else %}OFF{% endif %}
      preset_modes:
        - "Auto"
        - "Sleep"
        - "Low"
        - "Medium"
        - "High"
      preset_mode_state_topic: "aircleaner/device/A1B2C3D4E5F6"
      preset_mode_value_template: >-
        {% set mode = value_json.get('3') or (value_json.get('19', {}).get('3')) %}
        {% if mode == 1 %}Auto
        {% elif mode == 2 %}Sleep
        {% elif mode == 3 %}Low
        {% elif mode == 4 %}Medium
        {% elif mode == 5 %}High
        {% else %}Auto{% endif %}
      preset_mode_command_topic: "aircleaner/app/A1B2C3D4E5F6"
      preset_mode_command_template: >-
        {% if value == "Auto" %}{"1":3,"3":1}
        {% elif value == "Sleep" %}{"1":3,"3":2}
        {% elif value == "Low" %}{"1":3,"3":3}
        {% elif value == "Medium" %}{"1":3,"3":4}
        {% elif value == "High" %}{"1":3,"3":5}
        {% endif %}

  sensor:
    - name: "Atomy PM1.0"
      unique_id: atomy_pm1_0
      state_topic: "aircleaner/device/A1B2C3D4E5F6"
      unit_of_measurement: "µg/m³"
      device_class: pm1
      expire_after: 120
      value_template: "{{ value_json.get('11') if value_json.get('11') is not none else value_json.get('20', {}).get('11') }}"

    - name: "Atomy PM2.5"
      unique_id: atomy_pm25
      state_topic: "aircleaner/device/A1B2C3D4E5F6"
      unit_of_measurement: "µg/m³"
      device_class: pm25
      expire_after: 120
      value_template: "{{ value_json.get('10') if value_json.get('10') is not none else value_json.get('20', {}).get('10') }}"

    - name: "Atomy PM10"
      unique_id: atomy_pm10
      state_topic: "aircleaner/device/A1B2C3D4E5F6"
      unit_of_measurement: "µg/m³"
      device_class: pm10
      expire_after: 120
      value_template: "{{ value_json.get('9') if value_json.get('9') is not none else value_json.get('20', {}).get('9') }}"

    - name: "Atomy Temperature"
      unique_id: atomy_temperature
      state_topic: "aircleaner/device/A1B2C3D4E5F6"
      unit_of_measurement: "°C"
      device_class: temperature
      expire_after: 120
      value_template: "{{ value_json.get('13') if value_json.get('13') is not none else value_json.get('20', {}).get('13') }}"

    - name: "Atomy Humidity"
      unique_id: atomy_humidity
      state_topic: "aircleaner/device/A1B2C3D4E5F6"
      unit_of_measurement: "%"
      device_class: humidity
      expire_after: 120
      value_template: "{{ value_json.get('14') if value_json.get('14') is not none else value_json.get('20', {}).get('14') }}"

    - name: "Atomy Air Quality"
      unique_id: atomy_air_quality
      state_topic: "aircleaner/device/A1B2C3D4E5F6"
      expire_after: 120
      value_template: >-
        {% set q = value_json.get('27') if value_json.get('27') is not none else value_json.get('20', {}).get('27') %}
        {% if q == 1 %}Good
        {% elif q == 2 %}Moderate
        {% elif q == 3 %}Unhealthy
        {% elif q == 4 %}Hazardous
        {% else %}Unknown{% endif %}

  switch:
    - name: "Atomy Child Lock"
      unique_id: atomy_child_lock
      command_topic: "aircleaner/app/A1B2C3D4E5F6"
      state_topic: "aircleaner/device/A1B2C3D4E5F6"
      payload_on: '{"1":7,"7":2}'
      payload_off: '{"1":7,"7":1}'
      state_on: "ON"
      state_off: "OFF"
      value_template: >-
        {% set lock = value_json.get('7') or value_json.get('19', {}).get('7') %}
        {% if lock == 2 %}ON{% else %}OFF{% endif %}
```

#### 2. `automations.yaml` (1-Minute Sensor Polling Automation)

```yaml
- id: "atomy_air_purifier_poll_sensors"
  alias: "Atomy Air Purifier - Poll Sensor State"
  description: "Requests sensor readings from the Atomy air purifier every minute"
  trigger:
    - platform: time_pattern
      minutes: "/1"
  action:
    - service: mqtt.publish
      data:
        topic: "aircleaner/app/A1B2C3D4E5F6"
        payload: '{"1":11}'
  mode: single
```

---

#### Configured Home Assistant Entities (Clean English IDs)

* <b>`fan.atomy_air_purifier`</b>: Power (ON/OFF) & Speed Modes (Auto / Sleep / Low / Medium / High)
* <b>`sensor.atomy_pm1_0`</b>: PM1.0 Particle Measurement (µg/m³)
* <b>`sensor.atomy_pm25`</b>: PM2.5 Particle Measurement (µg/m³)
* <b>`sensor.atomy_pm10`</b>: PM10 Particle Measurement (µg/m³)
* <b>`sensor.atomy_temperature`</b>: Indoor Temperature (°C)
* <b>`sensor.atomy_humidity`</b>: Indoor Humidity (%)
* <b>`sensor.atomy_air_quality`</b>: Comprehensive Air Quality Status
* <b>`switch.atomy_child_lock`</b>: Child Lock Switch

---

### Conclusion & Final Thoughts

Even though the original app vendor went out of business and killed all smart cloud functionality, I successfully resurrected the hardware into a fully local Home Assistant device using APK reverse engineering, custom OpenSSL C-level patching, and 1-minute MQTT polling—all without needing hardware soldering or disassembly.

If you have legacy IoT devices abandoned by shut-down cloud services, I highly recommend trying this software bypass approach!
