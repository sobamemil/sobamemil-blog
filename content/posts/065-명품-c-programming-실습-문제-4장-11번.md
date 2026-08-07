---
title: "명품 C++ programming 실습 문제 4장 11번"
date: 2020-03-04T17:18:54+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "programming", "명품", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

다음은 커피자판기로 작동하는 프로그램을 만들기 위해 필요한 두 클래스이다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19 | class CoffeeVendingMachine {    // 커피자판기를 표현하는 클래스  Container tong[3];          // tong[0]는 커피, tong[1]은 물, tong[2]는 설탕통을 나타냄  void fill();                // 3개의 통을 모두 10으로 채움  void selectEspresso();      // 에스프레소를 선택한 경우, 커피 1, 물 1 소모  void selectAmericano();     // 아메리카노를 선택한 경우, 커피 1, 물 2 소모  void selectSugarCoffee();   // 설탕커피를 선택한 경우, 커피 1, 물 2, 설탕 1 소모  void show();               // 현재 커피, 물, 설탕의 잔량 출력  public:  void run();  // 커피 자판기 작동  };    class Container {               // 통 하나를 나타내는 클래스  int size;                   // 현재 저장 량, 최대 저장량은 10  public:  Container() {size = 10;}  void fill();                // 최대량(10)으로 채우기  void consume();             // 1 만큼 소모하기  int getSize();              // 현재 크기 리턴  }; |

다음과 같이 실행되도록 main() 함수와 CoffeeVendingMachine, Container를 완성하라.

만일 커피, 물, 설탕 중 잔량이 하나라도 부족해 커피를 제공할 수 없는 경우 '원료가 부족합니다.'를 출력하라.

**실행 결과 :**

![](https://img.sobamemil.com/posts/65/img_1.png)

**목적 및 힌트 :**

객체 배열 응용

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96  97  98  99  100  101  102  103  104  105  106  107  108  109  110  111  112  113  114  115  116  117  118 | #include<iostream>  using namespace std;    class Container {                 // 통 하나를 나타내는 클래스  int size;                    // 현재 저장 량, 최대 저장량은 10  public:  Container() {size = 10;}  void fill();                // 최대량(10)으로 채우기  void consume();                // 1 만큼 소모하기  int getSize();                // 현재 크기 리턴  };    class CoffeeVendingMachine {    // 커피자판기를 표현하는 클래스  Container tong[3];            // tong[0]는 커피, tong[1]은 물, tong[2]는 설탕통을 나타냄  void fill();                 // 3개의 통을 모두 10으로 채움  void selectEspresso();        // 에스프레소를 선택한 경우, 커피 1, 물 1 소모  void selectAmericano();        // 아메리카노를 선택한 경우, 커피 1, 물 2 소모  void selectSugarCoffee();    // 설탕커피를 선택한 경우, 커피 1, 물 2, 설탕 1 소모  void show();                // 현재 커피, 물, 설탕의 잔량 출력  public:  void run(); // 커피 자판기 작동  };    int start = 0;    void Container::fill(){  size = 10;  }  void Container::consume(){  size--;  }  int Container::getSize(){  return size;  }    void CoffeeVendingMachine::run(){  int num;  if (start==0)  cout << "\*\*\*\*\* 커피 자판기를 작동합니다. \*\*\*\*\*\n";  start++;  while(true){  cout << "메뉴를 눌러주세요(1:에스프레소, 2:아메리카노, 3:설탕커피, 4:잔량보기, 5:채우기)>> ";  cin >> num;  switch(num){  case 1:  selectEspresso();  break;  case 2:  selectAmericano();  break;  case 3:  selectSugarCoffee();  break;  case 4:  show();  break;  case 5:  fill();  break;  }  }  }    void CoffeeVendingMachine::selectEspresso(){  for(int i=0; i<3; i++){  if(tong[i].getSize() == 0) {  cout << "원료가 부족합니다.\n";  run();  }  }  tong[0].consume();  tong[1].consume();  cout << "에스프레소 드세요\n";  }    void CoffeeVendingMachine::selectAmericano(){  for(int i=0; i<3; i++){  if(tong[i].getSize() == 0) {  cout << "원료가 부족합니다.\n";  run();  }  }  tong[0].consume();  tong[1].consume(); tong[1].consume();  cout << "아메리카노 드세요\n";  }    void CoffeeVendingMachine::selectSugarCoffee(){  for(int i=0; i<3; i++){  if(tong[i].getSize() == 0) {  cout << "원료가 부족합니다.\n";  run();  }  }  tong[0].consume();  tong[1].consume(); tong[1].consume();  tong[2].consume();  cout << "설탕커피 드세요\n";  }    void CoffeeVendingMachine::show(){  cout << "커피 " << tong[0].getSize();  cout << ", 물 " << tong[1].getSize();  cout << ", 설탕 " << tong[2].getSize() << endl;  }    void CoffeeVendingMachine::fill(){  for(int i=0; i<3; i++){  tong[i].fill();  }  show();  }    int main() {  CoffeeVendingMachine \*coffee = new CoffeeVendingMachine;  coffee->run();  delete coffee;  } |

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 4장 13번](/67)  (3) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 12번](/66)  (2) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 10번](/64)  (1) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 9번](/63)  (2) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 8번](/62)  (1) | 2020.03.04 |