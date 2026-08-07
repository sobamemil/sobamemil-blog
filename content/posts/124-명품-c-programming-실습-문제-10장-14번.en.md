---
title: "명품 C++ programming 실습 문제 10장 14번"
date: 2020-03-11T14:59:59+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "iostream", "map", "programming", "맵", "명품", "실습문제", "연습문제", "컨테이터", "프로그래밍"]
---

<b>문제 :</b>

암호 관리 응용프로그램을 map을 이용하여 작성하라.

실행 과정은 다음과 같다.

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/124/img_1.png)

<b>목적 및 힌트 :</b>

map 컨테이너에 삽입 및 조회 응용

이름과 점수를 쌍으로 저장할 맵 컨테이너로 map<string, string>을 이용하면 됩니다.

아래 링크에 있는 실습 문제 10장 13번을 참고하세요.

[2020/03/11 - [C++/명품 C++ programming] - 명품 C++ programming 실습 문제 10장 13번](https://sobamemil.tistory.com/123)

[명품 C++ programming 실습 문제 10장 13번

문제 : map 컨테이너를 이용하여 (이름, 성적)을 저장하고 이름으로 성적을 조회하는 점수 관리 프로그램을 만들어라. 이름은 빈칸 없이 입력하는 것을 원칙으로 한다. 실행 결과 : 목적 및 힌트 : map 컨테이너..

sobamemil.tistory.com](https://sobamemil.tistory.com/123)

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46 | #include <iostream>  #include <map>  using namespace std;    void insert(map<string, string> &pwManager){  string name, pw;  cout << "이름 암호>> ";  cin >> name >> pw;  pwManager.insert(make\_pair(name, pw));  }    void checkNamePw(map<string, string> &pwManager){  string name, pw;  cout << "이름? "; cin >> name;  while(true){  cout << "암호? "; cin >> pw;  if(pwManager[name] == pw){  cout << "통과!!\n";  break;  }  else  cout << "실패~~\n"; // 틀리면 출력 후 다시 암호 질문  }  }    int main() {  map<string, string> pwManager;  cout << "\*\*\*\*\* 암호 관리 프로그램 WHO를 시작합니다 \*\*\*\*\*\n";    while(true){  cout << "삽입:1, 검사:2, 종료3>> ";  int n;  cin >> n;  switch(n){  case 1:  insert(pwManager);  break;  case 2:  checkNamePw(pwManager);  break;  case 3:  cout << "프로그램을 종료합니다...";  return 0;  }  }  } |

<b>설명 :</b>

실습 문제 10장 13번 문제와 비슷한 문제입니다.

참고하여 작성하면 도움이 될 것 같습니다.


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 10장 16번](/126)  (1) | 2020.03.11 |
| [명품 C++ programming 실습 문제 10장 15번](/125)  (3) | 2020.03.11 |
| [명품 C++ programming 실습 문제 10장 13번](/123)  (1) | 2020.03.11 |
| [명품 C++ programming 실습 문제 10장 12번](/122)  (3) | 2020.03.10 |
| [명품 C++ programming 실습 문제 10장 11번](/121)  (2) | 2020.03.10 |