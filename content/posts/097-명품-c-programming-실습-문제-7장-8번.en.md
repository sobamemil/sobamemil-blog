---
title: "명품 C++ programming 실습 문제 7장 8번"
date: 2020-03-06T18:20:01+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "circle", "friend", "programming", "명품", "실습문제", "연산자", "연습문제", "프렌드함수", "프로그래밍"]
---

**문제 :**

원을 추상화한 Circle 클래스는 간단히 아래와 같다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6 | class Circle{  int radius;  public:  Circle(int radius=0) { this->radius = radius; }  void show() { cout << "radius = " << radius << " 인 원" << endl; }  }; |

다음 연산이 가능하도록 연산자를 프렌드 함수로 작성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5 | Circle a(5), b(4);  ++a; // 반지름을 1 증가 시킨다.  b = a++; // 반지름을 1 증가 시킨다.  a.show();  b.show(); |

**실행 결과 :**

![](https://img.sobamemil.com/posts/97/img_1.png)

**목적 및 힌트 :**

프렌드 함수로 연산자 구현 연습

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30 | #include<iostream>  using namespace std;    class Circle{  int radius;  public:  Circle(int radius=0) { this->radius = radius; }  void show() { cout << "radius = " << radius << " 인 원" << endl; }  friend Circle& operator++(Circle& c);  friend Circle operator++(Circle& c, int x);  };    Circle& operator++(Circle& c){  c.radius++;  return c;  }    Circle operator++(Circle& c, int x){  Circle test = c;  c.radius++;  return test;  }    int main() {  Circle a(5), b(4);  ++a; // 반지름을 1 증가 시킨다.  b = a++; // 반지름을 1 증가 시킨다.  a.show();  b.show();  } |

**설명 :**

전위 ++ 연산과 후위 ++ 연산 모두 참조 매개 변수를 사용하고 전위 연산자의 경우 참조를 리턴합니다.

참조 매개 변수를 사용하지 않는다면, 매개 변수에 복사본이 전달되므로 본래의 값은 변하지 않습니다.

후위 연산자의 int x 매개 변수는 의미 없는 값이고, 이는 후위 연산자와 전위 연산자를 구분하기 위해 전달해주는 매개 변수입니다.

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 7장 10번](/99)  (3) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 9번](/98)  (1) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 7번](/96)  (3) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 6번](/95)  (1) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 5번](/94)  (1) | 2020.03.06 |