---
title: "폐업으로 버려진 애터미 공기청정기 Home Assistant 로컬 연동 성공기 (Tuya ESP8266 TLS 패치 및 우회)"
date: 2026-08-06T12:00:00+09:00
draft: false
tags: ["Home Assistant", "IoT", "Tuya", "Reverse Engineering", "OpenSSL"]
categories: ["🏠 Smart Home & DIY"]
---

I brought home the Atomy air purifier that was stored at my parents' house. 필터 상태나 하드웨어 자체의 공기 청정 성능은 상당히 괜찮은 편이라 I tried integrating it into my smart home setup for automation.

그런데 전용 앱 접속이 전혀 되지 않아서 애터미 고객센터에 문의해 보니, <b>"해당 앱 개발 및 서버 관리를 담당하던 외주 업체가 폐업하여 더 이상 서비스 지원이 불가능하다"</b>는 답변을 받았습니다. 확인해 보니 이미 iOS 앱스토어에서는 관련 앱이 완전히 내려간 상태였습니다. (안드로이드용 APK 파일만 인터넷에서 겨우 구할 수 있는 수준이었습니다.)

멀쩡한 하드웨어를 이대로 방치하거나 버리기엔 너무 아까워서, 아예 순정 클라우드를 끊어버리고 Home Assistant(HA)에 완전히 로컬 방식으로 연동하여 부활시켜 보기로 했습니다. 한 이틀 동안 삽질한 끝에 연동에 성공한 과정을 정리해 둡니다.

---

### 1차 시도: 하드웨어 개조(UART 납땜) 대신 소프트웨어 우회를 선택한 이유

처음에는 기기를 분해해서 메인보드의 <b>UART 시리얼 통신 핀(TX/RX/GND/3V3)</b>에 USB-to-TTL 젠더를 물리고 납땜해서 ESPHome이나 Tasmota 같은 커스텀 펌웨어를 덮어씌울까 생각했습니다.

하지만 시리얼 젠더를 따로 주문하고 택배를 기다리는 시간도 걸리고, 당장 오늘 밤에 바로 연동해보고 싶다는 마음이 컸습니다. 굳이 멀쩡한 보드를 분해해서 납땜하는 번거로운 과정을 거치기보다는, 기존 하드웨어를 그대로 유지하면서 소프트웨어적으로 제어권을 가져오는 무납땜 방식을 시도해 보기로 했습니다.

---

### 2차 시도: APK Reverse Engineering과 히든 API 발견

우선 구해낸 애터미 스마트홈 안드로이드 앱 APK 파일을 JADX 디컴파일러를 활용하여 앱 내부의 통신 로직을 Reverse Engineering해 보았습니다.

소스코드를 분석해 보니 공기청정기 내부 칩셋은 <b>Tuya계열 ESP8266</b>을 사용하고 있었습니다.  
기기의 Wi-Fi 버튼을 길게 눌러 SoftAP 모드(`Atomy_Air_Purifier`)로 전환하면, 기기 내부 HTTP 웹서버(`192.168.4.1:789`)가 열리며 다음과 같은 숨겨진 RESTful Provisioning API 3개가 작동한다는 것을 발견했습니다.

```text
1. MQTT Broker 주소 지정: http://192.168.4.1:789/setbroker?url=[HA_IP]&port=1885
2. 집 Wi-Fi 정보 주입:    http://192.168.4.1:789/provision?ssid=[SSID]&passwd=[PW]
3. Provisioning 완료 명령: http://192.168.4.1:789/endprovision
```

이 히든 API들을 이용하면 굳이 분해나 납땜을 하지 않고도, 이미 서버가 닫혀버린 애터미 자사 서버 대신 저희 집 내부의 Home Assistant OS IP로 MQTT Broker 주소를 강제 지정해 줄 수 있었습니다.

---

### 통곡의 벽: ESP8266 비표준 TLS 1.2 Handshake 오류

Broker 주소를 HA OS의 IP로 변경하고 기기를 접속시켜 보았는데, HA의 TLS 릴레이 포트에서 패킷을 받자마자 TLS Handshake가 즉시 실패하면서 접속이 튕겨 나갔습니다.

```text
SSL3 alert read:fatal:unexpected message (Alert number 10)
SSL_accept(): error:0A00006E:SSL routines::bad extension
```

#### 원인 분석
1. <b>레거시 Ciphers 요구</b>: ESP8266 칩셋 특성상 구형 Cipher(`AES128-SHA256`)만 지원합니다.
2. <b>TLS Extension 규격 미준수</b>: ESP8266의 펌웨어 TLS 라이브러리가 ClientHello를 송신할 때 `max_fragment_length` Extension 옵션을 TLS 표준 규격(1byte)이 아닌 2byte(`0x00 0x02`)로 송신하고 있었습니다.
3. <b>OpenSSL 3.x의 엄격한 Validation</b>: 최신 Linux 및 HA OS에 탑재된 OpenSSL 3.x 라이브러리는 이를 비표준 비정상 패킷으로 판단하고 즉시 Reject(`bad extension`)을 던지며 세션을 닫아버리는 것이었습니다.

---

### 해결책: OpenSSL 3.6.3 C 소스코드 패치 및 커스텀 Addon 빌드

