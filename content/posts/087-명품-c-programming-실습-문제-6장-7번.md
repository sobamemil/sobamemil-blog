---
title: "명품 C++ programming 실습 문제 6장 7번"
date: 2020-03-06T15:57:35+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["ascii", "C++", "cstdlib", "CTime", "programming", "rand()", "명품", "실습문제", "연습문제", "프로그래밍"]
---

<b>문제 :</b>

다음과 같은 static 멤버를 가진 Random 클래스를 완성하라(Open Challenge 힌트 참고).

그리고 Random 클래스를 이용하여 다음과 같이 랜덤한 값을 출력하는 main() 함수도 작성하라.

main()에서 Random 클래스의 seed() 함수를 활용하라.

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/87/img_1.png)

<b>목적 및 힌트 :</b>

static 멤버를 가진 클래스 만들기 및 사용 연습

정수를 랜덤하게 생성하는 코드는 다음을 이용하면 됩니다.

|  |  |
| --- | --- |
| 1  2  3 | srand((unsigned)time(0)); // 항상 다른 랜덤수를 방생시키기 위한 seed 설정  int n = rand(); // 0에서 RAND\_MAX(32767) 사이의 랜덤한 정수가 n에 발생  n = n % 100; // n은 0에서 99 사이의 정수 |

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56 | #include<iostream>  #include<ctime>  #include<cstdlib>  using namespace std;    class Random{  public:  static void seed() { srand((unsigned)time(0)); }  static int nextInt(int min=0, int max=32767);  static char nextAlphabet();  static double nextDouble();  };    int Random::nextInt(int min, int max){  int a=0;  while(true){  a = rand() % (max+1);  if(min<=a)  break;  }  return a;  }    char Random::nextAlphabet(){  char b = 0;  while(true){  b = rand() % 'z';  if( b>='a' || ('A'<=b && b<='Z') )  break;  }  return b;  }    double Random::nextDouble(){  double c = 0;  double max = 32767;  c = rand()/max;  return c;  }    int main() {  Random::seed();  cout << "1에서 100까지 랜덤한 정수 10개를 출력합니다\n";  for(int i=0; i<10; i++){  cout << Random::nextInt(1,100) << ' ';  }  cout << endl << "알파벳을 랜덤하게 10개를 출력합니다\n";  for(int i=0; i<10; i++){  cout << Random::nextAlphabet() << ' ';  }  cout << endl << "랜덤한 실수를 10개를 출력합니다\n";  for(int i=0; i<10; i++){  cout << Random::nextDouble() << ' ';  if(i==4) cout << endl;  }  } |

<b>설명 :</b>

랜덤한 정수를 생성하는 문제들을 많이 풀었었는데, 그것을 응용하여 정수 뿐 아니라 ASCII 코드와 실수를 다루는 문제입니다.

방식은 동일하기 때문에 크게 어렵지는 않습니다.


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 6장 9번](/89)  (2) | 2020.03.06 |
| [명품 C++ programming 실습 문제 6장 8번](/88)  (1) | 2020.03.06 |
| [명품 C++ programming 실습 문제 6장 6번](/86)  (2) | 2020.03.06 |
| [명품 C++ programming 실습 문제 6장 5번](/85)  (1) | 2020.03.06 |
| [명품 C++ programming 실습 문제 6장 4번](/84)  (2) | 2020.03.06 |