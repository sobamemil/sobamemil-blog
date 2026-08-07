---
title: "명품 C++ programming 실습 문제 6장 3번"
date: 2020-03-05T16:54:35+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "Function", "overloading", "programming", "디폴트매개변수", "명품", "실습문제", "연습문제", "프로그래밍", "함수중복"]
---

**문제 :**

함수 big()을 호출하는 경우는 다음과 같다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6 | int main() {  int x = big(3, 5); // 3과 5중 큰 값은 5는 최대값 100보다 작으므로, 5 리턴  int y = big(300, 60); // 300과 60 중 큰 값 300이 최대값 100보다 크므로, 100리턴  int z = big(30, 60, 50); // 30과 60 중 큰 값 60이 최대값 50보다 크므로, 50리턴  cout << x << ' ' << y << ' ' << z << endl;  } |

(1) big() 함수를 2개 중복하여 작성하고 프로그램을 완성하라.

(2) 디폴트 매개 변수를 가진 하나의 함수로 big()을 작성하고 프로그램을 완성하라.

**실행 결과 :**

![](https://img.sobamemil.com/posts/83/img_1.png)

**목적 및 힌트 :**

함수 중복, 디폴트 매개 변수 연습

**코드 :**

● 문제 (1)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28 | #include<iostream>  using namespace std;    int big(int a, int b){  int max = 100;  int big = a;  if(big<b)  big = b;  if(big>max)  big = max;  return big;  }  int big(int a, int b, int c){  int max = c;  int big = a;  if(big<b)  big = b;  if(big>max)  big = max;  return big;  }    int main() {  int x = big(3, 5); // 3과 5중 큰 값은 5는 최대값 100보다 작으므로, 5 리턴  int y = big(300, 60); // 300과 60 중 큰 값 300이 최대값 100보다 크므로, 100리턴  int z = big(30, 60, 50); // 30과 60 중 큰 값 60이 최대값 50보다 크므로, 50리턴  cout << x << ' ' << y << ' ' << z << endl;  } |

● 문제 (2)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19 | #include<iostream>  using namespace std;    int big(int a, int b, int c = 100){  int max = c;  int big = a;  if(big<b)  big = b;  if(big>max)  big = max;  return big;  }    int main() {  int x = big(3, 5); // 3과 5중 큰 값은 5는 최대값 100보다 작으므로, 5 리턴  int y = big(300, 60); // 300과 60 중 큰 값 300이 최대값 100보다 크므로, 100리턴  int z = big(30, 60, 50); // 30과 60 중 큰 값 60이 최대값 50보다 크므로, 50리턴  cout << x << ' ' << y << ' ' << z << endl;  } |


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 6장 5번](/85)  (1) | 2020.03.06 |
| [명품 C++ programming 실습 문제 6장 4번](/84)  (2) | 2020.03.06 |
| [명품 C++ programming 실습 문제 6장 2번](/82)  (3) | 2020.03.05 |
| [명품 C++ programming 실습 문제 6장 1번](/81)  (1) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 12번](/80)  (2) | 2020.03.05 |