---
title: "명품 C++ programming 실습 문제 11장 4번"
date: 2020-03-27T15:21:26+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "cin", "eof", "get", "ignore", "programming", "명품", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

한 줄에 '영어문장;한글문자' 형식으로 키 입력될 때, cin.ignore()를 이용하여 ';'이전에 입력된 문자열만 출력하는 프로그램을 작성하라.

아래에서 ^Z(ctrl-z) 키는 입력 종료를 나타내는 키이며, cin.get()은 EOF를 리턴한다.

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/135/img_1.png)

<b>목적 및 힌트 :</b>

cin.get(), EOF, cin.ignore() 활용

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | #include <iostream>  using namespace std;    int main() {  int ch;  while( (ch = cin.get()) != EOF ) {  if(ch == ';'){  cout.put('\n');  cin.ignore(100, '\n');  }  else  cout.put(ch);  }  } |

<b>설명 :</b>

cin.ignore() 함수에 대한 내용과 사용법은 실습 문제 11장 3번 문제를 참고하시면 됩니다.
