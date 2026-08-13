---
title: "명품 C++ programming 실습 문제 8장 5번"
date: 2020-03-09T13:36:05+09:00
draft: false
categories: ["개발 CS", "C++ 프로그래밍"]
tags: ["C++", "programming", "protected", "queue", "상속", "실습문제", "연습문제", "큐", "파생클래스", "프로그래밍"]
---

**문제 :**

문제 5~6에 적용되는 BaseArray 클래스는 다음과 같다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12 | class BaseArray {  int capacity; // 배열의 크기  int \*mem; // 정수 배열을 만들기 위한 메모리의 포인터  protected: // 생성자가 protected  BaseArray(int capacity=100){  this->capacity = capacity; mem = new int [capacity];  }  ~BaseArray() { delete [] mem; }  void put(int index, int val) { mem[index] = val; }  int get(int index) { return mem[index]; }  int getCapacity() { return capacity; }  }; |

BaseArray를 상속받아 큐처럼 작동하는 MyQueue 클래스를 작성하라.

MyQueue를 활용하는 사례는 다음과 같다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13 | MyQueue mQ(100);  int n;  cout << "큐에 삽입할 5개의 정수를 입력하라>> ";  for(int i=0; i<5; i++){  cin >> n;  mQ.enqueue(n); // 큐에 삽입  }  cout << "큐의 용량:" << mQ.capacity() << ", 큐의 크기:" << mQ.length() << endl;  cout << "큐의 원소를 순서대로 제거하여 출력한다>> ";  while(mQ.length() != 0){  cout << mQ.dequeue() << ' '; // 큐에서 제거하여 출력  }  cout << endl << "큐의 현재 크기 : " << mQ.length() << endl; |

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/106/img_1.png)

<b>목적 및 힌트 :</b>

상속과 protected, 파생 클래스 작성

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61 | #include<iostream>  using namespace std;    class BaseArray {  int capacity; // 배열의 크기  int \*mem; // 정수 배열을 만들기 위한 메모리의 포인터  protected: // 생성자가 protected  BaseArray(int capacity=100){  this->capacity = capacity; mem = new int [capacity];  }  ~BaseArray() { delete [] mem; }  void put(int index, int val) { mem[index] = val; }  int get(int index) { return mem[index]; }  int getCapacity() { return capacity; }  };    class MyQueue : public BaseArray{  int front = 0;  int rear = 0;  public:  MyQueue(int capacity) : BaseArray(capacity) {;}  void enqueue(int n){  if(rear >= getCapacity()){  cout << "Queue is full...\n";  exit(1);  }  rear++;  put(rear, n);  }  int capacity() {  return getCapacity();  }  int length() {  return rear;  }  int dequeue(){  if(rear < 0){  cout << "Queue is empty...\n";  exit(1);  }  ++front;  rear--;  return get(front);  }  };    int main() {  MyQueue mQ(100);  int n;  cout << "큐에 삽입할 5개의 정수를 입력하라>> ";  for(int i=0; i<5; i++){  cin >> n;  mQ.enqueue(n); // 큐에 삽입  }  cout << "큐의 용량:" << mQ.capacity() << ", 큐의 크기:" << mQ.length() << endl;  cout << "큐의 원소를 순서대로 제거하여 출력한다>> ";  while(mQ.length() != 0){  cout << mQ.dequeue() << ' '; // 큐에서 제거하여 출력  }  cout << endl << "큐의 현재 크기 : " << mQ.length() << endl;  } |

<b>설명 :</b>

큐(Queue)는 컴퓨터의 기본적인 자료 구조 중 한가지로, 먼저 집어 넣은 데이터가 먼저 나오는 FIFO(First In First Out)구조로 저장하는 형식을 말합니다.

큐에대한 설명은 아래 위키피디아 링크에 있습니다.

<https://ko.wikipedia.org/wiki/%ED%81%90_(%EC%9E%90%EB%A3%8C_%EA%B5%AC%EC%A1%B0)>

[큐 (자료 구조) - 위키백과, 우리 모두의 백과사전

위키백과, 우리 모두의 백과사전.

ko.wikipedia.org](https://ko.wikipedia.org/wiki/%ED%81%90_(%EC%9E%90%EB%A3%8C_%EA%B5%AC%EC%A1%B0))
