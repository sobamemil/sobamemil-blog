---
title: "명품 C++ programming 실습 문제 4장 14번"
date: 2020-03-04T17:50:03+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "cstdlib", "CTime", "gambling", "programming", "rand()", "명품", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

겜블링 게임을 만들어보자. 두 사람이 게임을 진행하며, 선수의 이름을 초기에 입력 받는다.

선수가 번갈아 자신의 차례에서 <Enter> 키를 치면 랜덤한 3개의 수가 생성되고 모두 동일한 수가 나오면 게임에서 이기게 된다.

숫자의 범위가 너무 크면 3개의 숫자가 일치할 가능성이 낮아 숫자의 범위를 0~2로 제한한다.

랜덤 정수 생성은 문제 5번의 힌트를 참고하라.

선수는 Player 클래스로 작성하고, 2명의 선수는 배열로 구성하라. 그리고 게임은 GamblingGame 클래스로 작성하라.

[2020/03/04 - [C++/명품 C++ programming] - 명품 C++ programming 실습 문제 4장 5번](https://sobamemil.tistory.com/59)

[명품 C++ programming 실습 문제 4장 5번

문제 : string 클래스를 이용하여 사용자가 입력한 영문 한 줄을 입력받고 글자 하나만 랜덤하게 수정하여 출력하는 프로그램을 작성하라. 목적 및 힌트 : string 클래스로 문자열 다루기 랜덤 정수를 발생시키기..

sobamemil.tistory.com](https://sobamemil.tistory.com/59)

**목적 및 힌트 :**

여러 클래스로 이루어진 객체 지향 프로그래밍 연습

**실행 결과 :**

![](https://img.sobamemil.com/posts/68/img_1.png)

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81 | #include<iostream>  #include<string>  #include <cstdlib>  #include <ctime>  using namespace std;    class Player{  string name;  public:  void setName(string name);  string getName(){return name;};  };    class GamblingGame {  Player \*p = new Player[2];  public:  GamblingGame();  void nameSet();  string ranNum(string n);  void startGame();  ~GamblingGame() { delete [] p;}  };    GamblingGame::GamblingGame(){  cout << "\*\*\*\*\* 갬블링 게임을 시작합니다. \*\*\*\*\*\n";  srand(time(NULL));  }    void GamblingGame::nameSet() {  string name;  cout << "첫번째 선수 이름>>";  cin >> name;  p[0].setName(name);  cout << "두번째 선수 이름>>";  cin >> name;  p[1].setName(name);  }    string GamblingGame::ranNum(string n){  int r[3];  cout << "\t\t";  for (int i = 0;i < 3;i++) {  r[i] = rand() % 3;  cout << r[i]<< "\t";  }  if(r[0]==r[1] && r[0]==r[2]) {  n +="님 승리!!";  return n;  }  else  return "아쉽군요!";  }    void GamblingGame::startGame(){  string n;  int i=0;  while(true){  string m;  cout << p[i % 2].getName() << ":\n";  getline(cin,n);  m = p[i % 2].getName();  n = ranNum(n);  if(n=="님 승리!!") {  cout << m + n;  break;  }  else  cout << n << endl;  i++;  }  }    void Player::setName(string n){  name = n;  }    int main(){  GamblingGame game;  game.nameSet();  game.startGame();  } |


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 5장 2번](/70)  (1) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 1번](/69)  (4) | 2020.03.05 |
| [명품 C++ programming 실습 문제 4장 13번](/67)  (3) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 12번](/66)  (2) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 11번](/65)  (3) | 2020.03.04 |