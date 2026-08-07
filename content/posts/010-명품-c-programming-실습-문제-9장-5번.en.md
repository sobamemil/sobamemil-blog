---
title: "명품 C++ programming 실습 문제 9장 5번"
date: 2019-11-21T01:46:15+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: []
---

<b>문제 :</b>

디지털 회로에서 기본적인 게이트로 OR 게이트, AND 게이트, XOR 게이트 등이 있다. 이들은 각각 두 입력 신호를 받아 OR 연산, AND 연산, XOR 연산을 수행한 결과를 출력한다. 이 게이트들을 각각 ORGate, XORGate, ANDGate 클래스로 작성하고자 한다. ORGate, XORGate, ANDGate 클래스가 AbstractGatef를 상속받도록 작성하라.

![](https://img.sobamemil.com/posts/10/img_1.png)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7 | class AbstractGate { // 추상 클래스  protected:  bool x, y;  public:  void set(bool x, bool y) { this->x = x; this->y = y; }  virtual bool operation()=0;  };  [Colored by Color Scripter](http://colorscripter.com/info#e) |

ANDGate, ORGate, XORGate를 활용하는 사례와 결과는 다음과 같다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11 | ANDGate andGate;  ORGate orGate;  XORGate xorGate;    andGate.set(true, false);  orGate.set(true, false);  xorGate.set(true, false);  cout.setf(ios::boolalpha); // 불린 값을 "true", "false" 문자열로 출력할 것을 지시  cout << andGate.operation() << endl; // AND 결과는 false  cout << orGate.operation() << endl;     // OR 결과는 true  cout << xorGate.operation() << endl; // XOR 결과는 true |

![](https://img.sobamemil.com/posts/10/img_2.png)

<b>목</b><b>적 및 힌트 :</b>

추상 클래스를 상속받는 파생 클래스 만들기

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51 | #include<iostream>  using namespace std;    class AbstractGate { // 추상 클래스  protected:  bool x, y;  public:  void set(bool x, bool y) { this->x = x; this->y = y; }  virtual bool operation()=0;  };    class ANDGate : public AbstractGate {  public:  virtual bool operation() {  if(x == true && y == true)  return true;  else return false;  }  };    class ORGate : public AbstractGate {  public:  virtual bool operation() {  if(x == true || y == true)  return true;  else return false;  }  };    class XORGate : public AbstractGate {  public:  virtual bool operation() {  if(x != y)  return true;  else return false;  }  };    int main() {  ANDGate andGate;  ORGate orGate;  XORGate xorGate;    andGate.set(true, false);  orGate.set(true, false);  xorGate.set(true, false);  cout.setf(ios::boolalpha); // 불린 값을 "true", "false" 문자열로 출력할 것을 지시  cout << andGate.operation() << endl; // AND 결과는 false  cout << orGate.operation() << endl;     // OR 결과는 true  cout << xorGate.operation() << endl; // XOR 결과는 true  }  [Colored by Color Scripter](http://colorscripter.com/info#e) |


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 9장 7번](/13)  (1) | 2019.11.21 |
| [명품 C++ programming 실습 문제 9장 6번](/11)  (1) | 2019.11.21 |
| [명품 C++ programming 실습 문제 9장 4번](/9)  (3) | 2019.11.21 |
| [명품 C++ programming 실습 문제 9장 3번](/8)  (2) | 2019.11.21 |
| [명품 C++ programming 실습 문제 9장 2번](/5)  (2) | 2019.11.20 |