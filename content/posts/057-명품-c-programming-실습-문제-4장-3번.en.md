---
title: "명품 C++ programming 실습 문제 4장 3번"
date: 2020-03-04T15:32:28+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "find()", "getline()", "npos", "programminig", "string", "명품", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

string 클래스를 이용하여 빈칸을 포함하는 문자열을 입력받고 문자열에서 'a'가 몇개 있는지 출력하는 프로그램을 작성해보자.

**목적 및 힌트 :**

getline(), string 클래스 활용

**실행 결과 :**

![](https://img.sobamemil.com/posts/57/img_1.png)

**코드 :**

(1) 문자열에서 'a'를 찾기 위해 string 클래스의 멤버 at()나 []를 이용하여 작성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15 | #include<iostream>  #include<string>  using namespace std;    int main() {  string str;  cout << "문자열 입력>>";  getline(cin,str);  int length = str.length();  int num = 0;  for(int i=0; i<length; i++){  if(str[i] == 'a') num++;  }  cout << "문자 a는 " << num << "개 있습니다." ;  } |

(2) 문자열에서 'a'를 찾기 위해 string 클래스의 find() 멤버 함수를 이용하여 작성하라. text.find('a', index);는 text 문자열의 index 위치부터 'a'를 찾아 문자열 내 인덱스를 리턴한다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18 | #include<iostream>  #include<string>  using namespace std;    int main() {  string str;  cout << "문자열 입력>>";  getline(cin,str);    int num = 0;  int j = -1;  while(true){  j = (int)str.find('a', j+1); // index 0 부터 'a'를 탐색  if(j == -1) break; // 'a'를 찾지 못했으면 break  num ++;  }  cout << "문자 a는 " << num << "개 있습니다." ;  } |

**설명 :**

string 클래스에 정의되어 있는 find() 멤버 함수는 찾고자 하는 문자를 찾지 못했을 때 npos 를 return 합니다.

npos는 string::npos로 정의되는 상수인데 unsinged int 입니다.

이때 npos를 int 타입으로 형변환 하면 나오는 값이 -1 입니다.


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 4장 5번](/59)  (3) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 4번](/58)  (5) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 2번](/56)  (1) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 1번](/55)  (1) | 2020.03.04 |
| [명품 C++ programming 실습 문제 3장 12번](/54)  (2) | 2020.03.03 |