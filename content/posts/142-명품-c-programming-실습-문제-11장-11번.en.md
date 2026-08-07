---
title: "C++ Programming Ch.11 Exercise 11 Solution"
date: 2020-04-02T14:19:10+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "Istream", "manipulator", "POS", "programming", "명품", "실습문제", "연습문제", "조작자", "프로그래밍"]
---

**Problem:**

다음은 프로그램과 Execution Result를 보여준다. pos 조작자를 작성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | #include <iostream>  using namespace std;    int main() {  int x, y;  cin >> pos >> x;  cin >> pos >> y;  cout << x << ',' << y << endl;  } |

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/142/img_1.png)

<b>Objective & Hints:</b>

조작자 작성 연습

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | #include <iostream>  using namespace std;    istream& pos (istream& ins) { // pos 조작자  cout << "위치는? ";  return ins;  }    int main() {  int x, y;  cin >> pos >> x;  cin >> pos >> y;  cout << x << ',' << y << endl;  } |


](
