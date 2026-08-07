---
title: "C++ Programming Ch.11 Exercise 7 Solution"
date: 2020-04-02T11:58:57+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "cctype", "iomanip", "isprint", "programming", "setf", "명품", "실습문제", "연습문제", "프로그래밍"]
---

**Problem:**

0에서 127까지 ASCII 코드와 해당 문자를 다음과 같이 출력하는 프로그램을 작성하라.

화면에 출력가능하지 않는 ASCII 코드는 '.'으로 출력하라.

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/138/img_1.png)

<b>Objective & Hints:</b>

cout으로 포맷 출력 응용 연습

문자가 출력 가능한지 알기 위해 bool isprint(int c); 함수를 사용하면 됩니다.

매개 변수 c는 문자 코드 값이고, <cctype> 헤더 파일을 include 해야합니다.

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46 | #include <iostream>  #include <cctype>  #include <iomanip>  using namespace std;    void showDec(int d) { // 10진수 출력  cout << setw(10) << dec << d;  }    void showHexa(int h) { // 16진수 출력  cout << setw(10) << hex << h;  }    void showChar(int c) { // ASCII 출력  int i=0;  if( (i = isprint(c)) != 0) // 출력 가능한 문자인지 확인  cout << setw(10) << (char)c;  else // 출력 불가능한 문자이면 "." 출력  cout << setw(10) << ".";  }    void print() {  for(int i=0; i<4; i++){  cout << setw(10) << "dec";  cout << setw(10) << "hexa";  cout << setw(10) << "char";  }  cout << endl;  for(int i=0; i<4; i++){  cout << setw(10) << "---";  cout << setw(10) << "----";  cout << setw(10) << "----";  }  cout << endl;  for(int i=0; i<128; i++){ // 127번 반복하여 dec, hexa, ASCII 출력  if(i%4==0 && i!=0)  cout << endl;  showDec(i);  showHexa(i);  showChar(i);  }  }  int main() {  cout.setf(ios::left); // 출력 포맷 왼쪽 정렬  print();  } |

<b>Explanation:</b>

포맷 출력을 하기 위해 조작자 setw() 함수를 사용하였고, 사용하기 위해서는 iomanip 헤더 파일을 include 해주어야 합니다.

입출력 조작자(manipulator)는 std::basic\_ostream의 << (출력)연산자나 std::basic\_istream의 >> (입력)연산자와 함께 사용할 수 있습니다.

또한 왼쪽으로 정렬하여 출력하는 포맷을 지정하기 위해 cout.setf(ios::left); 코드를 사용했고, ios\_base::setf() 함수와 조작자에 대한 내용은 아래 링크에서 자세히 볼 수 있습니다.

<http://www.cplusplus.com/reference/library/manipulators/>

[manipulators - C++ Reference

www.cplusplus.com](http://www.cplusplus.com/reference/library/manipulators/)

<http://www.cplusplus.com/reference/ios/ios_base/setf/>

[ios\_base::setf - C++ Reference

public member function set (1)fmtflags setf (fmtflags fmtfl); mask (2)fmtflags setf (fmtflags fmtfl, fmtflags mask); Set specific format flags The first form (1) sets the stream's format flags whose bits are set in fmtfl, leaving unchanged

www.cplusplus.com](http://www.cplusplus.com/reference/ios/ios_base/setf/)
