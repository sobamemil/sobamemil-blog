---
title: "명품 C++ programming 실습 문제 3장 9번"
date: 2020-03-03T17:11:09+09:00
draft: false
categories: ["개발 CS", "C++ 프로그래밍"]
tags: ["C++", "programming", "구현부", "명품", "생성자", "선언부", "소멸자", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

Oval 클래스는 주어진 사각형에 내접하는 타원을 추상화한 클래스이다.

Oval 클래스의 멤버는 모두 다음과 같다. Oval 클래스를 선언부와 구현부로 나누어 작성하라.

● 정수값의 사각형 너비와 높이를 가지는 width, height 변수 멤버

● 너비와 높이 값을 매개 변수로 받는 생성자

● 너비와 높이를 1로 초기화하는 매개 변수 없는 생성자

● width와 height를 출력하는 소멸자

● 타원이 너비를 리턴하는 getWidth() 함수 멤버

● 타원의 높이를 리턴하는 getHeight() 함수 멤버

● 타원의 너비와 높이를 변경하는 set(int w, int h) 함수 멤버

● 타원의 너비와 높이를 화면에 출력하는 show() 함수 멤버

Oval 클래스를 활용하는 코드의 사례와 실행 결과는 다음과 같다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | #include<iostream>  using namespace std;    int main() {  Oval a, b(3,4);  a.set(10, 20);  a.show();  cout << b.getWidth() << "," << b.getHeight() << endl;  } |

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/51/img_1.png)

<b>목적 및 힌트 :</b>

생성자/소멸자를 갖춘 클래스 만들기, 선언부와 구현부로 나누어 작성

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49 | #include<iostream>  using namespace std;    class Oval{  private:  int width, height;  public:  Oval();  Oval(int a, int b);  int getWidth();  int getHeight();  void set(int w, int h);  void show();  ~Oval();  };    Oval::Oval(){  width = 1;  height = 1;  }  Oval::Oval(int a, int b){  width = a;  height = b;  }  int Oval::getWidth(){  return width;  }  int Oval::getHeight(){  return height;  }  void Oval::set(int w, int h){  width = w;  height = h;  }    void Oval::show(){  cout << "width = " << width << ", height = " << height << endl;  }    Oval::~Oval(){  cout << "Oval 소멸 : width = " << width << ", height = " << height << endl;  }    int main() {  Oval a, b(3,4);  a.set(10, 20);  a.show();  cout << b.getWidth() << "," << b.getHeight() << endl;  } |

<b>설명 :</b>

구현부를 클래스 내부가 아닌 외부에 작성하여 선언부와 구현부를 나누어 작성하였습니다.

한 클래스에서 생성자는 여러 개 일 수 있지만 소멸자는 하나만 존재할 수 있습니다
