---
title: "C++ Programming Ch.8 Exercise 6 Solution"
date: 2020-03-09T13:43:11+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "LIFO", "programming", "Push", "stack", "스택", "실습문제", "연습문제", "자료구조", "프로그래밍"]
---<b>Problem:</b>

문제 5~6에 적용되는 BaseArray 클래스는 다음과 같다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12 | class BaseArray {  int capacity; // 배열의 크기  int \*mem; // 정수 배열을 만들기 위한 메모리의 포인터  protected: // 생성자가 protected  BaseArray(int capacity=100){  this->capacity = capacity; mem = new int [capacity];  }  ~BaseArray() { delete [] mem; }  void put(int index, int val) { mem[index] = val; }  int get(int index) { return mem[index]; }  int getCapacity() { return capacity; }  }; |

Write a 스택으로 작동하는 MyStack class that inherits from the BaseArray class.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13 | MyStack mStack(100);  int n;  cout << "스택에 삽입할 5개의 정수를 입력하라>> ";  for(int i=0; i<5; i++){  cin >> n;  mStack.push(n); // 스택에 푸시  }  cout << "스택 용량:" << mStack.capacity() << ", 스택 크기:" << mStack.length() << endl;  cout << "스택의 모든 원소를 팝하여 출력한다>> ";  while(mStack.length() != 0){  cout << mStack.pop() << ' '; // 스택에서 팝  }  cout << endl << "스택의 현재 크기 : " << mStack.length() << endl; |

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/107/img_1.png)

<b>Objective & Hints:</b>

상속과 protected, 파생 클래스 작성

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47 | #include<iostream>  using namespace std;    class BaseArray {  int capacity;  int \*mem;  protected:  BaseArray(int capacity=100){  this->capacity = capacity; mem = new int [capacity];  }  ~BaseArray() { delete [] mem; }  void put(int index, int val) { mem[index] = val; }  int get(int index) { return mem[index]; }  int getCapacity() { return capacity; }  };    class MyStack : public BaseArray{  int top=0;  public:  MyStack(int capacity) : BaseArray(capacity) {;}  void push(int val){  put(top, val);  top++;  }  int capacity() { return getCapacity(); }  int length() { return top; }  int pop() {  top--;  return get(top);  }  };    int main() {  MyStack mStack(100);  int n;  cout << "스택에 삽입할 5개의 정수를 입력하라>> ";  for(int i=0; i<5; i++){  cin >> n;  mStack.push(n); // 스택에 푸시  }  cout << "스택 용량:" << mStack.capacity() << ", 스택 크기:" << mStack.length() << endl;  cout << "스택의 모든 원소를 팝하여 출력한다>> ";  while(mStack.length() != 0){  cout << mStack.pop() << ' '; // 스택에서 팝  }  cout << endl << "스택의 현재 크기 : " << mStack.length() << endl;  } |

<b>Explanation:</b>

스택(Stack)은 제한적으로 접근할 수 있는 나열 구조입니다.

그 접근 방법은 언제나 목록의 끝에서만 일어나고, 끝먼저내기 목록(Pushdown list)이라고도 한다.

스택은 한 쪽 끝에서만 자료를 넣거나 뺄 수 있는 선형 구조(LIFO - Last In First Out)으로 되어 있습니다.

이처럼 나중에 넣은 값이 먼저 나오는 것을 LIFO 이라고 합니다.

스택에 대한 자세한 내용은 아래 위키피디아 링크에 있습니다.

<https://ko.wikipedia.org/wiki/%EC%8A%A4%ED%83%9D>

[스택 - 위키백과, 우리 모두의 백과사전

위키백과, 우리 모두의 백과사전. 스택(stack)은 제한적으로 접근할 수 있는 나열 구조이다. 그 접근 방법은 언제나 목록의 끝에서만 일어난다. 끝먼저내기 목록(Pushdown list)이라고도 한다. 스택은 한 쪽 끝에서만 자료를 넣거나 뺄 수 있는 선형 구조(LIFO - Last In First Out)으로 되어 있다. 자료를 넣는 것을 '밀어넣는다' 하여 푸쉬(push)라고 하고 반대로 넣어둔 자료를 꺼내는 것을 팝(pop)이라고 하는데, 이때 꺼

ko.wikipedia.org](https://ko.wikipedia.org/wiki/%EC%8A%A4%ED%83%9D)
