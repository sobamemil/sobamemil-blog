---
title: "C++ Programming Ch.3 Exercise 11 Solution"
date: 2020-03-03T18:40:58+09:00
draft: false
categories: ["💻 Dev & CS", "C++ Programming"]
tags: ["C++", "CPP", "Main", "programming", "Implementation", "Masterpiece", "Declaration", "Practice Problem", "Exercise", "Programming"]
---

**Problem:**

다음 코드에서 Box 클래스의 선언부와 구현부를 Box.h, Box.cpp 파일로 분리하고 main() 함수 부분을 main.cpp로 분리하여 전체 프로그램을 완성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27 | #include<iostream>  using namespace std;    class Box {  int width, height;  char fill;  public:  Box(int w, int h) { setSize(w, h); fill = '\*';}  void setFill(char f) {fill = f;}  void setSize(int w, int h) { width = w; height = h;}  void draw();  };  void Box::draw() {  for (int n = 0; n < height; n++) {  for (int m = 0; m < width; m++) cout << fill;  cout << endl;  }  }    int main() {  Box b(10, 2);  b.draw(); // 박스를 그린다.  cout << endl;  b.setSize(7, 4); // 박스의 크기를 변경한다.  b.setFill('^'); // 박스의 내부를 채울 문자를 '^'로 변경한다.  b.draw(); // 박스를 그린다.  } |

<b>Objective & Hints:</b>

선언부와 구현부로 나누기 연습

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/53/img_1.png)

<b>Code:</b>

● Box.h

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | class Box {  int width, height;  char fill;  public:  Box(int w, int h) { setSize(w, h); fill = '\*';}  void setFill(char f) {fill = f;}  void setSize(int w, int h) { width = w; height = h;}  void draw();  }; |

● Box.cpp

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11 | #include<iostream>  using namespace std;    #include "Box.h"    void Box::draw() {  for (int n = 0; n < height; n++) {  for (int m = 0; m < width; m++) cout << fill;  cout << endl;  }  } |

● main.cpp

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13 | #include<iostream>  using namespace std;    #include "Box.h"    int main() {  Box b(10, 2);  b.draw();  cout << endl;  b.setSize(7, 4);  b.setFill('^');  b.draw();  } |
