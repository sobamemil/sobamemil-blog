---
title: "명품 C++ programming 실습 문제 11장 12번"
date: 2020-04-02T16:58:54+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["12장", "C++", "coffeemachine", "iomanip", "programming", "객체지향", "명품", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

커피 자판기 시뮬레이터를 C++로 작성해보자. 실행 사례는 다음과 같다.

자판기는 보통 커피, 설탕  커피, 블랙 커피의 3종류만 판매한다.

단순화를 위해 실행 살에는 총 3인분의 재료만 가지도록 하였다. 커피 메뉴에 따라 필요한 재료들이 하나씩 없어진다.

객체 지향 구조에 따라 필요한 클래스를 작성하여 프로그램을 완성하라.

**실행 결과 :**

![](https://img.sobamemil.com/posts/143/img_1.png)

**목적 및 힌트 :**

객체 지향 구조로 종합 응용 연습

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96  97  98  99  100  101  102  103  104  105  106  107  108  109  110  111  112  113  114  115  116  117  118  119  120  121  122  123  124  125  126  127  128  129  130  131  132  133  134  135  136  137  138  139  140  141  142  143  144  145  146  147  148  149  150  151  152  153  154  155  156  157  158  159  160  161  162  163  164  165  166  167  168  169 | #include <iostream>  #include <iomanip>  using namespace std;    class Material {  protected:  string name;  int amount;  public:  string getName() {  return name;  }  int getAmount() {  return amount;  }  void setAmount(int amount) {  this->amount = amount;  }  bool subAmount(int amount) {  if(this->amount <= 0)  return false;  else  this->amount -= amount;  return true;  }  };    class Coffee : public Material {  public:  Coffee() {  name = "Coffee";  amount = 3;  }  };    class Sugar : public Material {  public:  Sugar() {  name = "Sugar";  amount = 3;  }  };    class Cream : public Material {  public:  Cream() {  name = "Cream";  amount = 3;  }  };    class Water : public Material {  public:  Water() {  name = "Water";  amount = 3;  }  };    class Cup : public Material {  public:  Cup() {  name = "Cup";  amount = 3;  }  };    class CoffeeMachine {  Material \*mat[]; // Material의 객체 배열 포인터 생성  public:  CoffeeMachine() { // 생성자에서 안내 멘트와 재료 상태 출력  cout << "-----명품 커피 자판기 켭니다.-----" << endl;  mat[0] = new Coffee();  mat[1] = new Sugar();  mat[2] = new Cream();  mat[3] = new Water();  mat[4] = new Cup();  showCoffeeMachineState();  cout << endl;  }  void showCoffeeMachineState() { // 재료 상태 출력  for(int i=0; i<5; i++) {  cout << setw(10) << mat[i]->getName();  for(int j=0; j<mat[i]->getAmount(); j++)  cout << "\*";  cout << endl;  }  }  void start() { // 메뉴 출력 시작  int num;  while(true) {  showMenu();  num = selectMenu();  if(num == 3) { // 채우기  for(int i=0; i<5; i++) {  mat[i]->setAmount(3);  }  cout << "모든 통을 채웁니다~~" << endl;  showCoffeeMachineState();  cout << endl;  continue;  }  else if(num == 4) { // 종료  cout << "프로그램을 종료합니다..." << endl;  exit(0);  }    if(mat[0]->subAmount(1) == false) { // coffee-1  cout << "재료가 부족합니다." << endl;  showCoffeeMachineState();  continue;  }  if(mat[3]->subAmount(1) == false) { // water-1  cout << "재료가 부족합니다." << endl;  showCoffeeMachineState();  continue;  }  if(mat[4]->subAmount(1) == false) { // cup-1  cout << "재료가 부족합니다." << endl;  showCoffeeMachineState();  continue;  }  // 기본 재료가 부족하지 않으면 실행  switch(num) {  case 0: // 보통 커피는 cream 추가 소모  if(mat[2]->subAmount(1) == false) { // cream-1  cout << "재료가 부족합니다." << endl;  showCoffeeMachineState();  continue;  }  cout << "맛있는 보통 커피 나왔습니다~~" << endl;  showCoffeeMachineState();  cout << endl;  break;  case 1: // 설탕 커피는 sugar 추가 소모  if(mat[1]->subAmount(1) == false) { // sugar-1  cout << "재료가 부족합니다." << endl;  showCoffeeMachineState();  continue;  }  cout << "맛있는 설탕 커피 나왔습니다~~" << endl;  showCoffeeMachineState();  cout << endl;  break;  case 2: // 블랙 커피는 추가 소모 없음  cout << "맛있는 블랙 커피 나왔습니다~~" << endl;  showCoffeeMachineState();  break;  default : // 잘못 입력  cout << "잘못 입력 하셨습니다." << endl << endl;  break;  }  }  }  void showMenu() {  cout << "보통 커피:0, 설탕 커피:1, 블랙 커피:2, 채우기:3, 종료:4>> ";  }  int selectMenu() {  int num;  cin >> num;  return num;  }  };    int main() {  cout.setf(ios::left);  CoffeeMachine c;  c.start();  } |

**설명 :**

문제에서 커피 재료에 대한 언급이 없어서 임의로 들어가는 재료를 선택 하였습니다.

모든 커피에 기본적으로 커피, 물, 컵은 소모됩니다.

일반 커피는 추가로 Cream이 소모되고, 설탕 커피는 추가로 Sugar가 소모됩니다.

블랙 커피는 기본 재료 외에 소모되는 재료가 없습니다.

**코딩은 내일부터 ;**

[저작자표시 비영리
(새창열림)](https://creativecommons.org/licenses/by-nc/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 11장 11번](/142)  (1) | 2020.04.02 |
| [명품 C++ programming 실습 문제 11장 10번](/141)  (1) | 2020.04.02 |
| [명품 C++ programming 실습 문제 11장 9번](/140)  (3) | 2020.04.02 |
| [명품 C++ programming 실습 문제 11장 8번](/139)  (1) | 2020.04.02 |
| [명품 C++ programming 실습 문제 11장 7번](/138)  (1) | 2020.04.02 |