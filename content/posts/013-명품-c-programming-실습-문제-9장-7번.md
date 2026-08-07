---
title: "명품 C++ programming 실습 문제 9장 7번"
date: 2019-11-21T11:45:27+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C", "C++", "programming", "과제", "명품", "소스코드", "실습문제", "실행결과", "연습문제", "프로그래밍"]
---

**문제 :**

사각형에 내접하는 도형을 표한하기 위한 Shape 클래스가 있다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | class Shape {  protected:  string name; // 도형의 이름  int width, height; // 도형이 내접하는 사각형의 너비와 높이  public:  Shape(string n="", int w=0, int h=0) { name = n; width = w; height = h; }  virtual double getArea() { return 0; } // dummy 값 리턴  string getName() { return name; } // 이름 리턴  };  [Colored by Color Scripter](http://colorscripter.com/info#e) |

Shape 클래스를 상속받아 타원을 표현하는 Oval, 사각형을 표현하는 Rect, 삼각형을 표현하는 Triangular 클래스를 작성하라. main()을 작성하고 실행하면 다음과 같다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10 | int main() {  Shape \*p[3];  p[0] = new Oval("빈대떡", 10, 20);  p[1] = new Rect("찰떡", 30, 40);  p[2] = new Triangular("토스트", 30, 40);  for(int i=0; i<3; i++)  cout << p[i]->getName() << " 넓이는 " << p[i]->getArea() << endl;    for(int i=0; i<3; i++) delete p[i];  }  [Colored by Color Scripter](http://colorscripter.com/info#e) |

![](https://img.sobamemil.com/posts/13/img_1.png)

**목적 및 힌트 :**

가상 함수를 가진 클래스를 상속받는 파생 클래스 만들기

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47 | #include<iostream>  using namespace std;    class Shape {  protected:  string name; // 도형의 이름  int width, height; // 도형이 내접하는 사각형의 너비와 높이  public:  Shape(string n="", int w=0, int h=0) { name = n; width = w; height = h; }  virtual double getArea() { return 0; } // dummy 값 리턴  string getName() { return name; } // 이름 리턴  };    class Oval : public Shape {  public:  Oval(string n, int w, int h) : Shape(n, w, h){;}  virtual double getArea() {  return 3.14 \* width \* height;  }  };    class Rect : public Shape {  public:  Rect(string n, int w, int h) : Shape(n, w, h){;}  virtual double getArea() {  return width \* height;  }  };    class Triangular : public Shape {  public:  Triangular(string n, int w, int h) : Shape(n, w, h){;}  virtual double getArea() {  return (width \* height) / 2;  }  };    int main() {  Shape \*p[3];  p[0] = new Oval("빈대떡", 10, 20);  p[1] = new Rect("찰떡", 30, 40);  p[2] = new Triangular("토스트", 30, 40);  for(int i=0; i<3; i++)  cout << p[i]->getName() << " 넓이는 " << p[i]->getArea() << endl;    for(int i=0; i<3; i++) delete p[i];  }  [Colored by Color Scripter](http://colorscripter.com/info#e) |


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 9장 9번](/18)  (1) | 2019.11.26 |
| [명품 C++ programming 실습 문제 9장 8번](/14)  (1) | 2019.11.21 |
| [명품 C++ programming 실습 문제 9장 6번](/11)  (1) | 2019.11.21 |
| [명품 C++ programming 실습 문제 9장 5번](/10)  (2) | 2019.11.21 |
| [명품 C++ programming 실습 문제 9장 4번](/9)  (3) | 2019.11.21 |