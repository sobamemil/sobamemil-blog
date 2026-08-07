---
title: "명품 C++ programming 실습 문제 5장 2번"
date: 2020-03-05T14:23:09+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "callByReference", "programming", "명품", "실습문제", "연습문제", "참조", "참조연산자", "프로그래밍", "호출"]
---

**문제 :**

다음 main() 함수와 실행 결과를 참고하여 half() 함수를 작성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5 | int main() {  double n = 20;  half(n); // n의 반값을 구해 n을 바꾼다.  cout << n; // 10이 출력된다.  } |

**실행 결과 :**

![](https://img.sobamemil.com/posts/70/img_1.png)

**목적 및 힌트 :**

참조 연습

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12 | #include<iostream>  using namespace std;    half(double &num){ // 참조에 의한 호출  num /= 2; // num으로 넘어온 본래의 값이 바뀜  }    int main() {  double n = 20;  half(n); // n의 반값을 구해 n을 바꾼다.  cout << n; // 10이 출력된다.  } |

**설명 :**

참조에 의한 호출을 사용해 매개변수의 본래의 값도 변경 되었습니다.

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 5장 4번](/72)  (1) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 3번](/71)  (1) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 1번](/69)  (4) | 2020.03.05 |
| [명품 C++ programming 실습 문제 4장 14번](/68)  (1) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 13번](/67)  (3) | 2020.03.04 |