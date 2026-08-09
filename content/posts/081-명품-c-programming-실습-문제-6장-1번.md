---
title: "명품 C++ programming 실습 문제 6장 1번"
date: 2020-03-05T16:27:22+09:00
draft: false
categories: ["💻 개발 & CS", "C++ 프로그래밍"]
tags: ["C++", "functionoverloading", "programming", "디폴트매개변수", "명품", "실습문제", "연습문제", "프로그래밍", "함수중복"]
---

**문제 :**

add() 함수를 호출하는 main() 함수는 다음과 같다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8 | int main() {  int a[] = {1,2,3,4,5};  int b[] = {6,7,8,9,10};  int c = add(a, 5); // 배열 a의 정수를 모두 더한 값 리턴  int d = add(a, 5, b); // 배열 a와 b의 정수를 모두 더한 값 리턴  cout << c << endl; // 15 출력  cout << d << endl; // 55 출력  } |

(1) add() 함수를 중복 작성하고 프로그램을 완성하라.

(2) 디폴트 매개 변수를 가진 하나의 add() 함수를 작성하고 프로그램을 완성하라.

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/81/img_1.png)

<b>목적 및 힌트 :</b>

함수 중복, 디폴트 매개 변수 연습

<b>코드 :</b>

● 문제 (1)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25 | #include<iostream>  using namespace std;    int add(int \*a, int b){  int sum  = 0;  for(int i=0; i<b; i++)  sum += a[i];  return sum;  }    int add(int \*a, int b, int \*c){  int sum  = 0;  for(int i=0; i<b; i++)  sum += a[i] + c[i];  return sum;  }    int main() {  int a[] = {1,2,3,4,5};  int b[] = {6,7,8,9,10};  int c = add(a, 5); // 배열 a의 정수를 모두 더한 값 리턴  int d = add(a, 5, b); // 배열 a와 b의 정수를 모두 더한 값 리턴  cout << c << endl; // 15 출력  cout << d << endl; // 55 출력  } |

● 문제 (2)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20 | #include<iostream>  using namespace std;    int add(int \*a, int b, int \*c = NULL) {  int sum  = 0;  for(int i=0; i<b; i++) {  sum += a[i];  if(c != NULL)  sum += c[i];  }  return sum;  }  int main() {  int a[] = {1,2,3,4,5};  int b[] = {6,7,8,9,10};  int c = add(a, 5); // 배열 a의 정수를 모두 더한 값 리턴  int d = add(a, 5, b); // 배열 a와 b의 정수를 모두 더한 값 리턴  cout << c << endl; // 15 출력  cout << d << endl; // 55 출력  } |

<b>설명 :</b>

디폴트 매개변수를 가진 함수를 작성하여 코드의 길이를 줄일 수 있습니다.
