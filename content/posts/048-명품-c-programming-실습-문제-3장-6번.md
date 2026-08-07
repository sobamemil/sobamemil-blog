---
title: "명품 C++ programming 실습 문제 3장 6번"
date: 2020-03-03T16:20:43+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "EvenRandom", "programming", "rand", "srand", "명품", "실습문제", "연습문제", "짝수", "프로그래밍"]
---

**문제 :**

문제 5번을 참고하여 짝수 정수만 랜덤하게 발생시키는 EvenRandom 클래스를 작성하고 EvenRandom 클래스를 이용하여 10개의 짝수를 랜덤하게 출력하는 프로그램을 완성하라.

0도 짝수로 처리한다.

[2020/03/03 - [C++/명품 C++ programming] - 명품 C++ programming 실습 문제 3장 5번](https://sobamemil.tistory.com/47)

[명품 C++ programming 실습 문제 3장 5번

문제 : 랜덤 수를 발생시키는 Random 클래스를 만들자. Random 클래스를 이용하여 랜덤 한 정수를 10개 출력하는 사례는 다음과 같다. Random 클래스가 생성자, next(), nextInRange()의 3개의 멤버 함수를 가지도..

sobamemil.tistory.com](https://sobamemil.tistory.com/47)

**목적 및 힌트 :**

클래스 작성 및 클래스 활용

**실행 결과 :**

![](https://img.sobamemil.com/posts/48/img_1.png)

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40 | #include<iostream>  #include<cstdlib>  #include<ctime>  using namespace std;    class EvenRandom{  public:  EvenRandom();  int next();  int nextInRange(int a, int b);  };  EvenRandom::EvenRandom(){  srand((unsigned)time(0));  }    int EvenRandom::next() {  int ran = rand();  if(ran%2 == 0) return ran;  else return --ran;  }  int EvenRandom::nextInRange(int a, int b){  int ran = rand()%(b-a+1) + a;  if(ran%2 == 0) return ran;  else return --ran;  }    int main(){  EvenRandom r;  cout << "-- 0에서 " << RAND\_MAX << "까지의 랜덤 정수 10 개--" << endl;  for(int i=0; i<10; i++) {  int n = r.next(); // 0에서 RAND\_MAX(32767) 사이의 랜덤한 정수  cout << n << ' ';  }  cout << endl << endl << "-- 2에서 " << "10 까지의 랜덤 정수 10 개 --" << endl;  for(int i=0; i<10; i++) {  int n = r.nextInRange(2,10); // 2에서 10 사이의 랜덤한 정수  cout << n << ' ';  }  cout << endl;  } |

**설명 :**

이전 글에 있는 실습 문제 5번을 참고하여 작성하면 되는 문제입니다.

짝수인 정수만 랜덤하게 출력하기 위해 if문으로 짝수인지 판단하고, 짝수가 아닐시 1을 빼서 return 해주었습니다.

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 3장 8번](/50)  (1) | 2020.03.03 |
| [명품 C++ programming 실습 문제 3장 7번](/49)  (2) | 2020.03.03 |
| [명품 C++ programming 실습 문제 3장 5번](/47)  (4) | 2020.03.03 |
| [명품 C++ programming 실습 문제 3장 4번](/46)  (8) | 2020.03.03 |
| [명품 C++ programming 실습 문제 3장 3번](/45)  (3) | 2020.03.02 |