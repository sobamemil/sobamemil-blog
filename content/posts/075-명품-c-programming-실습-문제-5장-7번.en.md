---
title: "명품 C++ programming 실습 문제 5장 7번"
date: 2020-03-05T15:09:01+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: []
---

<b>문제 :</b>

다음과 같이 선언된 정수를 저장하는 스택 클래스 MyIntStack을 구현하라.

MyIntStack 스택에 저장할 수 있는 정수의 최대 개수는 10이다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8 | class MyIntStack{  int p[10]; // 최대 10개의 정수 저장  int tos; // 스택의 꼭대기를 가리키는 인덱스  public:  MyIntStack();  bool push(int n); // 정수 n 푸시. 꽉 차 있으면 false, 아니면 true 리턴  bool pop(int &n); // 팝하여 n에 저장. 스택이 비어 있으면 false, 아니면 true 리턴  }; |

MyIntStack 클래스를 활용하는 코드와 실행 결과는 다음과 같다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13 | int main() {  MyIntStack a;  for(int i=0; i<11; i++) { // 11개를 푸시하면, 마지막에는 stack full이 된다.  if(a.push(i)) cout << i << ' '; // 푸시된 값 에코  else cout << endl << i+1 << " 번째 stack full" << endl;  }  int n;  for(int i=0; i<11; i++) { // 11개를 팝하면, 마지막에는 stack empty가 된다.  if(a.pop(n)) cout << n << ' '; // 팝 한 값 출력  else cout << endl << i+1 << " 번째 stack empty";  }  cout << endl;  } |

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/75/img_1.png)

<b>목적 및 힌트 :</b>

참조에 의한 호출로 효율적인 클래스 만들기

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49 | #include<iostream>  using namespace std;    class MyIntStack{  int p[10]; // 최대 10개의 정수 저장  int tos; // 스택의 꼭대기를 가리키는 인덱스  public:  MyIntStack();  bool push(int n); // 정수 n 푸시. 꽉 차 있으면 false, 아니면 true 리턴  bool pop(int &n); // 팝하여 n에 저장. 스택이 비어 있으면 false, 아니면 true 리턴  };    MyIntStack::MyIntStack(){  tos = 0; // 생성자에서 변수 초기화  }    bool MyIntStack::push(int n){  if(tos>9)  return false;  else {  p[tos] = n;  tos++;  return true;  }  }    bool MyIntStack::pop(int& n){ // 참조에 의한 호출  tos--;  if(tos<0)  return false;  else {  n = p[tos];  return true;  }  }    int main() {  MyIntStack a;  for(int i=0; i<11; i++) { // 11개를 푸시하면, 마지막에는 stack full이 된다.  if(a.push(i)) cout << i << ' '; // 푸시된 값 에코  else cout << endl << i+1 << " 번째 stack full" << endl;  }  int n;  for(int i=0; i<11; i++) { // 11개를 팝하면, 마지막에는 stack empty가 된다.  if(a.pop(n)) cout << n << ' '; // 팝 한 값 출력  else cout << endl << i+1 << " 번째 stack empty";  }  cout << endl;  } |

<b>설명 :</b>

참조에 의한 호출을 잘 사용하면 메모리 낭비를 줄이고 코드가 단순해져 효율적은 코드를 작성할 수 있습니다.


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 5장 9번](/77)  (3) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 8번](/76)  (9) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 6번](/74)  (1) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 5번](/73)  (1) | 2020.03.05 |
| [명품 C++ programming 실습 문제 5장 4번](/72)  (1) | 2020.03.05 |