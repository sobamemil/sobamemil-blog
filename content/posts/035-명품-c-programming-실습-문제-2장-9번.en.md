---
title: "C++ Programming Ch.2 Exercise 9 Solution"
date: 2020-02-28T17:36:57+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "cin", "cout", "getline", "programming", "명품", "실습문제", "연습문제", "코딩", "프로그래밍"]
---

**Problem:**

이름, 주소, 나이를 입력받아 다시 출력하는 프로그램을 작성하라. 실행 예시는 다음과 같다.

![](https://img.sobamemil.com/posts/35/img_1.png)

<b>Objective & Hints:</b>

빈칸을 포함하는 문자열 읽기

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/35/img_2.png)

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21 | #include<iostream>  using namespace std;    int main() {  char name[100];  char addr[100];  int age;    cout << "이름은?";  cin.getline(name,100);    cout << "주소는?";  cin.getline(addr,100);    cout << "나이는?";  cin >> age;    cout << name << ", " << addr << ", " << age << "세";    return 0;  } |
