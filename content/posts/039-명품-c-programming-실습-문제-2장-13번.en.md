---
title: "명품 C++ programming 실습 문제 2장 13번"
date: 2020-02-28T19:01:50+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "if문", "programming", "switch", "명품", "소스코드", "실습문제", "연습문제", "프로그래밍"]
---

<b>Problem:</b>

중식당의 주문 과정을 C++ 프로그램으로 작성해보자. 다음 실행 결과와 같이 메뉴와 사람 수를 입력받고 이를 출력하면 된다. 잘못된 입력을 가려내는 부분도 코드에 추가하라.

<b>Objective & Hints:</b>

C++ 프로그램으로 구성, 키 입력 등 종합 연습

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/39/img_1.png)

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31 | #include<iostream>  using namespace std;    int main() {  int num,tot;  cout << "\*\*\*\*\* 승리장에 오신 것을 환영합니다. \*\*\*\*\* \n";  while(true){  cout << "짬뽕:1, 짜장:2, 군만두:3, 종료:4>>  ";  cin >> num;  if(num == 4) {  cout << "오늘 영업은 끝났습니다.";  break;  }  if(num > 4)  {  cout << "다시 주문하세요!!\n";  continue;  }    cout << "몇인분?";  cin >> tot;    if(num==1)  cout << "짬뽕 " << tot << "인분 나왔습니다\n";  else if(num==2)  cout << "짜장 " << tot << "인분 나왔습니다\n";  else if(num==3)  cout << "군만두 " << tot << "인분 나왔습니다\n";  }    return 0;  } |

<b>Explanation:</b>

if문을 사용해 코드를 작성하였지만 switch 문을 사용해 작성할 수도 있습니다.


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 2장 15번](/41)  (3) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 14번](/40)  (3) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 12번](/38)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 11번](/37)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 10번](/36)  (1) | 2020.02.28 |