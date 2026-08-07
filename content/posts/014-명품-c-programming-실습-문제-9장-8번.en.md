---
title: "C++ Programming Ch.9 Exercise 8 Solution"
date: 2019-11-21T12:49:18+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C", "C++", "programming", "과제", "명품", "소스코드", "실습문제", "실행결과", "연습문제", "프로그래밍"]
---

<b>Problem:</b>

사각형에 내접하는 도형을 표현하기 위한 Shape 클래스가 있다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | class Shape {  protected:  string name; // 도형의 이름  int width, height; // 도형이 내접하는 사각형의 너비와 높이  public:  Shape(string n="", int w=0, int h=0) { name = n; width = w; height = h; }  virtual double getArea() { return 0; } // dummy 값 리턴  string getName() { return name; } // 이름 리턴  };   |

문제 7에 주어진 Shape 클래스를 추상 클래스로 만들고 문제 7을 다시 작성하라.

[2019/11/21 - [C++/명품 C++ programming] - 명품 C++ programming Exercise Problem 9장 7번](https://sobamemil.tistory.com/13)

[명품 C++ programming Exercise Problem 9장 7번

Problem: 사각형에 내접하는 도형을 표한하기 위한 Shape 클래스가 있다. 1 2 3 4 5 6 7 8 9 class Shape { protected: string name; // 도형의 이름 int width, height; // 도형이 내접하는 사각형의 너비와 높이 p..

sobamemil.tistory.com](https://sobamemil.tistory.com/13)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10 | int main() {  Shape \*p[3];  p[0] = new Oval("빈대떡", 10, 20);  p[1] = new Rect("찰떡", 30, 40);  p[2] = new Triangular("토스트", 30, 40);  for(int i=0; i<3; i++)  cout << p[i]->getName() << " 넓이는 " << p[i]->getArea() << endl;    for(int i=0; i<3; i++) delete p[i];  }   |

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/14/img_1.png)

<b>Objective & Hints:</b>

가상 함수를 가진 클래스를 추상 클래스로 만들기

Shape을 추상 클래스로 만들려면 getArea() 함수를 순수 가상 함수로 만들면 된다.

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47 | #include<iostream>  using namespace std;    class Shape {  protected:  string name;  int width, height;  public:  Shape(string n="", int w=0, int h=0) { name = n; width = w; height = h; }  virtual double getArea()=0;  string getName() { return name; }  };    class Oval : public Shape {  public:  Oval(string n, int w, int h) : Shape(n, w, h){;}  virtual double getArea() {  return 3.14 \* width \* height;  }  };    class Rect : public Shape {  public:  Rect(string n, int w, int h) : Shape(n, w, h){;}  virtual double getArea() {  return width \* height;  }  };    class Triangular : public Shape {  public:  Triangular(string n, int w, int h) : Shape(n, w, h){;}  virtual double getArea() {  return (width \* height) / 2;  }  };    int main() {  Shape \*p[3];  p[0] = new Oval("빈대떡", 10, 20);  p[1] = new Rect("찰떡", 30, 40);  p[2] = new Triangular("토스트", 30, 40);  for(int i=0; i<3; i++)  cout << p[i]->getName() << " 넓이는 " << p[i]->getArea() << endl;    for(int i=0; i<3; i++) delete p[i];  }   |
