---
title: "명품 C++ programming 실습 문제 10장 5번"
date: 2020-03-09T15:53:04+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "Generic", "programming", "template", "명품", "실습문제", "연습문제", "일반화", "프로그래밍", "함수"]
---

<b>Problem:</b>

다음 함수는 매개 변수로 주어진 두 개의 int 배열을 연결한 새로운 int 배열을 동적 할당받아 리턴한다.

|  |  |
| --- | --- |
| 1 | int \* concat(int a[], int sizea, int b[], int sizeb); |

concat가 int 배열뿐 아니라 다른 타입의 배열도 처리할 수 있도록 일반화하라.

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/115/img_1.png)

<b>Objective & Hints:</b>

함수의 힐반화에 대한 이해, 템플릿 함수 만들기

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24 | #include <iostream>  using namespace std;    template <class T>  T\* concat(T a[], int sizea, T b[], int sizeb){  T \*rArray = new T[sizea + sizeb]; // return 할 배열을 동적생성  for(int i=0; i<sizea+sizeb; i++){  if(i<sizea)  rArray[i] = a[i];  else  rArray[i] = b[i-sizea];  }  return rArray;  }    int main() {  int x[] = { 1, 10, 100, 5, 4 };  int y[] = { 7, 6, 10, 9 };  int \*a = concat(x, 5, y, 4);  int aSize = sizeof(x)/sizeof(x[0]) + sizeof(y)/sizeof(y[0]); // a에 들어있는 원소의 개수    for (int i = 0; i<aSize; i++)  cout << a[i] << ' ';  } |


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 10장 7번](/117)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 10장 6번](/116)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 10장 4번](/114)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 10장 3번](/113)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 10장 2번](/112)  (1) | 2020.03.09 |