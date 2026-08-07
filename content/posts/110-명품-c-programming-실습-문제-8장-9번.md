---
title: "명품 C++ programming 실습 문제 8장 9번"
date: 2020-03-09T15:13:20+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["airlinebook", "C++", "programming", "명품", "비행기예약", "상속", "실습문제", "연습문제", "프로그래밍", "프로그램"]
---

**문제 :**

비행기 예약 프로그램을 작성하라. 이 문제는 여러 개의 클래스와 객체들을 다루는 연습을 위한 것이다. 클래스 사이의 상속 관계는 없다.

항공사 이름은 '한성항공'이고, 8개의 좌석을 가진 3대의 비행기로 서울 부산 간 운항 사업을 한다.

각 비행기는 하루에 한 번만 운항하며 비행시간은 07시, 12시, 17시이다. 비행기 예약 프로그램은 다음의 기능을 가진다.

● 예약 : 비행 시간, 사용자의 이름, 좌석 번호를 입력받아 예약한다.

● 취소 : 비행 시간, 사용자의 이름, 좌석 번호를 입력받고 예약을 취소한다.

● 예약 보기 : 예약된 좌석 상황을 보여준다.

**실행 결과 :**

![](https://img.sobamemil.com/posts/110/img_1.png)

**목적 및 힌트 :**

종합 응용 연습(상속 필요 없음)

이 프로그램에 필요한 클래스를 AirlineBook, Schedule, Seat의 3개이며, main() 함수는 별도의 cpp 파일에 작성한다.

또한 사용자 입력을 전담하는 Console 클래스를 작성한다.

● AirlineBook 클래스 : Schedule 객체 3개 생성. 예약 시스템 작동

● Schedule 클래스 : 하나의 스케줄을 구현하는 클래스. 8개의 Seat 객체 생성. Seat 객체에 예약, 취소, 보기 등 관리

● Seat 클래스 : 하나의 좌석을 구현하는 클래스. 예약자 이름 저장, 좌석에 대한 예약, 취소, 보기 등 관리

● Console 클래스 : 메뉴를 출력하는 함수, 사용자로부터 메뉴 선택, 비행시간, 사용자 이름, 좌석 번호 등을 입력받는 멤버 함수들을 구현. 멤버들은 static으로 작성하는 것이 좋다.

![](https://img.sobamemil.com/posts/110/img_2.png)

**코드 :**

● 8-9.h

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47 | class Console{  public:  static int select\_menu();  static int select\_time();  static int input\_seat\_num();  static string input\_name();  };    class Seat{  string name;  public:  Seat() { name = {"---"}; }  void set\_name(string name) { this->name = name; }  void reset\_name() { name = {"---"}; }  string show\_name() { return name; }    };    class Schedule{  Seat \*seat;  string scname;  int seat\_num;  string person\_name;  public:  Schedule(){ seat = new Seat[8]; }  ~Schedule() { delete [] seat; }  void set\_scname(string scname){ this->scname = scname; }  void show\_schedule();  void set\_resv(int seat\_num, string person\_name);  void cancel\_resv(int seat\_num, string person\_name);  };      class AirlineBook{  Schedule \*schedule;  int menu;  int time;  public:  AirlineBook(){  schedule = new Schedule[3];  schedule[0].set\_scname("07");  schedule[1].set\_scname("12");  schedule[2].set\_scname("17");  }  ~AirlineBook(){ delete [] schedule; }  void start();  }; |

● 8-9.cpp

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96  97  98  99  100  101  102  103  104  105  106  107  108  109  110  111  112  113  114  115  116  117  118  119  120  121  122  123  124  125  126  127  128  129  130  131  132  133  134  135  136  137  138  139  140  141  142  143  144  145  146  147  148  149 | #include<iostream>  using namespace std;    #include"8-9.h"    int Console::select\_menu() {  cout << "예약:1, 취소:2, 보기:3, 끝내기:4>> ";  int menu;  cin >> menu;  return menu;  }    int Console::select\_time(){  cout << "07시:1, 12시:2, 17시:3>> ";  int time;  cin >> time;  return time;  }    int Console::input\_seat\_num() {  cout << "좌석 번호>> ";  int seat\_num;  cin >> seat\_num;  if(seat\_num < 1 || 8 < seat\_num){  cout << "없는 좌석 번호 입니다. 처음 메뉴로 돌아갑니다.\n";  return 0;  }  return seat\_num;  }    string Console::input\_name() {  cout << "이름 입력>> ";  string name;  cin >> name;  return name;  }    void AirlineBook::start(){  while(1){  menu = Console::select\_menu();  if(menu == 1 || menu == 2){  time = Console::select\_time();  if(menu == 1){  switch (time){  case 1:{  schedule[0].show\_schedule();  int seat\_num = Console::input\_seat\_num();  if(seat\_num == 0)  break;  string person\_name = Console::input\_name();  schedule[0].set\_resv(seat\_num, person\_name);  break;  }  case 2:{  schedule[1].show\_schedule();  int seat\_num = Console::input\_seat\_num();  if(seat\_num == 0)  break;  string person\_name = Console::input\_name();  schedule[1].set\_resv(seat\_num, person\_name);  break;  }  case 3:{  schedule[2].show\_schedule();  int seat\_num = Console::input\_seat\_num();  if(seat\_num == 0)  break;  string person\_name = Console::input\_name();  schedule[2].set\_resv(seat\_num, person\_name);  break;  }  case 4:  cout << "잘못 선택하셨습니다. 처음 메뉴로 돌아갑니다.\n";  }  }  else {  switch (time){  case 1:{  schedule[0].show\_schedule();  int seat\_num = Console::input\_seat\_num();  if(seat\_num == 0)  break;  string person\_name = Console::input\_name();  schedule[0].cancel\_resv(seat\_num,person\_name);  break;  }  case 2:{  schedule[1].show\_schedule();  int seat\_num = Console::input\_seat\_num();  if(seat\_num == 0)  break;  string person\_name = Console::input\_name();  schedule[1].cancel\_resv(seat\_num,person\_name);  break;  }  case 3:{  schedule[2].show\_schedule();  int seat\_num = Console::input\_seat\_num();  if(seat\_num == 0)  break;  string person\_name = Console::input\_name();  schedule[2].cancel\_resv(seat\_num,person\_name);  break;  }  case 4:  cout << "잘못 선택하셨습니다. 처음 메뉴로 돌아갑니다.\n";  }  }  }  else if(menu == 3){  for(int i=0; i<3; i++){  schedule[i].show\_schedule();  }  }  else if(menu == 4){  cout << "예약 시스템을 종료합니다.";  exit(0);  }  else {  cout << "잘못 입력하셨습니다. 메뉴를 다시 선택해 주세요.\n";  }  cout << endl;  }  }    void Schedule::show\_schedule(){  cout << this->scname << "시:";  for(int i=0; i<8; i++)  cout << "\t" << seat[i].show\_name();  cout << endl;  }    void Schedule::set\_resv(int seat\_num, string person\_name){  if(seat[seat\_num-1].show\_name() != "---")  cout << "이미 예약된 자리입니다. 처음 메뉴로 돌아갑니다.\n";  else seat[seat\_num-1].set\_name(person\_name);  }    void Schedule::cancel\_resv(int seat\_num,string person\_name){  if(seat[seat\_num-1].show\_name() == "---"){  cout <<  "이미 비어있는 자리입니다. 처음 메뉴로 돌아갑니다.\n";  return;  }  if(seat[seat\_num-1].show\_name() != person\_name){  cout << "예약된 이름과 일치하지 않습니다. 처음 메뉴로 돌아갑니다.\n";  return;  }  seat[seat\_num-1].reset\_name();  } |

● main.cpp

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11 | #include<iostream>  using namespace std;    #include"8-9.h"    int main() {  AirlineBook \*air = new AirlineBook();  cout << "\*\*\*\*\* 한성항공에 오신것을 환영합니다 \*\*\*\*\*\n\n";  air->start();  delete air;  } |

**설명 :**

상속이 필요 없는 문제입니다. 코드가 길기 때문에 차근차근 따라가며 이해하시면 됩니다.

전체적인 실행 과정 등을 간단하게 그려놓고 시작하면 훨씬 수월하게 작성할 수 있습니다.

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 10장 2번](/112)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 10장 1번](/111)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 8장 8번](/109)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 8장 7번](/108)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 8장 6번](/107)  (1) | 2020.03.09 |