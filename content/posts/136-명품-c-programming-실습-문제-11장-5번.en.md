---
title: "명품 C++ programming 실습 문제 11장 5번"
date: 2020-03-27T15:42:20+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["11장", "C++", "cin", "getline", "programming", "string", "명품", "실습문제", "연습문제"]
---

**문제 :**

다음 프로그램은 예제 11-3의 코드이다. 아래 코드에서 char [] 대신 string을 이용하여 문자열을 다루도록 프로그램을 재작성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18 | #include <iostream>  #include <cstring>  using namespace std;    int main() {  char cmd[80];  cout << "cin.get(char\*, int)로 문자열을 읽습니다." << endl;  while(true) {  cout << "종료하려면 exit를 입력하세요 >> ";  cin.get(cmd, 80); // 79개까지의 문자 읽음  if(strcmp(cmd, "exit") == 0 ) {  cout << "프로그램을 종료합니다....";  return 0;  }  else  cin.ignore(1); // 버퍼에 남아 있는 <Enter> 키 ('\n') 제거  }  } |

**실행 결과 :**

![](https://img.sobamemil.com/posts/136/img_1.png)

**목적 및 힌트 :**

getline()으로 string 객체에 문자열 읽어 들이기

cmd를 string 타입으로 선언하고 cin.get() 대신, string 객체에 문자열을 읽어들이는 getline(cin, cmd) 함수를 사용하면 됩니다.

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | #include <iostream>  using namespace std;    int main() {  string cmd;  while(true){  cout << "종료하려면 exit을 입력하세요 >> ";  getline(cin, cmd); // getline() 함수를 통해 문자열 입력  if(cmd == "exit") {  cout << "프로그램을 종료합니다....";  return 0;  }  }  } |


[저작자표시 비영리
(새창열림)](https://creativecommons.org/licenses/by-nc/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 11장 7번](/138)  (1) | 2020.04.02 |
| [명품 C++ programming 실습 문제 11장 6번](/137)  (1) | 2020.03.27 |
| [명품 C++ programming 실습 문제 11장 4번](/135)  (1) | 2020.03.27 |
| [명품 C++ programming 실습 문제 11장 3번](/134)  (3) | 2020.03.27 |
| [명품 C++ programming 실습 문제 11장 2번](/133)  (1) | 2020.03.27 |