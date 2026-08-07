---
title: "명품 C++ programming 실습 문제 3장 4번"
date: 2020-03-03T15:54:40+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["3장", "4번", "C++", "programming", "명품", "실습문제", "연습문제", "프로그래밍"]
---

<b>문제 :</b>

CoffeeMachine 클래스를 만들어보자. main() 함수와 실행 결과가 다음과 같도록 CoffeeMachine 클래스를 작성하라.

에스프레소 한 잔에는 커피와 물이 각각 1씩 소비되고, 아메리카노의 경우 커피는 1, 물은 2가 소비되고, 설탕 커피는 커피 1, 물 2, 설탕 1이 소비된다.

CoffeeMachine 클래스에는 어떤 멤버 변수와 어떤 멤버 함수가 필요한지 잘 판단하여 작성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | #include <iostream>  using namespace std;    int main() {  CoffeeMachine java(5, 10, 3); // 커피량:5, 물량:10, 설탕:6 으로 초기화  java.drinkEspresso(); // 커피 1, 물 1 소비  java.show(); // 현재 커피 머신의 상태 출력  java.drinkAmericano(); // 커피 1, 물 2 소비  java.show(); // 현재 커피 머신의 상태 출력  java.drinkSugarCoffee(); // 커피 1, 물 2, 설탕 1 소비  java.show(); // 현재 커피 머신의 상태 출력  java.fill(); // 커피 10, 물 10, 설탕 10 으로 채우기  java.show(); // 현재 커피 머신의 상태 출력 |

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/46/img_1.png)

<b>목적 및 힌트 :</b>

실세계의 객체를 클래스로 작성

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59 | #include<iostream>  using namespace std;    class CoffeeMachine{  private:  int coff, wat, sug;  public:  CoffeeMachine(int \_coff, int \_wat, int \_sug);  void drinkEspresso();  void drinkAmericano();  void drinkSugarCoffee();  void fill();  void show();    };    CoffeeMachine::CoffeeMachine(int \_coff, int \_wat, int \_sug){  coff = \_coff;  wat = \_wat;  sug = \_sug;  }    void CoffeeMachine::drinkEspresso(){  coff--;  wat--;  }    void CoffeeMachine::drinkAmericano() {  coff--;  wat--; wat--;  }    void CoffeeMachine::drinkSugarCoffee() {  coff--;  wat--; wat--;  sug--;  }    void CoffeeMachine::fill(){  coff = 10;  wat = 10;  sug = 10;  }    void CoffeeMachine::show(){  cout << "커피 머신 상태, 커피:" << coff << "\t물:" << wat << "\t설탕:" << sug << endl;  }    int main() {  CoffeeMachine java(5, 10, 3); // 커피량:5, 물량:10, 설탕:6 으로 초기화  java.drinkEspresso(); // 커피 1, 물 1 소비  java.show(); // 현재 커피 머신의 상태 출력  java.drinkAmericano(); // 커피 1, 물 2 소비  java.show(); // 현재 커피 머신의 상태 출력  java.drinkSugarCoffee(); // 커피 1, 물 2, 설탕 1 소비  java.show(); // 현재 커피 머신의 상태 출력  java.fill(); // 커피 10, 물 10, 설탕 10 으로 채우기  java.show(); // 현재 커피 머신의 상태 출력  } |
