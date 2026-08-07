---
title: "명품 C++ programming 실습 문제 6장 6번"
date: 2020-03-06T15:49:01+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "programming", "static", "명품", "실습문제", "연습문제", "프로그래밍"]
---

<b>문제 :</b>

동일한 크기의 배열을 변환하는 다음 2개의 static 멤버 함수를 가진 ArrayUtiliry2 클래스를 만들고, 이 클래스를 이용하여 아래 결과와 같이 출력되도록 프로그램을 완성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6 | // s1과 s2를 연결한 새로운 배열을 동적 생성하고 포인터 리턴  static int\* concat(int s1[], int s2[], int size);    // s1에서 s2에 있는 숫자를 모두 삭제한 새로운 배열을 동적 생성하여 리턴  // 리턴하는 배열의 크기는 retSize에 전달. retSize가 0인 경우 NULL 리턴  static int\* remove(int s1[], int s2[], int size, int& retSize); |

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/86/img_1.png)

<b>목적 및 힌트 :</b>

static 멤버를 가진 클래스 만들기 및 사용 연습

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68 | #include<iostream>  using namespace std;    class ArrayUtility2{  public:  // s1과 s2를 연결한 새로운 배열을 동적 생성하고 포인터 리턴  static int\* concat(int s1[], int s2[], int size);    // s1에서 s2에 있는 숫자를 모두 삭제한 새로운 배열을 동적 생성하여 리턴  // 리턴하는 배열의 크기는 retSize에 전달. retSize가 0인 경우 NULL 리턴  static int\* remove(int s1[], int s2[], int size, int& retSize);  };    int\* ArrayUtility2::concat(int s1[], int s2[], int size){  int\* tot = new int [size]; // 새로운 배열 동적 생성  for(int i=0; i<size/2; i++) {  tot[i] = s1[i];  }  for(int i=size/2, j=0; i<size; i++,j++){  tot[i] = s2[j];  }  return tot;  }    int\* ArrayUtility2::remove(int s1[], int s2[], int size, int& retSize){  int\* rmtot = new int [size/2];  int cnt;  for(int i=0; i<size/2; i++){  cnt = 0;  for(int j=0; j<size/2; j++){  if(s1[i] == s2[j]) {  cnt++;  }  }  if(cnt == 0) {  rmtot[i] = s1[i];  retSize++;  }  }  if(retSize == 0) return NULL;  return rmtot;  }    int main() {  int x[5], y[5];  int size,retSize = 0;  int \*p;  cout << "정수 5 개 입력하라. 배열 x에 삽입한다>>";  for(int i=0; i<5; i++){  cin >> x[i];  }  cout << "정수 5 개 입력하라. 배열 y에 삽입한다>>";  for(int i=0; i<5; i++){  cin >> y[i];  }  size = (sizeof(x) + sizeof(y)) / sizeof(int);  cout << "합친 정수 배열을 출력한다\n";  p = ArrayUtility2::concat(x,y,size);  for(int i=0; i<size; i++){  cout << p[i] << ' ';  }  cout << endl << "배열 x[]에서 y[]를 뺀 결과를 출력한다. 개수는 ";  p = ArrayUtility2::remove(x,y,size,retSize);  cout << retSize << endl;  for(int i=0; i<retSize; i++){  cout << p[i] << ' ';  }  } |

<b>설명 :</b>

static 멤버 함수를 작성하여 ArrayUtility2 클래스의 객체를 생성하지 않고도 함수를 호출하여 사용 하였습니다.


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 6장 8번](/88)  (1) | 2020.03.06 |
| [명품 C++ programming 실습 문제 6장 7번](/87)  (1) | 2020.03.06 |
| [명품 C++ programming 실습 문제 6장 5번](/85)  (1) | 2020.03.06 |
| [명품 C++ programming 실습 문제 6장 4번](/84)  (2) | 2020.03.06 |
| [명품 C++ programming 실습 문제 6장 3번](/83)  (1) | 2020.03.05 |