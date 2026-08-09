---
title: "명품 C++ programming 실습 문제 2장 14번"
date: 2020-02-28T19:34:38+09:00
draft: false
categories: ["💻 개발 & CS", "C++ 프로그래밍"]
tags: ["C++", "cin", "CString", "programming", "strcmp", "while", "명품", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

커피를 주문하는 간단한 C++ 프로그램을 작성해보자. 커피 종류는 "에스프레소", "아메리카노", "카푸치노"의 3가지이며 가격은 각각 2000원, 2300원, 2500원이다. 하루에 20000원 이상 벌게 되면 카페를 닫는다. 실행 결과와 같이 작동하는 프로그램을 작성하라.

<b>목적 및 힌트 :</b>

C++ 프로그램 구성. cin, strcmp() 활용 종합 연습

char coffee[100]; int num; cin >> coffee >> num; 으로 커피 이름과 잔 수를 입력받으면 됩니다.

또한 커피는 if(strcmp(coffee, "에스프레소") == 0 )과 같이 비교하면 됩니다.

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/40/img_1.png)

<b>코드:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33 | #include<iostream>  #include<cstring>  using namespace std;    int main() {  int num;  int tot=0;  char coffee[100];    cout << "에스프레소 2000원, 아메리카노 2300원, 카푸치노 2500원입니다.\n";    while(true) {  cout << "주문>> ";  cin >> coffee >> num;  if(strcmp(coffee,"에스프레소")==0) {  cout << 2000\*num << "원입니다. 맛있게 드세요\n";  tot+=2000\*num;  }  else if(strcmp(coffee,"아메리카노")==0) {  cout << 2300\*num << "원입니다. 맛있게 드세요\n";  tot+=2300\*num;  }  else if(strcmp(coffee,"카푸치노")==0) {  cout << 2500\*num << "원입니다. 맛있게 드세요\n";  tot+=2500\*num;  }  if(tot>20000) {  cout << "오늘 " << tot << "원을 판매하여 카페를 닫습니다. 내일 봐요~~~";  break;  }  }  return 0;  } |

<b>설명 :</b>

cin 연산자를 이용해 커피 종류와 잔 수를 한번에 입력받고 strcmp() 함수를 이용해 비교하여 각각 다른 코드를 수행하는 프로그램 입니다.
