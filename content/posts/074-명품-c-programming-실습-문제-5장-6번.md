---
title: "명품 C++ programming 실습 문제 5장 6번"
date: 2020-03-05T14:59:03+09:00
draft: false
categories: ["개발 CS", "C++ 프로그래밍"]
tags: ["C++", "programming", "reference", "명품", "실습문제", "연습문제", "참조", "참조리턴", "프로그래밍", "호출"]
---

**문제 :**

find() 함수의 원형은 다음과 같다. 문자열 a에서 문자 c를 찾아, 문자 c가 있는 공간에 대한 참조를 리턴한다.

만일 문자 c를 찾을 수 없다면 success 참조 매개 변수에 false를 설정한다.

물론 찾게 되면 success에 true를 설정한다.

|  |  |
| --- | --- |
| 1 | char& find(char a[], char c, bool& success); |

다음 main()이 잘 실행되도록 find()를 작성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11 | int main() {  char s[] = "Mike";  bool b = false;  char& loc = find(s, 'M', b);  if(b == false) {  cout << "M을 발견할 수 없다" << endl;  return 0;  }  loc = 'm'; // 'M' 위치에 'm' 기록  cout << s << endl; // "mike"가 출력됨  } |

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/74/img_1.png)

<b>목적 및 힌트 :</b>

참조에 의한 호출과 참조를 리턴하는 함수 작성

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24 | #include<iostream>  using namespace std;    char& find(char a[], char c, bool& success){  int len = sizeof(a);  for(int i=0; i<len; i++){  if(a[i]==c) {  success = true;  return a[i];  }  }  }    int main() {  char s[] = "Mike";  bool b = false;  char& loc = find(s, 'M', b);  if(b == false) {  cout << "M을 발견할 수 없다" << endl;  return 0;  }  loc = 'm'; // 'M' 위치에 'm' 기록  cout << s << endl; // "mike"가 출력됨  } |

<b>설명 :</b>

참조에 의한 호출 뿐 아니라 참조를 리턴하는 함수를 작성 하였습니다.

원하는 문자를 찾을 시 그 위치의 참조를 리턴해 참조변수 loc에 넣고 나중에 그 값을 변경 하였습니다.
