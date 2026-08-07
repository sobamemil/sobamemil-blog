---
title: "명품 C++ programming 실습 문제 2장 16번"
date: 2020-02-28T20:24:43+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "isalpha", "programming", "tolower", "명품", "실습문제", "알파벳", "연습문제", "프로그래밍", "히스토그램"]
---

<b>문제 :</b>

영문 텍스트를 입력받아 알파벳 히스토그램을 그리는 프로그램을 작성하라. 대문자는 모두 소문자로 집계하며, 텍스트 입력의 끝은 ';' 문자로 한다.

<b>목적 및 힌트 :</b>

문자열 읽기, C++ 프로그램 종합 응용

<b>입력 파일 :</b>

입력할 텍스트 파일을 첨부하였습니다.

[2-16.txt

0.00MB](https://blog.kakaocdn.net/dna/EsAHK/btqChFfPBnw/AAAAAAAAAAAAAAAAAAAAAOhcwRebixdRiSrFB2r5c8Z4mBZDeCt4ibUUEp2n5aCw/2-16.txt?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1788188399&allow_ip=&allow_referer=&signature=PEoHUr5ktP9MyFLvskuQj0jS1Q8%3D&attach=1&knm=tfile.txt)

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/42/img_1.png)

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29 | #include<iostream>  #include<cstring>  using namespace std;    int main() {  int tot=0; // 총 알파벳 개수  int alpha[27]={0}; // 각각의 알파벳을 나타냄  char text[10000]; // text를 저장할 배열    cout << "영문 텍스트를 입력하세요. 히스토그램을 그립니다.\n텍스트의 끝은 ; 입니다. 10000개까지 가능합니다.\n";  cin.getline(text,10000,';'); // 최대 10,000개의 영문 텍스트를 ';'전까지 입력받는다    for (int i = 0; i<strlen(text); i++) { // text[0]부터 text의 끝까지  if (isalpha(text[i])) { // text[i]가 알파벳이면 참  if(text[i]<91) text[i] = tolower(text[i]); // text[i]가 대문자이면 소문자로 변경  tot++;  alpha[text[i] - 97]++; // 각각의 알파벳이 몇개인지 카운트  }  }    cout << "총 알파벳 수 " << tot << endl << endl;  for (int i = 0; i < 26; ++i) { // 알파벳의 소문자 총 개수는 26개 (a~z)  cout << (char)(i+'a') << "(" << alpha[i] << ")"; // a부터 z까지 출력 후 각 (알파벳의 개수) 출력  cout << "\t:  "; // 포맷을 출력하기 위해 탭과 ":" 출력  for (int j = 1; j <= alpha[i]; j++) // 각 알파벳의 개수만큼 "\*" 출력  cout << "\*";  cout << endl;  }  } |

<b>설명 :</b>

cin.getline(buf, 10000, ';'); 을 이용하여 텍스트를 키보드로부터 읽으면 됩니다.

문자를 소문자로 바꿀 때 tolower(char c) 함수를 이용하고, 알파벳인지 검사하기 위해 isalpha(char c) 함수를 이용하면 됩니다.

또한 텍스트 입력을 쉽게 하려면, 입력할 텍스트를 첨부하였으니 ctrl-c로 복사하고, DOS 실행창에 마우스 오른쪽 버튼을 누르고 붙여 넣기 메뉴를 선택하거나 오른쪽 버튼만 눌러도 붙여 넣기가 됩니다.


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 3장 2번](/44)  (2) | 2020.03.02 |
| [명품 C++ programming 실습 문제 3장 1번](/43)  (1) | 2020.03.02 |
| [명품 C++ programming 실습 문제 2장 15번](/41)  (3) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 14번](/40)  (3) | 2020.02.28 |
| [명품 C++ programming 실습 문제 2장 13번](/39)  (1) | 2020.02.28 |