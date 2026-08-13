---
title: "삽입 정렬(Insertion Sort) 알고리즘"
date: 2020-03-17T23:05:39+09:00
draft: false
categories: ["개발 CS"]
tags: ["algo", "algorithm", "InsertionSort", "빅오", "삽입정렬", "시간복잡도", "알고리즘", "정렬", "프로그래밍 2019", "프로그래밍 2020"]
---삽입 정렬(Insertion Sort)이란?

자료 배열의 모든 요소를 앞에서부터 차례대로 이미 정렬된 배열 부분과 비교하여, 자신의 위치를 찾아 삽입함으로써 정렬을 완성하는 알고리즘입니다.

삽입 정렬의 시간 복잡도는 O(n2)이며 안정 정렬입니다.

또한 배열이 길어질수록 효율이 매우 떨어지지만 구현이 간단하다는 장점이 있습니다.

![](https://img.sobamemil.com/posts/127/img_1.png)

삽입 정렬의 예

![](https://img.sobamemil.com/posts/127/img_2.gif)

삽입 정렬의 애니메이션       -Simpsons contributor-

삽입 정렬 알고리즘을 구현하기 전에 의사코드(Pseudocode)로 먼저 이해를 하고 코드를 작성하는 것이 더 쉽게 작성할 수 있을 것입니다.

<b>Pseudocode :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | //InsertionSort pseudo code  InsertionSort(A,n) // sort A[1...n]  for j <- 2 to n  do key <- A[j]  i <- j-1  while i>0 and A[i]>key  do A[i+1] <- A[i]  i <- i-1  A[i+1] <- key |

<b>C</b><b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33 | #include <stdio.h>    // 삽입 정렬 (insertion sort)  void InsertionSort(int \*source, int size){  int i, j, keyValue;  for(i=1; i<size; i++){ // 처음에 1번 index의 원소가 key값이 됨  keyValue = source[(j=i)]; // i가 1씩 증가하며 source[(j=i)]를 key값으로 지정    // j는 i보다 하나 작게 설정.  // j가 i-1부터 0까지 역순으로 내려감  // key값이 source[j]보다 더 크면 중단  while ( --j >= 0 && keyValue < source[j] )  source[j+1] = source[j]; // source[j]를 source[j+1]로 밀어냄    source[j+1] = keyValue; // 알맞은 자리에 key값을 삽입  }  }    int main() {  int intArray[] = {2, 9, 8, 4, 5, 3, 1}; // 정렬할 int 배열  int i;    printf("정렬 전 배열 : ");  for(i=0; i<sizeof(intArray)/sizeof(intArray[0]); i++) // 정렬 전 배열 원소 출력  printf("%d ", intArray[i]);    InsertionSort(intArray, sizeof(intArray)/sizeof(intArray[0])); // 삽입 정렬 함수에 배열과 원소의 개수를 넘겨줌    printf("\n정렬 후 배열 : ");  for(i=0; i<sizeof(intArray)/sizeof(intArray[0]); i++) // 정렬 후 배열 원소 출력  printf("%d ", intArray[i]);  return 0;  } |

<b>JAVA 코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34 | public class insertionSort {    // 삽입 정렬 (Insertion Sort)  static void InsertionSort(int[] source)  {  int j, i, keyValue;  for(i = 1 ; i < source.length ; i++){ // source의 두번째 원소부터 key 값으로 지정  keyValue = source[(j=i)]; // i가 1씩 증가하며 source[(j=i)]를 key값으로 지정    // j는 i보다 하나 작게 설정.  // j가 i-1부터 0까지 역순으로 내려감  // key값이 source[j]보다 더 크면 중단  while( (--j >= 0) && ( source[j] > keyValue ) )  source[j+1] = source[j]; // source[j]를 source[j+1]로 밀어냄  source[j + 1] = keyValue; // 알맞은 자리에 key값을 삽입  }  }    public static void main(String[] args) {  int[] intArray = {2, 9, 8, 4, 5, 3, 1};    // 정렬 전 배열 출력  System.out.print("정렬 전 배열 : ");  for(int i=0; i<intArray.length; i++)  System.out.print(intArray[i] + " ");    InsertionSort(intArray); // 삽입 정렬 함수 호출    // 정렬 후 배열 출력  System.out.print("\n정렬 후 배열 : ");  for(int i=0; i<intArray.length; i++)  System.out.print(intArray[i] + " ");  }  } |

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/127/img_3.png)
