---
title: "명품 C++ programming 실습 문제 6장 8번"
date: 2020-03-06T16:11:59+09:00
draft: false
categories: ["개발 CS", "C++ 프로그래밍"]
tags: ["C++", "programming", "static", "Trace", "디버깅", "명품", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

디버깅에 필요한 정보를 저장하는 Trace 클래스를 만들어보자. 저자의 경험에 의하면, 멀티태스크 프로그램을 개발하거나 특별한 환경에서 작업할 때, Visual Studio의 디버거와 같은 소스 레벨 디버거를 사용하지 못하는 경우가 더러 있었고, 이때 실행 도중 정보를 저장하기 위해 Trace 클래스를 만들어 사용하였다.

Trace 클래스를 활용하는 다음 프로그램과 결과를 참고하여 Trace 클래스를 작성하고 전체 프로그램을 완성하라.

디버깅 정보는 100개로 제한한다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18 | void f() {  int a, b, c;  cout << "두 개의 정수를 입력하세요>>";  cin >> a >> b;  Trace::put("f()", "정수를 입력 받았음"); // 디버깅 정보 저장  c = a + b;  Trace::put("f()", "합 계산"); // 디버깅 정보 저장  cout << "합은 " << c << endl;  }    int main() {  Trace::put("main()", "프로그램을 시작합니다"); // 디버깅 정보 저장  f();  Trace::put("main()", "종료");    // put()의 첫 번째 매개 변수는 태그이고  // 두 번째 매개 변수는 디버깅 정보이다.  Trace::print("f()"); // "f()" 태그를 가진 디버깅 정보를 모두 출력한다.  Trace::print(); // 모든 디버깅 정보를 출력한다.  } |

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/88/img_1.png)

<b>목적 및 힌트 :</b>

static 멤버를 가진 클래스 만들기 종합 응용

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56 | #include<iostream>  #include<string>  using namespace std;    class Trace{  public:  static string tagInf[100];  static string debugInf[100];  static int count;  static void put(string tag, string debug);  static void print(string tag = "all");  };    int Trace::count = 0;  string Trace::tagInf[100];  string Trace::debugInf[100];    void f() {  int a, b, c;  cout << "두 개의 정수를 입력하세요>>";  cin >> a >> b;  Trace::put("f()", "정수를 입력 받았음"); // 디버깅 정보 저장  c = a + b;  Trace::put("f()", "합 계산"); // 디버깅 정보 저장  cout << "합은 " << c << endl;  }    void Trace::put(string tag, string debug){  tagInf[count] = tag;  debugInf[count] = debug;  count++;  }    void Trace::print(string tag){  if(tag == "all"){  cout << "----- 모든 Trace 정보를 출력합니다. -----\n";  for(int i=0; i<count ; i++){  cout << tagInf[i] << ":" << debugInf[i] << endl;  }  }  else {  cout << "----- " << tag << "태그의 Trace 정보를 출력합니다. -----\n";  for(int i=0; i<count; i++){  if(tagInf[i] == tag) cout << tagInf[i] << ":" << debugInf[i] << endl;  }  }  }    int main() {  Trace::put("main()", "프로그램을 시작합니다"); // 디버깅 정보 저장  f();  Trace::put("main()", "종료");    // put()의 첫 번째 매개 변수는 태그이고  // 두 번째 매개 변수는 디버깅 정보이다.  Trace::print("f()"); // "f()" 태그를 가진 디버깅 정보를 모두 출력한다.  Trace::print(); // 모든 디버깅 정보를 출력한다.  } |
