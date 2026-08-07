---
title: "C++ Programming Ch.10 Exercise 10 Solution"
date: 2020-03-10T18:07:00+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "Capital", "Iterator", "Nation", "programming", "vector", "명품", "실습문제", "연습문제", "프로그래밍"]
---<b>Problem:</b>

나라의 수도 맞추기 게임에 vector를 활용해보자. 나라 이름(nation)과 수도(capital) 문자열로 구성된 Nation 클래스를 만들고, vector<Nation> v;로 생성한 벡터를 이용하여 나라 이름과 수도 이름을 삽입할 수도 있고 랜덤하게 퀴즈를 볼 수도 있다.

프로그램 내에서 벡터에 Nation 객체를 여러 개 미리 삽입하여 퀴즈를 보도록 하라.

실행 화면은 다음과 같으며, 저자는 9개 나라의 이름과 수도를 미리 프로그램에서 삽입하였다.

문자열은 string 클래스를 이용하라.

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/120/img_1.png)

<b>Objective & Hints:</b>

vector에 객체의 삽입, 검색 응용 연습

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88 | #include <iostream>  #include <algorithm>    using namespace std;    class Nation {  string nation;  string capital;  public:  Nation(string n=0, string c=0) {  nation = n;  capital = c;  }  string getNation(){  return nation;  }  string getCapital() {  return capital;  }  bool nationCompare(string n) { //나라 이름을 비교하는 함수.  if(nation == n)  return true;  return false;  }  };    int main() {  vector<Nation> v;  v.push\_back(Nation("대한민국", "서울"));  v.push\_back(Nation("중국", "베이징"));  v.push\_back(Nation("북한", "평양"));  v.push\_back(Nation("미국", "와싱턴"));  v.push\_back(Nation("대만", "타이베이"));  v.push\_back(Nation("캐나다", "오타와"));  v.push\_back(Nation("스위스", "제네바"));  v.push\_back(Nation("프랑스", "파리"));  v.push\_back(Nation("이집트", "카이로"));    cout << "\*\*\*\*\* 나라의 수도 맞추기 게임을 시작합니다. \*\*\*\*\*\n";    while(true){  int num;  cout << "정보 입력: 1, 퀴즈: 2, 종료 3 >> ";  cin >> num;  switch(num){  case 1:  cout << "현재 " << v.size() << "개의 나라가 입력되어 있습니다.\n";  cout << "나라와 수도를 입력하세요(no no 이면 입력끝)\n";  for(int i=v.size()+1;; i++){  string n, c;  bool b;  cout << i << ">>";  cin >> n >> c;  if(n=="no" && c=="no")  break;  for(int j=0; j<v.size(); j++)  if(b=v.at(j).nationCompare(n)){  cout << "already exists !!\n";  i--;  break;  }  if(b)  continue;  v.push\_back(Nation(n, c)); // 정상적인 입력 값이면 vector v에 입력  }  break;    case 2:  int random;  while(true){  string c;  random = rand() % v.size(); // v에 들어있는 원소의 개수보다 작은 숫자를 얻음  cout << v.at(random).getNation() << "의 수도는?";  cin >> c;  if(c == "exit")  break;  else if(v.at(random).getCapital() == c) // 입력받은 수도가 맞으면 Correct 출력  cout << "Correct !!\n";  else  cout << "No !!\n";  }  break;    case 3:  return 0;  }  }  } |

<b>Explanation:</b>

코드가 그렇게 길지 않고 어렵지 않기 때문에 별 다른 함수를 사용하지 않고 main() 함수에서만 작성 하였습니다.
