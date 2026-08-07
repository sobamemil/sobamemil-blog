---
title: "명품 C++ programming 실습 문제 10장 9번"
date: 2020-03-10T17:50:23+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "Iterator", "programming", "vector", "명품", "벡터", "실습문제", "연습문제", "컨테이너", "프로그래밍"]
---

**문제 :**

STL의 vector 클래스를 이용하는 간단한 프로그램을 작성해보자. vector 객체를 생성하고, 키보드로부터 정수를 입력받을 때마다 정수를 벡터에 삽입하고 지금까지 입력된 수와 평균을 출력한느 프로그램을 작성하라.

0을 입력하면 프로그램이 종료된다.

**실행 결과 :**

![](https://img.sobamemil.com/posts/119/img_1.png)

**목적 및 힌트 :**

vector 컨테이너 활용 연습

정수만 다루는 벡터이므로 vector<int> v;를 이용하면 된다. iterator를 사용할 필요는 없다.

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20 | #include <iostream>  #include <vector>  using namespace std;    int main() {  vector<int> v;  double sum=0;  while(true){  int tmp;  cout << "정수를 입력하세요(0을 입력하면 종료)>>";  cin >> tmp;  if(!tmp) break; //입력한 정수가 0이면 종료  v.push\_back(tmp); // 입력한 정수가 0이 아니면 v에 삽입  for(int i=0; i<v.size(); i++) // vector v의 모든 원소 출력  cout << v.at(i) << ' ';  cout << endl;  sum += tmp;  cout << "평균 = " << sum/v.size() << endl;  }  } |

**설명 :**

vector 클래스의 size() 멤버 함수를 사용하면 원소의 개수를 알 수 있습니다.


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 10장 11번](/121)  (2) | 2020.03.10 |
| [명품 C++ programming 실습 문제 10장 10번](/120)  (1) | 2020.03.10 |
| [명품 C++ programming 실습 문제 10장 8번](/118)  (4) | 2020.03.09 |
| [명품 C++ programming 실습 문제 10장 7번](/117)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 10장 6번](/116)  (1) | 2020.03.09 |