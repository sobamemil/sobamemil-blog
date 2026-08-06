---
title: "명품 C++ programming 실습 문제 2장 7번"
date: 2020-02-28T17:07:48+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "cin.getline()", "CString", "programming", "strcmp()", "명품", "배열초기화", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

다음과 같이 "yes"가 입력될 때까지 종료하지 않는 프로그램을 작성하라. 사용자로부터의 입력은 cin.getline() 함수를 사용하라.

**목적 및 힌트 :**

공백을 포함하는 문자열 읽기

**실행 결과 :**

![](https://img.sobamemil.com/posts/33/img_1.png)

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17 | #include <iostream>  #include <cstring>  using namespace std;    int main() {  char A[] = "yes"; // 배열 선언시 "yes"로 초기화  char B[100];  while(true){  cout << "종료하고 싶으면 yes를 입력하세요>>";  cin.getline(B,100);  if(strcmp(A,B) == 0) break;  }    cout << "종료합니다...";    return 0;  } |

**설명 :**

2장 6번 문제와 거의 동일한 문제입니다.

cin.getline() 함수를 이용해 입력시에 공백을 포함하는 문자열 입력도 가능하게 만들 수 있는지 테스트 하는 문제입니다.

공유하기

게시글 관리

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 2장 9번](/35)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 8번](/34)  (2) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 6번](/32)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 5번](/31)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 4번](/30)  (1) | 2020.02.28 |
