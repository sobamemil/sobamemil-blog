---
title: "C++ Programming Ch.5 Exercise 11 Solution"
date: 2020-03-05T16:00:14+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "char*", "programming", "string", "명품", "문자열", "실습문제", "얕은복사생성자", "연습문제", "프로그래밍"]
---

<b>Problem:</b>

책의 이름과 가격을 저장하는 다음 Book 클래스에 대해 물음에 답하여라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | class Book {  char \*title; // 제목 문자열  int price; // 가격  public:  Book(const char\* title, int price);  ~Book();  void set(char\* title, int price);  void show() { cout << title << ' ' << price << "원" << endl; }  }; |

(1) Book 클래스의 생성자, 소멸자, set() 함수를 작성하라. set() 함수는 멤버 변수 title에 할당된 메모리가 있으면 먼저 반환한다. 그러고 나서 새로운 메모리를 할당받고 이곳에 매개 변수로 전달받은 책이름을 저장한다.

(2) 컴파일러가 삽입하는 디폴트 복사 생성자 코드는 무엇인가?

(3) 디폴트 복사 생성자만 있을 때 아래 main() 함수는 실행 오류가 발생한다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7 | int main() {  Book cpp("명품 C++", 10000);  Book java = cpp; // 복사 생성자 호출됨  java.set("명품자바", 12000);  cpp.show();  java.show();  } |

다음과 같이 실행 오류가 발생하지 않도록 깊은 복사 생성자를 작성하라.

![](https://img.sobamemil.com/posts/79/img_1.png)

(4) 문제 (3)에서 실행 오류가 발생하는 원인은 Book 클래스에서 C-스트링(char\* title) 방식으로 문자열을 다루었기 때문이다.

복사 생성자를 작성하지 말고 문자열을 string 클래스를 사용하여, 문제 (3)의 실행 오류가 발생하지 않도록 Book 클래스를 수정하라.

이 문제를 풀고 나면 문자열을 다룰 때, string을 사용해야하는 이유를 명확히 알게 될 것이다.

<b>Objective & Hints:</b>

복사 생성자의 필요성 이해

<b>Code:</b>

● 문제 (1)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19 | Book::Book(const char\* title, int price){  this->price = price;  int size = strlen(title) + 1;  this->title = new char[size];  strcpy(this->title, title);  }    Book::~Book() {  delete [] title;  }    void Book::set(const char\* title, int price) {  if(this->title)  delete [] this->title;  this->price = price;  int size = strlen(title) + 1;  this->title = new char[size];  strcpy(this->title, title);  } |

● 문제 (2)

|  |  |
| --- | --- |
| 1  2  3  4 | Book::Book(const Book& b){  this->title = b.title;  this->price = b.price;  } |

● 문제 (3)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49 | #include<iostream>  #include<cstring>  using namespace std;    class Book {  char \*title; // 제목 문자열  int price; // 가격  public:  Book(const Book& b);  Book(const char\* title, int price);  ~Book();  void set(const char\* title, int price);  void show() { cout << title << ' ' << price << "원" << endl; }  };    Book::Book(const char\* title, int price){  this->price = price;  int size = strlen(title) + 1;  this->title = new char[size];  strcpy(this->title, title);  }    Book::Book(const Book& b){  this->price = b.price;  int size = strlen(b.title) + 1;  this->title = new char[size];  strcpy(this->title, b.title);  }    Book::~Book() {  delete [] title;  }    void Book::set(const char\* title, int price) {  if(this->title) delete [] this->title;  this->price = price;  int size = strlen(title) + 1;  this->title = new char[size];  strcpy(this->title, title);  }      int main() {  Book cpp("명품 C++", 10000);  Book java = cpp; // 복사 생성자 호출됨  java.set("명품자바", 12000);  cpp.show();  java.show();  } |

● 문제 (4)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31 | #include<iostream>  #include<cstring>  #include<string>  using namespace std;    class Book {  string title;  int price;  public:  Book(string title, int price);  void set(string title, int price);  void show() {cout << title << ' ' << price << "원" << endl;}  };    Book::Book(string title, int price){  this->price = price;  this->title = title;  }    void Book::set(string title, int price) {  this->price = price;  this->title = title;  }    int main() {  Book cpp("명품 C++", 10000);  Book java = cpp;  java.set("명품자바", 12000);  cpp.show();  java.show();  } |

<b>Explanation:</b>

문자열을 다룰 때 char\* 방식이 아닌 string 클래스를 사용하면 훨씬 간단하고 쉽게 다룰 수 있습니다.

또한 얕은 복사 생성자는 오류를 유발할 가능성이 농후하므로 되도록이면 깊은 복사 생성자를 작성하는 습관을 들이면 좋습니다.
