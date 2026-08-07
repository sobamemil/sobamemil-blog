---
title: "명품 C++ programming 실습 문제 4장 5번"
date: 2020-03-04T15:56:03+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "cstdlib", "CTime", "programming", "srand", "공백문자", "명품", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

string 클래스를 이용하여 사용자가 입력한 영문 한 줄을 입력받고 글자 하나만 랜덤하게 수정하여 출력하는 프로그램을 작성하라.

**목적 및 힌트 :**

string 클래스로 문자열 다루기

랜덤 정수를 발생시키기 위해 다음 두 라인의 코드가 필요하며, <cstdlib>와 <ctime> 헤더 파일을 include 해야 한다.

|  |  |
| --- | --- |
| 1  2 | srand((unsinged)time(0)); // 시작할 때마다, 다른 랜덤수를 발생시키기 위한 seed 설정  int n = rand(); // 0에서 RAND\_MAX(32767) 사이의 랜덤한 정수 발생 |

**실행 결과 :**

![](https://img.sobamemil.com/posts/59/img_1.png)

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26 | #include <iostream>  #include <string>  #include <cstdlib>  #include <ctime>  using namespace std;    int main() {  string sent;  int n;  cout << "아래 한 줄을 입력하세요.(exit를 입력하면 종료합니다)" ;  while(true){  srand((unsigned)time(0));  cout << "\n>>";  getline(cin,sent);  if(sent == "exit") break;  int length = sent.length();  while(true){  n = rand()%length;  if(sent[n]!=' ')  break;  }  int a = rand()%25+95; // 임의의 문자 하나 선택  sent[n] = (char)a;  cout << sent;  }  } |

**설명 :**

어느 부분을 바꿀지 고를 때 공백문자는 바꾸지 않기 위해서 sent[n] != ' ' 이 아니면 다시 뽑도록 작성했습니다.

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 4장 7번](/61)  (3) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 6번](/60)  (1) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 4번](/58)  (5) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 3번](/57)  (1) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 2번](/56)  (1) | 2020.03.04 |