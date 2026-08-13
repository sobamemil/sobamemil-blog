---
title: "Merge Sort Algorithm"
date: 2020-03-18T14:20:58+09:00
draft: false
categories: ["Dev CS"]
tags: ["2019", "algorithm", "merge", "MergeSort", "Sort", "Pseudocode", "Algorithm", "Sorting", "Programming", "Merge Sort"]
---합병 정렬(Merge Sort)이란?

분할 정복 알고리즘(=Divide and conquer algorithm 즉, 그대로 해결할 수 없는 문제를 작은 문제로 분할하여 문제를 해결하는 방법이나 알고리즘입니다.)의 하나로 O(*n* log *n*)의 시간 복잡도를 가지고 있습니다.

합병 정렬의 작동 알고리즘은 아래와 같습니다.

1. 리스트의 길이가 1 이하이면 이미 정렬된 것으로 본다. 그렇지 않은 경우에는
2. 분할(divide) : 정렬되지 않은 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
3. 정복(conquer) : 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.
4. 결합(combine) : 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다. 이때 정렬 결과가 임시배열에 저장된다.
5. 복사(copy) : 임시 배열에 저장된 결과를 원래 배열에 복사한다.

이해가 잘 안간다면 아래 애니메이션을 통해 작동 원리를 쉽게 이해할 수 있습니다.

![](https://img.sobamemil.com/posts/129/img_1.gif)

합병 정렬의 애니메이션 -Swfung8-

<b>Pseudocode :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7 | //Merge Sort  MergeSort() //A[1...n]  1. If n=1, done // 원소가 1개이면 이미 정렬이 끝난 상태이다.  // 그렇지 않으면 A[1]에서 A[n/2]까지, A[n/2]+1에서 A[n]까지  // 분할하여 재귀적으로 정렬한다.  2. Recursively sort A[1...[n/2]] and A[[n/2]+1...n]  3. Merge 2 sorted lists // 나누어진 두 부분을 합친다. |

<b>C Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66 | #include <stdio.h>    void TopDownMergeSort(int A[], int B[], int n);  void TopDownSplitMerge(int B[], int iBegin, int iEnd, int A[]);  void TopDownMerge(int A[], int iBegin, int iMiddle, int iEnd, int B[]);  void CopyArray(int A[], int iBegin, int iEnd, int B[]);    int i, j, k;    // 배열 A[]는 정렬할 배열, 배열 B는 작업할 배열  void TopDownMergeSort(int A[], int B[], int n)  {  CopyArray(A, 0, n, B);           // 배열 A[]를 B[]로 복사  TopDownSplitMerge(B, 0, n, A);   // B[]에서 A[]로 데이터 정렬  }    // 배열 B[]를 소스로 사용하여 배열 A []를 정렬합니다.  void TopDownSplitMerge(int B[], int iBegin, int iEnd, int A[])  {  int iMiddle;  if(iEnd - iBegin < 2)                       // 만약 size == 1  return;                                 //   정렬 된 것으로 간주한다.  // 1보다 size가 크면 을 반으로 나눈다.  iMiddle = (iEnd + iBegin) / 2;              // iMiddle = 중간 지점  // 배열 A[]와 B[] 두 배열을 재귀 적으로 정렬  TopDownSplitMerge(A, iBegin,  iMiddle, B);  // 왼쪽 부분 정렬  TopDownSplitMerge(A, iMiddle,    iEnd, B);  // 오른쪽 부분 정렬  // 배열 B[]에서의 Execution Result를 배열 A[]로 병합(합병)  TopDownMerge(B, iBegin, iMiddle, iEnd, A);  }    // 배열의 왼쪽 절반은 B[ iBegin:iMiddle-1].  // 배열의 오른쪽 절반은 B[iMiddle:iEnd-1   ].  // 최종적으로 결과는   A[ iBegin:iEnd-1   ].  void TopDownMerge(int B[], int iBegin, int iMiddle, int iEnd, int A[])  {  i = iBegin, j = iMiddle;    // 왼쪽 또는 오른쪽 부분에 원소가 남아 있을 때까지  for (k = iBegin; k < iEnd; k++) {  // 왼쪽 부분 헤드가 존재하고 그것이 오른쪽 부분 헤드보다 작거나 같은 경우  if (i < iMiddle && (j >= iEnd || B[i] <= B[j])) {  A[k] = B[i];  i = i + 1;  } else {  A[k] = B[j];  j = j + 1;  }  }  }    void CopyArray(int A[], int iBegin, int iEnd, int B[])  {  for(k = iBegin; k < iEnd; k++)  B[k] = A[k];  }    int main() {  int A[] = {9,7,5,3,1,10,2};  int B[sizeof(A)/sizeof(A[0])];    TopDownMergeSort(A, B, sizeof(A)/sizeof(A[0]) );    for(i=0; i<sizeof(A)/sizeof(A[0]); i++)  printf("%d ", A[i]);  } |

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/129/img_2.png)
