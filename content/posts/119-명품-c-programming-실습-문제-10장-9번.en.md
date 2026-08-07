---
title: "C++ Programming Ch.10 Exercise 9 Solution"
date: 2020-03-10T17:50:23+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "Iterator", "programming", "vector", "명품", "벡터", "실습문제", "연습문제", "컨테이너", "프로그래밍"]
---<b>Problem:</b>

STL의 vector 클래스를 이용하는 간단한 프로그램을 작성해보자. vector 객체를 생성하고, 키보드로부터 정수를 입력받을 때마다 정수를 벡터에 삽입하고 지금까지 입력된 수와 평균을 출력한느 프로그램을 작성하라.

0을 입력하면 프로그램이 종료된다.

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/119/img_1.png)

<b>Objective & Hints:</b>

vector 컨테이너 활용 연습

정수만 다루는 벡터이므로 vector<int> v;를 이용하면 된다. iterator를 사용할 필요는 없다.

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20 | #include <iostream>  #include <vector>  using namespace std;    int main() {  vector<int> v;  double sum=0;  while(true){  int tmp;  cout << "정수를 입력하세요(0을 입력하면 종료)>>";  cin >> tmp;  if(!tmp) break; //입력한 정수가 0이면 종료  v.push\_back(tmp); // 입력한 정수가 0이 아니면 v에 삽입  for(int i=0; i<v.size(); i++) // vector v의 모든 원소 출력  cout << v.at(i) << ' ';  cout << endl;  sum += tmp;  cout << "평균 = " << sum/v.size() << endl;  }  } |

<b>Explanation:</b>

vector 클래스의 size() 멤버 함수를 사용하면 원소의 개수를 알 수 있습니다.
