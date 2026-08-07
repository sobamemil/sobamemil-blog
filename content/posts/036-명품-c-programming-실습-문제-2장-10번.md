---
title: "명품 C++ programming 실습 문제 2장 10번"
date: 2020-02-28T17:44:09+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "programming", "명품", "문자열", "소스코드", "실습문제", "연습문제", "코딩", "프로그래머", "프로그래밍"]
---

**문제 :**

문자열을 하나 입력받고 문자열의 부분 문자열을 다음과 같이 출력하는 프로그램을 작성하라. 예시는 다음과 같다.

![](https://img.sobamemil.com/posts/36/img_1.png)

**목적 및 힌트 :**

문자열 읽기, 문자열 다루기

**실행 결과 :**

![](https://img.sobamemil.com/posts/36/img_2.png)

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21 | #include <iostream>  using namespace std;    int main() {    cout << "문자열 입력>>";  char str[100];    cin.getline(str,100);    for(int i=1;i<100;i++){  for(int j=0;j<i;j++) {  cout << str[j];  }  if(str[i]=='\0') // 문자열의 끝이면 break  break;  cout << endl;  }    return 0;  } |

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 2장 12번](/38)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 11번](/37)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 9번](/35)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 8번](/34)  (2) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 7번](/33)  (1) | 2020.02.28 |