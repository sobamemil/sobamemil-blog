---
title: "C++ Programming Ch.2 Exercise 7 Solution"
date: 2020-02-28T17:07:48+09:00
draft: false
categories: ["💻 Dev & CS", "C++ Programming"]
tags: ["C++", "cin.getline()", "CString", "programming", "strcmp()", "Masterpiece", "Array Initialization", "Practice Problem", "Exercise", "Programming"]
---

**Problem:**

다음과 같이 "yes"가 입력될 때까지 종료하지 않는 프로그램을 작성하라. 사용자로부터의 입력은 cin.getline() 함수를 사용하라.

<b>Objective & Hints:</b>

공백을 포함하는 문자열 읽기

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/33/img_1.png)

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17 | #include <iostream>  #include <cstring>  using namespace std;    int main() {  char A[] = "yes"; // 배열 선언시 "yes"로 초기화  char B[100];  while(true){  cout << "종료하고 싶으면 yes를 입력하세요>>";  cin.getline(B,100);  if(strcmp(A,B) == 0) break;  }    cout << "종료합니다...";    return 0;  } |

<b>Explanation:</b>

2장 6번 문제와 거의 동일한 문제입니다.

cin.getline() 함수를 이용해 입력시에 공백을 포함하는 문자열 입력도 가능하게 만들 수 있는지 테스트 하는 문제입니다.
