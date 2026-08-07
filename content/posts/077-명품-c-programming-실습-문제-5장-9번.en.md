---
title: "명품 C++ programming 실습 문제 5장 9번"
date: 2020-03-05T15:32:46+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["*this", "Accumulator", "C++", "programming", "reference", "명품", "실습문제", "연습문제", "참조", "프로그래밍"]
---

<b>Problem:</b>

클래스 Accumulator는 add() 함수를 통해 계속 값을 누적하는 클래스로서, 다음과 같이 선언된다.

Accumulator 클래스를 구현하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7 | class Accumulator{  int value;  public:  Accumulator(int value); // 매개 변수 value로 멤버 value를 초기화한다.  Accumulator& add(int n); // value에 n을 더해 값을 누적한다.  int get(); // 누적된 값 value를 리턴한다.  }; |

Accumulator는 다음과 같이 main() 함수에 의해 활용된다.

|  |  |
| --- | --- |
| 1  2  3  4  5 | int main() {  Accumulator acc(10);  acc.add(5).add(6).add(7); // acc의 value 멤버가 28이 된다.  cout << acc.get(); // 28 출력  } |

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/77/img_1.png)

<b>Objective & Hints:</b>

참조 리턴의 의미 이해

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29 | #include<iostream>  using namespace std;    class Accumulator{  int value;  public:  Accumulator(int value); // 매개 변수 value로 멤버 value를 초기화한다.  Accumulator& add(int n); // value에 n을 더해 값을 누적한다.  int get(); // 누적된 값 value를 리턴한다.  };    Accumulator::Accumulator(int value){  this->value = value; // 매개 변수 value로 멤버 value를 초기화.  }    Accumulator& Accumulator::add(int n){  value += n; // value에 n을 더해 값을 누적한다.  return \*this; // 자기 자신의 참조 리턴  }    int Accumulator::get(){  return value; // 누적된 값 value를 리턴한다.  }    int main() {  Accumulator acc(10);  acc.add(5).add(6).add(7); // acc의 value 멤버가 28이 된다.  cout << acc.get(); // 28 출력  } |

<b>Explanation:</b>

Accumulator 클래스의 add() 멤버 함수에서 자신의 참조를 리턴해 acc.add(5).add(6).add(7); 에서 처럼 연속으로 함수를 호출해도 프로그래머의 목적대로 실행될 수 있도록 하였습니다.


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 5장 11번](/79)  (1) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 10번](/78)  (3) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 8번](/76)  (9) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 7번](/75)  (1) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 6번](/74)  (1) | 2020.03.05 |