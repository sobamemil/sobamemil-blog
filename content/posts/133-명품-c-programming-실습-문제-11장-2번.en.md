---
title: "C++ Programming Ch.11 Exercise 2 Solution"
date: 2020-03-27T15:03:49+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "cin", "get", "Istream", "ostream", "programming", "명품", "실습문제", "연습문제", "프로그래밍"]
---

**Problem:**

istream& get(char& ch) 함수를 이용하여 한 라인을 읽고 빈칸(' ')이 몇 개인지 출력하는 프로그램을 작성하라.

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/133/img_1.png)

<b>Objective & Hints:</b>

cin으로 키 입력 연습

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18 | #include <iostream>  using namespace std;    int main() {  char ch;  int cnt;    while(true){  cin.get(ch); // 키를 ch에 읽어옴  if(cin.eof()) // EOF 문자 즉 ctrl-z 키가 입력된 경우, 읽기 종료  break;  if(ch == '\n') // <Enter> 키가 입력된 경우 읽기 중단  break;  else if(ch == ' ')  cnt++;  }  cout << cnt;  } |
