---
title: "명품 C++ programming 실습 문제 10장 5번"
date: 2020-03-09T15:53:04+09:00
draft: false
categories: ["💻 개발 & CS", "C++ 프로그래밍"]
tags: ["C++", "Generic", "programming", "template", "명품", "실습문제", "연습문제", "일반화", "프로그래밍", "함수"]
---

**문제 :**

다음 함수는 매개 변수로 주어진 두 개의 int 배열을 연결한 새로운 int 배열을 동적 할당받아 리턴한다.

|  |  |
| --- | --- |
| 1 | int \* concat(int a[], int sizea, int b[], int sizeb); |

concat가 int 배열뿐 아니라 다른 타입의 배열도 처리할 수 있도록 일반화하라.

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/115/img_1.png)

<b>목적 및 힌트 :</b>

함수의 힐반화에 대한 이해, 템플릿 함수 만들기

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24 | #include <iostream>  using namespace std;    template <class T>  T\* concat(T a[], int sizea, T b[], int sizeb){  T \*rArray = new T[sizea + sizeb]; // return 할 배열을 동적생성  for(int i=0; i<sizea+sizeb; i++){  if(i<sizea)  rArray[i] = a[i];  else  rArray[i] = b[i-sizea];  }  return rArray;  }    int main() {  int x[] = { 1, 10, 100, 5, 4 };  int y[] = { 7, 6, 10, 9 };  int \*a = concat(x, 5, y, 4);  int aSize = sizeof(x)/sizeof(x[0]) + sizeof(y)/sizeof(y[0]); // a에 들어있는 원소의 개수    for (int i = 0; i<aSize; i++)  cout << a[i] << ' ';  } |
