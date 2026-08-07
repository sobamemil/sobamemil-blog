---
title: "명품 C++ programming 실습 문제 11장 2번"
date: 2020-03-27T15:03:49+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "cin", "get", "Istream", "ostream", "programming", "명품", "실습문제", "연습문제", "프로그래밍"]
---

<b>문제 :</b>

istream& get(char& ch) 함수를 이용하여 한 라인을 읽고 빈칸(' ')이 몇 개인지 출력하는 프로그램을 작성하라.

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/133/img_1.png)

<b>목적 및 힌트 :</b>

cin으로 키 입력 연습

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18 | #include <iostream>  using namespace std;    int main() {  char ch;  int cnt;    while(true){  cin.get(ch); // 키를 ch에 읽어옴  if(cin.eof()) // EOF 문자 즉 ctrl-z 키가 입력된 경우, 읽기 종료  break;  if(ch == '\n') // <Enter> 키가 입력된 경우 읽기 중단  break;  else if(ch == ' ')  cnt++;  }  cout << cnt;  } |


[저작자표시 비영리
(새창열림)](https://creativecommons.org/licenses/by-nc/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 11장 4번](/135)  (1) | 2020.03.27 |
| [명품 C++ programming 실습 문제 11장 3번](/134)  (3) | 2020.03.27 |
| [명품 C++ programming 실습 문제 11장 1번](/132)  (1) | 2020.03.27 |
| [명품 C++ programming 실습 문제 10장 16번](/126)  (1) | 2020.03.11 |
| [명품 C++ programming 실습 문제 10장 15번](/125)  (3) | 2020.03.11 |