---
title: "C++ Programming Ch.11 Exercise 8 Solution"
date: 2020-04-02T13:54:14+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "operator", "programming", "명품", "스트림입출력", "실습문제", "연산자", "연습문제", "참조자", "프로그래밍"]
---

**Problem:**

Circle 클래스는 다음과 같다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8 | class Circle {  string name;  int radius;  public:  Circle(int radius=1, string name="") {  this->radius = radius; this->name = name;  }  }; |

Circle 클래스의 객체를 입출력하는 다음 코드와 Execution Result를 참조하여 <<, >> 연산자를 작성하고 Circle 클래스를 수정하는 등 프로그램을 완성하라.

|  |  |
| --- | --- |
| 1  2  3 | Circle d, w;  cin >> d >> w; // 키보드 입력을 받아 객체 d와 w를 완성  cout << d << w << endl; // 객체 d, w 출력 |

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/139/img_1.png)

<b>Objective & Hints:</b>

스트림 입출력 연산자( <<, >>) 작성 연습

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32 | #include <iostream>  using namespace std;    class Circle { // 원을 표현하는 클래스  string name;  int radius;  public:  Circle(int radius=1, string name="") {  this->radius = radius; this->name = name;  }  friend ostream& operator << (ostream& os, Circle c); // friend 선언  friend istream& operator >> (istream& ins, Circle& c); // friend 선언, Circle& c 참조자 사용  };    ostream& operator << (ostream& os, Circle c) {  os << "(반지름이" << c.radius << "인 " << c.name << ")";  return os;  }    istream& operator >> (istream& ins, Circle& c) {  cout << "반지름 >> ";  ins >> c.radius;  cout << "이름 >> ";  ins >> c.name;  return ins;  }    int main() {  Circle d, w;  cin >> d >> w; // 키보드 입력을 받아 객체 d와 w를 완성  cout << d << w << endl; // 객체 d, w 출력  } |

<b>Explanation:</b>

스트림 입출력 연산자는 class 외부 함수로 작성해야 하고, >> 연산자 작성시에는 본래의 값이 바뀌어야 하기 때문에 매개변수로 참조자를 사용하여 받았습니다.
