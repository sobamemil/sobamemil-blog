---
title: "명품 C++ programming 실습 문제 3장 7번"
date: 2020-03-03T16:44:34+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "programming", "Random", "랜덤정수", "명품", "실습문제", "연습문제", "프로그래밍"]
---<b>문제 :</b>

문제 5번을 참고하여 생성자를 이용하여 짝수 홀수를 선택할 수 있도록 SelectableRandom 클래스를 작성하고 짝수 10개, 홀수 10개를 랜덤하게 발생시키는 프로그램을 작성하라.

[2020/03/03 - [C++/명품 C++ programming] - 명품 C++ programming 실습 문제 3장 5번](https://sobamemil.tistory.com/47)

[명품 C++ programming 실습 문제 3장 5번

문제 : 랜덤 수를 발생시키는 Random 클래스를 만들자. Random 클래스를 이용하여 랜덤 한 정수를 10개 출력하는 사례는 다음과 같다. Random 클래스가 생성자, next(), nextInRange()의 3개의 멤버 함수를 가지도..

sobamemil.tistory.com](https://sobamemil.tistory.com/47)

<b>목적 및 힌트 :</b>

클래스 작성에서 매개 변수를 가진 생성자의 활용

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/49/img_1.png)

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65 | #include<iostream>  #include<cstdlib>  #include<ctime>  using namespace std;    class SelectableRandom{  int num;  public:  SelectableRandom(int \_num); // 매개변수로 짝수 혹은 홀수를 받는다  int next();  int nextInRange(int a, int b);  };  SelectableRandom::SelectableRandom(int \_num){  num = \_num;  srand((unsigned)time(0));  }    int SelectableRandom::next() {  int ran = rand();  if(num%2 == 0){ // 짝수 return  if(ran%2 == 0)  return ran;  else  return --ran;  }  else {  if(ran%2 == 0) // 홀수 return  return ++ran;  else  return ran;  }  }    int SelectableRandom::nextInRange(int a, int b){  int ran = rand()%(b-a+1) + a;  if(num%2 == 0) { // 짝수 return  if(ran%2 == 0)  return ran;  else  return ++ran;  }  else { // 홀수 return  if(ran%2 == 0)  return ++ran;  else  return ran;  }  }    int main() {  SelectableRandom r1(0); // 짝수 랜덤 정수 발생  cout << "-- 0에서 " << RAND\_MAX << "까지의 짝수 랜덤 정수 10 개--" << endl;  for(int i=0; i<10; i++) {  int n = r1.next();  cout << n << ' ';  }    SelectableRandom r2(1); // 홀수 랜덤 정수 발생  cout << endl << endl << "-- 2에서 " << "9 까지의 랜덤 홀수  정수 10 개 --" << endl;  for(int i=0; i<10; i++) {  int n = r2.nextInRange(2,9);  cout << n << ' ';  }  cout << endl;  } |

<b>설명 :</b>

SelectableRandom 클래스에서 생성자를 이용하여 짝수 홀수를 선택할 수 있게 하였습니다.

생성자 호출 시 전달해준 매개변수가 짝수이면 짝수 출력, 홀수이면 홀수를 출력하게 작성 하였습니다.

이를 이용해 매개변수를 사용자에게 직접 입력받아 생성자 호출 시 인자로 넘겨주어 사용자가 직접 짝수, 홀수를 선택할 수 있게 작성할 수도 있습니다.
