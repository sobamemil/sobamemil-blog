---
title: "명품 C++ programming 실습 문제 10장 3번"
date: 2020-03-09T15:45:01+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "programming", "reversearray", "template", "명품", "실습문제", "연습문제", "제네릭", "템플릿", "프로그래밍"]
---

<b>문제 :</b>

배열의 원소를 반대 순서로 뒤집는 reverseArray() 함수를 템플릿으로 작성하라.

reverseArray()의 첫 번째 매개 변수는 배열에 대한 포인터이며 두 번째 매개 변수는 배열의 개수이다.

reverseArray()의 호출 사례는 다음과 같다.

|  |  |
| --- | --- |
| 1  2  3  4 | int x[] = { 1, 10, 100, 5, 4};  reverseArray(x, 5);  for(int i=0; i<5; i++)  cout << x[i] << ' '; // 4 5 100 10 1이 출력된다. |

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/113/img_1.png)

<b>목적 및 힌트 :</b>

템플릿 함수 만들기

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20 | #include <iostream>  using namespace std;    template <class T>  void reverseArray(T array [] , int n){  int j=n-1;  for(int i=0; j>i; i++){  T tmp = array[j];  array[j] = array[i];  array[i] = tmp;  j--;  }  }    int main() {  int x[] = { 1, 10, 100, 5, 4};  reverseArray(x, 5);  for(int i=0; i<5; i++)  cout << x[i] << ' '; // 4 5 100 10 1이 출력된다.  } |


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 10장 5번](/115)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 10장 4번](/114)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 10장 2번](/112)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 10장 1번](/111)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 8장 9번](/110)  (4) | 2020.03.09 |