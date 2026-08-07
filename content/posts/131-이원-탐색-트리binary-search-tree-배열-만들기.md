---
title: "이원 탐색 트리(Binary Search Tree) 배열 만들기"
date: 2020-03-19T15:06:28+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["binarysearchtree", "tree", "배열", "이원탐색", "이원탐색트리", "자료구조", "탐색", "트리", "파일처리", "파일처리론"]
---

**문제 :**

배열을 이용하여 이원 탐색 트리를 만들고 탐색하는 프로그램을 작성하라.

1. 입력 : 정렬이 되지 않은 숫자들

2. 프로그램 :

  2.1 입력된 숫자들을 하나씩 읽으면서 이원 탐색 트리 배열 만들기

  2.2 숫자 하나를 입력하면 이원탐색트리 알고리즘을 적용하여 해당하는 배열의 첨자를 출력하기

         (이 때 출력은 배열 원소들을 차례대로 출력하고 해당하는 배열 첨자를 출력)

**실행 결과 :**

![](https://img.sobamemil.com/posts/131/img_1.png)

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78 | #include<iostream>  using namespace std;    void newBinarySearchTree(int \*num\_arr, int size, int \*new\_num\_arr) {    for(int i=0; i<size+20; i++){ // 이원탐색트리 배열 -1로 초기화  new\_num\_arr[i] = -1;  }  new\_num\_arr[0] = num\_arr[0];    for(int i=1; i<size; i++){  int index=0;  // 새로 들어올 숫자가 이원탐색트리 배열의 루트보다 작으면 왼쪽으로 이동  if(new\_num\_arr[0] > num\_arr[i]) {  for(int j=2\*index+1;;) {  if(new\_num\_arr[j] != -1){ //삽입하려는 이원탐색트리 배열공간이 NULL이 아니면 비교  if(new\_num\_arr[j] < num\_arr[i]) j=2\*j+2; //  삽입하고자 하는 숫자가 더 크면 2j+2  else if(new\_num\_arr[j] > num\_arr[i]) j=2\*j+1; // 삽입하고자 하는 숫자가 더 작으면 2j+1  z  else {  //같은 숫자가 나오면 오류메시지 출력 후 프로그램 비정상 종료  cout << "same data error...\n"; exit(1);  }  }  else if(new\_num\_arr[j] == -1) { // 삽입하려는 이원탐색트리 배열 공간이 NULL이면 바로 삽입  new\_num\_arr[j] = num\_arr[i];  break;  }  }  }  // 새로 들어올 숫자가 이원탐색트리 배열의 루트보다 크면 오른쪽으로 이동  else if(new\_num\_arr[0] < num\_arr[i]) {  for(int j=2\*index+2;;) {  if(new\_num\_arr[j] != -1){ // 삽입하려는 이원탐색트리 배열공간이 NULL이 아니면 비교  if(new\_num\_arr[j] < num\_arr[i]) j=2\*j+2;  else if(new\_num\_arr[j] > num\_arr[i]) j=2\*j+1;  else {  cout << "same data error...\n"; exit(1);  }  }  else if(new\_num\_arr[j] == -1) {  new\_num\_arr[j] = num\_arr[i];  break;  }  }  }  else continue;  }  }    void find(int \*new\_num\_arr, int size) {  int x, flag;  cout << "찾고자 하는 숫자 입력 : ";  cin >>  x;    for(int i=0; i<size; i++) // 이원탐색트리 배열의 모든 원소 출력  cout << "arr[" << i << "] : " << new\_num\_arr[i] << endl;    for(int i=0; i<size; i++){  if(new\_num\_arr[i] == x) {  cout << "index : " << i;  flag = true;  break;  }  else  flag = false;  }  if(!flag) // flag가 false이면 찾고자 하는 숫자가 없다고 출력  cout << "찾고자 하는 숫자 없음\n";  }    int main() {  int num\_arr[] = {50, 40, 55, 30, 45, 54, 53, 1, 60, 301, 2};  int num\_arr\_size = sizeof(num\_arr)/sizeof(num\_arr[0]);  int \*new\_num\_arr = new int [num\_arr\_size + 20]; // 이원탐색트리 배열 공간 생성    newBinarySearchTree(num\_arr, num\_arr\_size, new\_num\_arr);  find(new\_num\_arr, num\_arr\_size + 20);  } |

**설명 :**

간단하게 구현하기 위해 입력 데이터로 숫자 배열을 만들어 넣어주고, 이원 탐색 트리 배열의 크기도 임의로 적당히 지정했습니다.

위의 코드의 경우 배열의 크기를 동적으로 할당받지 않았으므로 최악의 입력 데이터가 들어올 경우 오버플로우가 일어날 수 있으니 작성할 때 주의하셔서 수정하시면 됩니다.

**코딩은 내일부터 ;**

[저작자표시 비영리
(새창열림)](https://creativecommons.org/licenses/by-nc/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [알고리즘 & 코딩테스트](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%26%20%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [크러스컬 알고리즘 구현 1 (붕괴법칙을 적용하지 않은 방법)](/180)  (0) | 2021.04.09 |
| [R 프로그램 다운로드 설치 및 실행 방법](/179)  (0) | 2020.09.03 |
| [크러스컬(Kruskal) 알고리즘](/150)  (1) | 2020.07.02 |
| [합병 정렬(Merge Sort) 알고리즘](/129)  (1) | 2020.03.18 |
| [삽입 정렬(Insertion Sort) 알고리즘](/127)  (1) | 2020.03.17 |