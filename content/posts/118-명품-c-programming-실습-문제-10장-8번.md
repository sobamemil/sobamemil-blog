---
title: "명품 C++ programming 실습 문제 10장 8번"
date: 2020-03-09T17:19:46+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "programming", "다운캐스팅", "상속", "순수가상함수", "실습문제", "업캐스팅", "연습문제", "추상클래스", "프로그래밍"]
---

<b>문제 :</b>

문제 7을 푸는 다른 방법을 소개한다.

bigger() 함수의 다음 라인에서 > 연산자 때문에

|  |  |
| --- | --- |
| 1 | if(a > b) return a; |

T에 Circle과 같은 클래스 타입이 대입되면, 구체화가 실패하여 컴파일 오류가 발생한다.

이 문제를 해결하기 위해 다음과 같은 추상 클래스 Comparable을 제안한다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6 | class Comparable {  public:  virtual bool operator > (Comparable& op2) = 0; // 순수 가상 함수  virtual bool operator < (Comparable& op2) = 0; // 순수 가상 함수  virtual bool operator == (Comparable& op2) = 0; // 순수 가상 함수  }; |

Circle 클래스가 Comparable을 상속받아 순수 가상 함수를 모두 구현하면, 앞의 bigger() 템플릿 함수를 사용하는데 아무 문제가 없다.

Circle뿐 아니라, Comparable을 상속받은 모든 클래스를 bigger()에 사용할 수 있다.

Comparable을 상속받은 Circle 클래스를 완성하고 문제 7의 main()을 실행하여 테스트 하라.

[2020/03/09 - [C++/명품 C++ programming] - 명품 C++ programming 실습 문제 10장 7번](https://sobamemil.tistory.com/117)

[명품 C++ programming 실습 문제 10장 7번

문제 : 다음 프로그램은 컴파일 오류가 발생한다. 소스의 어디에서 왜 컴파일 오류가 발생하는가? 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 #include using namespace std; cl..

sobamemil.tistory.com](https://sobamemil.tistory.com/117)

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/118/img_1.png)

<b>목적 및 힌트 :</b>

템플릿 함수 작성시 상속과 연산자 중복의 필요성 이해

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52 | #include <iostream>  using namespace std;    class Comparable {  public:  virtual bool operator > (Comparable& op2) = 0; // 순수 가상 함수  virtual bool operator < (Comparable& op2) = 0; // 순수 가상 함수  virtual bool operator == (Comparable& op2) = 0; // 순수 가상 함수  };    class Circle : public Comparable {  int radius;  public:  Circle(int radius = 1) { this->radius = radius; }  int getRadius() { return radius; }  bool operator > (Comparable& op2) {  Circle \*c;  c = (Circle\*) &op2;  if(this->radius > c->getRadius())  return true;  return false;  }  bool operator < (Comparable& op2) {  Circle \*c;  c = (Circle\*) &op2;  if(this->radius < c->getRadius())  return true;  return false;  }  bool operator == (Comparable& op2) {  Circle \*c;  c = (Circle\*) &op2;  if(this->radius == c->getRadius())  return true;  return false;  }  };    template <class T>  T bigger(T a, T b) { // 두 개의 매개 변수를 비교하여 큰 값을 리턴  if (a > b) return a;  else return b;  }    int main() {  int a = 20, b = 50, c;  c = bigger(a, b);  cout << "20과 50중 큰 값은 " << c << endl;  Circle waffle(10), pizza(20), y;  y = bigger(waffle, pizza);  cout << "waffle과 pizza 중 큰 것의 반지름은 " << y.getRadius() << endl;  } |
