---
title: "C++ Programming Ch.3 Exercise 1 Solution"
date: 2020-03-02T17:24:18+09:00
draft: false
categories: ["💻 Dev & CS", "C++ Programming"]
tags: ["C++", "class", "constructor", "programming", "Parameter", "Masterpiece", "Constructor Overloading", "Practice Problem", "Exercise", "Programming"]
---

**Problem:**

아래 main()의 Execution Result가 다음과 같도록 Tower 클래스를 작성하라.

![](https://img.sobamemil.com/posts/43/img_1.png)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | #include <iostream>  using namespace std;    int main() {  Tower myTower; // 1 미터  Tower seoulTower(100); // 100 미터  cout << "높이는 " << myTower.getHeight() << "미터" << endl;  cout << "높이는 " << seoulTower.getHeight() << "미터" << endl;  } |

<b>Objective & Hints:</b>

2개의 생성자와 여러 멤버를 가진 클래스 만들기

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/43/img_2.png)

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29 | #include<iostream>  using namespace std;    class Tower{  int height;  public:  Tower();  Tower(int h);  int getHeight();  };    Tower::Tower(){ // 매개변수가 없는 생성자  height=1;  }    Tower::Tower(int h){ // 매개변수가 하나 있는 생성자  height=h;  }    int Tower::getHeight(){  return height;  }    int main() {  Tower myTower;  Tower seoulTower(100);  cout << "높이는 " << myTower.getHeight() << "미터" << endl;  cout << "높이는 " << seoulTower.getHeight() << "미터" << endl;  } |

<b>Explanation:</b>

C++에서는 생성자 중복(Constructor Overloading)이 가능한데, 이를 이용하여 매개 변수의 개수가 다른 생성자를 만드는 문제입니다.
