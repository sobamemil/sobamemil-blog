---
title: "명품 C++ programming 실습 문제 7장 4번"
date: 2020-03-06T17:45:53+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "friend", "programming", "명품", "실습문제", "연산자", "연습문제", "키워드", "프렌드", "프로그래밍"]
---

**문제 :**

1번 ~ 4번 문제까지 사용될 Book 클래스는 다음과 같습니다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | class Book{  string title;  int price, pages;  public:  Book(string title="", int price=0, int pages=0){  this->title = title; this->price = price; this->pages = pages;  }  void show() {  cout << title << " " << price << "원 " << pages << " 페이지" << endl;  }  string getTitle() {  return title;  }  }; |

다음 연산을 통해 책의 제목을 사전 순으로 비교하고자 한다.

< 연산자를 작성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8 | int main() {  Book a("청춘" , 2000 , 300);  string b;  cout << "책 이름을 입력하세요>>";  getline(cin, b); // 키보드로부터 문자열로 책 이름을 입력 받음  if(b < a)  cout << a.getTitle() << "이 " << b << "보다 뒤에 있구나!" << endl;  } |

**실행 결과 :**

![](https://img.sobamemil.com/posts/93/img_1.png)

**목적 및 힌트 :**

< 연산자 구현 연습

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33 | #include<iostream>  using namespace std;    class Book{  string title;  int price, pages;  public:  Book(string title="", int price=0, int pages=0){  this->title = title; this->price = price; this->pages = pages;  }  void show() {  cout << title << " " << price << "원 " << pages << " 페이지" << endl;  }  string getTitle() {  return title;  }  friend bool operator< (string b, Book& a);  };    bool operator< (string b, Book& a){  if(b < a.title)  return true;  return false;  }    int main() {  Book a("청춘" , 2000 , 300);  string b;  cout << "책 이름을 입력하세요>>";  getline(cin, b); // 키보드로부터 문자열로 책 이름을 입력 받음  if(b < a)  cout << a.getTitle() << "이 " << b << "보다 뒤에 있구나!" << endl;  } |

**설명 :**

< 연산자 함수를 클래스 외부 함수로 작성하고 클래스 내부에서 friend로 선언을 해주었습니다.

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 7장 6번](/95)  (1) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 5번](/94)  (1) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 3번](/92)  (1) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 2번](/91)  (3) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 1번](/90)  (3) | 2020.03.06 |