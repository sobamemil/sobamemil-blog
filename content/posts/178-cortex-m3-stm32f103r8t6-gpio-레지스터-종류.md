---
title: "Cortex-M3 STM32F103R8T6 GPIO 레지스터 종류"
date: 2020-07-08T11:55:22+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["Cortex-M3", "embedded", "GPIO", "MCU", "register", "STM32", "마이크로", "임베디드", "입출력포트", "컨트롤러"]
---

이 글에서는 Cortex-M3 STM32F103(STM32F103R8T6)(이하 cortex-m3)의 입출력 포트를 제어하기 위해 필요한 레지스터들의 종류에 대해 알아보겠습니다.

cortex-m3 마이크로컨트롤러는 데이터 출력용 레지스터(GPIOx\_ODR, GPIOx\_BSRR, GPIOx\_BRR)와 데이터 입출력 방향 제어 레지스터(GPIOx\_CRL, GPIOx\_CRH)와 데이터 입력 레지스터(GPIOx\_IDR), 그리고 입출력 값을 고정하는 용도의 레지스터(GPIOx\_LCKR)를 가지고 있고 이들에 대해 간단하게 설명하도록 하겠습니다.

참고로 GPIOx\_... 에서 x는 A~D 사이의 알파벳입니다.

<b>1. GPIOx\_CRL, GPIOx\_CRH (Port Configuration Register Low, Port Configuration Register High)</b>

- 이 레지스터는 입출력의 제어 설정을 하기 위한 레지스터입니다. 이 레지스터는 해당 포트의 입출력 선언 및 각 핀의 동작 모드를 설정할 수 있는데, 그 중 GPIOx\_CRL은 0~7번 핀을 설정하고, GPIOx\_CRH는 8~15번 핀을 설정합니다.

먼저 GPIOx\_CRL의 설정 방법은 아래와 같습니다.

