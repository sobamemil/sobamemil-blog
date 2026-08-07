---
title: "명품 C++ programming 실습 문제 11장 10번"
date: 2020-04-02T14:15:27+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "iostream", "programming", "prompt", "string", "명품", "실습문제", "연습문제", "조작자", "프로그래밍"]
---

**문제 :**

다음은 프로그램과 실행 결과를 보여준다.

prompt 조작자를 작성하여 프로그램을 완성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16 | #include <iostream>  #include <string>  using namespace std;    int main() {  string password;  while(true) {  cin >> prompt >> password;  if(password == "C++") {  cout << "login success!!" << endl;  break;  }  else  cout << "login fail. try again!!" << endl;  }  } |

**실행 결과 :**

![](https://img.sobamemil.com/posts/141/img_1.png)

**목적 및 힌트 :**

조작자 작성 연습

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21 | #include <iostream>  #include <string>  using namespace std;    istream& prompt(istream& ins) { // prompt 조작자  cout << "암호?";  return ins;  }    int main() {  string password;  while(true) {  cin >> prompt >> password;  if(password == "C++") {  cout << "login success!!" << endl;  break;  }  else  cout << "login fail. try again!!" << endl;  }  } |


[저작자표시 비영리
(새창열림)](https://creativecommons.org/licenses/by-nc/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 11장 12번](/143)  (5) | 2020.04.02 |
| [명품 C++ programming 실습 문제 11장 11번](/142)  (1) | 2020.04.02 |
| [명품 C++ programming 실습 문제 11장 9번](/140)  (3) | 2020.04.02 |
| [명품 C++ programming 실습 문제 11장 8번](/139)  (1) | 2020.04.02 |
| [명품 C++ programming 실습 문제 11장 7번](/138)  (1) | 2020.04.02 |