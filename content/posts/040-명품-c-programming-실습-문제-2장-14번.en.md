---
title: "명품 C++ programming 실습 문제 2장 14번"
date: 2020-02-28T19:34:38+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "cin", "CString", "programming", "strcmp", "while", "명품", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

커피를 주문하는 간단한 C++ 프로그램을 작성해보자. 커피 종류는 "에스프레소", "아메리카노", "카푸치노"의 3가지이며 가격은 각각 2000원, 2300원, 2500원이다. 하루에 20000원 이상 벌게 되면 카페를 닫는다. 실행 결과와 같이 작동하는 프로그램을 작성하라.

**목적 및 힌트 :**

C++ 프로그램 구성. cin, strcmp() 활용 종합 연습

char coffee[100]; int num; cin >> coffee >> num; 으로 커피 이름과 잔 수를 입력받으면 됩니다.

또한 커피는 if(strcmp(coffee, "에스프레소") == 0 )과 같이 비교하면 됩니다.

**실행 결과 :**

![](https://img.sobamemil.com/posts/40/img_1.png)

**코드:**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33 | #include<iostream>  #include<cstring>  using namespace std;    int main() {  int num;  int tot=0;  char coffee[100];    cout << "에스프레소 2000원, 아메리카노 2300원, 카푸치노 2500원입니다.\n";    while(true) {  cout << "주문>> ";  cin >> coffee >> num;  if(strcmp(coffee,"에스프레소")==0) {  cout << 2000\*num << "원입니다. 맛있게 드세요\n";  tot+=2000\*num;  }  else if(strcmp(coffee,"아메리카노")==0) {  cout << 2300\*num << "원입니다. 맛있게 드세요\n";  tot+=2300\*num;  }  else if(strcmp(coffee,"카푸치노")==0) {  cout << 2500\*num << "원입니다. 맛있게 드세요\n";  tot+=2500\*num;  }  if(tot>20000) {  cout << "오늘 " << tot << "원을 판매하여 카페를 닫습니다. 내일 봐요~~~";  break;  }  }  return 0;  } |

**설명 :**

cin 연산자를 이용해 커피 종류와 잔 수를 한번에 입력받고 strcmp() 함수를 이용해 비교하여 각각 다른 코드를 수행하는 프로그램 입니다.


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 2장 16번](/42)  (3) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 15번](/41)  (3) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 13번](/39)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 12번](/38)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 11번](/37)  (1) | 2020.02.28 |