![](https://img.sobamemil.com/posts/178/img_1.png)

GPIOx\_CRL

<b>CNFy[1:0]</b> : Port x configuration bits (y=0 ... 7) (Bits : 31:30, 27:26, 23:22, 19:18, 15:14, 11:10, 7:6, 3:2)

( = 포트 x의 각 비트에 대한 입출력 설정 및 동작모드 설정 비트)

- In input mode (입력 모드 일 때) (MODE[1:0]=00):

    00 : Analog mode

    01 : Floating input (reset state)

    10 : Input with pull-up / pull-down

    11 : Reserved

- In output mode (출력 모드 일 때) (MODE[1:0] > 00):

    00 : General purpose output push-pull

    01 : General purpose output Open-drain

    10 : Alternate function output Push-pull

    11 : Alternate function output Open-drain

<b>MODEy[1:0]</b> : Port x mode bits (y=0 ... 7) (Bits : 29:28, 25:24, 21:20, 17:16, 13:12, 9:8, 5:4, 1:0)

( = 포트 입출력 모드 설정 비트)

    00 : Input mode (reset state) ( = 입력 모드)

    01 : Output mode, max speed 10 MHz. ( = 출력 모드, 최대 동작 속도 10Mhz)

    10 : Output mode, max speed 2 MHz. ( = 출력 모드, 최대 동작 속도 2MHz)

    11 : Output mode, max speed 50 MHz ( = 출력 모드, 최대 동작 속도 50MHz)

그리고 GPIOx\_CRH의 설정 방법은 아래와 같습니다.

![](https://img.sobamemil.com/posts/178/img_2.png)

GPIOx\_CRH

<b>CNFy[1:0]</b> : Port x configuration bits (y= 8 .. 15) (Bits : 31:30, 27:26, 23:22, 19:18, 15:14, 11:10, 7:6, 3:2)

( = 포트 x의 각 비트에 대한 입출력 설정 및 동작모드 설정 비트)

- In input mode (입력 모드 일 때) (MODE[1:0]=00):

    00 : Analog mode

    01 : Floating input (reset state)

    10 : Input with pull-up / pull-down

    11 : Reserved

- In output mode (출력 모드 일 때) (MODE[1:0] > 00):

    00 : General purpose output push-pull

    01 : General purpose output Open-drain

    10 : Alternate function output Push-pull

    11 : Alternate function output Open-drain

<b>MODEy[1:0]</b> : Port x mode bits (y=8 ... 15) (Bits : 29:28, 25:24, 21:20, 17:16, 13:12, 9:8, 5:4, 1:0)

( = 포트 입출력 모드 설정 비트)

    00 : Input mode (reset state) ( = 입력 모드)

    01 : Output mode, max speed 10 MHz. ( = 출력 모드, 최대 동작 속도 10Mhz)

    10 : Output mode, max speed 2 MHz. ( = 출력 모드, 최대 동작 속도 2MHz)

    11 : Output mode, max speed 50 MHz ( = 출력 모드, 최대 동작 속도 50MHz)

<b>2. GPIOx\_IDR (Port Input Data Register)</b>

GPIOx\_IDR은 말 그대로 데이터 입력용 레지스터입니다. 즉, 읽기 전용 레지스터입니다.

포트의 핀 설정이 입력으로 되어있는 경우 PINx 레지스터에 해당하는 값을 읽으면 됩니다. 그러면 포트로부터 입력되는 데이터가 저장됩니다.

GPIOx\_IDR의 설정 방법은 아래와 같습니다.

![](https://img.sobamemil.com/posts/178/img_3.png)

GPIOx\_IDR

<b>IDRy</b> : Port input data (y= 0 .. 15) (Bits : 15:0)

<b>3. GPIOx\_ODR (Port Output Data Register)</b>

GPIOx\_ODR은 데이터를 해당 포트 전체를 통해 출력하기 위한 레지스터입니다. 포트의 핀 설정이 출력으로 되어있는 경우 출력하기 원하는 데이터 값을 GPIOx\_ODR에 넣어주면 됩니다. 이 레지스터는 읽기와 쓰기가 모두 가능합니다.

GPIOx\_ODR의 설정 방법은 아래와 같습니다.

![](https://img.sobamemil.com/posts/178/img_4.png)

GPIOx\_ODR

<b>ODRy</b> : Port output data (y= 0 .. 15) (Bits : 15:0)

<b>4. GPIOx\_BSRR (Port Bit Set/Reset Register)</b>

GPIOx\_BSRR은 제어 포트의 특정 핀만을 set/reset 하기 위한 레지스터이며, write-only 입니다.

GPIOx\_BSRR의 설정 방법은 아래와 같습니다.

![](https://img.sobamemil.com/posts/178/img_5.png)

GPIOx\_BSRR

<b>BRy</b> : Port x Reset bit y (y= 0 .. 15) (Bits : 31:16)

    0 : No action on the corresponding ODRx bit

    1 : Reset the corresponding ODRx bit

<b>BSy</b> : Port x Set bit y (y= 0 .. 15) (Bits : 15:0)

    0 : No action on the corresponding ODRx bit

    1 : Set the corresponding ODRx bit

<b>5. GPIOx\_BRR (Port Bit Reset Register)</b>

GPIOx\_BRR은 제어 포트의 특정 핀만을 reset 하기 위한 레지스터입니다. 또한, GPIOx\_BSRR과 동일하게 write-only 입니다.

GPIOx\_BRR의 설정 방법은 아래와 같습니다.

![](https://img.sobamemil.com/posts/178/img_6.png)

GPIOx\_BRR

<b>BRy</b> : Port x Reset bit y (y= 0 .. 15) (Bits : 15:0)

    0: No action on the corresponding ODRx bit

    1: Reset the corresponding ODRx bit

<b>6. GPIOx\_LCKR (Port Configuration Lock Register)</b>

GPIOx\_LCKR은 포트의 각 핀의 입출력 값을 고정하는 용도의 레지스터입니다.

GPIOx\_LCKR의 설정 방법은 아래와 같습니다.

![](https://img.sobamemil.com/posts/178/img_7.png)

GPIOx\_LCKR

<b>LCKK[16]</b> : Lock key (Bit : 16)

    0: Port configuration lock key not active

    1: Port configuration lock key active. GPIOx\_LCKR register is locked until the next reset.

- LOCK key writing sequence:

    Write 1

    Write 0

    Write 1

    Read 0

    Read 1 (this read is optional but confirms that the lock is active)

<b>LCKy</b> : Port x Lock bit y (y= 0 .. 15) (Bits : 15:0)

    0: Port configuration not locked

    1: Port configuration locked.


[저작자표시 비영리
(새창열림)](https://creativecommons.org/licenses/by-nc/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [시스템 & 임베디드](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/%EC%8B%9C%EC%8A%A4%ED%85%9C%20%26%20%EC%9E%84%EB%B2%A0%EB%94%94%EB%93%9C)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [ESP32-CAM 오류 : [E][camera.c:1049] camera\_probe(): Detected camera not supported. [E][camera.c:1249] esp\_camera\_init(): Camera probe failed with error 0x20004](/183)  (0) | 2021.05.09 |
| [시스템 프로그래밍 프로젝트 #7 최종 (Assembler in C)](/130)  (2) | 2020.03.19 |
| [시스템 프로그래밍 프로젝트 #1](/22)  (1) | 2020.01.12 |
| [시스템 프로그래밍 프로젝트 #2](/21)  (1) | 2020.01.12 |
| [시스템 프로그래밍 프로젝트 #3](/20)  (1) | 2020.01.12 |