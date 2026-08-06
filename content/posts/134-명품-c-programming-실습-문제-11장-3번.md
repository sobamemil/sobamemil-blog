---
title: "명품 C++ programming 실습 문제 11장 3번"
date: 2020-03-27T15:16:48+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["buffer", "C++", "cin", "ignore", "Istream", "programming", "명품", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

한 줄에 '영어문장;한글문자' 형식으로 키 입력될 때, cin.ignore()를 이용하여 ';' 이후에 입력된 문자열을 화면에 출력하는 프로그램을 작성하라.

아래에서 ^Z(ctrl-z) 키는 입력 종료는 나타내는 키이며, cin.get()은 EOF를 리턴한다.

**실행 결과 :**

![](https://img.sobamemil.com/posts/134/img_1.png)

**목적 및 힌트 :**

cin.get(), EOF, cin.ignore() 활용

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12 | #include <iostream>  using namespace std;    int main() {  int ch;  cin.ignore(100, ';'); // 영어 문장이 최대 99개의 문자로 입력된다고 가정한다.  while((ch=cin.get()) != EOF) {  cout.put(ch);  if(ch == '\n')  cin.ignore(100, ';'); // 영어 문장이 최대 99개의 문자로 입력된다고 가정한다.  }  } |

**설명 :**

ignore() 함수를 사용해서 입력 스트림 버퍼에 있는 문자들을 제거할 수 있습니다.

함수의 원형은 istream& ignore (streamsize n = 1, int delim = EOF); 이고 사용 예는 아래와 같습니다.

|  |  |
| --- | --- |
| 1  2  3 | cin.ignore(10); // 입력 스트림에서 10개의 문자 제거    cin.ignore(10, '\n'); // 입력 스트림에서 10개의 문자 제거, 제거 도중 '\n'을 만나면 '\n'을 제거하고 중단 |

ignore() 함수에 대한 더 자세한 내용은 아래 사이트에서 참고하시면 됩니다.

<http://www.cplusplus.com/reference/istream/istream/ignore/?kw=cin.ignore>

[istream::ignore - C++ Reference

public member function istream& ignore (streamsize n = 1, int delim = EOF); Extract and discard characters Extracts characters from the input sequence and discards them, until either n characters have been extracted, or one compares eq

www.cplusplus.com](http://www.cplusplus.com/reference/istream/istream/ignore/?kw=cin.ignore)

공유하기

게시글 관리

**코딩은 내일부터 ;**

[저작자표시 비영리
(새창열림)](https://creativecommons.org/licenses/by-nc/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 11장 5번](/136)  (3) | 2020.03.27 |
| [명품 C++ programming 실습 문제 11장 4번](/135)  (1) | 2020.03.27 |
| [명품 C++ programming 실습 문제 11장 2번](/133)  (1) | 2020.03.27 |
| [명품 C++ programming 실습 문제 11장 1번](/132)  (1) | 2020.03.27 |
| [명품 C++ programming 실습 문제 10장 16번](/126)  (1) | 2020.03.11 |
