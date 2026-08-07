---
title: "명품 C++ programming 실습 문제 3장 11번"
date: 2020-03-03T18:40:58+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "CPP", "Main", "programming", "구현부", "명품", "선언부", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

다음 코드에서 Box 클래스의 선언부와 구현부를 Box.h, Box.cpp 파일로 분리하고 main() 함수 부분을 main.cpp로 분리하여 전체 프로그램을 완성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27 | #include<iostream>  using namespace std;    class Box {  int width, height;  char fill;  public:  Box(int w, int h) { setSize(w, h); fill = '\*';}  void setFill(char f) {fill = f;}  void setSize(int w, int h) { width = w; height = h;}  void draw();  };  void Box::draw() {  for (int n = 0; n < height; n++) {  for (int m = 0; m < width; m++) cout << fill;  cout << endl;  }  }    int main() {  Box b(10, 2);  b.draw(); // 박스를 그린다.  cout << endl;  b.setSize(7, 4); // 박스의 크기를 변경한다.  b.setFill('^'); // 박스의 내부를 채울 문자를 '^'로 변경한다.  b.draw(); // 박스를 그린다.  } |

**목적 및 힌트 :**

선언부와 구현부로 나누기 연습

**실행 결과 :**

![](https://img.sobamemil.com/posts/53/img_1.png)

**코드 :**

● Box.h

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | class Box {  int width, height;  char fill;  public:  Box(int w, int h) { setSize(w, h); fill = '\*';}  void setFill(char f) {fill = f;}  void setSize(int w, int h) { width = w; height = h;}  void draw();  }; |

● Box.cpp

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11 | #include<iostream>  using namespace std;    #include "Box.h"    void Box::draw() {  for (int n = 0; n < height; n++) {  for (int m = 0; m < width; m++) cout << fill;  cout << endl;  }  } |

● main.cpp

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13 | #include<iostream>  using namespace std;    #include "Box.h"    int main() {  Box b(10, 2);  b.draw();  cout << endl;  b.setSize(7, 4);  b.setFill('^');  b.draw();  } |

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 4장 1번](/55)  (1) | 2020.03.04 |
| [명품 C++ programming 실습 문제 3장 12번](/54)  (2) | 2020.03.03 |
| [명품 C++ programming 실습 문제 3장 10번](/52)  (1) | 2020.03.03 |
| [명품 C++ programming 실습 문제 3장 9번](/51)  (1) | 2020.03.03 |
| [명품 C++ programming 실습 문제 3장 8번](/50)  (1) | 2020.03.03 |