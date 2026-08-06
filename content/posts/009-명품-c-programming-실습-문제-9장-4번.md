---
title: "명품 C++ programming 실습 문제 9장 4번"
date: 2019-11-21T01:08:27+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: []
---

**문제 :**

다음 추상 클래스 LoopAdder가 있다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31 | class LoopAdder { // 추상 클래스  string name; // 루프의 이름  int x, y, sum; // x에서 y까지의 합은 sum  void read(); // x, y 값을 읽어드리는 함수  void write(); // sum을 출력하는 함수  protected:  LoopAdder(string name="") { // 루프의 이름을 받는다. 초깃값은 ""  this->name = name;  }  int getX() { return x; }  int getY() { return y; }  virtual int calculate() = 0; // 순수 가상 함수. 루프를 돌며 합을 구하는 함수  public:  void run(); // 연산을 진행하는 함수  };    void LoopAdder::read() { // x, y 입력  cout << name << ":" << endl;  cout << "처음 수에서 두번째 수까지 더한다. 두 수를 입력하세요 >> ";  cin >> x >> y;  }    void LoopAdder::write() { // 결과 sum 출력  cout << x << "에서 " << y << "까지의 합 = " << sum << " 입니다" << endl;  }    void LoopAdder::run() {  read(); // x, y를 읽는다  sum = calculate(); // 루프를 돌면서 계산한다.  write(); // 결과 sum을 출력한다.  }  [Colored by Color Scripter](http://colorscripter.com/info#e) |

LoopAdder 클래스를 상속받아 다음 main() 함수와 실행 결과처럼 되도록 WhileLoopAdder, DoWhileLoopAdder 클래스를 작성하라. while 문, do-while 문을 이용하여 합을 구하도록 calculate() 함수를 각각 작성하면 된다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7 | int main() {  WhileLoopAdder whileLoop("While Loop");  DoWhileLoopAdder doWhileLoop("Do While Loop");    whileLoop.run();  doWhileLoop.run();  }  [Colored by Color Scripter](http://colorscripter.com/info#e) |

![](https://img.sobamemil.com/posts/9/img_1.png)

**목적 및 힌트 :**

추상 클래스를 상속받는 파생 클래스 만들기

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78 | #include<iostream>  using namespace std;    class LoopAdder { // 추상 클래스  string name; // 루프의 이름  int x, y, sum; // x에서 y까지의 합은 sum  void read(); // x, y 값을 읽어 들이는 함수  void write(); // sum을 출력하는 함수  protected:  LoopAdder(string name="") { // 루프의 이름을 받는다. 초깃값은 ""  this->name = name;  }  int getX() { return x; }  int getY() { return y; }  virtual int calculate() = 0; // 순수 가상 함수. 루프를 돌며 합을 구하는 함수  public:  void run(); // 연산을 진행하는 함수  };    void LoopAdder::read() { // x, y 입력  cout << name << ":" << endl;  cout << "처음 수에서 두번째 수까지 더한다. 두 수를 입력하세요 >> ";  cin >> x >> y;  }    void LoopAdder::write() { // 결과 sum 출력  cout << x << "에서 " << y << "까지의 합 = " << sum << " 입니다" << endl;  }    void LoopAdder::run() {  read(); // x, y를 읽는다  sum = calculate(); // 루프를 돌면서 계산한다.  write(); // 결과 sum을 출력한다.  }    class WhileLoopAdder : public LoopAdder {  string wloop;  public:  WhileLoopAdder(string wloop) : LoopAdder(wloop) {  this->wloop = wloop;  }  virtual int calculate() {  int tmp\_sum=0;  int tmp\_x = getX();  int tmp\_y = getY();  while(tmp\_x<=tmp\_y){  tmp\_sum += tmp\_x;  tmp\_x++;  }  return tmp\_sum;  }  };    class DoWhileLoopAdder : public LoopAdder {  string dwloop;  public:  DoWhileLoopAdder(string dwloop) : LoopAdder(dwloop) {  this->dwloop = dwloop;  }  virtual int calculate() {  int tmp\_sum=0;  int tmp\_x = getX();  int tmp\_y = getY();  do {  tmp\_sum += tmp\_x;  tmp\_x++;  }while(tmp\_x<=tmp\_y);  return tmp\_sum;  }  };    int main() {  WhileLoopAdder whileLoop("While Loop");  DoWhileLoopAdder doWhileLoop("Do While Loop");    whileLoop.run();  doWhileLoop.run();  }  [Colored by Color Scripter](http://colorscripter.com/info#e) |

공유하기

게시글 관리

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 9장 6번](/11)  (1) | 2019.11.21 |
| [명품 C++ programming 실습 문제 9장 5번](/10)  (2) | 2019.11.21 |
| [명품 C++ programming 실습 문제 9장 3번](/8)  (2) | 2019.11.21 |
| [명품 C++ programming 실습 문제 9장 2번](/5)  (2) | 2019.11.20 |
| [명품 C++ programming 실습 문제 9장 1번](/4)  (1) | 2019.11.20 |
