---
title: "C++ Programming Ch.7 Exercise 5 Solution"
date: 2020-03-06T17:55:15+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "friend", "programming", "명품", "실습문제", "연산자중복", "연습문제", "코딩", "프렌드함수", "프로그래밍"]
---<b>Problem:</b>

다음 main()에서 Color 클래스는 3요소(빨강, 초록, 파랑)로 하나의 색을 나타내는 클래스이다(4장 Exercise Problem 1번 참고).

+ 연산자로 색을 더하고, == 연산자로 색을 비교하고자 한다.

Execution Result를 참고하여 Color 클래스와 연산자, 그리고 프로그램을 완성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11 | int main() {  Color red(255, 0, 0), blue(0, 0, 255), c;  c = red + blue;  c.show(); // 색 값 출력    Color fuchsia(255,0,255);  if(c == fuchsia)  cout << "보라색 맞음";  else  cout << "보라색 아님";  } |

(1) +와 == 연산자를 Color 클래스의 멤버 함수로 구현하라.

(2) +와 == 연산자를 Color 클래스의 프렌드 함수로 구현하라.

[2020/03/04 - [C++/명품 C++ programming] - 명품 C++ programming Exercise Problem 4장 1번](https://sobamemil.tistory.com/55)

[명품 C++ programming Exercise Problem 4장 1번

Problem: 다음은 색의 3요소인 red, green, blue로 색을 추상화한 Color 클래스를 선언하고 활용하는 코드이다. 빈칸을 채워라. red, green, blue는 0~255의 값만 가진다. 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 1..

sobamemil.tistory.com](https://sobamemil.tistory.com/55)

<b>실행</b> <b>결과 :</b>

![](https://img.sobamemil.com/posts/94/img_1.png)

<b>Objective & Hints:</b>

연산자를 클래스의 멤버 함수와 프렌드로 각각 중복

<b>Code:</b>

● 문제 (1)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38 | #include<iostream>  using namespace std;    class Color{  int red, blue, green;  public:  Color(){;}  Color(int a, int b, int c) { red = a; green = b; blue = c; }  show() { cout << red << ' ' << green << ' ' << blue << endl; }  Color operator+ (Color b);  bool operator== (Color a);  };    Color Color::operator+ (Color b){  Color a;  a.red = this->red + b.red;  a.green = this->green + b.green;  a.blue = this->blue + b.blue;  return a;  }    bool Color::operator== (Color a){  if(this->red == a.red && this->blue == a.blue)  return true;  return false;  }    int main() {  Color red(255, 0, 0), blue(0, 0, 255), c;  c = red + blue;  c.show(); // 색 값 출력    Color fuchsia(255,0,255);  if(c == fuchsia)  cout << "보라색 맞음";  else  cout << "보라색 아님";  } |

● 문제 (2)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38 | #include<iostream>  using namespace std;    class Color{  int red, blue, green;  public:  Color(){;}  Color(int a, int b, int c) { red = a; green = b; blue = c; }  show() { cout << red << ' ' << green << ' ' << blue << endl; }  friend Color operator+ (Color a, Color b);  friend bool operator== (Color a, Color b);  };    Color operator+ (Color a, Color b){  Color c;  c.red = a.red + b.red;  c.green = a.green + b.green;  c.blue = a.blue + b.blue;  return c;  }    bool operator== (Color a, Color b){  if(a.red == b.red && a.blue == b.blue)  return true;  return false;  }    int main() {  Color red(255, 0, 0), blue(0, 0, 255), c;  c = red + blue;  c.show(); // 색 값 출력    Color fuchsia(255,0,255);  if(c == fuchsia)  cout << "보라색 맞음";  else  cout << "보라색 아님";  } |
