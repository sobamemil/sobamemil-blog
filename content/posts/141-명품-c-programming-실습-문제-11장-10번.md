---
title: "명품 C++ programming 실습 문제 11장 10번"
date: 2020-04-02T14:15:27+09:00
draft: false
categories: ["개발 CS", "C++ 프로그래밍"]
tags: ["C++", "iostream", "programming", "prompt", "string", "명품", "실습문제", "연습문제", "조작자", "프로그래밍"]
---

**문제 :**

다음은 프로그램과 실행 결과를 보여준다.

prompt 조작자를 작성하여 프로그램을 완성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16 | #include <iostream>  #include <string>  using namespace std;    int main() {  string password;  while(true) {  cin >> prompt >> password;  if(password == "C++") {  cout << "login success!!" << endl;  break;  }  else  cout << "login fail. try again!!" << endl;  }  } |

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/141/img_1.png)

<b>목적 및 힌트 :</b>

조작자 작성 연습

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21 | #include <iostream>  #include <string>  using namespace std;    istream& prompt(istream& ins) { // prompt 조작자  cout << "암호?";  return ins;  }    int main() {  string password;  while(true) {  cin >> prompt >> password;  if(password == "C++") {  cout << "login success!!" << endl;  break;  }  else  cout << "login fail. try again!!" << endl;  }  } |
