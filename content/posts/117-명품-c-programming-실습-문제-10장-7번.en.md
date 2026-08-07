---
title: "명품 C++ programming 실습 문제 10장 7번"
date: 2020-03-09T16:21:24+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "programming", "구체화", "명품", "실습문제", "연습문제", "제네릭", "중복함수", "템플릿", "프로그래밍"]
---

<b>문제 :</b>

다음 프로그램은 컴파일 오류가 발생한다. 소스의 어디에서 왜 컴파일 오류가 발생하는가?

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24 | #include <iostream>  using namespace std;    class Circle {  int radius;  public:  Circle(int radius = 1) { this->radius = radius; }  int getRadius() { return radius; }  };    template <class T>  T bigger(T a, T b) { // 두 개의 매개 변수를 비교하여 큰 값을 리턴  if (a > b) return a;  else return b;  }    int main() {  int a = 20, b = 50, c;  c = bigger(a, b);  cout << "20과 50중 큰 값은 " << c << endl;  Circle waffle(10), pizza(20), y;  y = bigger(waffle, pizza);  cout << "waffle과 pizza 중 큰 것의 반지름은 " << y.getRadius() << endl;  } |

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/117/img_1.png)

<b>목적 및 힌트 :</b>

템플릿 함수의 구체화의 실패 이해

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30 | #include <iostream>  using namespace std;    class Circle {  int radius;  public:  Circle(int radius = 1) { this->radius = radius; }  int getRadius() { return radius; }  };    Circle bigger(Circle a, Circle b){  if(a.getRadius() > b.getRadius())  return a;  return b;  }    template <class T>  T bigger(T a, T b) { // 두 개의 매개 변수를 비교하여 큰 값을 리턴  if (a > b) return a;  else return b;  }    int main() {  int a = 20, b = 50, c;  c = bigger(a, b);  cout << "20과 50중 큰 값은 " << c << endl;  Circle waffle(10), pizza(20), y;  y = bigger(waffle, pizza);  cout << "waffle과 pizza 중 큰 것의 반지름은 " << y.getRadius() << endl;  } |

<b>설명 :</b>

전체 코드 28번 줄에 있는 y = bigger(waffle, pizza);를 호출 시에 19번 줄에 있는 if(a>b) return a; 부분에서 오류가 발생합니다.

Circle과 같은 클래스는 > 연산자가 구현되어 있지 않기 때문에 구체화에 실패하기 때문입니다.

따라서 Circle 타입의 중복 함수를 작성하여 주면 bigger(waffle, pizza); 호출 시 템플릿 함수보다 중복 함수가 우선이기 때문에 템플릿 함수가 아닌 Circle 객체를 리턴하는 중복 함수가 호출됩니다.


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 10장 9번](/119)  (1) | 2020.03.10 |
| [명품 C++ programming 실습 문제 10장 8번](/118)  (4) | 2020.03.09 |
| [명품 C++ programming 실습 문제 10장 6번](/116)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 10장 5번](/115)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 10장 4번](/114)  (1) | 2020.03.09 |