---
title: "C++ Programming Ch.10 Exercise 12 Solution"
date: 2020-03-10T20:28:33+09:00
draft: false
categories: ["Dev CS", "C++ Programming"]
tags: ["C++", "openchallenge", "programming", "vector", "Masterpiece", "Vector", "Practice Problem", "Exercise", "Container", "Programming"]
---

**Problem:**

Open Challenge를 수정하여 사용자가 어휘를 삽입할 수 있도록 기능을 추가하라.

Execution Result는 다음과 같다.

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/122/img_1.png)

<b>Objective & Hints:</b>

vector 컨테이너의 종합 응용 연습

랜덤 정수를 방생시키기 위해 다음 두 라인의 코드가 필요하며, <ctime>과 <cstdlib>를 include 해야 합니다.

|  |  |
| --- | --- |
| 1  2 | srand((unsigned)time(0)); // 시작할 때마다, 다른 랜덤수를 발생시키기 위한 seed 설정  int n = rand(); // 0에서 RAND\_MAX(32767) 사이의 랜덤한 정수가 n에 발생 |

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96  97  98  99  100  101  102  103 | #include <iostream>  #include <vector>  #include <ctime>  #include <cstdlib>  using namespace std;    class Word {  string engWord, korWord;  public:  Word(string engWord=0, string korWord=0){  this->engWord = engWord;  this->korWord = korWord;  }  void inputWord(string engWord, string korWord){  this->engWord = engWord;  this->korWord = korWord;  }  string getEngWord(){ return engWord; }  string getKorWord(){ return korWord; }  };    void inputWord(vector<Word> &v) {  cout << "영어 단어에 exit을 입력하면 입력 끝\n";  string engWord, korWord;    while(true){  cout << "영어 >>"; cin >> engWord;  if(engWord == "exit")  break;  cout << "한글 >>"; cin >> korWord;  v.push\_back(Word(engWord, korWord));  }  }    void gameStart(vector<Word> &v) {  srand((unsigned)time(0));  int num;    cout << "영어 어휘 테스트를 시작합니다. 1~4 외 다른 입력시 종료.\n";    while(true){  int randNum = rand()%v.size();  cout << v.at(randNum).getEngWord() << "?\n";  string ex[4] = " ";  int tmp = rand()%4;  ex[tmp] = v.at(randNum).getKorWord();  for(int i=0; i<4; i++){  if(tmp == i)  continue;  while(true){ // 중복되는 숫자가 없게 처리  int numChosen = rand()%v.size();  if(ex[0]!=v.at(numChosen).getKorWord() && ex[1]!=v.at(numChosen).getKorWord() &&  ex[2]!=v.at(numChosen).getKorWord() && ex[3]!=v.at(numChosen).getKorWord()){  ex[i] = v.at(numChosen).getKorWord();  break;  }  }  }  for(int i=0; i<4; i++)  cout << "(" << i+1 << ") " << ex[i] << ' ';  cout << ":>";  cin >> num; // 숫자만 입력  if(num == -1 || num == 0 || num > 4) { // 입력받은 값이 -1이거나 1~4 외 다른 입력시 종료  break;  }  else {  if(ex[num-1] == v.at(randNum).getKorWord()) // Answers & Solutions이면 실행  cout << "Excellent !!\n";  else  cout << "No. !!\n";  }  }  }    int main() {  int num;    vector<Word> v;  v.push\_back(Word("honey", "애인"));  v.push\_back(Word("dall", "인형"));  v.push\_back(Word("painting", "그림"));  v.push\_back(Word("stock", "주식"));  v.push\_back(Word("bear", "곰"));  v.push\_back(Word("deal", "거래"));    cout << "\*\*\*\*\* 영어 어휘 테스트를 시작합니다. \*\*\*\*\*\n";  while(true){  cout << "어휘 삽입: 1, 어휘 테스트 : 2, 프로그램 종료:그외키 >> ";  cin >> num;  switch(num){  case 1:  inputWord(v);  cout << endl;  break;  case 2:  gameStart(v);  cout << endl;  break;  default:  return 0;  }  }  } |
