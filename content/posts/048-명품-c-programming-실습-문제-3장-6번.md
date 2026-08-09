---
title: "명품 C++ programming 실습 문제 3장 6번"
date: 2020-03-03T16:20:43+09:00
draft: false
categories: ["💻 개발 & CS", "C++ 프로그래밍"]
tags: ["C++", "EvenRandom", "programming", "rand", "srand", "명품", "실습문제", "연습문제", "짝수", "프로그래밍"]
---

**문제 :**

문제 5번을 참고하여 짝수 정수만 랜덤하게 발생시키는 EvenRandom 클래스를 작성하고 EvenRandom 클래스를 이용하여 10개의 짝수를 랜덤하게 출력하는 프로그램을 완성하라.

0도 짝수로 처리한다.

<b>목적 및 힌트 :</b>

클래스 작성 및 클래스 활용

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/48/img_1.png)

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40 | #include<iostream>  #include<cstdlib>  #include<ctime>  using namespace std;    class EvenRandom{  public:  EvenRandom();  int next();  int nextInRange(int a, int b);  };  EvenRandom::EvenRandom(){  srand((unsigned)time(0));  }    int EvenRandom::next() {  int ran = rand();  if(ran%2 == 0) return ran;  else return --ran;  }  int EvenRandom::nextInRange(int a, int b){  int ran = rand()%(b-a+1) + a;  if(ran%2 == 0) return ran;  else return --ran;  }    int main(){  EvenRandom r;  cout << "-- 0에서 " << RAND\_MAX << "까지의 랜덤 정수 10 개--" << endl;  for(int i=0; i<10; i++) {  int n = r.next(); // 0에서 RAND\_MAX(32767) 사이의 랜덤한 정수  cout << n << ' ';  }  cout << endl << endl << "-- 2에서 " << "10 까지의 랜덤 정수 10 개 --" << endl;  for(int i=0; i<10; i++) {  int n = r.nextInRange(2,10); // 2에서 10 사이의 랜덤한 정수  cout << n << ' ';  }  cout << endl;  } |

<b>설명 :</b>

이전 글에 있는 실습 문제 5번을 참고하여 작성하면 되는 문제입니다.

짝수인 정수만 랜덤하게 출력하기 위해 if문으로 짝수인지 판단하고, 짝수가 아닐시 1을 빼서 return 해주었습니다.
