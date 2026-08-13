---
title: "C++ Programming Ch.9 Exercise 9 Solution"
date: 2019-11-26T03:21:53+09:00
draft: false
categories: ["Dev CS", "C++ Programming"]
tags: ["C", "C++", "programming", "Assignment", "Masterpiece", "Source Code", "Practice Problem", "Execution Result", "Exercise", "Programming"]
---

**Problem:**

다음 그림과 같은 상속 구조를 갖는 클래스를 설계한다.

![](https://img.sobamemil.com/posts/18/img_1.png)

모든 프린터는 모델명(model), 제조사(manufacturer), 인쇄 매수(printedCount), 인쇄 종이 잔량(availableCount)을 나타내는 정보를 가진다. print(int pages) 함수와 show() 함수는 가상 함수로 구현하라. print(int pages)는 pages 만큼 프린트하는 함수이고, show() 함수는 현재 프린트의 모델, 제조사, 인쇄 매수, 인쇄 종이 잔량 등을 출력하는 함수이다.

잉크젯 프린터는 잉크 잔량(availableInk) 정보를 추가적으로 가지며, 레이저 프린터는 토너 잔량(availableToner) 정보를 추가적으로 가진다. 이들의 print(int pages) 멤버 함수는 프린터 타입에 맞게 구현하라. 각 클래스를 설계 구현하고 다음과 같이 실행되도록 전체 프로그램을 완성하라. InkJetPrinter 객체와 LaserPrinter 객체를 각각 하나만 동적으로 생성하여 시작한다.

<b>실행결과 :</b>

![](https://img.sobamemil.com/posts/18/img_2.png)

<b>Objective & Hints:</b>

가상 함수, 상속 종합 응용

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82 | #include<iostream>  using namespace std;    class Printer {  protected:  string model, manuf;  int ptd\_count,ava\_count;  public:  Printer(string mo, string maf, int ava\_c){  model = mo; manuf = maf; ava\_count = ava\_c;  }  virtual void print(int pages){;}  virtual void show() {;}  };    class InkJet : public Printer {  int ava\_ink;  public:  InkJet(string mo, string maf, int ava\_c, int ava\_ik) : Printer(mo, maf, ava\_c){ ava\_ink = ava\_ik; }  virtual void show(){  cout << model << " ," << manuf << " ,남은 종이 " << ava\_count << "장 ,남은 잉크 " << ava\_ink << endl;  }  virtual void print(int pages){  if(ava\_count >= pages && ava\_ink >= pages){  ava\_count -= pages;  ava\_ink -= pages;  cout << "프린트하였습니다.\n";  }  else  cout << "용지가 부족하여 프린트 할 수 없습니다.\n";  }  };    class Laser : public Printer {  int ava\_toner;  public:  Laser(string mo, string maf, int ava\_c, int ava\_tnr) : Printer(mo, maf, ava\_c){ ava\_toner = ava\_tnr;}  virtual void show(){  cout << model << " ," << manuf << " ,남은 종이 " << ava\_count << "장 ,남은 토너 " << ava\_toner << endl;  }  virtual void print(int pages){  if(ava\_count >= pages && ava\_toner >= pages){  ava\_count -= pages;  ava\_toner--;  cout << "프린트하였습니다.\n";  }  else  cout << "용지가 부족하여 프린트 할 수 없습니다.\n";  }  };    int main() {  int printer\_num, pages;  string choice;  Printer\* p[2];  p[0] = new InkJet("Officejet V40", "HP", 5, 10);  p[1] = new Laser("SCX-6x45", "삼성전자", 3, 20);  cout << "현재 작동중인 2 대의 프린터는 아래와 같다\n";  cout << "잉크젯 : "; p[0]->show();  cout << "레이저 : "; p[1]->show(); cout << endl;  while(true){  cout << "프린터(1: 잉크젯, 2: 레이저)와 매수 입력>>";  cin >> printer\_num >> pages;  if(printer\_num==1){  p[printer\_num-1]->print(pages);  p[0]->show();  p[1]->show();  }  else if(printer\_num==2) {  p[printer\_num-1]->print(pages);  p[0]->show();  p[1]->show();  }  else  cout << "잘못 입력하셨습니다.\n";    cout << "계속 프린트 하시겠습니까(y/n)>>";  cin >> choice;  if(choice != "y") return 0;  cout << endl;  }  }   |

<b>Explanation:</b>

8장 8번의 문제와 비슷한 문제입니다. 아래 링크를 참고하여 작성하시면 조금 더 수월하게 작성할 수 있습니다.
