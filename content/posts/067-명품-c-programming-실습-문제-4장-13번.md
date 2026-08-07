---
title: "명품 C++ programming 실습 문제 4장 13번"
date: 2020-03-04T17:45:19+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "CString", "programming", "tolower", "toupper", "명품", "실습문제", "연습문제", "프로그래밍", "히스토그램"]
---

**문제 :**

영문자로 구성된 텍스트에 대해 각 알파벳에 해당하는 문자가 몇 개인지 출력하는 히스토그램 클래스 Histogram을 만들어보자.

대문자는 모두 소문자로 변환하여 처리한다.

Histogram 클래스를 활용하는 사례와 실행 결과는 다음과 같다.

|  |  |
| --- | --- |
| 1  2  3  4  5 | Histogram elvisHisto("Wise men say, only fools rush in But I can't help, ");  elvisHisto.put("falling in love with you");  elvisHisto.putc('-');  elvisHisto.put("Elvis Presley");  elvisHisto.print(); |

**실행 결과 :**

![](https://img.sobamemil.com/posts/67/img_1.png)

**목적 및 힌트 :**

클래스 만들기 종합 응용

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55 | #include<iostream>  #include<string>  using namespace std;    class Histogram {  string sent;  public:  Histogram(string sent);  void put(string sent);  void putc(char c);  void print();  };    Histogram::Histogram(string text){  sent = text;  cout << sent << endl;  }  void Histogram::put(string text){  sent += text;  cout << text;  }  void Histogram::putc(char c){  sent += c;  cout << c;  }  void Histogram::print(){  int alpha[26] = { 0 };  int num = 0;  for (int i = 0; i < sent.length(); i++) {  if(isalpha(sent[i])){  char c = tolower(sent[i]);  alpha[c - 'a']++;  num++;  }  }  cout << endl << endl;  cout << "총 알파벳 수 " << num;  cout << endl << endl;  for (int i = 0; i < 26; ++i) {  char c = 'a' + i;  cout << c << " (" << alpha[i] << ")\t: ";  for (int j = 0; j < alpha[i]; ++j) {  cout << "\*";  }  cout << endl;  }  }    int main() {  Histogram elvisHisto("Wise men say, only fools rush in But I can't help, ");  elvisHisto.put("falling in love with you");  elvisHisto.putc('-');  elvisHisto.put("Elvis Presley");  elvisHisto.print();  } |

**설명 :**

아래 비슷한 문제를 참고하여 코드를 작성하면 조금 더 수월할 것 같습니다.

[2020/02/28 - [C++/명품 C++ programming] - 명품 C++ programming 실습 문제 2장 16번](https://sobamemil.tistory.com/42)

[명품 C++ programming 실습 문제 2장 16번

문제 : 영문 텍스트를 입력받아 알파벳 히스토그램을 그리는 프로그램을 작성하라. 대문자는 모두 소문자로 집계하며, 텍스트 입력의 끝은 ';' 문자로 한다. 목적 및 힌트 : 문자열 읽기, C++ 프로그램 종합 응용..

sobamemil.tistory.com](https://sobamemil.tistory.com/42)

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 5장 1번](/69)  (4) | 2020.03.05 |
| [명품 C++ programming 실습 문제 4장 14번](/68)  (1) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 12번](/66)  (2) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 11번](/65)  (3) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 10번](/64)  (1) | 2020.03.04 |