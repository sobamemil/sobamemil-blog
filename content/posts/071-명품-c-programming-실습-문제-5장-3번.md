---
title: "명품 C++ programming 실습 문제 5장 3번"
date: 2020-03-05T14:30:18+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "combine()", "programming", "string", "값에의한호출", "명품", "실습문제", "연습문제", "참조에의한호출", "프로그래밍"]
---

<b>문제 :</b>

다음과 같이 작동하도록 combine() 함수를 작성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6 | int main() {  string text1("I love you"), text2("very much");  string text3; // 비어있는 문자열  combine(text1, text2, text3); // text1과 " ", 그리고 text2를 덧붙여 text3 만들기  cout << text3; // "I love you very much" 출력  } |

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/71/img_1.png)

<b>목적 및 힌트 :</b>

string 클래스와 참조 사용 연습

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | #include<iostream>  #include<string>  using namespace std;    void combine(string t1, string t2, string &t3){  t3 = t1 + " " + t2;  }    int main() {  string text1("I love you"), text2("very much");  string text3; // 비어있는 문자열  combine(text1, text2, text3); // text1과 " ", 그리고 text2를 덧붙여 text3 만들기  cout << text3; // "I love you very much" 출력  } |

<b>설명 :</b>

combine() 함수에서 매개변수인 t1과 t2도 참조에 의한 호출을 사용하여 받아와도 됩니다.


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 5장 5번](/73)  (1) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 4번](/72)  (1) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 2번](/70)  (1) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 1번](/69)  (4) | 2020.03.05 |
| [명품 C++ programming 실습 문제 4장 14번](/68)  (1) | 2020.03.04 |