---
title: "C++ Programming Ch.11 Exercise 3 Solution"
date: 2020-03-27T15:16:48+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["buffer", "C++", "cin", "ignore", "Istream", "programming", "명품", "실습문제", "연습문제", "프로그래밍"]
---<b>Problem:</b>

한 줄에 '영어문장;한글문자' 형식으로 키 입력될 때, cin.ignore()를 이용하여 ';' 이후에 입력된 문자열을 화면에 출력하는 프로그램을 작성하라.

아래에서 ^Z(ctrl-z) 키는 입력 종료는 나타내는 키이며, cin.get()은 EOF를 리턴한다.

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/134/img_1.png)

<b>Objective & Hints:</b>

cin.get(), EOF, cin.ignore() 활용

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12 | #include <iostream>  using namespace std;    int main() {  int ch;  cin.ignore(100, ';'); // 영어 문장이 최대 99개의 문자로 입력된다고 가정한다.  while((ch=cin.get()) != EOF) {  cout.put(ch);  if(ch == '\n')  cin.ignore(100, ';'); // 영어 문장이 최대 99개의 문자로 입력된다고 가정한다.  }  } |

<b>Explanation:</b>

ignore() 함수를 사용해서 입력 스트림 버퍼에 있는 문자들을 제거할 수 있습니다.

함수의 원형은 istream& ignore (streamsize n = 1, int delim = EOF); 이고 사용 예는 아래와 같습니다.

|  |  |
| --- | --- |
| 1  2  3 | cin.ignore(10); // 입력 스트림에서 10개의 문자 제거    cin.ignore(10, '\n'); // 입력 스트림에서 10개의 문자 제거, 제거 도중 '\n'을 만나면 '\n'을 제거하고 중단 |

ignore() 함수에 대한 더 자세한 내용은 아래 사이트에서 참고하시면 됩니다.

<http://www.cplusplus.com/reference/istream/istream/ignore/?kw=cin.ignore>

[istream::ignore - C++ Reference

public member function istream& ignore (streamsize n = 1, int delim = EOF); Extract and discard characters Extracts characters from the input sequence and discards them, until either n characters have been extracted, or one compares eq

www.cplusplus.com](http://www.cplusplus.com/reference/istream/istream/ignore/?kw=cin.ignore)


](
