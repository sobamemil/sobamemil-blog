---
title: "명품 C++ programming 실습 문제 7장 9번"
date: 2020-03-06T18:43:43+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "circle", "friend", "programming", "명품", "실습문제", "연산자", "연습문제", "프렌드", "프로그래밍"]
---

**문제 :**

문제 8번의 Circle 객체에 대해 다음 연산이 가능하도록 연산자를 구현하라.

|  |  |
| --- | --- |
| 1  2  3  4 | Circle a(5), b(4);  b = 1+a; // b의 반지름을 a의 반지름에 1을 더한 것으로 변경  a.show();  b.show(); |

[2020/03/06 - [C++/명품 C++ programming] - 명품 C++ programming 실습 문제 7장 8번](https://sobamemil.tistory.com/97)

[명품 C++ programming 실습 문제 7장 8번

문제 : 원을 추상화한 Circle 클래스는 간단히 아래와 같다. 1 2 3 4 5 6 class Circle{ int radius; public: Circle(int radius=0) { this->radius = radius; } void show() { cout << "radius = " << radius <<..

sobamemil.tistory.com](https://sobamemil.tistory.com/97)

**실행 결과 :**

![](https://img.sobamemil.com/posts/98/img_1.png)

**목적 및 힌트 :**

프렌드 함수로 연산자 구현 연습

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22 | #include<iostream>  using namespace std;    class Circle{  int radius;  public:  Circle(int radius=0) { this->radius = radius; }  void show() { cout << "radius = " << radius << " 인 원" << endl; }  friend Circle operator+ (int x, Circle c);  };    Circle operator+ (int x, Circle c){  c.radius += x;  return c;  }    int main() {  Circle a(5), b(4);  b = 1+a; // b의 반지름을 a의 반지름에 1을 더한 것으로 변경  a.show();  b.show();  } |


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 7장 11번](/100)  (2) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 10번](/99)  (3) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 8번](/97)  (1) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 7번](/96)  (3) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 6번](/95)  (1) | 2020.03.06 |