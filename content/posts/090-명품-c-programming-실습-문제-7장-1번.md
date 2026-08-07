---
title: "명품 C++ programming 실습 문제 7장 1번"
date: 2020-03-06T16:54:56+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "friend", "programming", "명품", "실습문제", "연산자함수", "연습문제", "프렌드키워드", "프렌드함수", "프로그래밍"]
---

**문제 :**

1번 ~ 4번 문제까지 사용될 Book 클래스는 다음과 같습니다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | class Book{  string title;  int price, pages;  public:  Book(string title="", int price=0, int pages=0){  this->title = title; this->price = price; this->pages = pages;  }  void show() {  cout << title << " " << price << "원 " << pages << " 페이지" << endl;  }  string getTitle() {  return title;  }  }; |

Book 객체에 대해 다음 연산을 하고자 한다.

|  |  |
| --- | --- |
| 1  2  3  4  5 | Book a("청춘", 20000, 300) , b("미래", 30000, 500);  a += 500; // 책 a의 가격 500원 증가  b -= 500; // 책 b의 가격 500원 감소  a.show();  b.show(); |

(1) +=, -= 연산자 함수를 Book 클래스의 멤버 함수로 구현하라.

(2) +=, -= 연산자 함수를 Book 클래스 외부 함수로 구현하라.

**실행 결과 :**

![](https://img.sobamemil.com/posts/90/img_1.png)

**목적 및 힌트 :**

+=, -=, 참조 매개 변수, 참조 리턴의 연산자 구현 연습

**코드 :**

● 문제 (1)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36 | #include<iostream>  using namespace std;    class Book{  string title;  int price, pages;  public:  Book(string title="", int price=0, int pages=0){  this->title = title; this->price = price; this->pages = pages;  }  void show() {  cout << title << " " << price << "원 " << pages << " 페이지" << endl;  }  string getTitle() {  return title;  }  Book& operator+= (int a);  Book& operator-= (int a);  };    Book& Book::operator+=(int a) {  price += a;  return \*this;  }  Book& Book::operator-=(int a) {  price -= a;  return \*this;  }    int main() {  Book a("청춘", 20000, 300) , b("미래", 30000, 500);  a += 500;  b -= 500;  a.show();  b.show();  } |

● 문제 (2)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36 | #include<iostream>  using namespace std;    class Book{  string title;  int price, pages;  public:  Book(string title="", int price=0, int pages=0){  this->title = title; this->price = price; this->pages = pages;  }  void show() {  cout << title << " " << price << "원 " << pages << " 페이지" << endl;  }  string getTitle() {  return title;  }  friend Book operator+= (Book& b,int a);  friend Book operator-= (Book& b,int a);  };    Book operator+=(Book& b, int a) {  b.price += a;  return b;  }  Book operator-=(Book& b,int a) {  b.price -= a;  return b;  }    int main() {  Book a("청춘", 20000, 300) , b("미래", 30000, 500);  a += 500;  b -= 500;  a.show();  b.show();  } |

**설명 :**

문제 1번에서는 +=, -= 연산자 함수를 Book 클래스의 멤버 함수로 구현하였고,

문제 2번에서는 +=, -= 연산자 함수를 Book 클래스 외부 함수로 구현하였습니다.

연산자 함수를 클래스 외부 함수로 구현하기 위해 클래스 내부에서 friend로 선언을 해주었습니다.

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 7장 3번](/92)  (1) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 2번](/91)  (3) | 2020.03.06 |
| [명품 C++ programming 실습 문제 6장 9번](/89)  (2) | 2020.03.06 |
| [명품 C++ programming 실습 문제 6장 8번](/88)  (1) | 2020.03.06 |
| [명품 C++ programming 실습 문제 6장 7번](/87)  (1) | 2020.03.06 |