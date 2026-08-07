---
title: "C++ Programming Ch.4 Exercise 10 Solution"
date: 2020-03-04T17:03:15+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["10번", "4장", "C++", "programming", "명품", "실습문제", "연습문제", "프로그래밍"]
---

**Problem:**

다음에서 Person은 사람을, Family는 가족을 추상화한 클래스로서 완성되지 않은 클래스이다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15 | class Person {  string name;  public:  Person(string name) { this->name = name;}  string getName() { return name;}  };    class Family {  Person \*p; // Person 배열 포인터  int size; // Person 배열의 크기. 가족 구성원 수  public:  Family(string name, int size); // size 개수만큼 Person 배열 동적 생성  void show(); // 모든 가족 구성원 출력  ~Family();  }; |

다음 main()이 작동하도록 Person과 Family 클래스에 필요한 멤버들을 추가하고 코드를 완성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8 | int main() {  Family \*simpson = new Family("Simpson", 3); // 3명으로 구성된 Simpson 가족  simpson->setName(0, "Mr. Simpson");  simpson->setName(1, "Mrs. Simpson");  simpson->setName(2, "Bart Simpson");  simpson->show();  delete simpson;  } |

<b>Objective & Hints:</b>

객체의 동적 생성 및 소멸 응용

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/64/img_1.png)

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53 | #include<iostream>  #include<string>  using namespace std;    class Person {  string name;  public:  Person() {};  Person(string name) { this->name = name;}  string getName() { return name;}  void setName(string name) { this->name = name;}  };    class Family {  Person \*p; // Person 배열 포인터  int size; // Person 배열의 크기. 가족 구성원 수  string name;  public:  Family(string name, int size); // size 개수만큼 Person 배열 동적 생성  void setName(int num, string name);  void show(); // 모든 가족 구성원 출력  ~Family();  };    Family::Family(string name, int size){  p = new Person[size];  this->size = size;  this->name = name;  }    void Family::setName(int num, string name){  p[num].setName(name);  }    void Family::show(){  cout << name << "가족은 다음과 같이 " << size << "명 입니다.\n";  for(int i=0; i<size; i++){  cout << p[i].getName() << "\t";  }  }    Family::~Family(){  delete [] p;  }    int main() {  Family \*simpson = new Family("Simpson", 3); // 3명으로 구성된 Simpson 가족  simpson->setName(0, "Mr. Simpson");  simpson->setName(1, "Mrs. Simpson");  simpson->setName(2, "Bart Simpson");  simpson->show();  delete simpson;  } |
