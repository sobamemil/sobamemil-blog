---
title: "명품 C++ programming 실습 문제 6장 5번"
date: 2020-03-06T14:52:41+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["::", "C++", "programming", "scopeoperator", "static", "명품", "범위지정연산자", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

동일한 크기로 배열을 변환하는 다음 2개의 static 멤버 함수를 가진 ArrayUtility 클래스를 만들어라.

|  |  |
| --- | --- |
| 1  2  3  4 | static void intToDouble(int source[], double dest[], int size);  // int[]을 double[]로 변환  static void doubleToInt(double source[], int dest[], int size);  // double[]을 int[]로 변환 |

ArrayUtility를 활용하는 main()은 다음과 같다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13 | int main() {  int x[] = {1,2,3,4,5};  double y[5];  double z[] = {9.9,8.8,7.7,6.6,5.6};    ArrayUtility::intToDouble(x, y, 5); // x[] -> y[]  for(int i=0; i<5; i++) cout << y[i] << ' ';  cout << endl;    ArrayUtility::doubleToInt(z, x, 5); // z[] -> x[]  for(int i=0; i<5; i++) cout << x[i] << ' ';  cout << endl;  } |

**실행 결과 :**

![](https://img.sobamemil.com/posts/85/img_1.png)

**목적 및 힌트 :**

static 멤버 함수 만들기

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30 | #include<iostream>  using namespace std;    class ArrayUtility{  public:  static void intToDouble(int source[], double dest[], int size);  static void doubleToInt(double source[], int dest[], int size);  };    void ArrayUtility::intToDouble(int source[], double dest[], int size){  for(int i=0; i<size; i++) dest[i] = (double)source[i];  }    void ArrayUtility::doubleToInt(double source[], int dest[], int size){  for(int i=0; i<size; i++) dest[i] = (int)source[i];  }    int main() {  int x[] = {1,2,3,4,5};  double y[5];  double z[] = {9.9,8.8,7.7,6.6,5.6};    ArrayUtility::intToDouble(x, y, 5); // x[] -> y[]  for(int i=0; i<5; i++) cout << y[i] << ' ';  cout << endl;    ArrayUtility::doubleToInt(z, x, 5); // z[] -> x[]  for(int i=0; i<5; i++) cout << x[i] << ' ';  cout << endl;  } |

**설명 :**

static 멤버 함수를 만들어서 사용하는 문제입니다.

static 멤버 함수는 클래스의 객체가 생성되지 않아도 범위 지정 연산자(Scope Operator) :: 를 사용해서 접근할 수 있습니다.

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 6장 7번](/87)  (1) | 2020.03.06 |
| [명품 C++ programming 실습 문제 6장 6번](/86)  (2) | 2020.03.06 |
| [명품 C++ programming 실습 문제 6장 4번](/84)  (2) | 2020.03.06 |
| [명품 C++ programming 실습 문제 6장 3번](/83)  (1) | 2020.03.05 |
| [명품 C++ programming 실습 문제 6장 2번](/82)  (3) | 2020.03.05 |