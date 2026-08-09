---
title: "명품 C++ programming 실습 문제 5장 2번"
date: 2020-03-05T14:23:09+09:00
draft: false
categories: ["💻 개발 & CS", "C++ 프로그래밍"]
tags: ["C++", "callByReference", "programming", "명품", "실습문제", "연습문제", "참조", "참조연산자", "프로그래밍", "호출"]
---

**문제 :**

다음 main() 함수와 실행 결과를 참고하여 half() 함수를 작성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5 | int main() {  double n = 20;  half(n); // n의 반값을 구해 n을 바꾼다.  cout << n; // 10이 출력된다.  } |

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/70/img_1.png)

<b>목적 및 힌트 :</b>

참조 연습

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12 | #include<iostream>  using namespace std;    half(double &num){ // 참조에 의한 호출  num /= 2; // num으로 넘어온 본래의 값이 바뀜  }    int main() {  double n = 20;  half(n); // n의 반값을 구해 n을 바꾼다.  cout << n; // 10이 출력된다.  } |

<b>설명 :</b>

참조에 의한 호출을 사용해 매개변수의 본래의 값도 변경 되었습니다.
