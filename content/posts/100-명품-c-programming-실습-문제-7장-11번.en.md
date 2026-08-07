---
title: "명품 C++ programming 실습 문제 7장 11번"
date: 2020-03-06T19:57:15+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "Pop", "programming", "Push", "stack", "명품", "실습문제", "연습문제", "참조자", "프로그래밍"]
---

<b>Problem:</b>

스택 클래스 Stack을 만들고 푸시(push)용으로 << 연산자를, 팝(pop)을 위해 >> 연산자를, 비어 있는 스택인지를 알기 위해 ! 연산자를 작성하라.

다음 코드를 main()으로 작성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | Stack stack;  stack << 3 << 5 << 10; // 3,5,10 순서대로 push  while(true){  if(!stack) break; //stack empty  int x;  stack >> x; //stack의 top에 있는 정수 pop  cout << x << ' ';  }  cout << endl; |

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/100/img_1.png)

<b>Objective & Hints:</b>

참조 리턴 등 참조자(&) 사용이 필요한 연산자 종합 응용

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36 | #include<iostream>  using namespace std;    class Stack{  int stack[10];  int top;  public:  Stack(){ top=0; }  Stack& operator<< (int num){  stack[top] = num;  top++;  return \*this;  }  bool operator! (){  if(top)  return false;  return true; //top이 empty면 true 반환  }  Stack operator>> (int& x){  x = stack[top-1];  top--;  return \*this;  }  };    int main() {  Stack stack;  stack << 3 << 5 << 10; // 3,5,10 순서대로 push  while(true){  if(!stack) break; //stack empty  int x;  stack >> x; //stack의 top에 있는 정수 pop  cout << x << ' ';  }  cout << endl;  } |


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 8장 1번](/102)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 7장 12번](/101)  (3) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 10번](/99)  (3) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 9번](/98)  (1) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 8번](/97)  (1) | 2020.03.06 |