---
title: "C++ Programming Ch.9 Exercise 10 Solution"
date: 2019-11-26T13:00:11+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C", "C++", "programming", "과제", "링크드 리스트", "명품", "소스코드", "실습문제", "연습문제", "프로그래밍"]
---

<b>Problem:</b>

간단한 그래픽 편집기를 콘솔 바탕으로 만들어보자. 그래픽 편집기의 기능은 "삽입", "삭제", "모두보기", "종료" 의 4가지이고, 실행 과정은 다음과 같다.

![](https://img.sobamemil.com/posts/17/img_1.png)

<b>Objective & Hints:</b>

추상 클래스, 상속 종합 응용

Shape과 이를 상속받은 Circle, Line,Rect 클래스는 [그림9-13]을 이용하고 필요한 클래스와 main() 함수를 작성하라. 전체 프로그램은 대략 아래와 같이 구성된다.

![](https://img.sobamemil.com/posts/17/img_2.png)

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96  97  98  99  100  101  102  103  104  105  106  107  108  109  110  111  112  113  114  115  116  117  118  119  120  121  122  123  124  125  126  127  128  129  130  131  132  133  134  135  136  137  138  139  140  141  142  143  144  145  146  147  148  149  150  151  152  153  154  155  156  157  158  159  160  161  162  163  164  165  166  167  168  169  170  171  172  173  174  175  176  177  178  179  180  181  182  183 | #include<iostream>  #include<stdlib.h>    using namespace std;    class UI {  public:  static int show\_menu() {  int num;  cout << "삽입:1, 삭제:2, 모두보기:3, 종료:4 >>" ;  cin >> num;  return num;  }  static int input\_shape() {  int num;  cout << "선:1, 원:2, 사각형:3 >> ";  cin >> num;  return num;  }  static int del\_index() {  int num;  cout << "삭제하고자 하는 도형의 인덱스 >> ";  cin >> num;  return num;  }  };    class Shape { // Node  Shape\* next;  protected:  virtual void draw() { cout << "--Shape--" << endl; }  public:  Shape() { next = NULL; }  virtual ~Shape() {}  Shape\* add(Shape\* p) {  this->next = p;  return p;  }  Shape\* getNext() { return next; }  void paint() { draw(); }  void setNext(Shape \*p) { this->next = p->next; }  };    class Line : public Shape {  public:  virtual void draw() { cout << "Line" << endl; }  };    class Circle : public Shape {  public:  virtual void draw() { cout << "Circle" << endl; }  };    class Rect : public Shape {  public:  virtual void draw() { cout << "Rectangle" << endl; }  };      class GraphicEditor { // List  int node\_size;  Shape\* pStart;  Shape\* pLast;  public:  GraphicEditor() {  pStart = NULL;  node\_size = 0;  }  int run() {  cout << "그래픽 에디터입니다.\n";  while(true){  int num;  num = UI::show\_menu();  switch (num){  case 1:{  num = UI::input\_shape();  input\_new(num);  break;  }  case 2:{  if(pStart == NULL){  cout << "List Empty\n";  break;  }  num = UI::del\_index();  del(num);  break;  }  case 3:{  show();  break;  }  case 4:{  exit(0);  }  default :  cout << "메뉴를 잘못 선택하셨습니다.\n";  }  }  }  void input\_new(int n) {  switch (n){  case 1: {  if(node\_size == 0) {  pStart = new Line();  pLast = pStart;  }  else  pLast = pLast->add(new Line());  node\_size++;  break;  }  case 2: {  if(node\_size == 0){  pStart = new Circle();  pLast = pStart;  }  else  pLast = pLast->add(new Circle());  node\_size++;  break;  }  case 3: {  if(node\_size == 0){  pStart = new Rect();  pLast = pStart;  }  else  pLast = pLast->add(new Rect());  node\_size++;  break;  }  default :  cout << "메뉴를 잘못 선택하셨습니다.\n";  }    }  bool del(int n) {  int k=0;  Shape\* target\_node = pStart;  Shape\* priv\_node;  if(n == 0){  pStart = pStart->getNext();  delete target\_node;  }  else{  while( (target\_node != NULL) && (k < n)){  priv\_node = target\_node;  target\_node = target\_node->getNext();  k++;  }  if(target\_node == NULL){  cout << "없는 노드입니다.\n";  return false;  }  else {  priv\_node->setNext(target\_node);  delete target\_node;  }  }  node\_size--;    }  void show() {  Shape\* p = pStart;  int i=0;  if(p == NULL)  cout << "List Empty\n";  else  while(p != NULL){  cout << i << ": ";  p->paint();  p = p->getNext();  i++;  }  }  };    int main() {  GraphicEditor\* g\_editor = new GraphicEditor;  g\_editor->run();  delete g\_editor;  } |

<b>Explanation:</b>

전체적인 느낌을 참고만 하시면 될 것 같습니다.
