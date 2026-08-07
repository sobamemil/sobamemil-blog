---
title: "명품 C++ programming 실습 문제 7장 3번"
date: 2020-03-06T17:13:07+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["!연산자", "C++", "operator", "programming", "멤버함수", "명품", "실습문제", "연습문제", "프로그래밍"]
---

<b>문제 :</b>

1번 ~ 4번 문제까지 사용될 Book 클래스는 다음과 같습니다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | class Book{  string title;  int price, pages;  public:  Book(string title="", int price=0, int pages=0){  this->title = title; this->price = price; this->pages = pages;  }  void show() {  cout << title << " " << price << "원 " << pages << " 페이지" << endl;  }  string getTitle() {  return title;  }  }; |

다음 연산을 통해 공짜 책인지를 판별하도록 ! 연산자를 작성하라.

|  |  |
| --- | --- |
| 1  2 | Book book("벼룩시장" , 0 , 50); // 가격은 0  if(!book) cout << "공짜다" << endl; |

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/92/img_1.png)

<b>목적 및 힌트 :</b>

! 연산자 구현 연습

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29 | #include<iostream>  using namespace std;    class Book{  string title;  int price, pages;  public:  Book(string title="", int price=0, int pages=0){  this->title = title; this->price = price; this->pages = pages;  }  void show() {  cout << title << " " << price << "원 " << pages << " 페이지" << endl;  }  string getTitle() {  return title;  }  bool operator! ();  };    bool Book::operator!(){  if(price == 0)  return true;  return false;  }    int main() {  Book book("벼룩시장" , 0 , 50); // 가격은 0  if(!book) cout << "공짜다" << endl;  } |

<b>설명 :</b>

! 연산자 함수를 클래스의 멤버 함수로 구현 하였습니다.

가격을 비교하여 0이면 true를 return하고 0이 아니면 false를 return하면 됩니다.

가격은 음수가 아니라고 가정했습니다.
