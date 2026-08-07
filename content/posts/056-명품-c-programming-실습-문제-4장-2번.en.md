---
title: "명품 C++ programming 실습 문제 4장 2번"
date: 2020-03-04T15:17:39+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "delete", "heap", "programming", "댕글링포인터", "메모리누수", "명품", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

정수 공간 5개를 배열로 동적 할당받고, 정수를 5개 입력받아 평균을 구하고 출력한 뒤 배열을 소멸시키도록 main() 함수를 작성하라.

**목적 및 힌트 :**

배열의 동적 할당 및 반환

**실행 결과 :**

![](https://img.sobamemil.com/posts/56/img_1.png)

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | #include<iostream>  using namespace std;    int main() {  int \*p = new int[5];  double sum = 0;  cout << "정수 5개 입력>>";  for(int i=0; i<5; i++) {  cin >> p[i];  sum += p[i];  }  cout << "평균 " << sum/5;  delete [] p;  } |

**설명 :**

배열을 동적 할당하여 사용 및 반환하는 문제입니다.

메모리를 동적으로 할당받아 사용한 후에는 꼭 delete를 해주는 습관을 기르는 게 좋습니다.

delete를 하지 않을경우 자신도 모르는 사이에 메모리 누수(Memory Leak) 현상이 생길 수 있습니다.

또한 메모리를 delete 한다고 하여도 포인터는 살아있으므로 접근하지 않도록 주의해야 합니다.

이때 해제된 메모리 영역을 여전히 가르키고 있는 포인터를 댕글링 포인터(Dangling Pointer)라고 합니다.


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 4장 4번](/58)  (5) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 3번](/57)  (1) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 1번](/55)  (1) | 2020.03.04 |
| [명품 C++ programming 실습 문제 3장 12번](/54)  (2) | 2020.03.03 |
| [명품 C++ programming 실습 문제 3장 11번](/53)  (1) | 2020.03.03 |