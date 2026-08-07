---
title: "명품 C++ programming 실습 문제 10장 1번"
date: 2020-03-09T15:33:52+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "programming", "template", "구체화", "명품", "실습문제", "연습문제", "제네릭함수", "템플릿함수", "프로그래밍"]
---

<b>문제 :</b>

배열을 받아 가장 큰 값을 리턴하는 제네릭 함수 biggest()를 작성하라.

또한 main() 함수를 작성하여 biggest()를 호출하는 몇 가지 사례를 보여라.

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/111/img_1.png)

<b>목적 및 힌트 :</b>

템플릿 함수 만들기

biggest()를 호출하는 코드 사례는 다음과 같다.

|  |  |
| --- | --- |
| 1  2 | int x[] = {1, 10, 100, 5, 4};  cout << biggest(x, 5) << endl; // 5는 배열 x의 크기. 100이 출력된다. |

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16 | #include <iostream>  using namespace std;    template <class T>  T biggest(T a[], T n){  T big = a[0]; // 배열 a의 첫번째 원소를 big에 삽입  for(T i=1; i<n; i++)  big = big < a[i] ? a[i] : big; // big보다 a[i]의 값이 더 크면 big에 a[i]의 값을 삽입  return big;  }    int main() {  int big = 0;  int x[] = {1, 10, 100, 5, 4};  cout << biggest(x, 5) << endl;  } |

<b>설명 :</b>

제네릭 함수를 만들 때 프로그래머는 일반화된 타입 혹은 제네릭 타입(generic type)으로 매개 변수나 리턴 타입을 선언합니다.

제네릭 함수를 작성할 때 class 이름은 T가 아니여도 프로그래머 마음대로 작성할 수 있습니다.

템플릿 함수나 클래스의 제네릭 타입에 구체적인 타입을 주어, 구체화된 버전의 함수나 클래스 코드를 생성하는 작업을 구체화(specialization)라고 합니다.
