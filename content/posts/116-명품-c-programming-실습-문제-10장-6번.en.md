---
title: "명품 C++ programming 실습 문제 10장 6번"
date: 2020-03-09T16:07:40+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "for", "programming", "remove", "명품", "반복문", "실습문제", "연습문제", "템플릿", "프로그래밍"]
---

<b>문제 :</b>

다음 함수는 매개 변수로 주어진 int 배열 src에서 배열 minus에 들어있는 같은 정수를 모두 삭제한 새로운 int 배열을 동적으로 할당받아 리턴한다.

retSize는 remove() 함수의 실행 결과를 리턴하는 배열의 크기를 전달받는다.

|  |  |
| --- | --- |
| 1 | int \* remove(int src[], int sizeSrc, int minus[], int sizeMinus, int& resSize); |

템플릿을 이용하여 remove를 일반화하라.

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/116/img_1.png)

<b>목적 및 힌트 :</b>

함수의 일반화에 대한 이해, 템플릿 함수 만들기

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41 | #include <iostream>  using namespace std;    template <class T>  T\* remove(T src[], int sizeSrc, T minus[], int sizeMinus, int & retsize){  int j;  T\* tmpArray = new T[sizeSrc];  for(int i=0; i<sizeSrc; i++){  for(j=0; j<sizeMinus; j++){  if(src[i] == minus[j]){ // src의 원소와 minus의 원소가 같으면 j의 값을 하나 내린 후 break  --j;  break;  }  }  if(j==sizeMinus){ // j==sizeMinus 라는건 src와 minus에 같은 원소가 없어 중간에 break 되지 않은 경우  tmpArray[retsize] = src[i]; // src[i]를 동적 할당 하여 생성한 tmpArray에 삽입  retsize++; // return 할 size의 값을 하나 올려줌  }  }  return tmpArray;  }    int main() {  int a[] = { 1,2,3,4,5,6,7,8,9,10 };  int b[] = { 5,6,7,8,9 };  int size=0;  int \*p = remove(a, 10, b,5, size);  for (int i = 0; i < size; ++i)  cout << p[i] << ' ';  cout << endl;  delete[] p;  size = 0;  char c[] = { 'a','b','i','m','c','d','e',};  char d[] = { 'k','i','m','n','u' };  char \*q = remove(c, 7, d, 5,size);  for (int i = 0; i < size; ++i)  cout << q[i] << ' ';  cout << endl;  delete[] q;    } |

<b>설명 :</b>

src[]의 값과 minus[]의 값을 2중 for문을 이용하여 비교 및 삭제 하였습니다.


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 10장 8번](/118)  (4) | 2020.03.09 |
| [명품 C++ programming 실습 문제 10장 7번](/117)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 10장 5번](/115)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 10장 4번](/114)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 10장 3번](/113)  (1) | 2020.03.09 |