---
title: "명품 C++ programming 실습 문제 10장 13번"
date: 2020-03-11T14:46:02+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "map", "programming", "맵", "명품", "실습문제", "연습문제", "컨테이너", "프로그래밍"]
---

<b>문제 :</b>

map 컨테이너를 이용하여 (이름, 성적)을 저장하고 이름으로 성적을 조회하는 점수 관리 프로그램을 만들어라.

이름은 빈칸 없이 입력하는 것을 원칙으로 한다.

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/123/img_1.png)

<b>목적 및 힌트 :</b>

map 컨테이너 활용

이름과 점수를 쌍으로 저장할 맵 컨테이너로 map<string, int>를 이용하면 된다.

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38 | #include<iostream>  #include<string>  #include<map>  using namespace std;    int main() {  map<string, int> Score; // map 컨테이너 생성. 키는 한글 이름, 값은 정수 점수    cout << "\*\*\*\*\* 점수관리 프로그램 HIGH SCORE을 시작합니다 \*\*\*\*\*\n";  while(true){  int num;  int score;  string name;  cout << "입력:1, 조회:2, 종료:3 >> ";  cin >> num;  switch (num){  case 1:  cout << "이름과 점수>> ";  cin >> name >> score;  Score.insert(make\_pair(name, score)); // map에 저장  break;  case 2:  cout << "이름 >> ";  cin >> name;  if(Score.find(name) == Score.end()) // name '키'를 끝까지 찾았는데 없음  cout << "없음" << endl;  else  cout << name << "의 점수는 " <<Score[name] << endl; // Score에서 name의 값을 찾아 출력  break;  case 3:  cout << "프로그램을 종료합니다...\n";  return 0;  default :  cout << "제대로 입력해\n";  break;  }  }  } |

<b>설명 :</b>

map 컨테이너를 사용하기 위해서는 map 헤더파일을 include 해주어야 합니다.

map 컨테이너는 key와 value가 쌍으로 저장되는 컨테이너 입니다.

key는 고유한 값이기 때문에 중복으로 저장될 수 없습니다.

map에 대한 내용은 아래 링크에서 자세히 설명되어 있습니다.

<http://www.cplusplus.com/reference/map/map/>

[map - C++ Reference

difference\_typea signed integral type, identical to: iterator\_traits ::difference\_type usually the same as ptrdiff\_t

www.cplusplus.com](http://www.cplusplus.com/reference/map/map/)
