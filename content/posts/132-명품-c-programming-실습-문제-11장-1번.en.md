---
title: "C++ Programming Ch.11 Exercise 1 Solution"
date: 2020-03-27T14:58:42+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["11장", "C++", "cin", "get()", "programming", "명품", "스트림", "실습문제", "연습문제", "프로그래밍"]
---<b>Problem:</b>

int cin.get() 함수를 이용하여 키보드로부터 한 라인을 읽고 'a'가 몇 개인지 출력하는 프로그램을 작성하라.

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/132/img_1.png)

<b>Objective & Hints:</b>

cin으로 키 입력 연습

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | #include <iostream>  using namespace std;    int main() {  int a;  int cnt=0;  while( (a = cin.get() ) != EOF ){  if(a == 'a')  cnt++;  else if(a == '\n')  break;  }  cout << cnt;  } |

<b>Explanation:</b>

cin은 C++ 표준 입출력 스트림 객체입니다. 따라서 iostream 헤더 파일은 include 했다면 저절로 cin 객체가 생성되어 바로 사용할 수 있습니다.


](
