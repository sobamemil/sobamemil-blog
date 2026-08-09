---
title: "C++ Programming Ch.10 Exercise 14 Solution"
date: 2020-03-11T14:59:59+09:00
draft: false
categories: ["💻 Dev & CS", "C++ Programming"]
tags: ["C++", "iostream", "map", "programming", "Map", "Masterpiece", "Practice Problem", "Exercise", "Container", "Programming"]
---

**Problem:**

암호 관리 응용프로그램을 map을 이용하여 작성하라.

실행 과정은 다음과 같다.

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/124/img_1.png)

<b>Objective & Hints:</b>

map 컨테이너에 삽입 및 조회 응용

이름과 점수를 쌍으로 저장할 맵 컨테이너로 map<string, string>을 이용하면 됩니다.

아래 링크에 있는 Exercise Problem 10장 13번을 참고하세요.

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46 | #include <iostream>  #include <map>  using namespace std;    void insert(map<string, string> &pwManager){  string name, pw;  cout << "이름 암호>> ";  cin >> name >> pw;  pwManager.insert(make\_pair(name, pw));  }    void checkNamePw(map<string, string> &pwManager){  string name, pw;  cout << "이름? "; cin >> name;  while(true){  cout << "암호? "; cin >> pw;  if(pwManager[name] == pw){  cout << "통과!!\n";  break;  }  else  cout << "실패~~\n"; // 틀리면 출력 후 다시 암호 질문  }  }    int main() {  map<string, string> pwManager;  cout << "\*\*\*\*\* 암호 관리 프로그램 WHO를 시작합니다 \*\*\*\*\*\n";    while(true){  cout << "삽입:1, 검사:2, 종료3>> ";  int n;  cin >> n;  switch(n){  case 1:  insert(pwManager);  break;  case 2:  checkNamePw(pwManager);  break;  case 3:  cout << "프로그램을 종료합니다...";  return 0;  }  }  } |

<b>Explanation:</b>

Exercise Problem 10장 13번 문제와 비슷한 문제입니다.

참고하여 작성하면 도움이 될 것 같습니다.
