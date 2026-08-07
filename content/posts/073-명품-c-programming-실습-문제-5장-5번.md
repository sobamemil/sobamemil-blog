---
title: "명품 C++ programming 실습 문제 5장 5번"
date: 2020-03-05T14:49:33+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "increaseBy()", "programming", "값에의한호출", "명품", "실습문제", "연습문제", "참조", "참조에의한호출", "프로그래밍"]
---<b>문제 :</b>

다음 Circle 클래스가 있다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8 | class Circle{  int radius;  public:  Circle(int r) {radius =r;}  int getRadius() {return radius;}  void setRadius(int r) {radius = r;}  void show() {cout << "반지름이 " << radius << "인 원" << endl;}  }; |

Circle 객체 b를 a에 더하여 a를 키우고자 다음 함수를 작성하였다.

|  |  |
| --- | --- |
| 1  2  3  4 | void increaseBy(Circle a, Circle b) {  int r = a.getRadius() + b.getRadius();  a.setRadius(r);  } |

다음 코드를 실행하면 increaseBy() 함수는 목적대로 실행되는가?

|  |  |
| --- | --- |
| 1  2  3  4  5 | int main() {  Circle x(10), y(5);  increaseBy(x, y); // x의 반지름이 15인 원을 만들고자 한다.  x.show(); // "반지름이 15인 원"을 출력한다.  } |

main() 함수의 목적을 달성하도록 increaseBy() 함수를 수정하라.

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/73/img_1.png)

<b>목적 및 힌트 :</b>

참조에 의한 호출 연습

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22 | #include<iostream>  using namespace std;    class Circle{  int radius;  public:  Circle(int r) {radius =r;}  int getRadius() {return radius;}  void setRadius(int r) {radius = r;}  void show() {cout << "반지름이 " << radius << "인 원" << endl;}  };    void increaseBy(Circle &a, Circle &b) {  int r = a.getRadius() + b.getRadius();  a.setRadius(r);  }    int main() {  Circle x(10), y(5);  increaseBy(x, y); // x의 반지름이 15인 원을 만들고자 한다.  x.show(); // "반지름이 15인 원"을 출력한다.  } |

<b>설명 :</b>

문제에 나와있는 코드대로 작성하여 실행해보면 객체 x에는 아무런 변화가 없이 "반지름이 10인 원"이 출력될 것입니다.

문제에서는 값에 의한 호출을 사용하였기 때문에 increaseBy() 함수의 목적대로 실행되지 않은것 입니다.

따라서 increaseBy() 함수의 매개변수를 참조에 의한 호출을 사용하여 받으면 main() 함수의 목적을 달성할 수 있을 것입니다.
