---
title: "Kruskal's Minimum Spanning Tree Algorithm"
date: 2020-07-02T18:03:16+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["Greedy", "Kruskal", "MST", "가중치", "그래프", "알고리즘", "욕심쟁이방법", "크러스컬", "탐욕법"]
---

**크러스컬(Kruskal) 알고리즘이란?**

Kruskal's Algorithm은 최소 비용 신장 그래프를 찾는 알고리즘 입니다.

변의 개수를 E, 꼭지점의 개수를 V라고 한다면 Kruskal's Algorithm은 O(ElogV)의 시간 복잡도를 갖습니다.

<b>크러스컬의 MST(욕심쟁이 방법) 알고리즘 간략 Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15 | edge\_set kruskal\_MST(edge\_set E, int n) {  sort(E); // 간선 정렬  edge\_set MST\_E = { };  for (i=0; i<n; i++) init\_set(i); // n개의 집합(트리)을 생성  while(MST\_E의 간선 수 < n - 1) {  (u, v) = E의 최소 가중치 간선;  E = E - {(u, v)};  if(find(u) != find(v)) // u와 v가 다른 집합(트리) 원소  {  MST\_E = MST\_E ∪ {(u, v)}; // 간선 추가  union(u, v); // 두 집합(트리)을 합병  }  }  return MST\_E;  } |

<b>- 예제 -</b>

<b>입력으로 받을 그래프 :</b>

![](https://img.sobamemil.com/posts/150/img_1.png)

가중치 그래프

<b>실행 예 :</b>

![](https://img.sobamemil.com/posts/150/img_2.png)

실행 예

<b>구조 :</b>

Kruskal's Algorithm을 구현하기 위해서는 크게 세 가지 중요한 부분이 있습니다.

첫 번째로 최초에 정점 하나를 원소로 하는 집합을 만드는 init set 연산

두 번째로 임의의 정점이 어느 집합의 원소인지를 알아내는 find 연산

마지막으로 두 집합을 하나로 합치는 union 연산

이 알고리즘에서는 2번 줄에 간선을 정렬하는 부분이 전체 알고리즘의 복잡도를 좌우하게 되는데, 주어진 그래프의 정점의 수가 n이고 간선의 수가 e이라고 할 때, 정렬 방법 중 성능이 우수한 퀵정렬, 합병정렬 등을 사용한다면 O(e loge)의 시간 복잡도를 갖습니다.

위쪽에서 변의 개수를 E, 꼭지점의 개수를 V라고 한다면 Kruskal's Algorithm은 O(ElogV)의 시간 복잡도를 갖는다고 하였는데, 그 이유는 간선의 수 e는 최대 O(n^2) 이므로 O(e loge) = O(e logn^2) = O(2e logn) = O(e logn) 가 성립하므로 둘 중 어떠한 복잡도로 말해도 틀린 것이 아니기 때문입니다.

Kruskal's Algorithm에 대한 실제 구현 예제는 아래 링크에서 볼 수 있습니다.

[2021.04.09 - [알고리즘] - Kruskal's Algorithm 구현 1 (Method without applying the Collapse Rule)](https://sobamemil.tistory.com/180)
