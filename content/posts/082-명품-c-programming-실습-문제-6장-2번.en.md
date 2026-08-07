---
title: "명품 C++ programming 실습 문제 6장 2번"
date: 2020-03-05T16:44:47+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "overloading", "programming", "디폴트", "매개변수", "명품", "실습문제", "연습문제", "프로그래밍", "함수중복"]
---

**문제 :**

Person 클래스의 객체를 생성하는 main() 함수는 다음과 같다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | class Person {  int id;  double weight;  string name;  public:  void show() { cout << id << ' ' << weight << ' ' << name << endl; }  };    int main() {  Person grace, ashley(2, "Ashley"), helen(3, "Helen", 32.5);  grace.show();  ashley.show();  helen.show();  } |

(1) 생성자를 중복 작성하고 프로그램을 완성하라.

(2) 디폴트 매개 변수를 가진 하나의 생성자를 작성하고 프로그램을 완성하라.

**실행 결과 :**

![](https://img.sobamemil.com/posts/82/img_1.png)

**목적 및 힌트 :**

함수 중복, 디폴트 매개 변수 연습

**코드 :**

● 문제 (1)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39 | #include<iostream>  #include<string>  using namespace std;    class Person {  int id;  double weight;  string name;  public:  Person();  Person(int id, string name);  Person(int id, string name, double weight);  void show() { cout << id << ' ' << weight << ' ' << name << endl; }  };    Person::Person() {  id = 1;  weight = 20.5;  name = "Grace";  }    Person::Person(int id, string name) {  this->id = id;  weight = 20.5;  this->name = name;  }    Person::Person(int id, string name, double weight) {  this->id = id;  this->weight = weight;  this->name = name;  }    int main() {  Person grace, ashley(2, "Ashley"), helen(3, "Helen", 32.5);  grace.show();  ashley.show();  helen.show();  } |

● 문제 (2)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25 | #include<iostream>  #include<string>  using namespace std;    class Person {  int id;  double weight;  string name;  public:  Person(int id = 1, string name = "Grace", double weight = 20.5);  void show() { cout << id << ' ' << weight << ' ' << name << endl; }  };    Person::Person(int id, string name, double weight){  this->id = id;  this->weight = weight;  this->name = name;  }    int main() {  Person grace, ashley(2, "Ashley"), helen(3, "Helen", 32.5);  grace.show();  ashley.show();  helen.show();  } |

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 6장 4번](/84)  (2) | 2020.03.06 |
| [명품 C++ programming 실습 문제 6장 3번](/83)  (1) | 2020.03.05 |
| [명품 C++ programming 실습 문제 6장 1번](/81)  (1) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 12번](/80)  (2) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 11번](/79)  (1) | 2020.03.05 |