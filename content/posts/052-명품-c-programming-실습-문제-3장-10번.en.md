---
title: "C++ Programming Ch.3 Exercise 10 Solution"
date: 2020-03-03T17:52:41+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "Main", "programming", "구현부", "명품", "선언부", "실습문제", "연습문제", "프로그래밍", "헤더파일"]
---<b>Problem:</b>

다수의 클래스를 선언하고 활용하는 간단한 문제이다. 더하기(+), 빼기(-), 곱하기(\*), 나누기(/)를 수행하는 4개의 클래스를 Add, Sub, Mul, Div를 만들고자 한다.

이들은 모두 공통으로 다음 멤버를 가진다.

● int 타입 변수 a, b : 피연산자

● void setValue(int x, int y) 함수 : 매개 변수 x, y를 멤버 a, b에 복사

● int calculate() 함수 : 연산을 실행하고 결과 리턴

![](https://img.sobamemil.com/posts/52/img_1.png)

main() 함수는 Add, Sub, Mul, Div 클래스 타입의 객체 a, s, m, d를 생성하고, 아래와 같이 키보드로부터 두 개의 정수와 연산자를 입력받고, a, s, m, d 객체 중에서 연산을 처리할 객체의 setValue() 함수를 호출한 후, calculate()를 호출하여 결과를 화면에 출력한다.

프로그램은 무한 루프를 돈다.

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/52/img_2.png)

<b>Objective & Hints:</b>

클래스와 객체 활용 연습

<b>Code:</b>

(1) 클래스의 선언부와 구현부를 분리하고, 모든 코드를 Calculator.cpp 파일에 작성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91 | #include <iostream>  using namespace std;    class Add{  private:  int a, b;  public:  void setValue(int x, int y);  int calculate();  };  void Add::setValue(int x, int y){  a = x;  b = y;  }  int Add::calculate(){  return a + b;  }    class Sub{  private:  int a, b;  public:  void setValue(int x, int y);  int calculate();  };  void Sub::setValue(int x, int y){  a = x;  b = y;  }  int Sub::calculate(){  return a - b;  }    class Mul{  private:  int a, b;  public:  void setValue(int x, int y);  int calculate();  };  void Mul::setValue(int x, int y){  a = x;  b = y;  }  int Mul::calculate(){  return a \* b;  }    class Div{  private:  int a, b;  public:  void setValue(int x, int y);  int calculate();  };  void Div::setValue(int x, int y){  a = x;  b = y;  }  int Div::calculate(){  return a / b;  }    int main() {  Add a;  Sub s;  Mul m;  Div d;  int x, y;  char c;  while(true){  cout << "두 정수와 연산자를 입력하세요>>";  cin >> x >> y >> c;  if(c == '+') {  a.setValue(x,y);  cout << a.calculate() << endl;  }  else if(c == '-') {  s.setValue(x,y);  cout << s.calculate() << endl;  }  else if(c == '\*') {  m.setValue(x,y);  cout << m.calculate() << endl;  }  else if(c == '/') {  d.setValue(x,y);  cout << d.calculate() << endl;  }  }  } |

(2) 클래스의 선언부와 구현부를 헤더 파일과 cpp 파일로 나누어 프로그램을 작성하라.

<b>●</b>3-10.h

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31 | class Add{  private:  int a, b;  public:  void setValue(int x, int y);  int calculate();  };    class Div{  private:  int a, b;  public:  void setValue(int x, int y);  int calculate();  };    class Mul{  private:  int a, b;  public:  void setValue(int x, int y);  int calculate();  };    class Sub{  private:  int a, b;  public:  void setValue(int x, int y);  int calculate();  }; |

● 3-10.cpp

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33 | #include<iostream>  using namespace std;    #include "3-10.h"    void Add::setValue(int x, int y){  a = x;  b = y;  }  int Add::calculate(){  return a + b;  }  void Sub::setValue(int x, int y){  a = x;  b = y;  }  int Sub::calculate(){  return a - b;  }  void Mul::setValue(int x, int y){  a = x;  b = y;  }  int Mul::calculate(){  return a \* b;  }  void Div::setValue(int x, int y){  a = x;  b = y;  }  int Div::calculate(){  return a / b;  } |

● main.cpp

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34 | #include<iostream>  using namespace std;    #include "3-10.h"    int main() {  Add a;  Sub s;  Mul m;  Div d;  int x, y;  char c;    while(true){  cout << "두 정수와 연산자를 입력하세요>>";  cin >> x >> y >> c;  if(c == '+') {  a.setValue(x,y);  cout << a.calculate() << endl;  }  else if(c == '-') {  s.setValue(x,y);  cout << s.calculate() << endl;  }  else if(c == '\*') {  m.setValue(x,y);  cout << m.calculate() << endl;  }  else if(c == '/') {  d.setValue(x,y);  cout << d.calculate() << endl;  }  }  } |

<b>Explanation:</b>

하나의 프로그램을 헤더 파일과 cpp 파일로 나누어 작성하는 문제입니다.

각각의 파일들을 한 프로젝트에 넣어놓고 구현부 cpp 파일과 main cpp 파일에서 헤더파일을 include 해주시면 됩니다.

앞으로 프로그램을 작성할 때 지금처럼 헤더파일과 구현부 cpp파일, main cpp파일로 나누어 작성하는걸 추천합니다.
