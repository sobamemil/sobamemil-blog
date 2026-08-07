---
title: "명품 C++ programming 실습 문제 2장 6번"
date: 2020-02-28T17:01:06+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "CString", "programming", "strcmp", "string.h", "명품", "문자열비교", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

문자열을 두 개 입력받고 두 개의 문자열이 같은지 검사하는 프로그램을 작성하라. 만일 같으면 "같습니다", 아니면 "같지 않습니다"를 출력하라.

**목적 및 힌트 :**

공백 없이 입력된 문자열 읽기 (빈칸 없이 입력)

**실행 결과 :**

![](https://img.sobamemil.com/posts/32/img_1.png)

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21 | #include<iostream>  #include<cstring>  using namespace std;    int main() {  char pw1[100];  char pw2[100];    cout << "새 암호를 입력하세요>>";  cin.getline(pw1,100);    cout << "새 암호를 다시 한 번 입력하세요>>";  cin.getline(pw2,100);    if(strcmp(pw1,pw2)==0)  cout << "같습니다";  else  cout << "같지 않습니다";    return 0;  } |

**설명 :**

각각의 배열의 원소들을 하나하나 비교하여 입력받은 두 문자열이 서로 같은지 판단할 수도 있지만 strcmp() 함수를 사용하여 비교, 판단 하였습니다.

c++에서 strcmp() 함수는 cstring 헤더파일에 정의되어 있으므로 cstring 헤더파일을 include 해주었습니다.

strcmp() 함수는 두 문자열이 정확하게 일치한다면 0 을 리턴한다.

일치하지 않을 경우, 일치 하지 않는 첫 번째 문자를 비교해 str1 이 str2 보다 크다면 0 보다 큰 값을 아니면 0 보다 작은 값을 리턴합니다.

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 2장 8번](/34)  (2) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 7번](/33)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 5번](/31)  (1) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 4번](/30)  (1) | 2020.02.28 |
| [명품 C++ programming 실습문제 2장 3번](/29)  (1) | 2020.02.28 |