---
title: "C++ Programming Ch.4 Exercise 2 Solution"
date: 2020-03-04T15:17:39+09:00
draft: false
categories: ["💻 Dev & CS", "C++ Programming"]
tags: ["C++", "delete", "heap", "programming", "Dangling Pointer", "Memory Leak", "Masterpiece", "Practice Problem", "Exercise", "Programming"]
---

**Problem:**

정수 공간 5개를 배열로 동적 할당받고, 정수를 5개 입력받아 평균을 구하고 출력한 뒤 배열을 소멸시키도록 main() 함수를 작성하라.

<b>Objective & Hints:</b>

배열의 동적 할당 및 반환

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/56/img_1.png)

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | #include<iostream>  using namespace std;    int main() {  int \*p = new int[5];  double sum = 0;  cout << "정수 5개 입력>>";  for(int i=0; i<5; i++) {  cin >> p[i];  sum += p[i];  }  cout << "평균 " << sum/5;  delete [] p;  } |

<b>Explanation:</b>

배열을 동적 할당하여 사용 및 반환하는 문제입니다.

메모리를 동적으로 할당받아 사용한 후에는 꼭 delete를 해주는 습관을 기르는 게 좋습니다.

delete를 하지 않을경우 자신도 모르는 사이에 메모리 누수(Memory Leak) 현상이 생길 수 있습니다.

또한 메모리를 delete 한다고 하여도 포인터는 살아있으므로 접근하지 않도록 주의해야 합니다.

이때 해제된 메모리 영역을 여전히 가르키고 있는 포인터를 댕글링 포인터(Dangling Pointer)라고 합니다.
