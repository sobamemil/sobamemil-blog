---
title: "C++ Programming Ch.7 Exercise 7 Solution"
date: 2020-03-06T18:10:47+09:00
draft: false
categories: ["💻 Dev & CS", "C++ Programming"]
tags: ["C++", "friend", "programming", "Masterpiece", "Practice Problem", "Operator Overloading", "Operator Function", "Exercise", "Friend Function", "Programming"]
---

**Problem:**

2차원 행렬을 추상화한 Matrix 클래스를 활용하는 다음 코드가 있다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8 | Matrix a(4,3,2,1), b;  int x[4], y[4]={1,2,3,4}; // 2차원 행렬의 4 개의 원소 값  a >> x; // a의 각 원소를 배열 x에 복사. x[]는 {4,3,2,1}  b << y; // 배열 y의 원소 값을 b의 각 원소에 설정    for(int i=0; i<4; i++) cout << x[i] << ' '; // x[] 출력  cout << endl;  b.show(); |

(1) <<, >> 연산자 함수를 Matrix의 멤버 함수로 구현하라.

(2) <<, >> 연산자 함수를 Matrix의 프렌드 함수로 구현하라.

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/96/img_1.png)

<b>Objective & Hints:</b>

<<, >> 연산자와 클래스 구현 연습

<b>Code:</b>

● 문제 (1)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41 | #include<iostream>  using namespace std;    class Matrix{  int arr[4];  public:  Matrix(){;}  Matrix(int a, int b, int c, int d) { arr[0]=a; arr[1]=b; arr[2]=c; arr[3]=d; }  void show();  void operator>> (int x[]);  void operator<< (int y[]);  };    void Matrix::show() {  cout << "Matrix" << " = { ";  for(int i=0; i<4; i++) cout << this->arr[i] << ' ';  cout << "}" << endl;  }    void Matrix::operator>> (int x[]){  for(int i=0; i<4; i++){  x[i] = this->arr[i];  }  }    void Matrix::operator<< (int y[]){  for(int i=0; i<4; i++){  this->arr[i] = y[i];  }  }    int main() {  Matrix a(4,3,2,1), b;  int x[4], y[4]={1,2,3,4}; // 2차원 행렬의 4 개의 원소 값  a >> x; // a의 각 원소를 배열 x에 복사. x[]는 {4,3,2,1}  b << y; // 배열 y의 원소 값을 b의 각 원소에 설정    for(int i=0; i<4; i++) cout << x[i] << ' '; // x[] 출력  cout << endl;  b.show();  } |

● 문제 (2)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41 | #include<iostream>  using namespace std;    class Matrix{  int arr[4];  public:  Matrix(){;}  Matrix(int a, int b, int c, int d) { arr[0]=a; arr[1]=b; arr[2]=c; arr[3]=d; }  void show();  friend void operator>> (Matrix& a, int x[]);  friend void operator<< (Matrix& b, int y[]);  };    void Matrix::show() {  cout << "Matrix" << " = { ";  for(int i=0; i<4; i++) cout << this->arr[i] << ' ';  cout << "}" << endl;  }    void operator>> (Matrix& a, int x[]){  for(int i=0; i<4; i++){  x[i] = a.arr[i];  }  }    void operator<< (Matrix& b, int y[]){  for(int i=0; i<4; i++){  b.arr[i] = y[i];  }  }    int main() {  Matrix a(4,3,2,1), b;  int x[4], y[4]={1,2,3,4}; // 2차원 행렬의 4 개의 원소 값  a >> x; // a의 각 원소를 배열 x에 복사. x[]는 {4,3,2,1}  b << y; // 배열 y의 원소 값을 b의 각 원소에 설정    for(int i=0; i<4; i++) cout << x[i] << ' '; // x[] 출력  cout << endl;  b.show();  } |
