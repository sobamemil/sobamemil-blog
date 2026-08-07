---
title: "명품 C++ programming 실습 문제 2장 8번"
date: 2020-02-28T17:24:52+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "CString", "getline", "programming", "strcpy", "strlen", "명품", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

한 라인에 ';' 으로 5개의 이름을 구분하여 입력받아, 각 이름을 끊어내어 화면에 출력하고 가장 긴 이름을 판별하라.

**목적 및 힌트 :**

cin.getline()으로 문자열 읽기

';'까지 문자열을 읽고자 하면 다음 코드를 사용하고

|  |  |
| --- | --- |
| 1  2 | char name[100];  cin.getline(name, 100, ';'); |

5개 읽어야 하니 5번 루프를 돈다.

**실행 결과 :**

![](https://img.sobamemil.com/posts/34/img_1.png)

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25 | #include<iostream>  #include<cstring>  using namespace std;    int main() {    int A=0;  int i;  char name[100];  char longName[100];    cout << "5 명의 이름을 ';' 으로 구분하여 입력하세요 \n>>";    for(i=1;i<6;i++){  cin.getline(name,100,';');  cout << i << " : " << name << endl;  if(A < strlen(name)) {  A = strlen(name);  strcpy(longName,name);  }  }  cout << "가장 긴 이름은 " << longName;    return 0;  } |

**설명 :**

cin.getline() 을 이용하여 입력 받았는데 이때 ';'를 구분자로 사용하여 입력 받았습니다.

';'를 기준으로 구분하여 문자열을 입력받고 그 문자열의 길이를 변수 A와 비교하여 A보다 긴 name[] 문자열은 strcpy() 함수를 이용하여 배열 longName[]에 복사 하였습니다.

strlen() 함수를 이용하여 각각의 문자열의 길이를 구하였고, strcpy() 함수를 이용하여 문자열을 복사 하였습니다.

strlen() 함수와 strcpy() 함수는 c++에서 cstring 헤더파일에 정의되어 있습니다.

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 2장 10번](/36)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 9번](/35)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 7번](/33)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 6번](/32)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 5번](/31)  (1) | 2020.02.28 |