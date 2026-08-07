---
title: "명품 C++ programming 실습 문제 8장 8번"
date: 2020-03-09T14:18:19+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "printmachine", "programming", "동적생성", "명품", "상속", "실습문제", "연습문제", "프로그래밍", "프린터프로그램"]
---

<b>문제 :</b>

다음 그림과 같은 상속 구조를 갖는 클래스를 설계한다.

모든 프린터는 모델명(model), 제조사(manufacturer), 인쇄 매수(printedCount), 인쇄 종이 잔량(availableCount)을 나타내는 정보와 print(int pages) 멤버 함수를 가지며, print()가 호출할 때마다 pages 매의 용지를 사용한다.

잉크젯 프린터는 잉크 잔량(availableInk) 정보와 printInkJet(int pages) 멤버 함수를 추가적으로 가지며, 레이저 프린터는 토너 잔량(availableToner) 정보와 역시 printLaser(int pages) 멤버 함수를 추가적으로 가진다.

각 클래스에 적절한 접근 지정으로 멤버 변수와 함수, 생성자, 소멸자를 작성하고, 다음과 같이 실행되도록 전체 프로그램을 완성하라.

잉크젯 프린터 객체와 레이저 프린터 객체를 각각 하나만 동적 생성하여 시작한다.

![](https://img.sobamemil.com/posts/109/img_1.png)

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/109/img_2.png)

<b>목적 및 힌트 :</b>

상속 구조로 종합 응용 연습

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96  97  98  99  100  101  102  103  104  105  106  107  108  109  110  111  112  113  114  115  116  117  118  119  120  121  122  123  124  125 | #include<iostream>  using namespace std;    class PrintMachine {  string model, manuf;  int pcount, avlcount;  protected:  PrintMachine(string model, string manuf, int avlcount){  this->model=model;  this->manuf=manuf;  this->avlcount=avlcount;  }  bool print(int pages){  if(avlcount < pages){  cout << "용지가 부족하여 프린트 할 수 없습니다.\n";  return false;  }  for(int i=0; i< pages; i++){  avlcount--;  }  return true;  }  string get\_model(){ return model; }  string get\_manuf(){ return manuf; }  int get\_avlcount(){ return avlcount; }  };    class PrintInkJet : public PrintMachine {  int avlink;  public:  PrintInkJet(string model, string manuf, int avlcount, int avlink) : PrintMachine(model, manuf, avlcount){  this->avlink = avlink;  }  bool printInkJet(int pages){  if(print(pages));  else return false;  if(avlink < pages){  cout << "잉크가 부족하여 프린트 할 수 없습니다.\n";  return false;  }  for(int i=0; i<pages; i++){  avlink--;  }  return true;  }  void show(){  cout << get\_model() << "\t," << get\_manuf() << "\t,남은 종이 " << get\_avlcount() << "장\t,남은 잉크 " << avlink << endl;  }  };    class PrintLaser : public PrintMachine {  int avltoner;  public:  PrintLaser(string model, string manuf, int avlcount, int avltoner) : PrintMachine(model, manuf, avlcount){  this->avltoner = avltoner;  }  bool printLaser(int pages){  if(print(pages));  else return false;  if(avltoner < pages){  cout << "토너가 부족하여 프린트 할 수 없습니다.\n";  return false;  }  for(int i=0; i<pages; i++)  avltoner--;  return true;  }  void show(){  cout << get\_model() << " ," << get\_manuf() << "\t,남은 종이 " << get\_avlcount() << "장\t,남은토너 " << avltoner << endl;  }  };    int main() {  int pnum, pages;  char yon;  PrintInkJet\* inkjet = new PrintInkJet("Officejet V40", "Hp", 5, 10);  PrintLaser\* laser = new PrintLaser("SCX-6x45", "삼성전자", 3, 20);  cout << "현재 작동중인 2 대의 프린터는 아래와 같다\n";  cout << "잉크젯 : ";  inkjet->show();  cout << "레이저 : ";  laser->show();  cout << endl;    while(true){  cout << "프린터(1:잉크젯, 2:레이저)와 매수 입력>>";  cin >> pnum >> pages;  if(pnum==1)  if(inkjet->printInkJet(pages))  cout << "프린트 하였습니다.\n";  if(pnum==2)  if(laser->printLaser(pages))  cout << "프린트 하였습니다.\n";  if(pnum != 1 && pnum != 2) cout << "프린터를 잘못 선택하셨습니다.\n";  /\* 또는  switch(pnum){  case 1:  if(inkjet->printInkJet(pages))  cout << "프린트 하였습니다.\n";  break;  case 2:  if(laser->printLaser(pages))  cout << "프린트 하였습니다.\n";  break;  default :  cout << "프린터를 잘못 선택하셨습니다.\n";  break;  } switch문 사용 가능 \*/  inkjet->show();  laser->show();  while(true){  cout << "계속 프린트 하시겠습니까(y/n)>>";  cin >> yon;  cout << endl;  if(yon=='n')  return 0;  else if(yon=='y')  break;  else  cout << "잘못 입력하셨습니다.\n";  }  }  delete inkjet;  delete laser;  } |


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 10장 1번](/111)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 8장 9번](/110)  (4) | 2020.03.09 |
| [명품 C++ programming 실습 문제 8장 7번](/108)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 8장 6번](/107)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 8장 5번](/106)  (1) | 2020.03.09 |