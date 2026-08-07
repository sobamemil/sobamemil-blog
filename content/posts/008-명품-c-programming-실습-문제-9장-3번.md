---
title: "명품 C++ programming 실습 문제 9장 3번"
date: 2019-11-21T00:53:08+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["2019", "2020", "3번", "9장", "C++", "programming", "명품", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

다음 추상 클래스 LoopAdder가 있다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31 | class LoopAdder { // 추상 클래스  string name; // 루프의 이름  int x, y, sum; // x에서 y까지의 합은 sum  void read(); // x, y 값을 읽어 들이는 함수  void write(); // sum을 출력하는 함수  protected:  LoopAdder(string name="") { // 루프의 이름을 받는다. 초깃값은 ""  this->name = name;  }  int getX() { return x; }  int getY() { return y; }  virtual int calculate() = 0; // 순수 가상 함수. 루프를 돌며 합을 구하는 함수  public:  void run(); // 연산을 진행하는 함수  };    void LoopAdder::read() { // x, y 입력  cout << name << ":" << endl;  cout << "처음 수에서 두번째 수까지 더한다. 두 수를 입력하세요 >> ";  cin >> x >> y;  }    void LoopAdder::write() { // 결과 sum 출력  cout << x << "에서 " << y << "까지의 합 = " << sum << " 입니다" << endl;  }    void LoopAdder::run() {  read(); // x, y를 읽는다  sum = calculate(); // 루프를 돌면서 계산한다.  write(); // 결과 sum을 출력한다.  } |

LoopAdder 클래스를 상속받아 다음 main() 함수와 실행 결과처럼 되도록 ForLoopAdder 클래스를 작성하라. ForLoopAdder 클래스의 calculate() 함수는 for 문을 이용하여 합을 구한다.

|  |  |
| --- | --- |
| 1  2  3  4 | int main() {  ForLoopAdder forLoop("For Loop");  forLoop.run();  } |

![](https://img.sobamemil.com/posts/8/img_1.png)

**목적 및 힌트 :**

추상 클래스를 상속받는 파생 클래스 만들기

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52 | #include<iostream>  using namespace std;    class LoopAdder { // 추상 클래스  string name; // 루프의 이름  int x, y, sum; // x에서 y까지의 합은 sum  void read(); // x, y 값을 읽어 들이는 함수  void write(); // sum을 출력하는 함수  protected:  LoopAdder(string name="") { // 루프의 이름을 받는다. 초깃값은 ""  this->name = name;  }  int getX() { return x; }  int getY() { return y; }  virtual int calculate() = 0; // 순수 가상 함수. 루프를 돌며 합을 구하는 함수  public:  void run(); // 연산을 진행하는 함수  };    void LoopAdder::read() { // x, y 입력  cout << name << ":" << endl;  cout << "처음 수에서 두번째 수까지 더한다. 두 수를 입력하세요 >> ";  cin >> x >> y;  }    void LoopAdder::write() { // 결과 sum 출력  cout << x << "에서 " << y << "까지의 합 = " << sum << " 입니다" << endl;  }    void LoopAdder::run() {  read(); // x, y를 읽는다  sum = calculate(); // 루프를 돌면서 계산한다.  write(); // 결과 sum을 출력한다.  }    class ForLoopAdder : public LoopAdder {  string str;  public:  ForLoopAdder(string str="") : LoopAdder(str) { this->str = str; }  virtual int calculate() {  int sum=0;  int x = getX();  int y = getY();  for(; x<=y; x++) sum += x;  return sum;  }  };    int main() {  ForLoopAdder forLoop("For Loop");  forLoop.run();  } |

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 9장 6번](/11)  (1) | 2019.11.21 |
| [명품 C++ programming 실습 문제 9장 5번](/10)  (2) | 2019.11.21 |
| [명품 C++ programming 실습 문제 9장 4번](/9)  (3) | 2019.11.21 |
| [명품 C++ programming 실습 문제 9장 2번](/5)  (2) | 2019.11.20 |
| [명품 C++ programming 실습 문제 9장 1번](/4)  (1) | 2019.11.20 |