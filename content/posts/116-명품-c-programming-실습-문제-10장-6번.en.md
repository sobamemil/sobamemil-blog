---
title: "C++ Programming Ch.10 Exercise 6 Solution"
date: 2020-03-09T16:07:40+09:00
draft: false
categories: ["💻 Dev & CS", "C++ Programming"]
tags: ["C++", "for", "programming", "remove", "Masterpiece", "Loop", "Practice Problem", "Exercise", "Template", "Programming"]
---

**Problem:**

다음 함수는 매개 변수로 주어진 int 배열 src에서 배열 minus에 들어있는 같은 정수를 모두 삭제한 새로운 int 배열을 동적으로 할당받아 리턴한다.

retSize는 remove() 함수의 Execution Result를 리턴하는 배열의 크기를 전달받는다.

|  |  |
| --- | --- |
| 1 | int \* remove(int src[], int sizeSrc, int minus[], int sizeMinus, int& resSize); |

템플릿을 이용하여 remove를 일반화하라.

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/116/img_1.png)

<b>Objective & Hints:</b>

함수의 일반화에 대한 이해, 템플릿 함수 만들기

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41 | #include <iostream>  using namespace std;    template <class T>  T\* remove(T src[], int sizeSrc, T minus[], int sizeMinus, int & retsize){  int j;  T\* tmpArray = new T[sizeSrc];  for(int i=0; i<sizeSrc; i++){  for(j=0; j<sizeMinus; j++){  if(src[i] == minus[j]){ // src의 원소와 minus의 원소가 같으면 j의 값을 하나 내린 후 break  --j;  break;  }  }  if(j==sizeMinus){ // j==sizeMinus 라는건 src와 minus에 같은 원소가 없어 중간에 break 되지 않은 경우  tmpArray[retsize] = src[i]; // src[i]를 동적 할당 하여 생성한 tmpArray에 삽입  retsize++; // return 할 size의 값을 하나 올려줌  }  }  return tmpArray;  }    int main() {  int a[] = { 1,2,3,4,5,6,7,8,9,10 };  int b[] = { 5,6,7,8,9 };  int size=0;  int \*p = remove(a, 10, b,5, size);  for (int i = 0; i < size; ++i)  cout << p[i] << ' ';  cout << endl;  delete[] p;  size = 0;  char c[] = { 'a','b','i','m','c','d','e',};  char d[] = { 'k','i','m','n','u' };  char \*q = remove(c, 7, d, 5,size);  for (int i = 0; i < size; ++i)  cout << q[i] << ' ';  cout << endl;  delete[] q;    } |

<b>Explanation:</b>

src[]의 값과 minus[]의 값을 2중 for문을 이용하여 비교 및 삭제 하였습니다.
