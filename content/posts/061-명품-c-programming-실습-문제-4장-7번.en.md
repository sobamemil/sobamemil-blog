---
title: "C++ Programming Ch.4 Exercise 7 Solution"
date: 2020-03-04T16:13:47+09:00
draft: false
categories: ["Dev CS", "C++ Programming"]
tags: ["C++", "circle", "programming", "Object Array", "Dynamic Array", "Masterpiece", "Practice Problem", "Exercise", "Programming"]
---

**Problem:**

다음과 같이 원을 추상화한 Circle 클래스가 있다.

Circle 클래스와 main() 함수를 작성하고 3개의 Circle 객체를 가진 배열을 선언하고, 반지름 값을 입력받고 면적이 100보다 큰 원의 개수를 출력하는 프로그램을 완성하라.

Circle 클래스도 완성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6 | class Circle {  int radius; // 원의 반지름 값  public:  void setRadius(int radius); // 반지름을 설정한다.  double getArea(); // 면적을 리턴한다.  }; |

<b>Objective & Hints:</b>

객체 배열 다루기 연습

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/61/img_1.png)

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31 | #include<iostream>  using namespace std;    class Circle {  int radius; // 원의 반지름 값  public:  void setRadius(int radius); // 반지름을 설정한다.  double getArea(); // 면적을 리턴한다.  };    void Circle::setRadius(int r){  radius = r;  }    double Circle::getArea(){  return radius \* radius \* 3.14;  }    int main() {  int cnt=0, r;  Circle \*pArray = new Circle[3]; // 동적으로 객체 배열 생성  for(int i=0; i<3; i++){  cout << "원 " << i+1 << "의 반지름 >> ";  cin >> r;  pArray[i].setRadius(r);  if(pArray[i].getArea() > 100) // 면적이 100보다 크면 카운트  cnt++;  }  cout << "면적이 100보다 큰 원은 " << cnt << "개 입니다";  delete pArray;  } |
