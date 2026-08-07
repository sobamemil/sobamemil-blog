---
title: "명품 C++ programming 실습 문제 2장 10번"
date: 2020-02-28T17:44:09+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "programming", "명품", "문자열", "소스코드", "실습문제", "연습문제", "코딩", "프로그래머", "프로그래밍"]
---<b>문제 :</b>

문자열을 하나 입력받고 문자열의 부분 문자열을 다음과 같이 출력하는 프로그램을 작성하라. 예시는 다음과 같다.

![](https://img.sobamemil.com/posts/36/img_1.png)

<b>목적 및 힌트 :</b>

문자열 읽기, 문자열 다루기

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/36/img_2.png)

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21 | #include <iostream>  using namespace std;    int main() {    cout << "문자열 입력>>";  char str[100];    cin.getline(str,100);    for(int i=1;i<100;i++){  for(int j=0;j<i;j++) {  cout << str[j];  }  if(str[i]=='\0') // 문자열의 끝이면 break  break;  cout << endl;  }    return 0;  } |
