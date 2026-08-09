---
title: "C++ Programming Ch.6 Exercise 4 Solution"
date: 2020-03-06T14:38:18+09:00
draft: false
categories: ["💻 Dev & CS", "C++ Programming"]
tags: ["Problem 4", "Chapter 6", "C++", "programming", "Default Parameter", "Masterpiece", "Practice Problem", "Exercise", "Overloaded Constructor", "Programming"]
---

**Problem:**

다음 클래스에 중복된 생성자를 디폴트 매개 변수를 가진 하나의 생성자로 작성하고 테스트 프로그램을 작성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20 | class MyVector{  int \*mem;  int size;  public:  MyVector();  MyVector(int n, int val);  ~MyVector() { delete [] mem; }  };    MyVector::MyVector() {  mem = new int [100];  size = 100;  for(int i=0; i<size; i++) mem[i] = 0;  }    MyVector::MyVector(int n, int val) {  mem = new int [n];  size = n;  for(int i=0; i<size; i++) mem[i] = val;  } |

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/84/img_1.png)

<b>Objective & Hints:</b>

디폴트 매개 변수 연습

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32 | #include<iostream>  using namespace std;    class MyVector{  int \*mem;  int size;  public:  MyVector(int n = 100, int val = 0);  void show();  ~MyVector() { delete [] mem; }  };    MyVector::MyVector(int n, int val) {  mem = new int [n];  size = n;  for(int i=0; i<size; i++) mem[i] = val;  }    void MyVector::show(){  cout << "size = " << size << endl;  for(int i=0; i<size; i++) cout << mem[i] << ' ';  cout << endl;  }    int main() {  MyVector a;  MyVector b(10, 50);  cout << "testing ..." << endl << endl;  a.show();  cout << endl;  b.show();  } |
