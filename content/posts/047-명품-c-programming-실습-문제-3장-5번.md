---
title: "명품 C++ programming 실습 문제 3장 5번"
date: 2020-03-03T16:09:46+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "cstdlib", "CTime", "programming", "rand()", "Random", "명품", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

랜덤 수를 발생시키는 Random 클래스를 만들자. Random 클래스를 이용하여 랜덤 한 정수를 10개 출력하는 사례는 다음과 같다.

Random 클래스가 생성자, next(), nextInRange()의 3개의 멤버 함수를 가지도록 작성하고 main() 함수와 합쳐 하나의 cpp 파일에 구현하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | int main() {  Random r;  cout << "-- 0에서 " << RAND\_MAX << "까지의 랜덤 정수 10 개--" << endl;  for(int i=0; i<10; i++) {  int n = r.next(); // 0에서 RAND\_MAX(32767) 사이의 랜덤한 정수  cout << n << ' ';  }  cout << endl << endl << "-- 2에서 " << "4 까지의 랜덤 정수 10 개 --" << endl;  for(int i=0; i<10; i++) {  int n = r.nextInRange(2,4); // 2에서 4 사이의 랜덤한 정수  cout << n << ' ';  }  cout << endl;  } |

**목적 및 힌트 :**

클래스와 멤버 변수, 멤버 함수 만들기

RAND\_MAX 상수는 <cstdlib> 헤더 파일에 선언되어 있는 정수 32767.

랜덤 정수를 발생시키기 위해서는 다음 두 라인의 코드가 필요하고, <cstdlib>와 <ctime> 헤더 파일을 include 해야 한다.

|  |  |
| --- | --- |
| 1  2 | srand((unsinged)time(0)); // 시작할 때마다, 다른 랜덤수를 발생시키기 위한 seed 설정.  int n = rand(); // 0에서 RAND\_MAX(32767) 사이의 랜덤한 정수 발생. |

**실행 결과 :**

![](https://img.sobamemil.com/posts/47/img_1.png)

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36 | #include<iostream>  #include<cstdlib>  #include<ctime>  using namespace std;    class Random{  public:  Random();  int next();  int nextInRange(int a, int b);  };  Random::Random(){  srand((unsigned)time(0));  }    int Random::next() {  return rand();  }  int Random::nextInRange(int a, int b){  return rand()%(b-a+1) + a;  }    int main() {  Random r;  cout << "-- 0에서 " << RAND\_MAX << "까지의 랜덤 정수 10 개--" << endl;  for(int i=0; i<10; i++) {  int n = r.next(); // 0에서 RAND\_MAX(32767) 사이의 랜덤한 정수  cout << n << ' ';  }  cout << endl << endl << "-- 2에서 " << "4 까지의 랜덤 정수 10 개 --" << endl;  for(int i=0; i<10; i++) {  int n = r.nextInRange(2,4); // 2에서 4 사이의 랜덤한 정수  cout << n << ' ';  }  cout << endl;  } |

**설명 :**

a~b 사이의 랜덤한 정수를 return 해주기 위해 rand() % (b-a+1) + a; 라는 식을 사용했습니다.


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 3장 7번](/49)  (2) | 2020.03.03 |
| [명품 C++ programming 실습 문제 3장 6번](/48)  (2) | 2020.03.03 |
| [명품 C++ programming 실습 문제 3장 4번](/46)  (8) | 2020.03.03 |
| [명품 C++ programming 실습 문제 3장 3번](/45)  (3) | 2020.03.02 |
| [명품 C++ programming 실습 문제 3장 2번](/44)  (2) | 2020.03.02 |