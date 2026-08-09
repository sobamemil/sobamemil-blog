---
title: "명품 C++ programming 실습 문제 7장 2번"
date: 2020-03-06T17:02:25+09:00
draft: false
categories: ["💻 개발 & CS", "C++ 프로그래밍"]
tags: ["==", "C++", "friend", "operator", "programming", "명품", "실습문제", "연산자", "연습문제", "프로그래밍"]
---

**문제 :**

1번 ~ 4번 문제까지 사용될 Book 클래스는 다음과 같습니다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | class Book{  string title;  int price, pages;  public:  Book(string title="", int price=0, int pages=0){  this->title = title; this->price = price; this->pages = pages;  }  void show() {  cout << title << " " << price << "원 " << pages << " 페이지" << endl;  }  string getTitle() {  return title;  }  }; |

Book 객체를 활용하는 사례이다.

|  |  |
| --- | --- |
| 1  2  3  4 | Book a("명품 C++" , 30000, 500), b("고품 C++", 30000, 500);  if(a == 30000) cout << "정가 30000원" << endl; // price 비교  if(a == "명품 C++") cout << "명품 C++ 입니다." << endl; // 책 title 비교  if(a == b) cout << "두 책이 같은 책입니다." << endl;  // title, price, pages 모두 비교 |

(1) 세 개의 == 연산자 함수를 가진 Book 클래스를 작성하라.

(2) 세 개의 == 연산자를 프렌드 함수로 작성하라.

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/91/img_1.png)

<b>목적 및 힌트 :</b>

== 연산자 구현 연습

<b>코드 :</b>

● 문제 (1)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43 | #include<iostream>  using namespace std;    class Book{  string title;  int price, pages;  public:  Book(string title="", int price=0, int pages=0){  this->title = title; this->price = price; this->pages = pages;  }  void show() {  cout << title << " " << price << "원 " << pages << " 페이지" << endl;  }  string getTitle() {  return title;  }  bool operator== (int a);  bool operator== (string a);  bool operator== (Book& a);  };    bool Book::operator==(int a){  if(price == a)  return true;  return false;  }  bool Book::operator==(string a){  if(title == a)  return true;  return false;  }  bool Book::operator==(Book& a){  if(this->price == a.price && this->title == a.title)  return true;  return false;  }    int main() {  Book a("명품 C++" , 30000, 500), b("고품 C++", 30000, 500);  if(a == 30000) cout << "정가 30000원" << endl; // price 비교  if(a == "명품 C++") cout << "명품 C++ 입니다." << endl; // 책 title 비교  if(a == b) cout << "두 책이 같은 책입니다." << endl;  // title, price, pages 모두 비교  } |

● 문제 (2)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43 | #include<iostream>  using namespace std;    class Book{  string title;  int price, pages;  public:  Book(string title="", int price=0, int pages=0){  this->title = title; this->price = price; this->pages = pages;  }  void show() {  cout << title << " " << price << "원 " << pages << " 페이지" << endl;  }  string getTitle() {  return title;  }  friend bool operator== (Book& b, int a);  friend bool operator== (Book& b, string a);  friend bool operator== (Book& b, Book& a);  };    bool operator==(Book& b, int a){  if(b.price == a)  return true;  return false;  }  bool operator==(Book& b, string a){  if(b.title == a)  return true;  return false;  }  bool operator==(Book& b, Book& a){  if(b.price == a.price && b.title == a.title)  return true;  return false;  }    int main() {  Book a("명품 C++" , 30000, 500), b("고품 C++", 30000, 500);  if(a == 30000) cout << "정가 30000원" << endl; // price 비교  if(a == "명품 C++") cout << "명품 C++ 입니다." << endl; // 책 title 비교  if(a == b) cout << "두 책이 같은 책입니다." << endl; // title, price, pages 모두 비교  } |
