---
title: "C++ Programming Ch.9 Exercise 6 Solution"
date: 2019-11-21T02:04:07+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C", "C++", "programming", "과제", "명품", "소스코드", "실습문제", "실행결과", "연습문제", "프로그래밍"]
---<b>Problem:</b>

다음 AbstractStack은 정수 스택 클래스로서 추상 클래스이다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7 | class AbstrackStack {  public:  virtual bool push(int n) = 0; // 스택에 n을 푸시한다. 스택이 full이면 false 리턴  virtual bool pop(int& n) = 0; // 스택에서 팝한 정수를 n에 저장하고 스택이 empty이면 false 리턴    virtual int size() = 0;  };   |

이를 상속받아 정수를 푸시, 팝하는 IntStack 클래스를 만들고 사용 사례를 보여라.

<b>Objective & Hints:</b>

스택을 추상 클래스로 표현하고 구현하기

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/11/img_1.png)

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71 | #include<iostream>  using namespace std;    class AbstrackStack {  public:  virtual bool push(int n) = 0; // 스택에 n을 푸시한다. 스택이 full이면 false 리턴  virtual bool pop(int& n) = 0; // 스택에서 팝한 정수를 n에 저장하고 스택이 empty이면 false 리턴    virtual int size() = 0;  };    class IntStack : public AbstrackStack {  int s, full, top;  int\* int\_stack;  public:  IntStack(int s = 3){    int\_stack = new int [s];  full = s;  top = -1;  }  ~IntStack(){ delete [] int\_stack; }  virtual bool push(int n){  if(top == full) return false;  ++top;  int\_stack[top] = n;  return true;  }  virtual bool pop(int& n){  if(top==-1) return false;  n = int\_stack[top];  top--;  return true;  }  virtual int size() {  return top+1;  }  };    int main() {  int c, pop;  bool b;    IntStack intstack(5);    while(true){  cout << "1: push\t\t2: pop\t\t3: show\_size\t\t4: exit\n선택하세요>> ";  cin >> c;  if(c == 1){  cout << "push 할 정수를 입력하세요>>";  cin >> c;  b = intstack.push(c);  if(!b)  cout << "stack is full...\n";  else  cout << "success!\n";  }  else if(c == 2){  b = intstack.pop(pop);  if(!b)  cout << "stack is empty...\n";  else  cout << "pop : "<< pop << endl;  }  else if(c == 3)  cout << "size : " << intstack.size() << endl;  else  return 0;  cout << endl;  }  }   |
