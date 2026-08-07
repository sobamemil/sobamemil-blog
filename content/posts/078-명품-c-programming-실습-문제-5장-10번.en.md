---
title: "명품 C++ programming 실습 문제 5장 10번"
date: 2020-03-05T15:40:57+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "programming", "string", "명품", "문자열", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

참조를 리턴하는 코드를 작성해보자. 다음 코드와  실행 결과를 참고하여 append() 함수를 작성하고 전체 프로그램을 완성하라.

append()는 Buffer 객체에 문자열을 추가하고 Buffer 객체에 대한 참조를 반환하는 함수이다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | class Buffer{  string text;  public:  Buffer(string text) { this->text = text; }  void add(string next) { text += next; } // text에 next 문자열 덧붙이기  void print() { cout << text << endl; }  };    int main() {  Buffer buf("Hello");  Buffer& temp = append(buf, "Guys"); // buf의 문자열에 "Guys" 덧붙임  temp.print(); // "HelloGuys" 출력  buf.print(); // "HelloGuys" 출력  } |

**실행 결과 :**

![](https://img.sobamemil.com/posts/78/img_1.png)

**목적 및 힌트 :**

참조 매개 변수와 참조 리턴 이해

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23 | #include<iostream>  #include<string>  using namespace std;    class Buffer{  string text;  public:  Buffer(string text) { this->text = text; }  void add(string next) { text += next; } // text에 next 문자열 덧붙이기  void print() { cout << text << endl; }  };    Buffer& append(Buffer& s, string g){  s.add(g);  return s;  }    int main() {  Buffer buf("Hello");  Buffer& temp = append(buf, "Guys"); // buf의 문자열에 "Guys" 덧붙임  temp.print(); // "HelloGuys" 출력  buf.print(); // "HelloGuys" 출력  } |


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 5장 12번](/80)  (2) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 11번](/79)  (1) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 9번](/77)  (3) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 8번](/76)  (9) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 7번](/75)  (1) | 2020.03.05 |