---
title: "명품 C++ programming 실습 문제 4장 12번"
date: 2020-03-04T17:34:53+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "circle", "CircleManager", "programming", "객체배열", "객체포인터", "명품", "실습문제", "연습문제", "프로그래밍"]
---

**문제 :**

다음은 이름과 반지름을 속성으로 가진 Circle 클래스와 이들을 배열로 관리하는 CircleManager 클래스이다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8 | class Circle{  int radius; // 원의 반지름 값  string name; // 원의 이름  public:  void setCircle(string name, int radius); // 이름과 반지름 설정  double getArea();  string getName();  }; |

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | class CircleManager {  Circle \*p; // Circle 배열에 대한 포인터  int size; // 배열의 크기  public:  CircleManager(int size); // size 크기의 배열을 동적 생성. 사용자로부터 입력 완료  ~CircleManager();  void searchByName(); // 사용자로부터 원의 이름을 입력받아 면적 출력  void searchByArea(); // 사용자로부터 면적을 입력받아 면적보다 큰 원의 이름 출력  }; |

키보드에서 원의 개수를 입력받고, 그 개수만큼 원의 이름과 반지름을 입력받고, 다음과 같이 실행되도록 main() 함수를 작성하라.

Circle, CircleManager 클래스도 완성하라.

**목적 및 힌트 :**

객체의 동적 생성 및 소멸 응용

**실행 결과 :**

![](https://img.sobamemil.com/posts/66/img_1.png)

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82 | #include<iostream>  #include<string>  using namespace std;    class Circle{  int radius; // 원의 반지름 값  string name; // 원의 이름  public:  void setCircle(string name, int radius); // 이름과 반지름 설정  double getArea();  string getName();  };    class CircleManager {  Circle \*p; // Circle 배열에 대한 포인터  int size; // 배열의 크기  int radius;  string name;  public:  CircleManager(int size); // size 크기의 배열을 동적 생성. 사용자로부터 입력 완료  ~CircleManager();  void searchByName(); // 사용자로부터 원의 이름을 입력받아 면적 출력  void searchByArea(); // 사용자로부터 면적을 입력받아 면적보다 큰 원의 이름 출력  };    void Circle::setCircle(string name, int radius){  this->name = name;  this->radius = radius;  }    double Circle::getArea(){  return radius \* radius \* 3.14;  }    string Circle::getName(){  return name;  }    CircleManager::CircleManager(int size){  p = new Circle[size];  this->size = size;  for(int i=0; i<size; i++){  cout << "원 " << i+1 << "의 이름과 반지름 >> ";  cin >> name >> radius;  p[i].setCircle(name,radius);  }  }    CircleManager::~CircleManager(){  delete [] p;  }    void CircleManager::searchByName(){  cout << "검색하고자 하는 원의 이름 >> ";  cin >> name;  for(int i=0; i<size; i++){  if(name == p[i].getName()){  cout << name << "의 면적은 " << p[i].getArea() << endl;  }  }  }    void CircleManager::searchByArea(){  cout << "최소 면적을 정수로 입력하세요 >> ";  cin >> radius;  cout << radius << "보다 큰 원을 검색합니다.\n";  for(int i=0; i<size; i++){  if(radius<p[i].getArea()){  cout << p[i].getName() << "의 면적은 " << p[i].getArea() <<",";  }  }  }    int main() {  int size;  cout << "원의 개수 >> ";  cin >> size;  CircleManager CM(size);  CM.searchByName();  CM.searchByArea();    } |

**코딩은 내일부터 ;**

[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 4장 14번](/68)  (1) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 13번](/67)  (3) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 11번](/65)  (3) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 10번](/64)  (1) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 9번](/63)  (2) | 2020.03.04 |