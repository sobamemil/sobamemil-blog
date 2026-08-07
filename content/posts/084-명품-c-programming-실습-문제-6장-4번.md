---
title: "명품 C++ programming 실습 문제 6장 4번"
date: 2020-03-06T14:38:18+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["4번", "6장", "C++", "programming", "디폴트매개변수", "명품", "실습문제", "연습문제", "중복생성자", "프로그래밍"]
---

<b>문제 :</b>

다음 클래스에 중복된 생성자를 디폴트 매개 변수를 가진 하나의 생성자로 작성하고 테스트 프로그램을 작성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20 | class MyVector{  int \*mem;  int size;  public:  MyVector();  MyVector(int n, int val);  ~MyVector() { delete [] mem; }  };    MyVector::MyVector() {  mem = new int [100];  size = 100;  for(int i=0; i<size; i++) mem[i] = 0;  }    MyVector::MyVector(int n, int val) {  mem = new int [n];  size = n;  for(int i=0; i<size; i++) mem[i] = val;  } |

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/84/img_1.png)

<b>목적 및 힌트 :</b>

디폴트 매개 변수 연습

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32 | #include<iostream>  using namespace std;    class MyVector{  int \*mem;  int size;  public:  MyVector(int n = 100, int val = 0);  void show();  ~MyVector() { delete [] mem; }  };    MyVector::MyVector(int n, int val) {  mem = new int [n];  size = n;  for(int i=0; i<size; i++) mem[i] = val;  }    void MyVector::show(){  cout << "size = " << size << endl;  for(int i=0; i<size; i++) cout << mem[i] << ' ';  cout << endl;  }    int main() {  MyVector a;  MyVector b(10, 50);  cout << "testing ..." << endl << endl;  a.show();  cout << endl;  b.show();  } |


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 6장 6번](/86)  (2) | 2020.03.06 |
| [명품 C++ programming 실습 문제 6장 5번](/85)  (1) | 2020.03.06 |
| [명품 C++ programming 실습 문제 6장 3번](/83)  (1) | 2020.03.05 |
| [명품 C++ programming 실습 문제 6장 2번](/82)  (3) | 2020.03.05 |
| [명품 C++ programming 실습 문제 6장 1번](/81)  (1) | 2020.03.05 |