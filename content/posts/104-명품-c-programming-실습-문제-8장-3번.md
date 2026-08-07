---
title: "명품 C++ programming 실습 문제 8장 3번"
date: 2020-03-09T13:18:25+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "programming", "기본클래스", "명품", "상속", "실습문제", "연습문제", "접근지정자", "파생클래스", "프로그래밍"]
---

**문제 :**

문제 3~4에 적용되는 2차원 상의 한 점을 표현하는 Point 클래스가 있다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | class Point {  int x,y;  public:  point(int x, int y) { this->x = x; this->y = y; }  int getX(){ return x; }  int getY(){ return y; }  protected:  void move(int x, int y) { this->x = x; this->y = y; }  }; |

다음 main() 함수가 실행되도록 Point 클래스를 상속받은 ColorPoint 클래스를 작성하고, 전체 프로그램을 완성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6 | int main() {  ColorPoint cp(5, 5, "RED");  cp.setPoint(10, 20);  cp.setColor("BLUE");  cp.show();  } |

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/104/img_1.png)

<b>목적 및 힌트 :</b>

상속, 파생 클래스 작성

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37 | #include<iostream>  using namespace std;    class Point {  int x,y;  public:  point(int x, int y) { this->x = x; this->y = y; }  int getX(){ return x; }  int getY(){ return y; }  protected:  void move(int x, int y) { this->x = x; this->y = y; }  };    class ColorPoint : public Point {  string color;  public:  ColorPoint(int x, int y, string color){  point(x, y);  this->color = color;  }  void setPoint(int x, int y){  move(x, y);  }  void setColor(string color){  this->color = color;  }  void show(){  cout << color << "색으로 (" << getX() << "," << getY() << ")에 위치한 점입니다.";  }  };    int main() {  ColorPoint cp(5, 5, "RED");  cp.setPoint(10, 20);  cp.setColor("BLUE");  cp.show();  } |
