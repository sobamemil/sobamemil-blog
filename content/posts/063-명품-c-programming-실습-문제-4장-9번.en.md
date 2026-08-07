---
title: "C++ Programming Ch.4 Exercise 9 Solution"
date: 2020-03-04T16:48:36+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "compare()", "programming", "string", "명품", "실습문제", "연습문제", "프로그래밍"]
---

<b>Problem:</b>

다음과 같은 Person 클래스가 있다.

Person 클래스와 main() 함수를 작성하여, 3개의 Person 객체를 가지는 배열을 선언하고, 다음과 같이 키보드에서 이름과 전화번호를 입력받아 출력하고 검색하는 프로그램을 완성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | class Person{  string name;  string tel;  public:  Person();  string getName() { return name; }  string getTel() { return tel; }  void set(string name, string tel);  }; |

<b>Objective & Hints:</b>

객체 배열과 string 응용 연습

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/63/img_1.png)

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48 | #include<iostream>  #include<string>  using namespace std;    class Person{  string name;  string tel;  public:  Person();  string getName() { return name; }  string getTel() { return tel; }  void set(string name, string tel);  };    Person::Person(){} // 생성자    void Person::set(string N, string T){  name = N;  tel = T;  }    int main(){  string Name,Tel;  Person \*pInf = new Person [3];    cout << "이름과 전화 번호를 입력해 주세요\n";    for(int i=0; i<3; i++){  cout << "사람 " << i+1 << ">> ";  cin >> Name >> Tel;  pInf[i].set(Name,Tel);  }    cout << "모든 사람의 이름은 ";  for(int i=0; i<3; i++){  cout << pInf[i].getName() << " ";  }    cout << endl << "전화번호 검색합니다. 이름을 입력하세요>>";  cin >> Name;    for(int i=0; i<3; i++){  if(Name.compare(pInf[i].getName())==0) {  cout << "전화 번호는 " << pInf[i].getTel();  break;  }  }  } |

<b>Explanation:</b>

string 클래스의 compare() 멤버 함수를 이용하여 찾고자 하는 문자열과 저장되어 있는 문자열을 비교 하였습니다.

compare() 함수는 매개변수로 들어온 str을 비교해서 같으면 0을 반환하고, 다르면 0이 아닌 값을 반환합니다.

이때 호출한 문자열이 매개변수로 들어온 문자열보다 사전순으로 빠르면 음수(-1)를 반환하고,

호출한 문자열이 매개변수로 들어온 문자열보다 사전순으로 느리면 양수(1)을 반환합니다.
