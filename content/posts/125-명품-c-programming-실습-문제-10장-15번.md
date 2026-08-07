---
title: "명품 C++ programming 실습 문제 10장 15번"
date: 2020-03-11T15:11:10+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "erase()", "iostream", "Iterator", "programming", "vector", "명품", "실습문제", "연습문제", "프로그래밍"]
---<b>문제 :</b>

vector를 이용하여 아래 Circle 클래스의 객체를 삽입하고 삭제하는 프로그램을 작성하라.

삭제 시에는 이름이 같은 모든 원을 삭제한다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10 | class Circle {  string name; // 이름  int radius; // 반지름  public:  Circle(int radius, string name) {  this->radius = radius; this->name = name;  }  double getArea() { return 3.14\*radius\*radius; }  string getName() { return name; }  }; |

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/125/img_1.png)

<b>목적 및 힌트 :</b>

객체 포인터를 vector에 삽입, 삭제 연습

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60 | #include<iostream>  #include<vector>  using namespace std;    class Circle {  string name; // 이름  int radius; // 반지름  public:  Circle(int radius, string name) {  this->radius = radius; this->name = name;  }  double getArea() { return 3.14\*radius\*radius; }  string getName() { return name; }  };    int main() {  cout << "원을 삽입하고 삭제하는 프로그램입니다.\n";  vector<Circle\*> v;    while(true){  int num;  int radius;  string name;  cout << "삽입:1, 삭제:2, 모두보기:3, 종료:4 >> ";  cin >> num;  switch (num){  case 1:  cout << "생성하고자 하는 원의 반지름과 이름은 >> ";  cin >> radius >> name;  v.push\_back(new Circle(radius, name));  break;  case 2:{  cout << "삭제하고자 하는 원의 이름은 >> ";  cin >> name;  vector<Circle\*>::iterator it = v.begin();  while(it != v.end()){  Circle \*p = \*it;  if(p->getName() == name){  it = v.erase(it);  delete p;  }  else  it++;  }  break;  }  case 3:{  vector<Circle\*>::iterator it;  for(it=v.begin(); it!=v.end(); it++){  Circle \*p = \*it;  cout << p->getName() << endl;  }  cout << endl;  break;  }  case 4:  return 0;  }  }  } |

<b>설명 :</b>

vector<Circle\*> v; 형식으로 벡터를 생성합니다.

v.erase(it)는 벡터 v에서 it가 가리키는 원소를 삭제하고 난 다음, 벡터 내에 삭제된 다음 지점의 첫 원소에 대한 포인터를 리턴합니다.

그러므로 원소를 삭제한 후 다음 원소의 주소를 잡으려면 간단히 다음과 같이 하면 됩니다.

|  |  |
| --- | --- |
| 1 | it = v.erase(it); |
