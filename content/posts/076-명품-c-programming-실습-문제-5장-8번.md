---
title: "명품 C++ programming 실습 문제 5장 8번"
date: 2020-03-05T15:19:47+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "Copy", "programming", "명품", "복사", "복사생성자", "실습문제", "연습문제", "참조", "프로그래밍"]
---

**문제 :**

문제 7번의 MyIntStack을 수정하여 다음과 같이 선언하였다.

스택에 저장할 수 있는 정수의 최대 개수는 생성자에서 주어지고 size 멤버에 유지한다.

MyIntStack 클래스를 작성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | class MyIntStack{  int \*p; // 스택 메모리로 사용할 포인터  int size; // 스택의 최대 크기  int tos; // 스택의 탑을 가리키는 인덱스  public:  MyIntStack();  MyIntStack(int size);  MyIntStack(const MyIntStack& s); // 복사 생성자  ~MyIntStack();  bool push(int n); // 정수 n을 스택에 푸시한다.  // 스택이 꽉 차 있으면 false를, 아니면 true 리턴  bool pop(int &n); // 스택의 탑에 있는 값을 n에 팝한다.  // 만일 스택이 비어 있으면 false를, 아니면 true 리턴  }; |

MyIntStack 클래스를 활용하는 코드와 실행 결과는 다음과 같다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13 | int main () {  MyIntStack a(10);  a.push(10);  a.push(20);  MyIntStack b = a; // 복사 생성  b.push(30);    int n;  a.pop(n); // 스택 a 팝  cout << "스택 a에서 팝한 값 " << n << endl;  b.pop(n); // 스택 b 팝  cout << "스택 b에서 팝한 값 " << n << endl;  } |

**실행 결과 :**

![](https://img.sobamemil.com/posts/76/img_1.png)

[2020/03/05 - [C++/명품 C++ programming] - 명품 C++ programming 실습 문제 5장 7번](https://sobamemil.tistory.com/75)

[명품 C++ programming 실습 문제 5장 7번

문제 : 다음과 같이 선언된 정수를 저장하는 스택 클래스 MyIntStack을 구현하라. MyIntStack 스택에 저장할 수 있는 정수의 최대 개수는 10이다. 1 2 3 4 5 6 7 8 class MyIntStack{ int p[10]; // 최대 10개의..

sobamemil.tistory.com](https://sobamemil.tistory.com/75)

**목적 및 힌트 :**

복사 생성자 활용

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69 | #include<iostream>  #include<cstring>  using namespace std;    class MyIntStack{  int \*p; // 스택 메모리로 사용할 포인터  int size; // 스택의 최대 크기  int tos; // 스택의 탑을 가리키는 인덱스  public:  MyIntStack();  MyIntStack(int size);  MyIntStack(const MyIntStack& s); // 복사 생성자  ~MyIntStack();  bool push(int n); // 정수 n을 스택에 푸시한다.  // 스택이 꽉 차 있으면 false를, 아니면 true 리턴  bool pop(int &n); // 스택의 탑에 있는 값을 n에 팝한다.  // 만일 스택이 비어 있으면 false를, 아니면 true 리턴  };    MyIntStack::MyIntStack(int size){  this->size = size;  p = new int [size];  tos = 0;  }    MyIntStack::MyIntStack(const MyIntStack& s){  this->p = new int [s.size];  this->size = s.size;  this->tos = s.tos;  for(int i=0; i <= s.tos; i++)  this->p[i] = s.p[i];  }    bool MyIntStack::push(int n){  if(tos>size)  return false;  else {  p[tos++] = n;  return true;  }  }    bool MyIntStack::pop(int &n){  if(tos<0)  return false;  else {  n = p[--tos];  return true;  }  }    MyIntStack::~MyIntStack(){  delete [] p; p = NULL;  }    int main () {  MyIntStack a(10);  a.push(10);  a.push(20);  MyIntStack b = a; // 복사 생성  b.push(30);    int n;  a.pop(n); // 스택 a 팝  cout << "스택 a에서 팝한 값 " << n << endl;  b.pop(n); // 스택 b 팝  cout << "스택 b에서 팝한 값 " << n << endl;  } |


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 5장 10번](/78)  (3) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 9번](/77)  (3) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 7번](/75)  (1) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 6번](/74)  (1) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 5번](/73)  (1) | 2020.03.05 |