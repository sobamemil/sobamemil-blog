---
title: "C++ Programming Ch.4 Exercise 4 Solution"
date: 2020-03-04T15:42:39+09:00
draft: false
categories: ["💻 Dev & CS", "C++ Programming"]
tags: ["Problem 4", "Chapter 4", "C++", "programming", "Dynamic Array", "Masterpiece", "Practice Problem", "Exercise", "Coding", "Programming"]
---

**Problem:**

다음과 같은 Sample 클래스가 있다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12 | class Sample{  int \*p;  int size;  public:  Sample(int n) {    // 생성자  size = n; p = new int [n]; // n개 정수 배열의 동적 생성  }  void read(); // 동적 할당받은 정수 배열 p에 사용자로부터 정수를 입력 받음  void write(); // 정수 배열을 화면에 출력  int big(); // 정수 배열에서 가장 큰 수 리턴  ~Sample(); // 소멸자  }; |

다음 main() 함수가 실행되도록 Sample 클래스를 완성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6 | int main() {  Sample s(10); // 10개 정수 배열을 가진 Sample 객체 생성  s.read(); // 키보드에서 정수 배열 읽기  s.write(); // 정수 배열 출력  cout << "가장 큰 수는 " << s.big() << endl; // 가장 큰 수 출력  } |

<b>Objective & Hints:</b>

동적 배열을 가진 클래스 다루기

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/58/img_1.png)

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45 | #include<iostream>  using namespace std;    class Sample{  int \*p;  int size;  public:  Sample(int n) { // 생성자  size = n; p = new int [n]; // n개 정수 배열의 동적 생성  }  void read();  // 동적 할당받은 정수 배열 p에 사용자로부터 정수를 입력 받음  void write(); // 정수 배열을 화면에 출력  int big(); // 정수 배열에서 가장 큰 수 리턴  ~Sample();  // 소멸자  };    void Sample::read(){  for(int i=0; i<size; i++){  cin >> p[i];  }  }    void Sample::write(){  for(int i=0; i<size; i++){  cout << p[i] << " ";  }  cout << endl;  }    int Sample::big(){  int big = 0;  for(int i=0; i<size; i++){  if(big < p[i]) big = p[i];  }  return big;  }    Sample::~Sample(){}    int main() {  Sample s(10); // 10개 정수 배열을 가진 Sample 객체 생성  s.read();  // 키보드에서 정수 배열 읽기  s.write();  // 정수 배열 출력  cout << "가장 큰 수는 " << s.big() << endl; // 가장 큰 수 출력  } |
