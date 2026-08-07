---
title: "C++ Programming Ch.7 Exercise 9 Solution"
date: 2020-03-06T18:43:43+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "circle", "friend", "programming", "명품", "실습문제", "연산자", "연습문제", "프렌드", "프로그래밍"]
---

**Problem:**

문제 8번의 Circle 객체에 대해 다음 연산이 가능하도록 연산자를 구현하라.

|  |  |
| --- | --- |
| 1  2  3  4 | Circle a(5), b(4);  b = 1+a; // b의 반지름을 a의 반지름에 1을 더한 것으로 변경  a.show();  b.show(); |

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/98/img_1.png)

<b>Objective & Hints:</b>

프렌드 함수로 연산자 구현 연습

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22 | #include<iostream>  using namespace std;    class Circle{  int radius;  public:  Circle(int radius=0) { this->radius = radius; }  void show() { cout << "radius = " << radius << " 인 원" << endl; }  friend Circle operator+ (int x, Circle c);  };    Circle operator+ (int x, Circle c){  c.radius += x;  return c;  }    int main() {  Circle a(5), b(4);  b = 1+a; // b의 반지름을 a의 반지름에 1을 더한 것으로 변경  a.show();  b.show();  } |
