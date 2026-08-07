---
title: "C++ Programming Ch.2 Exercise 11 Solution"
date: 2020-02-28T17:55:18+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: []
---

**Problem:**

다음 C 프로그램을 C++ 프로그램으로 수정하여 실행하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12 | #include <stdio.h>  int main() {  int k, n=0;  int sum=0;  printf("끝 수를 입력하세요>>");  scanf("%d", &n);  for(k=1; k<=n; k++) {  sum += k;  }  printf("1에서 %d까지의 합은 %d 입니다.\n", n, sum);  return 0;  } |

<b>Objective & Hints:</b>

C++ Programming에 대한 전반적인 이해

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/37/img_1.png)

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12 | #include <iostream>  using namespace std;    int main() {  int n=0;  int sum=0;  cout << "끝 수를 입력하세요>>";  cin >> n;  for(int k=1; k<=n; k++)  sum += k;  cout << "1에서 " << n << "까지의 합은 " << sum << "입니다." << endl;  } |

<b>Explanation:</b>

C 로 쓰여진 프로그램을 C++ 프로그램으로 수정하여 실행하는 문제 입니다.

위의 코드에서 for문 안에서 변수 k를 선언 하였습니다.

이처럼 C++에서는 C와 다르게 변수의 선언 위치가 자유롭습니다.
