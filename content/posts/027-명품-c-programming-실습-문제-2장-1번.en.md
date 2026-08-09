---
title: "C++ Programming Ch.2 Exercise 1 Solution"
date: 2020-02-28T16:12:18+09:00
draft: false
categories: ["💻 Dev & CS", "C++ Programming"]
tags: ["C++", "cout", "endl", "programming", "\\n", "\\t", "Masterpiece", "Practice Problem", "Exercise", "Programming"]
---

**Problem:**

cout과 << 연산자를 이용하여, 1에서 100까지 정수를 다음과 같이 한 줄에 10개씩 출력하라. 각 정수는 탭으로 분리하여 출력하라.

![](https://img.sobamemil.com/posts/27/img_1.png)

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/27/img_2.png)

<b>Objective & Hints:</b>

cout 활용, 화면 출력

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | #include<iostream>  using namespace std;    int main(){  int i;    for(i=1;i<101;i++){  cout << i << "\t";  if(i%10==0) // 10개마다 개행문자 출력  cout << endl;  }    return 0;  } |

<b>Explanation:</b>

각 정수를 "\t" 을 이용하여 출력하고, 10개 출력시마다 개행문자를 출력해주면 되는 문제입니다.
