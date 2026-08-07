---
title: "명품 C++ programming 실습 문제 5장 4번"
date: 2020-03-05T14:39:43+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["Big", "C++", "programming", "reference", "명품", "실습문제", "연습문제", "참조", "프로그래밍", "호출"]
---

**문제 :**

아래와 같이 원형이 주어진 bigger()를 작성하고 사용자로부터 2개의 정수를 입력받아 큰 값을 출력하는 main()을 작성하라.

bigger()는 인자로 주어진 a, b가 같으면 true, 아니면 false를 리턴하고 큰 수는 big에 전달한다.

|  |  |
| --- | --- |
| 1 | bool bigger(int a, int b, int& big); |

**실행 결과 :**

![](https://img.sobamemil.com/posts/72/img_1.png)

**목적 및 힌트 :**

참조에 의한 호출 연습

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24 | #include<iostream>  using namespace std;    bool bigger(int a, int b, int& big){  if(a==b)  return true;  else {  if(a>b)  big = a;  else  big = b;  return false;  }  }    int main() {  int a, b, big;  cout << "두개의 정수를 입력하세요>>";  cin >> a >> b;  if(!bigger(a, b, big))  cout << "큰 수는 : " << big;  else  cout << "두 정수가 같습니다.";  } |

**설명 :**

이 문제와 같이 2개 이상의 값을 return 하고 싶을 때 참조에 의한 호출을 사용하면 원하는대로 작동하게 할 수 있습니다.


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 5장 6번](/74)  (1) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 5번](/73)  (1) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 3번](/71)  (1) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 2번](/70)  (1) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 1번](/69)  (4) | 2020.03.05 |