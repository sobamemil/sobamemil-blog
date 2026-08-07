---
title: "명품 C++ programming 실습 문제 2장 4번"
date: 2020-02-28T16:37:04+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "cin", "float", "programming", "가장 큰 수", "명품", "실수", "실습문제", "연습문제", "프로그래밍"]
---

<b>문제 :</b>

소수점을 가지는 5개의 실수를 입력 받아 제일 큰 수를 화면에 출력하라.

<b>목적 및 힌트 :</b>

cin 활용, 키보드로부터 실수 읽기

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/30/img_1.png)

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20 | #include <iostream>  using namespace std;    int main() {  float a[5], big;  int i;    cout << "5 개의 실수를 입력하라>>";  for(i=0;i<5;i++)  // 5개의 실수 입력 받기  cin >> a[i];  big = a[0]; // a의 첫번째 원소를 big에 삽입    for(i=1;i<5;i++)  if(big<a[i]) //a[i]가 big보다 크면 big에 삽입  big=a[i];    cout << "제일 큰 수 = " << big;    return 0;  } |

<b>설명 :</b>

제일 큰 수를 big 변수에 넣기위해 for문을 이용해 big과 실수 배열 a[]의 원소들을 하나하나 비교했습니다.


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 2장 6번](/32)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 5번](/31)  (1) | 2020.02.28 |
| [명품 C++ programming 실습문제 2장 3번](/29)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 2번](/28)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 1번](/27)  (1) | 2020.02.28 |