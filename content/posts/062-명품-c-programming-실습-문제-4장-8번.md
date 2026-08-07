---
title: "명품 C++ programming 실습 문제 4장 8번"
date: 2020-03-04T16:23:04+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "programming", "객체배열", "객체포인터", "동적배열", "동적할당", "명품", "프로그래밍"]
---<b>문제 :</b>

실습 문제 7의 문제를 수정해보자. 사용자로부터 다음과 같이 원의 개수를 입력받고, 원의 개수만큼 반지름을 입력받는 방식으로 수정하라.

원의 개수에 따라 동적으로 배열을 할당받아야 한다.

[2020/03/04 - [C++/명품 C++ programming] - 명품 C++ programming 실습 문제 4장 7번](https://sobamemil.tistory.com/61)

[명품 C++ programming 실습 문제 4장 7번

문제 : 다음과 같이 원을 추상화한 Circle 클래스가 있다. Circle 클래스와 main() 함수를 작성하고 3개의 Circle 객체를 가진 배열을 선언하고, 반지름 값을 입력받고 면적이 100보다 큰 원의 개수를 출력하는 프..

sobamemil.tistory.com](https://sobamemil.tistory.com/61)

<b>목적 및 힌트 :</b>

객체 배열 응용 연습

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/62/img_1.png)

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33 | #include<iostream>  using namespace std;    class Circle{  int radius;  public:  void setRadius(int radius);  double getArea();  };    void Circle::setRadius(int r){  radius = r;  }    double Circle::getArea(){  return radius \* radius \* 3.14;  }    int main() {  int r, num, cnt=0;  cout << "원의 개수 >> ";  cin >> num ;  Circle \*pArray = new Circle[num]; // 입력받은 num만큼 동적으로 객체 배열 생성  for(int i=0; i<num; i++){  cout << "원 " << i+1 << "의 반지름 >> ";  cin >> r;  pArray->setRadius(r);  if(pArray->getArea() > 100)  cnt++;  pArray++;  }  cout << "면적이 100보다 큰 원은 " << cnt << "개 입니다";  } |

<b>설명 :</b>

pArray++; 을 이용해서 다음 객체 포인터를 선택할 수 있습니다.
