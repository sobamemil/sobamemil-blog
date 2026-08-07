---
title: "명품 C++ programming 실습 문제 11장 9번"
date: 2020-04-02T14:00:37+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "iostream", "programming", "명품", "실습문제", "연산자중복", "연습문제", "입력스트림", "출력스트림", "프로그래밍"]
---

**문제 :**

다음은 Phone 클래스이다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11 | class Phone { // 전화 번호를 표현하는 클래스  string name;  string telnum;  string address;  public:  Phone(string name="", string telnum="", string address="") {  this->name = name;  this->telnum = telnum;  this->address = address;  }  }; |

Phone 클래스의 객체를 입출력하는 아래 코드와 실행 결과를 참조하여 <<, >> 연산자를 작성하고 Phone 클래스를 수정하는 등 프로그램을 완성하라.

|  |  |
| --- | --- |
| 1  2  3 | Phone girl, boy;  cin >> girl >> boy;  cout << girl << endl << boy << endl; |

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/140/img_1.png)

<b>목적 및 힌트 :</b>

스트림 입출력 연산자( <<, >> ) 작성 연습

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37 | #include <iostream>  using namespace std;    class Phone { // 전화 번호를 표현하는 클래스  string name;  string telnum;  string address;  public:  Phone(string name="", string telnum="", string address="") {  this->name = name;  this->telnum = telnum;  this->address = address;  }  friend ostream& operator << (ostream& os, Phone p); // friend 작성  friend istream& operator >> (istream& ins, Phone& p); // friend 작성, Phone& p 참조자 사용  };    ostream& operator << (ostream& os, Phone p) {  os << "(" << p.name << "," << p.telnum << "," << p.address << ")";  return os;  }    istream& operator >> (istream& ins, Phone& p) {  cout << "이름:";  ins >> p.name;  cout << "전화번호:";  ins >> p.telnum;  cout << "주소:";  ins >> p.address;  return ins;  }    int main() {  Phone girl, boy;  cin >> girl >> boy; // 전화 번호를 키보드로부터 읽는다.  cout << girl << endl << boy << endl; // 전화 번호를 출력한다.  } |


](
