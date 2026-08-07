---
title: "명품 C++ programming 실습 문제 2장 11번"
date: 2020-02-28T17:55:18+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: []
---

<b>문제 :</b>

다음 C 프로그램을 C++ 프로그램으로 수정하여 실행하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12 | #include <stdio.h>  int main() {  int k, n=0;  int sum=0;  printf("끝 수를 입력하세요>>");  scanf("%d", &n);  for(k=1; k<=n; k++) {  sum += k;  }  printf("1에서 %d까지의 합은 %d 입니다.\n", n, sum);  return 0;  } |

<b>목적 및 힌트 :</b>

C++ 프로그래밍에 대한 전반적인 이해

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/37/img_1.png)

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12 | #include <iostream>  using namespace std;    int main() {  int n=0;  int sum=0;  cout << "끝 수를 입력하세요>>";  cin >> n;  for(int k=1; k<=n; k++)  sum += k;  cout << "1에서 " << n << "까지의 합은 " << sum << "입니다." << endl;  } |

<b>설명 :</b>

C 로 쓰여진 프로그램을 C++ 프로그램으로 수정하여 실행하는 문제 입니다.

위의 코드에서 for문 안에서 변수 k를 선언 하였습니다.

이처럼 C++에서는 C와 다르게 변수의 선언 위치가 자유롭습니다.


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 2장 13번](/39)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 12번](/38)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 10번](/36)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 9번](/35)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 8번](/34)  (2) | 2020.02.28 |