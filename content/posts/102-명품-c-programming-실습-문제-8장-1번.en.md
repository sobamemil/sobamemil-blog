---
title: "명품 C++ programming 실습 문제 8장 1번"
date: 2020-03-09T12:56:19+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "inheritance", "programming", "기본클래스", "상속", "실습문제", "연습문제", "접근지정자", "파생클래스", "프로그래밍"]
---

<b>Problem:</b>

문제 1~2에 적용되는 원을 추상화한 Circle 클래스가 있다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8 | class Circle{  int radius;  public:  Circle(int radius=0) { this->radius = radius; }  int getRadius() { return radius; }  void setRadius(int radius) { this->radius = radius; }  double getArea() { return 3.14\*radius\*radius; }  }; |

다음 코드가 실행되도록 Circle을 상속받은 NamedCircle 클래스를 작성하고 전체 프로그램을 완성하라.

|  |  |
| --- | --- |
| 1  2 | NamedCircle waffle(3, "waffle"); // 반지름이 3이고 이름이 waffle인 원  waffle.show(); |

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/102/img_1.png)

<b>Objective & Hints:</b>

상속, 파생 클래스와 생성자 작성

NamedCircle 클래스에 디폴트 매개 변수를 가진 생성자를 작성해야 한다.

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28 | #include<iostream>  using namespace std;    class Circle{  int radius;  public:  Circle(int radius=0) { this->radius = radius; }  int getRadius() { return radius; }  void setRadius(int radius) { this->radius = radius; }  double getArea() { return 3.14\*radius\*radius; }  };    class NameCircle : public Circle{  string name;  public:  NameCircle(int radius, string name){  setRadius(radius);  this->name = name;  }  void show() {  cout << "반지름이 " << getRadius() << "인 " << this->name;  }  };    int main() {  NameCircle waffle(3, "waffle"); // 반지름이 3이고 이름이 waffle인 원  waffle.show();  } |

<b>Explanation:</b>

Circle 클래스를 상속받은 NameCircle 클래스의 객체를 만들어 Circle 클래스의 멤버들에 접근하는 문제입니다.

상속 개념이 없다면 객체 지향 언어라고 말하지 않습니다. 많은 장점이 있는 기능이므로 잘 익혀두시면 좋습니다.

접근지정자에 대한 내용은 아래 링크에서 자세히 다루고 있습니다.

<https://en.cppreference.com/w/cpp/language/access>

[access specifiers - cppreference.com

In a member-specification of a class/struct or union, define the accessibility of subsequent members. In a base-specifier of a derived class declaration, define the accessibility of inherited members of the subsequent base class. [edit] Syntax public : mem

en.cppreference.com](https://en.cppreference.com/w/cpp/language/access)


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 8장 3번](/104)  (9) | 2020.03.09 |
| [명품 C++ programming 실습 문제 8장 2번](/103)  (4) | 2020.03.09 |
| [명품 C++ programming 실습 문제 7장 12번](/101)  (3) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 11번](/100)  (2) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 10번](/99)  (3) | 2020.03.06 |