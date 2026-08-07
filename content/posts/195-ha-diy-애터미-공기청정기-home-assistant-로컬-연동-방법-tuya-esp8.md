---
title: "[HA / DIY] 애터미 공기청정기 Home Assistant 로컬 연동 방법 (Tuya ESP8266 TLS 패치 및 우회)"
date: 2026-08-06T16:55:41+09:00
draft: false
categories: ["🏠 스마트홈 & DIY"]
tags: ["ESP8266", "ha", "home assistant", "IOT", "openssl", "스마트홈", "애터미 공기청정기"]
---# 폐업으로 버려진 애터미 공기청정기 Home Assistant 로컬 연동 성공기 (Tuya ESP8266 TLS 패치 및 우회)

부모님 댁에 보관되어 있던 애터미 공기청정기를 집으로 가져왔습니다. 필터 상태나 하드웨어 자체의 공기 청정 성능은 상당히 괜찮은 편이라 스마트홈에 붙여서 자동화로 활용해 보려고 했습니다.

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

```cpp
1. MQTT Broker 주소 지정: http://192.168.4.1:789/setbroker?url=[HA_IP]&port=1885
2. 집 Wi-Fi 정보 주입:    http://192.168.4.1:789/provision?ssid=[SSID]&passwd=[PW]
3. Provisioning 완료 명령: http://192.168.4.1:789/endprovision
```

이 히든 API들을 이용하면 굳이 분해나 납땜을 하지 않고도, 이미 서버가 닫혀버린 애터미 자사 서버 대신 저희 집 내부의 Home Assistant OS IP로 MQTT Broker 주소를 강제 지정해 줄 수 있었습니다.

---

### 통곡의 벽: ESP8266 비표준 TLS 1.2 Handshake 오류

Broker 주소를 HA OS의 IP로 변경하고 기기를 접속시켜 보았는데, HA의 TLS 릴레이 포트에서 패킷을 받자마자 TLS Handshake가 즉시 실패하면서 접속이 튕겨 나갔습니다.

```cpp
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

```cpp
# patch.py - OpenSSL TLS Extension Validation Bypass
path = "/build/openssl/ssl/statem/extensions_srvr.c"
text = open(path).read()

idx = text.find("tls_parse_ctos_maxfragmentlen")
brace = text.find("{", idx)

# 함수 시작 부분에 조기 return 1; 을 주입하여 규격 검사 Bypass
patched = text[:brace+1] + "\n    (void)s; (void)pkt; (void)context; return 1;\n" + text[brace+1:]
open(path, "w").write(patched)
```

디버깅 과정에서 `openssl s_server`를 컨테이너 비대화형 환경에서 테스트할 때 Stdin EOF로 인해 프로세스가 수신 직후 즉시 닫히는 이슈가 있었으나, 파이프 보완 및 `socat` 정적 컴파일을 통해 안정적인 릴레이 바이너리를 생성했습니다.

이 패치된 OpenSSL을 기반으로 Alpine Linux 환경에서 커스텀 Addon(`local_atomy_bridge`) Docker 이미지를 새로 빌드했습니다.

최종 통신 아키텍처는 다음과 같습니다:  
`[공기청정기] --(TLS 1.2 / Port 1885)--> [socat TLS Decryptor] --(Plaintext MQTT / Port 11883)--> [Local Mosquitto] --(Bridge)--> [HA Core]`

---

### 프로토콜 반전: 1분 주기 수치 요청(Polling) 자동화의 발견

통신이 성공한 후 수치가 지속적으로 들어오지 않는 현상이 있어 패킷 구조를 추가 분석해 보았습니다.

알고 보니 이 공기청정기는 센서 수치를 자발적으로 끊임없이 수신하는 스트리밍 방식이 아니라, **앱에서 요청 패킷을 쏘아줄 때만 측정값을 응답하는 '요청-응답 폴링(Polling)' 아키텍처**를 가지고 있었습니다.

따라서 1분마다 `aircleaner/app/[MAC]` 토픽으로 `'{"1":11}'` 데이터 요청 패킷을 수신해 주는 폴링 자동화를 Home Assistant `automations.yaml`에 등록함으로써, 매분 정각 실시간으로 온습도(`27.1°C`, `68.1%`) 및 센서 데이터가 완전하게 수신되는 것을 확인했습니다.

*(참고: PM2.5 센서의 경우 물리 모듈을 제외해 둔 상태여서 `0` 수치가 정상이 들어오는 것이 확인되었으며, 추후 샤오미 호환 레이저 PM2.5 모듈로 교체 시 즉시 실제 미세먼지 수치가 연동되는 구조입니다.)*

---

### 최종 구성 코드 (`configuration.yaml` & `automations.yaml`)

#### 1. `configuration.yaml` (MQTT 엔티티 정의)

```cpp
mqtt:
  fan:
    - name: "Atomy Air Purifier"
      unique_id: atomy_air_purifier_fan
      state_topic: "aircleaner/device/A1B2C3D4E5F6"
      command_topic: "aircleaner/app/A1B2C3D4E5F6"
      value_template: "{{ 'POWER_ON' if value_json['2'] == 1 else 'POWER_OFF' }}"
      payload_on: '{"1":2,"2":1}'
      payload_off: '{"1":2,"2":2}'

  sensor:
    - name: "Atomy PM25"
      unique_id: atomy_pm25
      state_topic: "aircleaner/device/A1B2C3D4E5F6"
      value_template: "{{ value_json['3'] if value_json['3'] is defined else states('sensor.atomy_pm25') }}"
      unit_of_measurement: "µg/m³"
      device_class: pm25

    - name: "Atomy Temperature"
      unique_id: atomy_temperature
      state_topic: "aircleaner/device/A1B2C3D4E5F6"
      value_template: "{{ value_json['4'] if value_json['4'] is defined else states('sensor.atomy_temperature') }}"
      unit_of_measurement: "°C"
      device_class: temperature

    - name: "Atomy Humidity"
      unique_id: atomy_humidity
      state_topic: "aircleaner/device/A1B2C3D4E5F6"
      value_template: "{{ value_json['5'] if value_json['5'] is defined else states('sensor.atomy_humidity') }}"
      unit_of_measurement: "%"
      device_class: humidity
