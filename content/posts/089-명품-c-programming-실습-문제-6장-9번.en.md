---
title: "명품 C++ programming 실습 문제 6장 9번"
date: 2020-03-06T16:36:17+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["Board", "C++", "programming", "static", "게시판프로그램", "명품", "실습문제", "연습문제", "전역변수", "프로그래밍"]
---

**문제 :**

게시판 프로그램을 작성해보자. 멀티태스킹의 경우 여러 사용자들이 게시판에 글을 올리기 때문에 게시판 객체는 전체 하나만 있어야 한다. 그러므로 게시판 객체의 멤버들은 static으로 작성한다.

다음은 게시판 기능을 하는 Board 클래스를 활용하는 main() 코드이다. 실행 결과를 참고하여 Board 클래스를 만들고 전체 프로그램을 완성하라.

static 연습이 목적이기 때문에 게시판 기능을 글을 올리는 기능과 게시글을 모두 출력하는 기능으로 제한하고 main()도 단순화하였다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8 | int main() {  // Board myBoard; // 객체 생성은 컴파일 오류입니다.  Board::add("중간고사는 감독 없는 자율 시험입니다.");  Board::add("코딩 라운지 많이 이용해 주세요.");  Board::print();  Board::add("진소린 학생이 경진대회 입상하였습니다. 축하해주세요");  Board::print();  } |

**실행 결과 :**

![](https://img.sobamemil.com/posts/89/img_1.png)

**목적 및 힌트 :**

static 멤버를 가진 클래스 만들기 종합 응용

Board 클래스에는 게시글을 저장하기 위한 string 배열과 다음 저장할 위치 정보를 가진 static 멤버 변수가 필요하다.

static 멤버 변수는 전역 변수로 선언하는 것이 반드시 필요하다.

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36 | #include<iostream>  #include<string>  using namespace std;    class Board{  public:  static int cnt;  // static 멤버 변수 선언  static string \*coment; // static 멤버 변수 선언  static void add(string str);  static void print();  };    // static 변수 공간 할당. //반드시 프로그램의 전역 공간에 선언  int Board::cnt = 0;  string \*Board::coment = new string [100];    void Board::add(string str){  coment[cnt] = str;  cnt++;  }    void Board::print(){  cout << "\*\*\*\*\*\*\*\*\*\*\*\*\* 게시판입니다. \*\*\*\*\*\*\*\*\*\*\*\*\*\n";  for(int i=0; i<cnt; i++)  cout << i << ": " << coment[i] << endl;  cout << endl;  }    int main() {  // Board myBoard; // 객체 생성은 컴파일 오류입니다.  Board::add("중간고사는 감독 없는 자율 시험입니다.");  Board::add("코딩 라운지 많이 이용해 주세요.");  Board::print();  Board::add("진소린 학생이 경진대회 입상하였습니다. 축하해주세요");  Board::print();  } |

**설명 :**

static 멤버 변수는 변수의 공간을 할당받는 선언문이 추가적으로 필요합니다.

이 선언문은 클래스 바깥의 전역 공간에 선언되어야 하며 그렇지 않을 시 링크 오류가 발생합니다.

class의 객체가 생성되지 않아도 프로그램이 시작되면 static 멤버는 class와 상관없이 생성됩니다.

클래스 내부의 static 멤버라고 할 지라도 static 멤버는 객체 내부가 아닌 별도의 공간에 생성됩니다.

또한 static 멤버 함수는 오직 static 멤버들만 접근이 가능하고 static 멤버 함수에서 non-static 멤버에 접근하는 것은 허용되지 않습니다.


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 7장 2번](/91)  (3) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 1번](/90)  (3) | 2020.03.06 |
| [명품 C++ programming 실습 문제 6장 8번](/88)  (1) | 2020.03.06 |
| [명품 C++ programming 실습 문제 6장 7번](/87)  (1) | 2020.03.06 |
| [명품 C++ programming 실습 문제 6장 6번](/86)  (2) | 2020.03.06 |