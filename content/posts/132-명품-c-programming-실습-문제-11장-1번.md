---
title: "명품 C++ programming 실습 문제 11장 1번"
date: 2020-03-27T14:58:42+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["11장", "C++", "cin", "get()", "programming", "명품", "스트림", "실습문제", "연습문제", "프로그래밍"]
---

<b>문제 :</b>

int cin.get() 함수를 이용하여 키보드로부터 한 라인을 읽고 'a'가 몇 개인지 출력하는 프로그램을 작성하라.

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/132/img_1.png)

<b>목적 및 힌트 :</b>

cin으로 키 입력 연습

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | #include <iostream>  using namespace std;    int main() {  int a;  int cnt=0;  while( (a = cin.get() ) != EOF ){  if(a == 'a')  cnt++;  else if(a == '\n')  break;  }  cout << cnt;  } |

<b>설명 :</b>

cin은 C++ 표준 입출력 스트림 객체입니다. 따라서 iostream 헤더 파일은 include 했다면 저절로 cin 객체가 생성되어 바로 사용할 수 있습니다.


[저작자표시 비영리
(새창열림)](https://creativecommons.org/licenses/by-nc/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 11장 3번](/134)  (3) | 2020.03.27 |
| [명품 C++ programming 실습 문제 11장 2번](/133)  (1) | 2020.03.27 |
| [명품 C++ programming 실습 문제 10장 16번](/126)  (1) | 2020.03.11 |
| [명품 C++ programming 실습 문제 10장 15번](/125)  (3) | 2020.03.11 |
| [명품 C++ programming 실습 문제 10장 14번](/124)  (1) | 2020.03.11 |