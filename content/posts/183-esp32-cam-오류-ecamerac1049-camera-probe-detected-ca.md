---
title: "ESP32-CAM 오류 : [E][camera.c:1049] camera_probe(): Detected camera not supported. [E][camera.c:1249] esp_camera_init(): Camera probe failed with error 0x20004"
date: 2021-05-09T16:37:23+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["AI THINKER", "arduino", "CAM", "esp32", "esp32cam", "스케치", "아두이노", "업로드", "오류", "컴파일"]
---

ESP32-CAM 스케치 작성 및 컴파일 시 아래와 같은 오류가 발생하는 경우가 있습니다.

[E][camera.c:1049] camera\_probe(): Detected camera not supported.  
[E][camera.c:1249] esp\_camera\_init(): Camera probe failed with error 0x20004

저는 WebServerCam 예제를 실행할 때에도 이러한 오류가 발생 하였습니다.

분명 와이파이 id와 password를 올바르게 넣었고, 코드도 예제 코드이므로 오류가 발생할 부분이 없는데 이러한 오류가 발생하여 서버가 올라가지 않는 일이 생겨서 당황스러웠습니다.

저의 해결 방법은  예제 코드의 상단 부분에 주석처리 되어있는 부분 중 CAMERA\_MODEL을 지정해주는 부분에서

#define CAMERA\_MODEL\_WROVER\_KIT // Has PSRAM 이 부분이 주석 해제 되어 있었는데 이 부분을 다시 주석처리 하고

#define CAMERA\_MODEL\_AI\_THINKER // Has PSRAM 이 부분을 주석 해제 해주었더니 정상적으로 동작하였습니다.

해결된 이유를 알려드리면 저는 아두이노 보드에 연결하여 컴파일 및 업로드 한 것이 아니라 ESP32-CAM-MB라는 모듈을 장착하여 컴파일 및 업로드 하였는데, ESP32-CAM-MB 모듈을 장착하여 업로드 하는 경우는 아두이노 보드에 연결하여 업로드 하는 경우와 다르게 설정을 해주어야 한다는 것을 모르고 있었기 때문에 간단하게 CAMERA\_MODEL\_AI\_THINKER를 #define 해줌으로 해결 하였습니다.

공유하기

게시글 관리

**코딩은 내일부터 ;**

[저작자표시 비영리
(새창열림)](https://creativecommons.org/licenses/by-nc/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [시스템 & 임베디드](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/%EC%8B%9C%EC%8A%A4%ED%85%9C%20%26%20%EC%9E%84%EB%B2%A0%EB%94%94%EB%93%9C)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [Cortex-M3 STM32F103R8T6 GPIO 레지스터 종류](/178)  (0) | 2020.07.08 |
| [시스템 프로그래밍 프로젝트 #7 최종 (Assembler in C)](/130)  (2) | 2020.03.19 |
| [시스템 프로그래밍 프로젝트 #1](/22)  (1) | 2020.01.12 |
| [시스템 프로그래밍 프로젝트 #2](/21)  (1) | 2020.01.12 |
| [시스템 프로그래밍 프로젝트 #3](/20)  (1) | 2020.01.12 |
