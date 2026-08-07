---
title: "명품 C++ programming 실습 문제 3장 1번"
date: 2020-03-02T17:24:18+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "class", "constructor", "programming", "매개변수", "명품", "생성자중복", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

아래 main()의 실행 결과가 다음과 같도록 Tower 클래스를 작성하라.

![](https://img.sobamemil.com/posts/43/img_1.png)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | #include <iostream>  using namespace std;    int main() {  Tower myTower; // 1 미터  Tower seoulTower(100); // 100 미터  cout << "높이는 " << myTower.getHeight() << "미터" << endl;  cout << "높이는 " << seoulTower.getHeight() << "미터" << endl;  } |

**목적 및 힌트 :**

2개의 생성자와 여러 멤버를 가진 클래스 만들기

**실행 결과 :**

![](https://img.sobamemil.com/posts/43/img_2.png)

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29 | #include<iostream>  using namespace std;    class Tower{  int height;  public:  Tower();  Tower(int h);  int getHeight();  };    Tower::Tower(){ // 매개변수가 없는 생성자  height=1;  }    Tower::Tower(int h){ // 매개변수가 하나 있는 생성자  height=h;  }    int Tower::getHeight(){  return height;  }    int main() {  Tower myTower;  Tower seoulTower(100);  cout << "높이는 " << myTower.getHeight() << "미터" << endl;  cout << "높이는 " << seoulTower.getHeight() << "미터" << endl;  } |

**설명 :**

C++에서는 생성자 중복(Constructor Overloading)이 가능한데, 이를 이용하여 매개 변수의 개수가 다른 생성자를 만드는 문제입니다.

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 3장 3번](/45)  (3) | 2020.03.02 |
| [명품 C++ programming 실습 문제 3장 2번](/44)  (2) | 2020.03.02 |
| [명품 C++ programming 실습 문제 2장 16번](/42)  (3) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 15번](/41)  (3) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 14번](/40)  (3) | 2020.02.28 |