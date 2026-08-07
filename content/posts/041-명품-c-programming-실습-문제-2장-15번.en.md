---
title: "C++ Programming Ch.2 Exercise 15 Solution"
date: 2020-02-28T20:00:03+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "cstdlib", "CString", "programming", "stdlib.h", "strtok", "명품", "실습문제", "연습문제", "프로그래밍"]
---

<b>Problem:</b>

덧셈(+), 뺄셈(-), 곱셈(\*), 나눗셈(/), 나머지(%)의 정수 5척 연산을 할 수 있는 프로그램을 작성하라. 식은 다음과 같은 형식으로 입력된다. 정수와 연산자는 하나의 빈칸으로 분리된다.

![](https://img.sobamemil.com/posts/41/img_1.png)

<b>Objective & Hints:</b>

공백을 포함하는 문자열 읽기, C++ 프로그램 종합 응용

한 줄을 문자열로 읽고, 공백 문자를 찾아 연산자와 두 개의 피연산자를 구분한 후, 계산하면 됩니다.

문자열을 정수로 바꿀 때 atoi() 함수를 이용하면 됩니다.

예를 들면 atoi("34") = 34 입니다.

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/41/img_2.png)

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36 37 | #include<iostream>  #include<cstring> #include<cstdlib>  using namespace std;    int main(){    char sic[100];  char \*symbol;    int front,rear;    while(true){  cout << "? ";  cin.getline(sic,100);  front = atoi(strtok(sic, " "));  symbol = strtok(NULL, " ");  rear = atoi(strtok(NULL, " "));    if(\*symbol == '+'){  cout << front << " + " << rear << " = " << front+rear << endl;  }  else if(\*symbol == '-'){  cout << front << " - " << rear << " = " << front-rear << endl;  }  else if(\*symbol == '\*'){  cout << front << " \* " << rear << " = " << front\*rear << endl;  }  else if(\*symbol == '/'){  cout << front << " / " << rear << " = " << front/rear << endl;  }  else if(\*symbol == '%'){  cout << front << " % " << rear << " = " << front%rear << endl;  }  }  return 0;  } |

<b>Explanation:</b>

atoi() 함수는 stdlib.h 또는 cstdlib 헤더 파일에 정의되어 있습니다.

strtok() 함수를 이용해 구분자를 공백으로 하여 공백을 기준으로 입력받은 문자열을 나누어 각각 front, symbol, rear에 넣어 사용했습니다.

strtok() 함수 또한 cstring 헤더 파일에 정의되어 있습니다.

**char \*strtok(char \*\_String, char const \*\_Delimiter);**

strtok() 함수는 자른 문자열을 반환, 더 이상 자를 문자열이 없으면 NULL을 반환하기 때문에 두번째 token을 나눌 때 부터는 char \*\_String에 자를 문자열이 아닌 NULL을 넣어 주어야 합니다.
