---
title: "명품 C++ programming 실습 문제 2장 2번"
date: 2020-02-28T16:19:50+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "cout", "endl", "programming", "구구단출력", "명품", "소스코드", "실습문제", "연습문제", "프로그래밍"]
---<b>문제 :</b>

cout과 << 연산자를 이용하여 다음과 같이 구구단을 출력하는 프로그램을 작성하라.

![](https://img.sobamemil.com/posts/28/img_1.png)

<b>목적 및 힌트 :</b>

cout 활용, 화면 출력

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/28/img_2.png)

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15 | #include<iostream>  using namespace std;    int main() {  int i, j;    for(i=1; i<10; i++){  for(j=1; j<10; j++) {  cout << j << "x" << i << "=" << j\*i << '\t';  if(j==9) // 9단 출력 후 줄바꿈.  cout << endl;  }  }  return 0;  } |

<b>설명 :</b>

구구단을 전부 출력하는데 9단 출력 후 줄바꿈을 해주면 되는 문제입니다.

이중 for문을 사용하여 출력하였습니다.
