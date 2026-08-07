---
title: "명품 C++ programming 실습 문제 2장 2번"
date: 2020-02-28T16:19:50+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "cout", "endl", "programming", "구구단출력", "명품", "소스코드", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

cout과 << 연산자를 이용하여 다음과 같이 구구단을 출력하는 프로그램을 작성하라.

![](https://img.sobamemil.com/posts/28/img_1.png)

**목적 및 힌트 :**

cout 활용, 화면 출력

**실행 결과 :**

![](https://img.sobamemil.com/posts/28/img_2.png)

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15 | #include<iostream>  using namespace std;    int main() {  int i, j;    for(i=1; i<10; i++){  for(j=1; j<10; j++) {  cout << j << "x" << i << "=" << j\*i << '\t';  if(j==9) // 9단 출력 후 줄바꿈.  cout << endl;  }  }  return 0;  } |

**설명 :**

구구단을 전부 출력하는데 9단 출력 후 줄바꿈을 해주면 되는 문제입니다.

이중 for문을 사용하여 출력하였습니다.

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 2장 4번](/30)  (1) | 2020.02.28 |
| [명품 C++ programming 실습문제 2장 3번](/29)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 1번](/27)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 9장 10번](/17)  (1) | 2019.11.26 |
| [명품 C++ programming 실습 문제 9장 9번](/18)  (1) | 2019.11.26 |