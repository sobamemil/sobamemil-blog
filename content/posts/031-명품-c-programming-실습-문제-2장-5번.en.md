---
title: "명품 C++ programming 실습 문제 2장 5번"
date: 2020-02-28T16:49:19+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "cin", "cin.getline", "getline", "programming", "명품", "문자열입력", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

<Enter> 키가 입력될 때까지 문자들을 읽고, 입력된 문자 'x'의 개수를 화면에 출력하라.

**목적 및 힌트 :**

cin.getline() 함수를 이용해 한 줄의 문자열 읽기

**실행 결과 :**

![](https://img.sobamemil.com/posts/31/img_1.png)

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19 | #include <iostream>  using namespace std;    int main() {  int i,x=0;  char a[100];    cout << "문자들을 입력하라(100개 미만).\n";    cin.getline(a,100); // 문자열 단위로 읽음    for(i=0; i<100; i++){  if(a[i]=='x') // a[i]가 'x'이면 카운트  x++;  }  cout << "x의 개수는 " << x;    return 0;  } |

**설명 :**

cin을 이용하여 입력 받으면 띄어쓰기를 포함한 문자열은 입력 받을 수 없다.

따라서 이 문제는 cin.getline()을 이용하여 문자열 단위로 입력받아야 한다.

배열 a[]의 원소를 전부 탐색하여 문자 'x'와 비교하여 카운트 하였다.

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 2장 7번](/33)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 6번](/32)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 4번](/30)  (1) | 2020.02.28 |
| [명품 C++ programming 실습문제 2장 3번](/29)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 2번](/28)  (1) | 2020.02.28 |