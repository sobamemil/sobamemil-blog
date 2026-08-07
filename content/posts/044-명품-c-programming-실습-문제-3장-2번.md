---
title: "명품 C++ programming 실습 문제 3장 2번"
date: 2020-03-02T17:38:17+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "programming", "stoi", "string", "substr", "명품", "실습문제", "연습문제", "클래스", "프로그래밍"]
---

**문제 :**

날짜를 다루는 Date 클래스를 작성하고자 한다. Date를 이용하는 main()과 실행 결과는 다음과 같다.

클래스 Date를 작성하여 아래 프로그램에 추가하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | #include <iostream>  using namespace std;    int main() {  Date virth(2014, 3, 20);  Date independenceDay("1945/8/15");  independenceDay.show();  cout << birth.getYear() << ',' << birth.getMonth() << ',' << birth.getDay() << endl;  } |

**실행 결과 :**

![](https://img.sobamemil.com/posts/44/img_1.png)

****목적 및 힌트 :****

2개의 생성자와 여러 멤버를 가진 클래스 만들기

stoi() 함수를 이용하면 string의 문자열을 숫자로 변환할 수 있습니다.

ex)  string s = "1945";

      int n = stoi(s); // n은 정수 1945

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52 | #include<iostream>  #include<string>  using namespace std;    class Date{  private:  int Year, Month, Day;  public:  Date(int a, int b, int c);  Date(string s);  void show();  int getYear();  int getMonth();  int getDay();  };    Date::Date(int a, int b, int c){  Year = a;  Month = b;  Day = c;  }    Date::Date(string s){  Year = stoi(s.substr(0,4));  Month = stoi(s.substr(5,1));  Day = stoi(s.substr(7,2));  }    void Date::show(){  cout << Year << "년" << Month << "월" << Day << "일\n";  }    int Date::getYear(){  return Year;  }    int Date::getMonth(){  return Month;  }    int Date::getDay(){  return Day;  }    int main(){  Date birth(2014, 3, 20);  Date independenceDay("1945/8/15");  independenceDay.show();  cout << birth.getYear() << ',' << birth.getMonth() << ',' << birth.getDay() << endl;    return 0;  } |

**설명 :**

string 타입의 매개변수를 넘겨받은 생성자가 실행되면 string 헤더파일의 substr() 함수를 이용하여 각각 Year, Month, Day로 나누었다.

그 후 다시 나누어진 string을 stoi() 함수를 이용하여 int 형식으로 바꾸어 저장 및 출력 해주었습니다.

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 3장 4번](/46)  (8) | 2020.03.03 |
| [명품 C++ programming 실습 문제 3장 3번](/45)  (3) | 2020.03.02 |
| [명품 C++ programming 실습 문제 3장 1번](/43)  (1) | 2020.03.02 |
| [명품 C++ programming 실습 문제 2장 16번](/42)  (3) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 15번](/41)  (3) | 2020.02.28 |