기기의 펌웨어를 직접 수정할 수는 없었기에, HA OS 측에서 패킷을 받아주는 OpenSSL 라이브러리의 C 소스코드를 직접 다운로드하여 규격 검사 로직을 Bypass하도록 패치하기로 결정했습니다.

OpenSSL 3.6.3 소스코드의 `ssl/statem/extensions_srvr.c` 파일 내 `tls_parse_ctos_maxfragmentlen` 함수 진입부에 조기 정상 승인(`return 1;`)을 반환하도록 Python 패치 스크립트를 작성하여 적용했습니다.

```python
# patch.py - OpenSSL TLS Extension Validation Bypass
path = "/build/openssl/ssl/statem/extensions_srvr.c"
text = open(path).read()

idx = text.find("tls_parse_ctos_maxfragmentlen")
brace = text.find("{", idx)

# 함수 시작 부분에 조기 return 1; 을 주입하여 규격 검사 Bypass
patched = text[:brace+1] + "\n    (void)s; (void)pkt; (void)context; return 1;\n" + text[brace+1:]
open(path, "w").write(patched)
```

---

### 프로토콜 반전: 1분 주기 수치 요청(Polling) 자동화의 발견

통신이 성공한 후 수치가 지속적으로 들어오지 않는 현상이 있어 패킷 구조를 추가 분석해 보았습니다.

알고 보니 이 공기청정기는 센서 수치를 자발적으로 끊임없이 수신하는 스트리밍 방식이 아니라, **앱에서 요청 패킷을 쏘아줄 때만 측정값을 응답하는 '요청-응답 폴링(Polling)' 아키텍처**를 가지고 있었습니다.

따라서 1분마다 `aircleaner/app/[MAC]` 토픽으로 `'{"1":11}'` 데이터 요청 패킷을 수신해 주는 폴링 자동화를 Home Assistant `automations.yaml`에 등록함으로써, 매분 정각 실시간으로 온습도(`27.1°C`, `68.1%`) 및 센서 데이터가 완전하게 수신되는 것을 확인했습니다.

*(참고: PM2.5 센서의 경우 물리 모듈을 제외해 둔 상태여서 `0` 수치가 정상이 들어오는 것이 확인되었으며, 추후 샤오미 호환 레이저 PM2.5 모듈로 교체 시 즉시 실제 미세먼지 수치가 연동되는 구조입니다.)*

---

### 최종 구성 코드 (`configuration.yaml` & `automations.yaml`)

실제 기기 통신을 캡처해서 얻은 진짜 페이로드 구조를 앱 소스코드(`AppDataFrame.Key` 상수)와 대조해 맞춘, 실제로 동작을 검증한 설정입니다.

#### 1. `configuration.yaml` (MQTT 엔티티 정의)
*(주의: `A1B2C3D4E5F6` 자리에 본인 공기청정기의 MAC 주소를 입력하세요)*

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
    - name: "Atomy PM2.5"
      unique_id: atomy_pm25
      state_topic: "aircleaner/device/A1B2C3D4E5F6"
      unit_of_measurement: "µg/m³"
      device_class: pm25
      value_template: "{{ value_json.get('10') if value_json.get('10') is not none else value_json.get('20', {}).get('10') }}"

    - name: "Atomy Temperature"
      unique_id: atomy_temperature
      state_topic: "aircleaner/device/A1B2C3D4E5F6"
      unit_of_measurement: "°C"
      device_class: temperature
      value_template: "{{ value_json.get('13') if value_json.get('13') is not none else value_json.get('20', {}).get('13') }}"

    - name: "Atomy Humidity"
      unique_id: atomy_humidity
      state_topic: "aircleaner/device/A1B2C3D4E5F6"
      unit_of_measurement: "%"
      device_class: humidity
      value_template: "{{ value_json.get('14') if value_json.get('14') is not none else value_json.get('20', {}).get('14') }}"

    - name: "Atomy Air Quality"
      unique_id: atomy_air_quality
      state_topic: "aircleaner/device/A1B2C3D4E5F6"
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

> 값 필드가 `0`일 수 있는 센서(PM2.5 등)는 `or` 대신 `is not none` 체크를 써야 합니다. Jinja의 `or`는 `0`을 "값 없음"으로 취급해서 정상적인 0 수치를 놓치는 버그가 있습니다.

#### 2. `automations.yaml` (1분 센서 폴링 자동화)
기기는 센서값을 자발적으로 보내지 않고, `{"1":11}` (`SENSOR_STATE` 명령) 요청에만 응답합니다. 그래서 이 폴링 자동화가 없으면 센서 엔티티들은 계속 `unknown` 상태로 남습니다.

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

### 마무리 소감

앱 개발사의 폐업으로 스마트 기능이 완전히 죽어버렸던 기기였지만, 굳이 부속을 따로 사서 납땜하거나 분해하는 번거로움 없이 APK Reverse Engineering, OpenSSL 소스 패치, 그리고 1분 주기 수치 요청 자동화로 Home Assistant 로컬 기기로 완벽하게 부활시킬 수 있었습니다.

비록 이틀 정도 시간 소요했지만 HA로 잘 동작하는 걸 보고 있으니 뿌듯하군요 하하.
