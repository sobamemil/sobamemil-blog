---
title: "명품 C++ programming 실습 문제 10장 4번"
date: 2020-03-09T15:48:38+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "Generic", "programming", "template", "명품", "실습문제", "연습문제", "제네릭", "템플릿", "프로그래밍"]
---

**문제 :**

배열에서 원소를 검색하는 search() 함수를 템플릿으로 작성하라.

search()의 첫 번째 매개 변수는 검색하고자 하는 원소 값이고, 두 번째 매개 변수는 배열이며, 세 번째 매개 변수는 배열의 개수이다.

search() 함수가 검색에 성공하면 true를, 아니면 false를 리턴한다.

search()의 호출 사례는 다음과 같다.

|  |  |
| --- | --- |
| 1  2  3 | int x[] = {1, 10, 100, 5, 4};  if(search(100, x, 5)) cout << "100이 배열 x에 포함되어 있다"; // 이 cout 실행  else cout << "100이 배열 x에 포함되어 있지 않다"; |

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/114/img_1.png)

<b>목적 및 힌트 :</b>

템플릿 함수 만들기

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18 | #include<iostream>  using namespace std;      template <class T>  bool search(T search, T arr[], T arr\_size){  for(int i=0; i<arr\_size; i++){  if( arr[i] == search)  return true;  }  return false;  }    int main() {  int x[] = {1, 10, 100, 5, 4};  if(search(100, x, 5)) cout << "100이 배열 x에 포함되어 있다"; // 이 cout 실행  else cout << "100이 배열 x에 포함되어 있지 않다";  } |
