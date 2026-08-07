---
title: "명품 C++ programming 실습 문제 4장 4번"
date: 2020-03-04T15:42:39+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["4번", "4장", "C++", "programming", "동적배열", "명품", "실습문제", "연습문제", "코딩", "프로그래밍"]
---

**문제 :**

다음과 같은 Sample 클래스가 있다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12 | class Sample{  int \*p;  int size;  public:  Sample(int n) {    // 생성자  size = n; p = new int [n]; // n개 정수 배열의 동적 생성  }  void read(); // 동적 할당받은 정수 배열 p에 사용자로부터 정수를 입력 받음  void write(); // 정수 배열을 화면에 출력  int big(); // 정수 배열에서 가장 큰 수 리턴  ~Sample(); // 소멸자  }; |

다음 main() 함수가 실행되도록 Sample 클래스를 완성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6 | int main() {  Sample s(10); // 10개 정수 배열을 가진 Sample 객체 생성  s.read(); // 키보드에서 정수 배열 읽기  s.write(); // 정수 배열 출력  cout << "가장 큰 수는 " << s.big() << endl; // 가장 큰 수 출력  } |

**목적 및 힌트 :**

동적 배열을 가진 클래스 다루기

**실행 결과 :**

![](https://img.sobamemil.com/posts/58/img_1.png)

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45 | #include<iostream>  using namespace std;    class Sample{  int \*p;  int size;  public:  Sample(int n) { // 생성자  size = n; p = new int [n]; // n개 정수 배열의 동적 생성  }  void read();  // 동적 할당받은 정수 배열 p에 사용자로부터 정수를 입력 받음  void write(); // 정수 배열을 화면에 출력  int big(); // 정수 배열에서 가장 큰 수 리턴  ~Sample();  // 소멸자  };    void Sample::read(){  for(int i=0; i<size; i++){  cin >> p[i];  }  }    void Sample::write(){  for(int i=0; i<size; i++){  cout << p[i] << " ";  }  cout << endl;  }    int Sample::big(){  int big = 0;  for(int i=0; i<size; i++){  if(big < p[i]) big = p[i];  }  return big;  }    Sample::~Sample(){}    int main() {  Sample s(10); // 10개 정수 배열을 가진 Sample 객체 생성  s.read();  // 키보드에서 정수 배열 읽기  s.write();  // 정수 배열 출력  cout << "가장 큰 수는 " << s.big() << endl; // 가장 큰 수 출력  } |

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 4장 6번](/60)  (1) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 5번](/59)  (3) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 3번](/57)  (1) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 2번](/56)  (1) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 1번](/55)  (1) | 2020.03.04 |