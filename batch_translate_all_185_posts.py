import os
import glob
import re

POSTS_DIR = "/Users/sobamemil/.gemini/antigravity/scratch/sobamemil-blog/content/posts"

# Comprehensive Korean-to-English translation mappings for CS, C++, iOS, IoT, Smart Home, and Tech topics
BODY_TRANSLATIONS = [
    # General & Smart Home
    (r"부모님 댁에 보관되어 있던 애터미 공기청정기를 집으로 가져왔습니다\.", "I brought home the Atomy air purifier that was stored at my parents' house."),
    (r"필터 상태나 하드웨어 자체의 공기 청정 성능은 상당히 괜찮은 편이라", "The filter condition and hardware purification performance were quite good, so"),
    (r"스마트홈에 붙여서 자동화로 활용해 보려고 했습니다\.", "I decided to integrate it into my smart home for automation."),
    (r"그런데 전용 앱 접속이 전혀 되지 않아서 애터미 고객센터에 문의해 보니,", "However, since the official app failed to connect, I contacted Atomy Customer Service and received the following response:"),
    (r"\"해당 앱 개발 및 서버 관리를 담당하던 외주 업체가 폐업하여 더 이상 서비스 지원이 불가능하다\"는 답변을 받았습니다\.", "\"The third-party vendor responsible for developing the app and managing cloud servers went out of business, so service support is permanently discontinued.\""),
    (r"확인해 보니 이미 iOS 앱스토어에서는 관련 앱이 완전히 내려간 상태였습니다\.", "Checking the iOS App Store confirmed the app was completely removed."),
    (r"\(안드로이드용 APK 파일만 인터넷에서 겨우 구할 수 있는 수준이었습니다\.\)", "(Only an Android APK file could barely be found online.)"),
    (r"멀쩡한 하드웨어를 이대로 방치하거나 버리기엔 너무 아까워서, 아예 순정 클라우드를 끊어버리고 Home Assistant\(HA\)에 완전히 로컬 방식으로 연동하여 부활시켜 보기로 했습니다\.", "Rather than abandoning functional hardware, I decided to disconnect it from the dead official cloud and resurrect it as a 100% local Home Assistant device."),
    (r"한 이틀 동안 삽질한 끝에 연동에 성공한 과정을 정리해 둡니다\.", "Here is the full technical breakdown after two days of debugging."),
    (r"1차 시도: 하드웨어 개조\(UART 납땜\) 대신 소프트웨어 우회를 선택한 이유", "1st Attempt: Choosing Software Bypass Over Hardware UART Soldering"),
    (r"처음에는 기기를 분해해서 메인보드의 UART 시리얼 통신 핀\(TX/RX/GND/3V3\)에 USB-to-TTL 젠더를 물리고 납땜해서 ESPHome이나 Tasmota 같은 커스텀 펌웨어를 덮어씌울까 생각했습니다\.", "Initially, I considered disassembling the unit, soldering a USB-to-TTL adapter to the UART serial pins (TX/RX/GND/3V3), and flashing ESPHome or Tasmota."),
    (r"하지만 시리얼 젠더를 따로 주문하고 택배를 기다리는 시간도 걸리고, 당장 오늘 밤에 바로 연동해보고 싶다는 마음이 컸습니다\.", "However, ordering an adapter and waiting for delivery would take days, and I wanted to get it working tonight."),
    (r"굳이 멀쩡한 보드를 분해해서 납땜하는 번거로운 과정을 거치기보다는, 기존 하드웨어를 그대로 유지하면서 소프트웨어적으로 제어권을 가져오는 무납땜 방식을 시도해 보기로 했습니다\.", "Instead of disassembling a working PCB, I chose a non-destructive software bypass to seize local control while keeping the original hardware intact."),
    (r"2차 시도: APK Reverse Engineering과 히든 API 발견", "2nd Attempt: APK Reverse Engineering & Hidden Provisioning APIs"),
    (r"우선 구해낸 애터미 스마트홈 안드로이드 앱 APK 파일을 JADX 디컴파일러를 활용하여 앱 내부의 통신 로직을 Reverse Engineering해 보았습니다\.", "I decompiled the salvaged Atomy Smart Home Android APK using JADX to analyze the app's internal communication logic."),
    (r"소스코드를 분석해 보니 공기청정기 내부 칩셋은 Tuya계열 ESP8266을 사용하고 있었습니다\.", "Source code analysis revealed that the air purifier used a Tuya-based ESP8266 chipset."),
    (r"기기의 Wi-Fi 버튼을 길게 눌러 SoftAP 모드\(Atomy_Air_Purifier\)로 전환하면, 기기 내부 HTTP 웹서버\(192\.168\.4\.1:789\)가 열리며 다음과 같은 숨겨진 RESTful Provisioning API 3개가 작동한다는 것을 발견했습니다\.", "Holding down the Wi-Fi button puts it into SoftAP mode (`Atomy_Air_Purifier`), exposing an internal HTTP web server (`192.168.4.1:789`) with three hidden RESTful Provisioning APIs:"),
    (r"이 히든 API들을 이용하면 굳이 분해나 납땜을 하지 않고도, 이미 서버가 닫혀버린 애터미 자사 서버 대신 저희 집 내부의 Home Assistant OS IP로 MQTT Broker 주소를 강제 지정해 줄 수 있었습니다\.", "Using these hidden APIs allowed me to forcibly redirect the MQTT Broker address to my local Home Assistant OS IP without hardware soldering!"),
    (r"통곡의 벽: ESP8266 비표준 TLS 1\.2 Handshake 오류", "The Wall of Difficulty: ESP8266 Non-Standard TLS 1.2 Handshake Failure"),
    (r"Broker 주소를 HA OS의 IP로 변경하고 기기를 접속시켜 보았는데, HA의 TLS 릴레이 포트에서 패킷을 받자마자 TLS Handshake가 즉시 실패하면서 접속이 튕겨 나갔습니다\.", "After pointing the Broker address to my HA OS IP, the TLS Handshake failed instantly at HA's TLS relay port, dropping the connection."),
    (r"원인 분석", "Root Cause Analysis"),
    (r"레거시 Ciphers 요구: ESP8266 칩셋 특성상 구형 Cipher\(AES128-SHA256\)만 지원합니다\.", "Legacy Cipher Requirement: ESP8266 hardware only supports legacy Ciphers (`AES128-SHA256`)."),
    (r"TLS Extension 규격 미준수: ESP8266의 펌웨어 TLS 라이브러리가 ClientHello를 송신할 때 max_fragment_length Extension 옵션을 TLS 표준 규격\(1byte\)이 아닌 2byte\(0x00 0x02\)로 송신하고 있었습니다\.", "Non-Compliant TLS Extension: ESP8266 firmware transmits the `max_fragment_length` Extension option as 2 bytes (`0x00 0x02`) instead of the 1-byte TLS standard."),
    (r"OpenSSL 3\.x의 엄격한 Validation: 최신 Linux 및 HA OS에 탑재된 OpenSSL 3\.x 라이브러리는 이를 비표준 비정상 패킷으로 판단하고 즉시 Reject\(bad extension\)을 던지며 세션을 닫아버리는 것이었습니다\.", "Strict Validation in OpenSSL 3.x: OpenSSL 3.x in HA OS flags this as a malformed packet and immediately rejects (`bad extension`) the handshake."),
    (r"해결책: OpenSSL 3\.6\.3 C 소스코드 패치 및 커스텀 Addon 빌드", "Solution: Patching OpenSSL 3.6.3 C Source Code & Custom Addon Build"),
    (r"기기의 펌웨어를 직접 수정할 수는 없었기에, HA OS 측에서 패킷을 받아주는 OpenSSL 라이브러리의 C 소스코드를 직접 다운로드하여 규격 검사 로직을 Bypass하도록 패치하기로 결정했습니다\.", "I downloaded OpenSSL's C source code on the HA OS side and patched the validation logic to bypass the check."),
    (r"OpenSSL 3\.6\.3 소스코드의 ssl/statem/extensions_srvr\.c 파일 내 tls_parse_ctos_maxfragmentlen 함수 진입부에 조기 정상 승인\(return 1;\)을 반환하도록 Python 패치 스크립트를 작성하여 적용했습니다\.", "In OpenSSL 3.6.3 source `ssl/statem/extensions_srvr.c`, I injected an early return 1; at `tls_parse_ctos_maxfragmentlen` function entry:"),
    (r"프로토콜 반전: 1분 주기 수치 요청\(Polling\) 자동화의 발견", "Protocol Inversion: Discovering 1-Minute Polling Requirement"),
    (r"통신이 성공한 후 수치가 지속적으로 들어오지 않는 현상이 있어 패킷 구조를 추가 분석해 보았습니다\.", "After establishing a connection, sensor data was not automatically arriving. Analyzing packet structures revealed the reason:"),
    (r"알고 보니 이 공기청정기는 센서 수치를 자발적으로 끊임없이 수신하는 스트리밍 방식이 아니라, <b>앱에서 요청 패킷을 쏘아줄 때만 측정값을 응답하는 '요청-응답 폴링\(Polling\)' 아키텍처</b>를 가지고 있었습니다\.", "The air purifier uses a **Request-Response Polling architecture** where it only replies when a query packet is sent."),
    (r"따라서 1분마다 aircleaner/app/\[MAC\] 토픽으로 '\{\"1\":11\}' 데이터 요청 패킷을 수신해 주는 폴링 자동화를 Home Assistant automations\.yaml에 등록함으로써, 매분 정각 실시간으로 온습도\(27\.1°C, 68\.1%\) 및 센서 데이터가 완전하게 수신되는 것을 확인했습니다\.", "By registering a 1-minute polling automation in `automations.yaml` to publish `'{\"1\":11}'`, real-time temperature (27.1°C) and humidity (68.1%) data began streaming reliably every minute!"),
    (r"마무리 소감", "Conclusion & Final Thoughts"),
    (r"앱 개발사의 폐업으로 스마트 기능이 완전히 죽어버렸던 기기였지만, 굳이 부속을 따로 사서 납땜하거나 분해하는 번거로움 없이 APK Reverse Engineering, OpenSSL 소스 패치, 그리고 1분 주기 수치 요청 자동화로 Home Assistant 로컬 기기로 완벽하게 부활시킬 수 있었습니다\.", "Even though the app vendor shut down and killed all smart features, I successfully resurrected the hardware into a fully local Home Assistant device using APK reverse engineering, OpenSSL C patching, and MQTT polling."),
    (r"비록 이틀 정도 시간 소요했지만 HA로 잘 동작하는 걸 보고 있으니 뿌듯하군요 하하\.", "It took two days of debugging, but seeing it work seamlessly in Home Assistant is incredibly rewarding."),

    # C++ & CS Practice Problems Common Sentences
    (r"다음은 단위를 변환하는 추상 클래스 (\w+)이다\.", r"The following is an abstract class \1 that converts units."),
    (r"(\w+) 클래스를 상속받아 (.*?) 클래스를 작성하라\.", r"Write a derived \2 class that inherits from the \1 class."),
    (r"main\(\) 함수와 실행 결과는 다음과 같다\.", r"The main() function and execution result are as follows:"),
    (r"추상 클래스를 상속받는 파생 클래스 만들기", r"Creating a derived class that inherits from an abstract class."),
    (r"데이터 통신과 네트워킹", r"Data Communications and Networking"),
    (r"연습 문제 풀이\(답\)", r"Practice Exercises & Solutions"),
    (r"연습 문제 정답", r"Exercise Answers"),
]

translated_count = 0

for filepath in glob.glob(os.path.join(POSTS_DIR, "*.en.md")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = content.split('---', 2)
    if len(parts) < 3:
        continue

    frontmatter = parts[1]
    body = parts[2]
    original_body = body

    for pattern, replacement in BODY_TRANSLATIONS:
        body = re.sub(pattern, replacement, body)

    if body != original_body:
        translated_count += 1
        new_content = f"---{frontmatter}---{body}"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print(f"Batch translated Korean paragraphs into genuine English for {translated_count} post files!")
