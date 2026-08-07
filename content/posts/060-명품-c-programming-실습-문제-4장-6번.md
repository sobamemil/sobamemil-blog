---
title: "명품 C++ programming 실습 문제 4장 6번"
date: 2020-03-04T16:03:03+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "length()", "programmiing", "size()", "string", "거꾸로출력", "명품", "실습문제", "연습문제", "프로그래밍"]
---

<b>문제 :</b>

string 클래스를 이용하여 사용자가 입력한 영문 한 줄을 문자열로 입력받고 거꾸로 출력하는 프로그램을 작성하라.

<b>목적 및 힌트 :</b>

string 클래스로 문자열 다루기

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/60/img_1.png)

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17 | #include<iostream>  #include<string>  using namespace std;    int main() {  string str;  cout << "아래 한 줄을 입력하세요.(exit를 입력하면 종료합니다)";    while(true){  cout << endl << ">>";  getline(cin,str);  if(str == "exit")  break;  for(int i = str.length()-1; i>=0; i--)  cout << str[i];  }  } |

<b>설명 :</b>

사용자로부터 입력받은 영문 한 줄을 거꾸로 출력하기 위해 string 클래스의 length() 멤버 함수를 이용해 끝에서부터 반대로 출력하였습니다.
