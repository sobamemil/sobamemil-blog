---
title: "C++ Programming Ch.4 Exercise 1 Solution"
date: 2020-03-04T15:05:27+09:00
draft: false
categories: ["💻 Dev & CS", "C++ Programming"]
tags: ["C++", "programming", "Object Array", "Object Pointer", "Masterpiece", "Practice Problem", "Exercise", "Pointer", "Programming", "Arrow Operator"]
---

**Problem:**

다음은 색의 3요소인 red, green, blue로 색을 추상화한 Color 클래스를 선언하고 활용하는 코드이다. 빈칸을 채워라.

red, green, blue는 0~255의 값만 가진다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31 | #include<iostream>  using namespace std;    class Color {  int red, green, blue;  public:  Color() {red = green = blue = 0;}  Color(int r, int g, int b) {red = r; green = g; blue = b;}  void setColor(int r, int g, int b) {red = r; green = g; blue = b;}  void show() {cout << red << ' ' << green << ' ' << blue << endl;}  };    int main() {  Color screenColor(255,0,0); // 빨간색의 screenColor 객체 생성  Color \*p;     // Color 타입의 포인터 변수 p 선언  ＿＿＿＿＿    // (1) p가 screenColor의 주소를 가지도록 코드 작성  ＿＿＿＿＿    // (2) p와 show()를 이용하여 screenColor 색 출력  ＿＿＿＿＿    // (3) Color의 일차원 배열 colors 선언. 원소는 3개  ＿＿＿＿＿    // (4) p가 colors 배열을 가리키도록 코드 작성    // (5) p와 setColor()를 이용하여 colors[0], colors[1], colors[2]가  // 각각 빨강, 초록, 파랑색을 가지도록 코드 작성  ＿＿＿＿＿  ＿＿＿＿＿  ＿＿＿＿＿    // (6) p와 show()를 이용하여 colors 배열의 모든 객체의 색 출력. for 문 이용  ＿＿＿＿＿  ＿＿＿＿＿  ＿＿＿＿＿  } |

<b>Objective & Hints:</b>

객체 포인터와 객체 배열 활용

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/55/img_1.png)

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31 | #include<iostream>  using namespace std;    class Color {  int red, green, blue;  public:  Color() {red = green = blue = 0;}  Color(int r, int g, int b) {red = r; green = g; blue = b;}  void setColor(int r, int g, int b) {red = r; green = g; blue = b;}  void show() {cout << red << ' ' << green << ' ' << blue << endl;}  };    int main() {  Color screenColor(255,0,0); // 빨간색의 screenColor 객체 생성  Color \*p;            // Color 타입의 포인터 변수 p 선언  p = &screenColor;    // (1) p가 screenColor의 주소를 가지도록 코드 작성  p->show();           // (2) p와 show()를 이용하여 screenColor 색 출력  Color colors[3];     // (3) Color의 일차원 배열 colors 선언. 원소는 3개  p = colors;          // (4) p가 colors 배열을 가리키도록 코드 작성    // (5) p와 setColor()를 이용하여 colors[0], colors[1], colors[2]가  // 각각 빨강, 초록, 파랑색을 가지도록 코드 작성  p[0].setColor(255,0,0);  p[1].setColor(0,255,0);  p[2].setColor(0,0,255);    // (6) p와 show()를 이용하여 colors 배열의 모든 객체의 색 출력. for 문 이용  for(int i=0; i<3; i++){  p[i].show();  }  } |

<b>Explanation:</b>

객체 포인터와 객체 배열의 사용법을 익히는 문제입니다.

클래스 타입의 포인터 변수가 같은 클래스 타입의 객체의 주소를 가지도록 한 후,

화살표 연산자(->)를 이용하여 클래스 멤버를 호출할 수 있습니다.
