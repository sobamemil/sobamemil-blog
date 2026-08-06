---
title: "명품 C++ programming 실습 문제 11장 11번"
date: 2020-04-02T14:19:10+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "Istream", "manipulator", "POS", "programming", "명품", "실습문제", "연습문제", "조작자", "프로그래밍"]
---

**문제 :**

다음은 프로그램과 실행 결과를 보여준다. pos 조작자를 작성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | #include <iostream>  using namespace std;    int main() {  int x, y;  cin >> pos >> x;  cin >> pos >> y;  cout << x << ',' << y << endl;  } |

**실행 결과 :**

![](https://img.sobamemil.com/posts/142/img_1.png)

**목적 및 힌트 :**

조작자 작성 연습

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | #include <iostream>  using namespace std;    istream& pos (istream& ins) { // pos 조작자  cout << "위치는? ";  return ins;  }    int main() {  int x, y;  cin >> pos >> x;  cin >> pos >> y;  cout << x << ',' << y << endl;  } |

공유하기

게시글 관리

**코딩은 내일부터 ;**

[저작자표시 비영리
(새창열림)](https://creativecommons.org/licenses/by-nc/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 11장 12번](/143)  (5) | 2020.04.02 |
| [명품 C++ programming 실습 문제 11장 10번](/141)  (1) | 2020.04.02 |
| [명품 C++ programming 실습 문제 11장 9번](/140)  (3) | 2020.04.02 |
| [명품 C++ programming 실습 문제 11장 8번](/139)  (1) | 2020.04.02 |
| [명품 C++ programming 실습 문제 11장 7번](/138)  (1) | 2020.04.02 |
