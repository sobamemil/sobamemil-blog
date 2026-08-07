---
title: "명품 C++ programming 실습 문제 10장 11번"
date: 2020-03-10T19:14:39+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["book", "C++", "fflush", "programming", "vector", "명품", "벡터", "실습문제", "연습문제", "프로그래밍"]
---

<b>문제 :</b>

책의 년도, 책이름, 저자 이름을 담은 Book 클래스를 만들고, vector<Book> v;로 생성한 벡터를 이용하여 책을 입고하고, 저자와 년도로 검색하는 프로그램을 작성하라.

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/121/img_1.png)

<b>목적 및 힌트 :</b>

vector에 객체의 삽입, 검색 응용 연습

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63 | #include<iostream>  #include<vector>  #include<string>  using namespace std;    class Book{  int year;  string b\_name;  string p\_name;  public:  void set(int year, string b\_name, string p\_name){  this->year = year; this->b\_name = b\_name; this->p\_name = p\_name;  }  string getP(){  return p\_name;  }  int getY(){  return year;  }  void show(){  cout << year << "년도, " << b\_name << ", " << p\_name << endl;  }  };    int main() {  vector<Book> v;  Book b;  int year;  string b\_name;  string p\_name;    cout << "입고할 책을 입력하세요. 년도에 -1을 입력하면 입고를 종료합니다.\n";    while(true){  cout << "년도>>";  cin >> year;  if(year==-1)  break;  fflush(stdin);  cout << "책이름>>";  getline(cin, b\_name);  cout << "저자>>";  getline(cin, p\_name);    b.set(year, b\_name, p\_name);  v.push\_back(b);  }    cout << "총 입고된 책은 " << v.size() << "권 입니다.\n";  cout << "검색하고자 하는 저자 이름을 입력하세요>>";  fflush(stdin);  getline(cin, p\_name);  for(int i=0; i<v.size(); i++){  if(v[i].getP() == p\_name)  v[i].show();  }  cout << "검색하고자 하는 년도를 입력하세요>>";  cin >> year;  for(int i=0; i<v.size(); i++){  if(v[i].getY() == year)  v[i].show();  }  } |

<b>설명 :</b>

c 표준 함수인 fflush() 함수의 원형은 다음과 같습니다.

int fflush( FILE \*stream );

fflush() 함수의 매뉴얼에는 출력 스트림에 대해서만 정의되어 있습니다.

위 코드에서 사용한 fflush(stdin); 부분은 출력 스트림이 아닌 입력 스트림을 비우기 위해 사용한 것이므로 정의되지 않은 사용 방법입니다.

따라서 확실히 작동한다고 장담할 수 없고 권장되지 않는 방법입니다.


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 10장 13번](/123)  (1) | 2020.03.11 |
| [명품 C++ programming 실습 문제 10장 12번](/122)  (3) | 2020.03.10 |
| [명품 C++ programming 실습 문제 10장 10번](/120)  (1) | 2020.03.10 |
| [명품 C++ programming 실습 문제 10장 9번](/119)  (1) | 2020.03.10 |
| [명품 C++ programming 실습 문제 10장 8번](/118)  (4) | 2020.03.09 |