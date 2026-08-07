---
title: "명품 C++ programming 실습 문제 2장 1번"
date: 2020-02-28T16:12:18+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "cout", "endl", "programming", "\\n", "\\t", "명품", "실습문제", "연습문제", "프로그래밍"]
---

<b>Problem:</b>

cout과 << 연산자를 이용하여, 1에서 100까지 정수를 다음과 같이 한 줄에 10개씩 출력하라. 각 정수는 탭으로 분리하여 출력하라.

![](https://img.sobamemil.com/posts/27/img_1.png)

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/27/img_2.png)

<b>Objective & Hints:</b>

cout 활용, 화면 출력

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | #include<iostream>  using namespace std;    int main(){  int i;    for(i=1;i<101;i++){  cout << i << "\t";  if(i%10==0) // 10개마다 개행문자 출력  cout << endl;  }    return 0;  } |

<b>Explanation:</b>

각 정수를 "\t" 을 이용하여 출력하고, 10개 출력시마다 개행문자를 출력해주면 되는 문제입니다.


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습문제 2장 3번](/29)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 2번](/28)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 9장 10번](/17)  (1) | 2019.11.26 |
| [명품 C++ programming 실습 문제 9장 9번](/18)  (1) | 2019.11.26 |
| [명품 C++ programming 실습 문제 9장 8번](/14)  (1) | 2019.11.21 |