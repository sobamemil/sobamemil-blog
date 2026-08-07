---
title: "명품 C++ programming 실습 문제 3장 3번"
date: 2020-03-02T17:56:41+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["Account", "C++", "programming", "명품", "실습문제", "연습문제", "클래스", "프로그래밍", "함수"]
---

**문제 :**

은행에서 사용하는 프로그램을 작성하기 위해, 은행 계좌 하나를 표현하는 클래스 Account가 필요하다.

계좌 정보는 계좌의 주인, 계좌 번호, 잔액을 나타내는 3 멤버 변수로 이루어진다.

main() 함수의 실행과 결과가 다음과 같도록 Account 클래스를 작성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10 | #include <iostream>  using namespace std;    int main() {  Account a("Kitae", 1, 5000); // id 1번, 잔액 5000원, 이름이 Kitae인 계좌 성  a.deposit(50000); // 50000원 저금  cout << a.getOwner() << "의 잔액은 " << a.inquiry() << endl;  int money = a.withdraw(20000); // 20000원 출금. withdraw()는 출금한 실제 금액 리턴  cout << a.getOwner() << "의 잔액은 " << a.inquiry() << endl;  } |

**실행 결과 :**

![](https://img.sobamemil.com/posts/45/img_1.png)

**목적 및 힌트 :**

실세계의 객체를 클래스로 작성

Account는 name, id, balance(잔액)의 3 멤버 변수와 생성자, getOwner(), deposit(), withdraw(), inquiry()의 3 멤버 함수를 가지는 클래스로 만들면 된다.

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48 | #include<iostream>  #include<string>  using namespace std;    class Account{  private:  string name;  int id;  int money;  public:  Account(string s,int a, int b);  void deposit(int a);  string getOwner();  int withdraw(int a);  int inquiry();    };    Account::Account(string s, int a, int b){  name = s;  id = a;  money = b;  }    void Account::deposit(int a){  money += a;  }    string Account::getOwner(){  return name;  }    int Account::withdraw(int a){  money -= a;  return a;  }    int Account::inquiry(){  return money;  }    int main(){  Account a("Kitae", 1, 5000);  a.deposit(50000);  cout << a.getOwner() << "의 잔액은 " << a.inquiry() << endl;  int money = a.withdraw(20000);  cout << a.getOwner() << "의 잔액은 " << a.inquiry() << endl;  } |

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 3장 5번](/47)  (4) | 2020.03.03 |
| [명품 C++ programming 실습 문제 3장 4번](/46)  (8) | 2020.03.03 |
| [명품 C++ programming 실습 문제 3장 2번](/44)  (2) | 2020.03.02 |
| [명품 C++ programming 실습 문제 3장 1번](/43)  (1) | 2020.03.02 |
| [명품 C++ programming 실습 문제 2장 16번](/42)  (3) | 2020.02.28 |