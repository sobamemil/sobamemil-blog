---
title: "명품 C++ programming 실습 문제 7장 6번"
date: 2020-03-06T18:01:44+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "Matrix", "programming", "명품", "실습문제", "연산자중복", "연산자함수", "연습문제", "프렌드함수", "프로그래밍"]
---

**문제 :**

2차원 행렬을 추상화한 Matrix 클래스를 작성하고, show() 멤버 함수와 다음 연산이 가능하도록 연산자를 모두 구현하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6 | Matrix a(1,2,3,4), b(2,3,4,5), c;  c = a + b;  a += b;  a.show(); b.show(); c.show();  if(a==c)  cout << "a and c are the same" << endl; |

(1) 연산자 함수를 Matrix의 멤버 함수로 구현하라.

(2) 연산자 함수를 Matrix의 프렌드 함수로 구현하라.

**실행 결과 :**

![](https://img.sobamemil.com/posts/95/img_1.png)

**목적 및 힌트 :**

연산자와 클래스 구현 연습

**코드 :**

● 문제 (1)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54 | #include<iostream>  using namespace std;    class Matrix{  int num[4];  public:  Matrix(){;}  Matrix(int a, int b, int c, int d){  num[0] = a; num[1] = b; num[2] = c; num[3] = d;  };  void show();  Matrix operator+ (Matrix b);  Matrix operator+= (Matrix &b);  bool operator== (Matrix b);  };    Matrix Matrix::operator+ (Matrix b){  Matrix t;  for(int i=0; i<4; i++)  t.num[i] = this->num[i] + b.num[i];  return t;  }    Matrix Matrix::operator+= (Matrix &b){  for(int i=0; i<4; i++)  this->num[i] += b.num[i];  return \*this;  }    bool Matrix::operator== (Matrix c){  for(int i=0; i<4; i++){  if(this->num[i] == c.num[i]);  else  return false;  }  return true;  }    void Matrix::show(){  cout << "Matrix = { ";  for(int i=0; i<4; i++){  cout << this->num[i] << ' ';  }  cout << "}" << endl;  }    int main() {  Matrix a(1,2,3,4), b(2,3,4,5), c;  c = a + b;  a += b;  a.show(); b.show(); c.show();  if(a==c)  cout << "a and c are the same" << endl;  }  [Colored by Color Scripter](http://colorscripter.com/info#e) |

● 문제 (2)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53 | #include<iostream>  using namespace std;    class Matrix{  int num[4];  public:  Matrix(){;}  Matrix(int a, int b, int c, int d){  num[0] = a; num[1] = b; num[2] = c; num[3] = d;  };  void show();  friend Matrix operator+ (Matrix a, Matrix b);  friend void operator+= (Matrix &a, Matrix &b);  friend bool operator== (Matrix a, Matrix b);  };    Matrix operator+ (Matrix a, Matrix b){  Matrix t;  for(int i=0; i<4; i++)  t.num[i] = a.num[i] + b.num[i];  return t;  }    void operator+= (Matrix &a, Matrix &b){  for(int i=0; i<4; i++)  a.num[i] += b.num[i];  }    bool operator== (Matrix a, Matrix c){  for(int i=0; i<4; i++){  if(a.num[i] == c.num[i]);  else  return false;  }  return true;  }    void Matrix::show(){  cout << "Matrix = { ";  for(int i=0; i<4; i++){  cout << this->num[i] << ' ';  }  cout << "}" << endl;  }    int main() {  Matrix a(1,2,3,4), b(2,3,4,5), c;  c = a + b;  a += b;  a.show(); b.show(); c.show();  if(a==c)  cout << "a and c are the same" << endl;  } |

**설명 :**

이 문제를 해결하기 위해서는 +, +=, == 연산자를 구현하여야 합니다.

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 7장 8번](/97)  (1) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 7번](/96)  (3) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 5번](/94)  (1) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 4번](/93)  (3) | 2020.03.06 |
| [명품 C++ programming 실습 문제 7장 3번](/92)  (1) | 2020.03.06 |