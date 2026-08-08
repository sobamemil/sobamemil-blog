---
title: "C++ Programming Ch.4 Exercise 13 Solution"
date: 2020-03-04T17:45:19+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "CString", "programming", "tolower", "toupper", "Masterpiece", "Practice Problem", "Exercise", "Programming", "Histogram"]
---

**Problem:**

영문자로 구성된 텍스트에 대해 각 알파벳에 해당하는 문자가 몇 개인지 출력하는 히스토그램 클래스 Histogram을 만들어보자.

대문자는 모두 소문자로 변환하여 처리한다.

Histogram 클래스를 활용하는 사례와 Execution Result는 다음과 같다.

|  |  |
| --- | --- |
| 1  2  3  4  5 | Histogram elvisHisto("Wise men say, only fools rush in But I can't help, ");  elvisHisto.put("falling in love with you");  elvisHisto.putc('-');  elvisHisto.put("Elvis Presley");  elvisHisto.print(); |

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/67/img_1.png)

<b>Objective & Hints:</b>

클래스 만들기 종합 응용

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55 | #include<iostream>  #include<string>  using namespace std;    class Histogram {  string sent;  public:  Histogram(string sent);  void put(string sent);  void putc(char c);  void print();  };    Histogram::Histogram(string text){  sent = text;  cout << sent << endl;  }  void Histogram::put(string text){  sent += text;  cout << text;  }  void Histogram::putc(char c){  sent += c;  cout << c;  }  void Histogram::print(){  int alpha[26] = { 0 };  int num = 0;  for (int i = 0; i < sent.length(); i++) {  if(isalpha(sent[i])){  char c = tolower(sent[i]);  alpha[c - 'a']++;  num++;  }  }  cout << endl << endl;  cout << "총 알파벳 수 " << num;  cout << endl << endl;  for (int i = 0; i < 26; ++i) {  char c = 'a' + i;  cout << c << " (" << alpha[i] << ")\t: ";  for (int j = 0; j < alpha[i]; ++j) {  cout << "\*";  }  cout << endl;  }  }    int main() {  Histogram elvisHisto("Wise men say, only fools rush in But I can't help, ");  elvisHisto.put("falling in love with you");  elvisHisto.putc('-');  elvisHisto.put("Elvis Presley");  elvisHisto.print();  } |

<b>Explanation:</b>

아래 비슷한 문제를 참고하여 코드를 작성하면 조금 더 수월할 것 같습니다.
