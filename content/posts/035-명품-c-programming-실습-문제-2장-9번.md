---
title: "명품 C++ programming 실습 문제 2장 9번"
date: 2020-02-28T17:36:57+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "cin", "cout", "getline", "programming", "명품", "실습문제", "연습문제", "코딩", "프로그래밍"]
---

**문제 :**

이름, 주소, 나이를 입력받아 다시 출력하는 프로그램을 작성하라. 실행 예시는 다음과 같다.

![](https://img.sobamemil.com/posts/35/img_1.png)

**목적 및 힌트 :**

빈칸을 포함하는 문자열 읽기

**실행 결과 :**

![](https://img.sobamemil.com/posts/35/img_2.png)

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21 | #include<iostream>  using namespace std;    int main() {  char name[100];  char addr[100];  int age;    cout << "이름은?";  cin.getline(name,100);    cout << "주소는?";  cin.getline(addr,100);    cout << "나이는?";  cin >> age;    cout << name << ", " << addr << ", " << age << "세";    return 0;  } |

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 2장 11번](/37)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 10번](/36)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 8번](/34)  (2) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 7번](/33)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 6번](/32)  (1) | 2020.02.28 |