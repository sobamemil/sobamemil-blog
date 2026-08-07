---
title: "C++ Programming Ch.5 Exercise 3 Solution"
date: 2020-03-05T14:30:18+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "combine()", "programming", "string", "값에의한호출", "명품", "실습문제", "연습문제", "참조에의한호출", "프로그래밍"]
---

**Problem:**

다음과 같이 작동하도록 combine() 함수를 작성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6 | int main() {  string text1("I love you"), text2("very much");  string text3; // 비어있는 문자열  combine(text1, text2, text3); // text1과 " ", 그리고 text2를 덧붙여 text3 만들기  cout << text3; // "I love you very much" 출력  } |

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/71/img_1.png)

<b>Objective & Hints:</b>

string 클래스와 참조 사용 연습

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | #include<iostream>  #include<string>  using namespace std;    void combine(string t1, string t2, string &t3){  t3 = t1 + " " + t2;  }    int main() {  string text1("I love you"), text2("very much");  string text3; // 비어있는 문자열  combine(text1, text2, text3); // text1과 " ", 그리고 text2를 덧붙여 text3 만들기  cout << text3; // "I love you very much" 출력  } |

<b>Explanation:</b>

combine() 함수에서 매개변수인 t1과 t2도 참조에 의한 호출을 사용하여 받아와도 됩니다.
