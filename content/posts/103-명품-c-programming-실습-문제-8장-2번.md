---
title: "명품 C++ programming 실습 문제 8장 2번"
date: 2020-03-09T13:11:20+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "namedcircle", "programming", "기본클래스", "명품", "상속", "실습문제", "연습문제", "파생클래스", "프로그래밍"]
---

**문제 :**

문제 1~2에 적용되는 원을 추상화한 Circle 클래스가 있다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8 | class Circle{  int radius;  public:  Circle(int radius=0) { this->radius = radius; }  int getRadius() { return radius; }  void setRadius(int radius) { this->radius = radius; }  double getArea() { return 3.14\*radius\*radius; }  }; |

다음과 같이 배열을 선언하여 다음 실행 결과가 나오도록 Circle을 상속받은 NamedCircle 클래스와 main() 함수 등 필요한 함수를 작성하라.

|  |  |
| --- | --- |
| 1 | NamedCircle pizza[5]; |

**실행 결과 :**

![](https://img.sobamemil.com/posts/103/img_1.png)

**목적 및 힌트 :**

상속, 파생 클래스 작성 및 응용

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43 | #include<iostream>  using namespace std;    class Circle{  int radius;  public:  Circle(int radius=0) { this->radius = radius; }  int getRadius() { return radius; }  void setRadius(int radius) { this->radius = radius; }  double getArea() { return 3.14\*radius\*radius; }  };    class NameCircle : public Circle{  string name;  public:  void setRN(int R, string N){  setRadius(R);  this->name = N;  }  string getName(){  return name;  }  };    int main() {  string name;  int radius,big;  double size[5];  NameCircle pizza[5];  cout << "5 개의 정수 반지름과 원의 이름을 입력하세요\n";  for(int i=0; i<5; i++){  cout << i+1 << ">> ";  cin >> radius >> name;  pizza[i].setRN(radius,name);  size[i] = pizza[i].getArea();  }  big=0;  for(int i=0; i<4; i++){  if(size[i] < size[i+1])  big = i+1;  }  cout << "가장 면적이 큰 피자는 " << pizza[big].getName() << "입니다";  } |

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 8장 4번](/105)  (3) | 2020.03.09 |
| [명품 C++ programming 실습 문제 8장 3번](/104)  (9) | 2020.03.09 |
| [명품 C++ programming 실습 문제 8장 1번](/102)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 7장 12번](/101)  (3) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 11번](/100)  (2) | 2020.03.06 |