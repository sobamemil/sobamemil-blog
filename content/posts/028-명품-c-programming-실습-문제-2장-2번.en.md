---
title: "C++ Programming Ch.2 Exercise 2 Solution"
date: 2020-02-28T16:19:50+09:00
draft: false
categories: ["Dev CS", "C++ Programming"]
tags: ["C++", "cout", "endl", "programming", "Multiplication Table", "Masterpiece", "Source Code", "Practice Problem", "Exercise", "Programming"]
---

**Problem:**

cout과 << 연산자를 이용하여 다음과 같이 구구단을 출력하는 프로그램을 작성하라.

![](https://img.sobamemil.com/posts/28/img_1.png)

<b>Objective & Hints:</b>

cout 활용, 화면 출력

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/28/img_2.png)

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15 | #include<iostream>  using namespace std;    int main() {  int i, j;    for(i=1; i<10; i++){  for(j=1; j<10; j++) {  cout << j << "x" << i << "=" << j\*i << '\t';  if(j==9) // 9단 출력 후 줄바꿈.  cout << endl;  }  }  return 0;  } |

<b>Explanation:</b>

구구단을 전부 출력하는데 9단 출력 후 줄바꿈을 해주면 되는 문제입니다.

이중 for문을 사용하여 출력하였습니다.
