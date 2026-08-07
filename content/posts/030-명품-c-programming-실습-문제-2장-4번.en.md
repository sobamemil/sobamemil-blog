---
title: "C++ Programming Ch.2 Exercise 4 Solution"
date: 2020-02-28T16:37:04+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "cin", "float", "programming", "가장 큰 수", "명품", "실수", "실습문제", "연습문제", "프로그래밍"]
---

<b>Problem:</b>

소수점을 가지는 5개의 실수를 입력 받아 제일 큰 수를 화면에 출력하라.

<b>Objective & Hints:</b>

cin 활용, 키보드로부터 실수 읽기

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/30/img_1.png)

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20 | #include <iostream>  using namespace std;    int main() {  float a[5], big;  int i;    cout << "5 개의 실수를 입력하라>>";  for(i=0;i<5;i++)  // 5개의 실수 입력 받기  cin >> a[i];  big = a[0]; // a의 첫번째 원소를 big에 삽입    for(i=1;i<5;i++)  if(big<a[i]) //a[i]가 big보다 크면 big에 삽입  big=a[i];    cout << "제일 큰 수 = " << big;    return 0;  } |

<b>Explanation:</b>

제일 큰 수를 big 변수에 넣기위해 for문을 이용해 big과 실수 배열 a[]의 원소들을 하나하나 비교했습니다.
