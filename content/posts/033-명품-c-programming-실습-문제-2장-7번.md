---
title: "명품 C++ programming 실습 문제 2장 7번"
date: 2020-02-28T17:07:48+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "cin.getline()", "CString", "programming", "strcmp()", "명품", "배열초기화", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

다음과 같이 "yes"가 입력될 때까지 종료하지 않는 프로그램을 작성하라. 사용자로부터의 입력은 cin.getline() 함수를 사용하라.

<b>목적 및 힌트 :</b>

공백을 포함하는 문자열 읽기

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/33/img_1.png)

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17 | #include <iostream>  #include <cstring>  using namespace std;    int main() {  char A[] = "yes"; // 배열 선언시 "yes"로 초기화  char B[100];  while(true){  cout << "종료하고 싶으면 yes를 입력하세요>>";  cin.getline(B,100);  if(strcmp(A,B) == 0) break;  }    cout << "종료합니다...";    return 0;  } |

<b>설명 :</b>

2장 6번 문제와 거의 동일한 문제입니다.

cin.getline() 함수를 이용해 입력시에 공백을 포함하는 문자열 입력도 가능하게 만들 수 있는지 테스트 하는 문제입니다.
