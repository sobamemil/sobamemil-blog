---
title: "명품 C++ programming 실습 문제 10장 16번"
date: 2020-03-11T17:04:39+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "map", "programming", "STL", "vector", "명품", "실습문제", "연습문제", "컨테이너", "프로그래밍"]
---

**문제 :**

vector<Shape\*> v;를 이용하여 간단한 그래픽 편집기를 콘솔 바탕으로 만들어보자.

생성된 도형 객체를 v에 삽입하고 관리하라. 9장 실습 문제 10번의 힌트를 참고하라.

Shape과 Circle, Line, Rect 클래스는 다음과 같다.

![](https://img.sobamemil.com/posts/126/img_1.png)

[2019/11/26 - [C++/명품 C++ programming] - 명품 C++ programming 실습 문제 9장 10번](https://sobamemil.tistory.com/17)

[명품 C++ programming 실습 문제 9장 10번

문제 : 간단한 그래픽 편집기를 콘솔 바탕으로 만들어보자. 그래픽 편집기의 기능은 "삽입", "삭제", "모두보기", "종료" 의 4가지이고, 실행 과정은 다음과 같다. 목적 및 힌트 : 추상 클래스, 상속 종합 응용 S..

sobamemil.tistory.com](https://sobamemil.tistory.com/17)

**실행 결과 :**

![](https://img.sobamemil.com/posts/126/img_2.png)

**목적 및 힌트 :**

vector를 활용하는 종합 응용

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96  97  98  99  100  101  102  103  104  105  106  107  108  109  110  111  112  113  114 | #include <iostream>  #include <vector>  using namespace std;    class Shape {  protected:  virtual void draw() = 0;  public:  void paint() { draw(); }  };    class Circle : public Shape {  protected:  virtual void draw(){ cout << "Circle" << endl; }  };    class Rect : public Shape {  protected:  virtual void draw() { cout << "Rectangle" << endl; }  };    class Line : public Shape {  protected:  virtual void draw() { cout << "Line" << endl; }  };    class UI {  public:  static int seleteMenu() {  int n;  cout << "삽입:1, 삭제:2, 모두보기:3, 종료:4 >> ";  cin >> n;  return n;  }  static int seleteShape() {  int n;  cout << "선:1, 원:2, 사각형:3 >> ";  cin >> n;  return n;  }  static int seleteDelIndex() {  int n;  cout << "삭제하고자 하는 도형의 인덱스 >> ";  cin >> n;  return n;  }  static void showAll(vector<Shape\*> &v, vector<Shape\*>::iterator &it) {  int i=0;  for(it = v.begin();it!=v.end(); it++, i++){ // vector v의 첫 원소부터 끝 원소까지 탐색 및 출력  cout << i << ": ";  v.at(i)->paint();  }  }  };    class GraphicEditor {  vector<Shape\*> v;  vector<Shape\*>::iterator it;  public:  GraphicEditor() {  cout << "그래픽 에디터입니다.\n";  start();  }  void start() {  while(true){  int n;  n = UI::seleteMenu();  switch(n){  case 1: //삽입을 선택한 경우  n = UI::seleteShape();  switch(n){  case 1: //선을 선택한 경우  v.push\_back(new Line());  break;  case 2: //원을 선택한 경우  v.push\_back(new Circle());  break;  case 3: //사각형을 선택한 경우  v.push\_back(new Rect());  break;  default:  cout << "잘못 선택하셨습니다.\n";  break;  }  break;  case 2:{ //삭제를 선택한 경우  n = UI::seleteDelIndex();  if(n >= v.size() || n < 0){ // 없는 인덱스에 대한 예외처리  cout << "없는 인덱스 입니다.\n";  break;  }  it = v.begin();  Shape\* tmp = \*(it+n); // vector에서 원소가 삭제되고 난 후 객체 delete를 위해 저장  v.erase(it+n); // it+n 위치에 있는 원소 삭제  delete tmp; // vector에서 삭제된 객체 delete  break;  }  case 3: //모두 보기를 선택한 경우  UI::showAll(v, it); //매개변수로 vector v와 v의 iterator를 넘김  break;  case 4: // 종료를 선택한 경우  return; //프로그램 종료  default:  cout << "잘못 입력하셨습니다.\n";  break;  }  }  }    };    int main () {  new GraphicEditor();  } |

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 11장 2번](/133)  (1) | 2020.03.27 |
| [명품 C++ programming 실습 문제 11장 1번](/132)  (1) | 2020.03.27 |
| [명품 C++ programming 실습 문제 10장 15번](/125)  (3) | 2020.03.11 |
| [명품 C++ programming 실습 문제 10장 14번](/124)  (1) | 2020.03.11 |
| [명품 C++ programming 실습 문제 10장 13번](/123)  (1) | 2020.03.11 |