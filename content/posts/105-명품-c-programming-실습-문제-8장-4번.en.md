---
title: "C++ Programming Ch.8 Exercise 4 Solution"
date: 2020-03-09T13:26:22+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["accessspecifiers", "C++", "programming", "Default Parameter", "Masterpiece", "Inheritance", "Practice Problem", "Exercise", "Access Specifier", "Programming"]
---

**Problem:**

문제 3~4에 적용되는 2차원 상의 한 점을 표현하는 Point 클래스가 있다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | class Point {  int x,y;  public:  point(int x, int y) { this->x = x; this->y = y; }  int getX(){ return x; }  int getY(){ return y; }  protected:  void move(int x, int y) { this->x = x; this->y = y; }  }; |

다음 main() 함수가 실행되도록 Point 클래스를 상속받는 ColorPoint 클래스를 작성하고, 전체 프로그램을 완성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | int main() {  ColorPoint zeroPoint; // BLACK 색에 (0, 0) 위치의 점  zeroPoint.show(); // zeroPoint를 출력한다.    ColorPoint cp(5, 5);  cp.setPoint(10, 20);  cp.setColor("BLUE");  cp.show(); // cp를 출력한다.  } |

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/105/img_1.png)

<b>Objective & Hints:</b>

상속, 파생 클래스와 생성자 작성 및 응용

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40 | #include<iostream>  using namespace std;    class Point {  int x,y;  public:  point(int x, int y) { this->x = x; this->y = y; }  int getX(){ return x; }  int getY(){ return y; }  protected:  void move(int x, int y) { this->x = x; this->y = y; }  };    class ColorPoint : public Point {  string color;  public:  ColorPoint(int x=0, int y=0, string color="BLACK"){  point(x, y);  this->color = color;  }  void setPoint(int x, int y){  move(x, y);  }  void setColor(string color){  this->color = color;  }  void show(){  cout << color << "색으로 (" << getX() << "," << getY() << ")에 위치한 점입니다.\n";  }  };    int main() {  ColorPoint zeroPoint; // BLACK 색에 (0, 0) 위치의 점  zeroPoint.show(); // zeroPoint를 출력한다.    ColorPoint cp(5, 5);  cp.setPoint(10, 20);  cp.setColor("BLUE");  cp.show(); // cp를 출력한다.  } |

<b>Explanation:</b>

ColorPoint 클래스의 생성자를 디폴트 매개 변수가 있는 생성자로 작성해주면 되는 문제입니다.
