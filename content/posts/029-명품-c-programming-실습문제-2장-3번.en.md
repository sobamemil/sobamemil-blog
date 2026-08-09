---
title: "명품 C++ programming 실습문제 2장 3번"
date: 2020-02-28T16:27:30+09:00
draft: false
categories: ["💻 Dev & CS", "C++ Programming"]
tags: ["C++", "cin", "cout", "programming", "Masterpiece", "Source Code", "Practice Problem", "Operator", "Exercise", "Programming"]
---

**Problem:**

키보드로부터 두 개의 정수를 읽어 큰 수를 화면에 출력하라.

<b>Objective & Hints:</b>

cin 활용, 키보드로부터 정수 읽기

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/29/img_1.png)

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15 | #include<iostream>  using namespace std;    int main(){  int a,b;  cout << "두 수를 입력하라>>";  cin >> a >> b; // cin 연산자를 이용하여 두개의 정수 입력받기  cout << "큰 수 = ";  if(a<b)  cout << b;  else  cout << a;    return 0;  } |

<b>Explanation:</b>

c++에서 새로 등장한 cin 연산자를 사용할 수 있는지에 대한 문제입니다.

cin >> a >> b 와 같이 한번에 여러개를 입력받을 수 있습니다.
