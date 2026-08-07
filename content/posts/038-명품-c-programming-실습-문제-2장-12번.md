---
title: "명품 C++ programming 실습 문제 2장 12번"
date: 2020-02-28T18:15:45+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "programming", "매개변수", "명품", "실습문제", "연습문제", "프로그래밍", "함수선언", "함수중복"]
---

<b>문제 :</b>

다음 C 프로그램을 C++ 프로그램으로 수정하여 실행하라. 이 프로그램의 실행 결과는 실습 문제 11과 같다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18 | #include <stdio.h>  int sum();    int main() {  int n=0;  printf("끝 수를 입력하세요>>");  scanf("%d", &n);  printf("1에서 %d까지의 합은 %d 입니다.\n", n, sum(1,n));  return 0;  }    int sum(int a, int b) {  int k, res=0;  for(k=a; k<=b; k++){  res += k;  }  return res;  } |

<b>[2020/02/28 - [C++/명품 C++ programming] - 명품 C++ programming 실습 문제 2장 11번](https://sobamemil.tistory.com/37)</b>

[명품 C++ programming 실습 문제 2장 11번

문제 : 다음 C 프로그램을 C++ 프로그램으로 수정하여 실행하라. 1 2 3 4 5 6 7 8 9 10 11 12 #include int main() { int k, n=0; int sum=0; printf("끝 수를 입력하세요>>"); scanf("%d", &n); for(k=..

sobamemil.tistory.com](https://sobamemil.tistory.com/37)

<b>목적 및 힌트 :</b>

C++ 프로그래밍에 대한 전반적인 이해

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/38/img_1.png)

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18 | #include <iostream>  using namespace std;    int sum(int a, int b);    int main() {  int n=0;  cout << "끝 수를 입력하세요>>";  cin >> n;  cout << "1에서 " << n << "까지의 합은 " << sum(1, n) << " 입니다." << endl;  }    int sum(int a, int b) {  int res=0;  for(int k=a; k<=b; k++)  res += k;  return res;  } |

<b>설명 :</b>

C++ 에서는 Function Overloading이 가능하기 때문에 함수의 원형 선언시에 매개 변수까지 모두 동일하게 선언하여야 합니다.