```

#### 2. `automations.yaml` (1분 센서 폴링 자동화)

```cpp
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

### 최종 연동 성공 및 Entities 구성

패치된 Addon이 정상 구동된 상태에서 SoftAP Provisioning을 다시 진행하자, 마침내 TLS Handshake가 완전하게 통과되었습니다.

```cpp
1786000700: New connection from 127.0.0.1:58980 on port 11883.
2026/08/06 07:18:20 socat[9] N SSL connection using AES128-SHA256
1786000700: New client connected from 127.0.0.1 as Client-XXXXXXXXXXXX (p2, c1, k60, u'atomy_bridge').
2026/08/06 07:18:20 socat[9] N write(6, 0x7f1497d0e000, 81) completed
2026/08/06 07:19:05 socat[9] N write(6, 0x7f1497d0e000, 2) completed (PINGREQ Keepalive)
```

로그를 보면 클라이언트명으로 Keepalive 60초(`k60`) 세션이 안정적으로 수립되었으며, 45초 간격으로 PINGREQ/PINGRESP 패킷을 주고받으며 끊김 없이 실시간 Payload 수신 및 제어가 가능해졌습니다.

#### 구성 완료된 Home Assistant Entities (Clean English IDs)

* <b>`fan.atomy_air_purifier`</b>: 전원(ON/OFF) 및 풍량 모드 (Auto / Sleep / Low / Medium / High)
* <b>`sensor.atomy_pm25`</b>: PM2.5 미세먼지 측정값 (µg/m³)
* <b>`sensor.atomy_temperature`</b>: 실내 온도 (°C)
* <b>`sensor.atomy_humidity`</b>: 실내 습도 (%)
* <b>`sensor.atomy_air_quality`</b>: 종합 공기질 상태
* <b>`switch.atomy_child_lock`</b>: Child Lock 스위치

---

### 마무리 소감

앱 개발사의 폐업으로 스마트 기능이 완전히 죽어버렸던 기기였지만, 굳이 부속을 따로 사서 납땜하거나 분해하는 번거로움 없이 APK Reverse Engineering과 C 소스 수준의 OpenSSL 패치로 Home Assistant 로컬 기기로 완벽하게 부활시킬 수 있었습니다.

비록 이틀 정도 시간 소요했지만 HA로 잘 동작하는 걸 보고 있으니 뿌듯하군요 하하

다른 분들도 혹시 앱 서비스가 종료되어 사용하지 못하고 계신 구형 IoT 기기가 있다면, 위와 같은 방식으로 접근해 보시는 것을 추천해 드립니다. HA 애드온 리포지터리 패키지도 만들어 두었으니 필요하신 분들은 활용해 보셔도 좋을 것 같습니다.


](
