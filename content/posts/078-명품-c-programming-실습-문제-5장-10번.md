---
title: "명품 C++ programming 실습 문제 5장 10번"
date: 2020-03-05T15:40:57+09:00
draft: false
categories: ["개발 CS", "C++ 프로그래밍"]
tags: ["C++", "programming", "string", "명품", "문자열", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

참조를 리턴하는 코드를 작성해보자. 다음 코드와  실행 결과를 참고하여 append() 함수를 작성하고 전체 프로그램을 완성하라.

append()는 Buffer 객체에 문자열을 추가하고 Buffer 객체에 대한 참조를 반환하는 함수이다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | class Buffer{  string text;  public:  Buffer(string text) { this->text = text; }  void add(string next) { text += next; } // text에 next 문자열 덧붙이기  void print() { cout << text << endl; }  };    int main() {  Buffer buf("Hello");  Buffer& temp = append(buf, "Guys"); // buf의 문자열에 "Guys" 덧붙임  temp.print(); // "HelloGuys" 출력  buf.print(); // "HelloGuys" 출력  } |

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/78/img_1.png)

<b>목적 및 힌트 :</b>

참조 매개 변수와 참조 리턴 이해

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23 | #include<iostream>  #include<string>  using namespace std;    class Buffer{  string text;  public:  Buffer(string text) { this->text = text; }  void add(string next) { text += next; } // text에 next 문자열 덧붙이기  void print() { cout << text << endl; }  };    Buffer& append(Buffer& s, string g){  s.add(g);  return s;  }    int main() {  Buffer buf("Hello");  Buffer& temp = append(buf, "Guys"); // buf의 문자열에 "Guys" 덧붙임  temp.print(); // "HelloGuys" 출력  buf.print(); // "HelloGuys" 출력  } |
