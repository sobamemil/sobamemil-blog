---
title: "C++ Programming Ch.9 Exercise 1 Solution"
date: 2019-11-20T22:55:26+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C", "C++", "programming", "명품", "소스코드", "실습문제", "실행결과", "연습문제", "프로그래밍"]
---<b>Problem:</b>

The following is an abstract class Converter that converts units.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19 | #include<iostream>  using namespace std;    class Converter {  protected:  double ratio;  virtual double convert(double src)=0; // src를 다른 단위로 변환한다.  virtual string getSourceString()=0; // src 단위 명칭  virtual string getDestString()=0; // dest 단위 명칭  public:  Converter(double ratio) { this->ratio = ratio; }  void run(){  double src;  cout << getSourceString() << "을 " << getDestString() << "로 바꿉니다. ";  cout << getSourceString() << "을 입력하세요>> ";  cin >> src;  cout << "변환 결과 : " << convert(src) << getDestString() << endl;  }  };   |

Write a 달러를 원화로 환산하는 WonToDollar class that inherits from the Converter class. The main() function and execution result are as follows.

|  |  |
| --- | --- |
| 1  2  3  4 | int main() {  WonToDollar wd(1010); // 1달러에 1010원  wd.run();  }   |

![](https://img.sobamemil.com/posts/4/img_1.png)

<b>Objective & Hints:</b>

Creating a derived class that inherits from an abstract class.

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39 | #include<iostream>  using namespace std;    class Converter {  protected:  double ratio;  virtual double convert(double src)=0; // src를 다른 단위로 변환한다.  virtual string getSourceString()=0; // src 단위 명칭  virtual string getDestString()=0; // dest 단위 명칭  public:  Converter(double ratio) { this->ratio = ratio; }  void run(){  double src;  cout << getSourceString() << "을 " << getDestString() << "로 바꿉니다. ";  cout << getSourceString() << "을 입력하세요>> ";  cin >> src;  cout << "변환 결과 : " << convert(src) << getDestString() << endl;  }  };    class WonToDollar : public Converter { // Converter class 상속  int won;  public:  WonToDollar(int won) : Converter(won) { this->won = won; } // 매개변수가 있는 Converter 생성자 호출  double convert(double src){  return src/won;  }  virtual string getSourceString(){  return "원";  }  virtual string getDestString(){  return "달러";  }  };    int main() {  WonToDollar wd(1010); // 1달러에 1010원  wd.run();  } |
