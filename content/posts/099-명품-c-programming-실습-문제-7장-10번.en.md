---
title: "C++ Programming Ch.7 Exercise 10 Solution"
date: 2020-03-06T19:52:18+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "programming", "Statistics", "명품", "실습문제", "연습문제", "참조리턴", "참조연산자", "참조자", "프로그래밍"]
---<b>Problem:</b>

통계를 내는 Statistics 클래스를 만들려고 한다.

데이터는 Statistics 클래스 내부에 int 배열을 동적으로 할당받아 유지한다.

다음과 같은 연산이 잘 이루어지도록 Statistics 클래스와 !, >>, <<, ~ 연산자 함수를 작성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16 | int main() {  Statistics stat;  if(!stat) cout << "현재 통계 데이타가 없습니다." << endl;    int x[5];  cout << "5 개의 정수를 입력하라>>";  for(int i=0; i<5; i++) cin >> x[i]; // x[i]에 정수 입력    for(int i=0; i<5; i++) stat << x[i]; // x[i] 값을 통계 객체에 삽입한다.  stat << 100 << 200; // 100, 200을 통계 객체에 삽입한다.  ~stat; // 통계 데이터를 모두 출력한다.    int avg;  stat >> avg; // 통계 객체로부터 평균을 받는다.  cout << "avg=" << avg << endl;  // 평균을 출력한다.  } |

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/99/img_1.png)

<b>Objective & Hints:</b>

참조 리턴 등 참조자(&) 사용이 필요한 연산자 종합 응용

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51 | #include<iostream>  using namespace std;    class Statistics{  int \*a;  int cnt; //배열의 원소 개수  public:  Statistics() { a = new int[8]; cnt=0; }    bool operator! (){  if( this->a && this->cnt==0) return true;  return false;  }    Statistics& operator<< (int num){  this->a[cnt] = num;  cnt ++;  return \*this;  }  void operator~ (){  for(int i=0; i<cnt; i++)  cout << this->a[i] << ' ';  cout << endl;  }  void operator>> (int& avg){  avg = 0;  for(int i=0; i<cnt; i++)  avg += a[i];  avg /= cnt;  }  ~Statistics(){  delete [] a;  }  };    int main() {  Statistics stat;  if(!stat) cout << "현재 통계 데이타가 없습니다." << endl;    int x[5];  cout << "5 개의 정수를 입력하라>>";  for(int i=0; i<5; i++) cin >> x[i]; // x[i]에 정수 입력    for(int i=0; i<5; i++) stat << x[i]; // x[i] 값을 통계 객체에 삽입한다.  stat << 100 << 200; // 100, 200을 통계 객체에 삽입한다.  ~stat; // 통계 데이터를 모두 출력한다.    int avg;  stat >> avg; // 통계 객체로부터 평균을 받는다.  cout << "avg=" << avg << endl;  // 평균을 출력한다.  } |
