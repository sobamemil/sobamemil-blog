---
title: "명품 C++ programming 실습 문제 7장 12번"
date: 2020-03-06T20:09:44+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "programming", "SortedArray", "명품", "복사생성자", "실습문제", "연산자", "연습문제", "중복", "프로그래밍"]
---

**문제 :**

정수 배열을 항상 증가 순으로 유지하는 SortedArray 클래스를 작성하려고 한다.

아래의 main() 함수가 작동할 만큼만 SortedArray 클래스를 작성하고 +와 = 연산자도 작성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13 | class SortedArray{  int size; // 현재 배열의 크기  int \*p; // 정수 배열에 대한 포인터  void sort(); // 정수 배열을 오름차순으로 정렬  public:  SortedArray(); // p는 NULL로 size는 0으로 초기화  SortedArray(SortedArray& src); // 복사 생성자  SortedArray(int p[], int size); // 생성자. 정수 배열과 크기를 전달받음  ~SortedArray(); // 소멸자  SortedArray operator+ (SortedArray& op2); // 현재 배열에 op2 배열 추가  SortedArray& operator= (const SortedArray& op2); // 현재 배열에 op2 배열 복사  void show(); // 배열의 원소 출력  }; |

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12 | int main() {  int n[] = { 2, 20, 6 };  int m[] = { 10, 7, 8, 30 };  SortedArray a(n, 3), b(m, 4), c;    c = a + b; // +, = 연산자 작성 필요  // + 연산자가 SortedArray 객체를 리턴하므로 복사 생성자 필요    a.show();  b.show();  c.show();  } |

**실행 결과 :**

![](https://img.sobamemil.com/posts/101/img_1.png)

**목적 및 힌트 :**

연산자 중복, 복사 생성자의 종합 응용

+ 연산자는 SortedArray 객체를 리턴하므로 복사 생성자가 반드시 필요하다.

a=b; 연산에서 = 연산자는 객체a의 배열 메모리를 모두 delete 시키고 객체 b의 크기만큼 다시 할당받은 후 객체 b의 배열 내용을 복사하도록 작성되어야 한다.

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96 | #include<iostream>  using namespace std;    class SortedArray{  int size; // 현재 배열의 크기  int \*p; // 정수 배열에 대한 포인터  void sort(); // 정수 배열을 오름차순으로 정렬  public:  SortedArray(); // p는 NULL로 size는 0으로 초기화  SortedArray(SortedArray& src); // 복사 생성자  SortedArray(int p[], int size); // 생성자. 정수 배열과 크기를 전달받음  ~SortedArray(); // 소멸자  SortedArray operator+ (SortedArray& op2); // 현재 배열에 op2 배열 추가  SortedArray& operator= (const SortedArray& op2); // 현재 배열에 op2 배열 복사  void show(); // 배열의 원소 출력  };    void SortedArray::show() {  sort();  cout << "배열 출력 : ";  for(int i=0; i<size; i++)  cout << p[i] << ' ';  cout << endl;  }    SortedArray::SortedArray(){  size = 0;  p = NULL;  }    SortedArray::SortedArray(int p[], int size){  this->p = new int [size];  this->size = size;  for(int i=0; i<size; i++)  this->p[i] = p[i];  }    SortedArray::SortedArray(SortedArray& src){  this->size = src.size;  this->p = new int [this->size];  for(int i=0; i<this->size; i++)  this->p[i] = src.p[i];  }    SortedArray& SortedArray::operator= (const SortedArray& op2){  delete [] p; // 배열 메모리 delete  this->size = op2.size;  this->p = new int [this->size]; // 객체 op2의 크기만큼 다시 동적 할당  for(int i=0; i<this->size; i++)  this->p[i] = op2.p[i];  return \*this;  }    SortedArray SortedArray::operator+ ( SortedArray& op2){  SortedArray test;  test.size = this->size + op2.size;  test.p = new int [test.size];  for(int i=0; i<test.size; i++){  if(i < this->size)  test.p[i] = this->p[i];  else  test.p[i] = op2.p[i-(test.size-op2.size)]; //total size - op2.size = this->size  }  return test;  }    void SortedArray::sort(){  int swp;  for(int i=0; i<size; i++){ //p[0] ~ p[size] sequential sort  for(int j=i; j<size; j++){  if(p[i]<p[j] || p[i]==p[j]);  else {  swp = p[i];  p[i] = p[j];  p[j] = swp;  }  }  }  }    SortedArray::~SortedArray() {  if(p) delete [] p;  }    int main() {  int n[] = { 2, 20, 6 };  int m[] = { 10, 7, 8, 30 };  SortedArray a(n, 3), b(m, 4), c;    c = a + b; // +, = 연산자 작성 필요  // + 연산자가 SortedArray 객체를 리턴하므로 복사 생성자 필요    a.show();  b.show();  c.show();  } |


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 8장 2번](/103)  (4) | 2020.03.09 |
| [명품 C++ programming 실습 문제 8장 1번](/102)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 7장 11번](/100)  (2) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 10번](/99)  (3) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 9번](/98)  (1) | 2020.03.06 |