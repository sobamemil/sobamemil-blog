---
title: "C++ Programming Ch.5 Exercise 1 Solution"
date: 2020-03-05T14:16:37+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["&", "C++", "callByReference", "callByValue", "programming", "명품", "실습문제", "연습문제", "참조", "프로그래밍"]
---<b>Problem:</b>

두 개의 Circle 객체를 교환하는 swap() 함수를 '참조에 의한 호출'이 되도록 작성하고 호출하는 프로그램을 작성하라.

<b>Objective & Hints:</b>

참조에 의한 호출 연습

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/69/img_1.png)

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25 | #include<iostream>  using namespace std;    class Circle {  int num;  public:  Circle();  Circle(int num) {this->num = num;}  void setNum(int num) {this->num = num;}  int getNum() {return num;}  };    void swap(Circle &a, Circle &b) {  int swap;  swap = a.getNum();  a.setNum(b.getNum());  b.setNum(swap);  }    int main() {  Circle a(5), b(10);  cout << a.getNum() << " " << b.getNum() << endl;  swap(a,b);  cout << a.getNum() << " " << b.getNum();  } |

<b>Explanation:</b>

참조에 의한 호출(Call by Reference)을 연습해보는 문제입니다.

swap() 함수에서 매개변수로 객체를 받을때 참조 연산자(&)를 이용하여 받아서 사용하면 되는 문제입니다.

참조를 사용하면 유용한 경우가 많지만 본래의 값이 바뀌면 안되는 경우에는 조심해서 사용하셔야 합니다.
