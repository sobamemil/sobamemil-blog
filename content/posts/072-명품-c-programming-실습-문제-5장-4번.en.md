---
title: "C++ Programming Ch.5 Exercise 4 Solution"
date: 2020-03-05T14:39:43+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["Big", "C++", "programming", "reference", "명품", "실습문제", "연습문제", "참조", "프로그래밍", "호출"]
---

**Problem:**

아래와 같이 원형이 주어진 bigger()를 작성하고 사용자로부터 2개의 정수를 입력받아 큰 값을 출력하는 main()을 작성하라.

bigger()는 인자로 주어진 a, b가 같으면 true, 아니면 false를 리턴하고 큰 수는 big에 전달한다.

|  |  |
| --- | --- |
| 1 | bool bigger(int a, int b, int& big); |

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/72/img_1.png)

<b>Objective & Hints:</b>

참조에 의한 호출 연습

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24 | #include<iostream>  using namespace std;    bool bigger(int a, int b, int& big){  if(a==b)  return true;  else {  if(a>b)  big = a;  else  big = b;  return false;  }  }    int main() {  int a, b, big;  cout << "두개의 정수를 입력하세요>>";  cin >> a >> b;  if(!bigger(a, b, big))  cout << "큰 수는 : " << big;  else  cout << "두 정수가 같습니다.";  } |

<b>Explanation:</b>

이 문제와 같이 2개 이상의 값을 return 하고 싶을 때 참조에 의한 호출을 사용하면 원하는대로 작동하게 할 수 있습니다.
