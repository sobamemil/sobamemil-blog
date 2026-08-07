---
title: "명품 C++ programming 실습문제 2장 3번"
date: 2020-02-28T16:27:30+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "cin", "cout", "programming", "명품", "소스코드", "실습문제", "연산자", "연습문제", "프로그래밍"]
---

**문제 :**

키보드로부터 두 개의 정수를 읽어 큰 수를 화면에 출력하라.

**목적 및 힌트 :**

cin 활용, 키보드로부터 정수 읽기

**실행 결과 :**

![](https://img.sobamemil.com/posts/29/img_1.png)

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15 | #include<iostream>  using namespace std;    int main(){  int a,b;  cout << "두 수를 입력하라>>";  cin >> a >> b; // cin 연산자를 이용하여 두개의 정수 입력받기  cout << "큰 수 = ";  if(a<b)  cout << b;  else  cout << a;    return 0;  } |

**설명 :**

c++에서 새로 등장한 cin 연산자를 사용할 수 있는지에 대한 문제입니다.

cin >> a >> b 와 같이 한번에 여러개를 입력받을 수 있습니다.

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 2장 5번](/31)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 4번](/30)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 2번](/28)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 1번](/27)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 9장 10번](/17)  (1) | 2019.11.26 |