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

**실행 결과 :**

![](https://img.sobamemil.com/posts/135/img_1.png)

**목적 및 힌트 :**

cin.get(), EOF, cin.ignore() 활용

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | #include <iostream>  using namespace std;    int main() {  int ch;  while( (ch = cin.get()) != EOF ) {  if(ch == ';'){  cout.put('\n');  cin.ignore(100, '\n');  }  else  cout.put(ch);  }  } |

**설명 :**

cin.ignore() 함수에 대한 내용과 사용법은 실습 문제 11장 3번 문제를 참고하시면 됩니다.

[2020/03/27 - [명품 C++ programming] - 명품 C++ programming 실습 문제 11장 3번](https://sobamemil.tistory.com/134)

[명품 C++ programming 실습 문제 11장 3번

문제 : 한 줄에 '영어문장;한글문자' 형식으로 키 입력될 때, cin.ignore()를 이용하여 ';' 이후에 입력된 문자열을 화면에 출력하는 프로그램을 작성하라. 아래에서 ^Z(ctrl-z) 키는 입력 종료는 나타내는 키이며..

sobamemil.tistory.com](https://sobamemil.tistory.com/134)

**코딩은 내일부터 ;**

[저작자표시 비영리
(새창열림)](https://creativecommons.org/licenses/by-nc/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 11장 6번](/137)  (1) | 2020.03.27 |
| [명품 C++ programming 실습 문제 11장 5번](/136)  (3) | 2020.03.27 |
| [명품 C++ programming 실습 문제 11장 3번](/134)  (3) | 2020.03.27 |
| [명품 C++ programming 실습 문제 11장 2번](/133)  (1) | 2020.03.27 |
| [명품 C++ programming 실습 문제 11장 1번](/132)  (1) | 2020.03.27 |