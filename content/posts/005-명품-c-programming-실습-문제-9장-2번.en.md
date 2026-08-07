---
title: "C++ Programming Ch.9 Exercise 2 Solution"
date: 2019-11-20T23:09:20+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["2019", "2020", "converter", "KM", "Mile", "public", "단위변환", "추상클래스", "파생클래스", "프로그래밍"]
---<b>Problem:</b>

The following is an abstract class Converter that converts units.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16 | class Converter {  protected:  double ratio;  virtual double convert(double src)=0; // src를 다른 단위로 변환한다.  virtual string getSourceString()=0; // src 단위 명칭  virtual string getDestString()=0; // dest 단위 명칭  public:  Converter(double ratio) { this->ratio = ratio; }  void run(){  double src;  cout << getSourceString() << "을 " << getDestString() << "로 바꿉니다. ";  cout << getSourceString() << "을 입력하세요>> ";  cin >> src;  cout << "변환 결과 : " << convert(src) << getDestString() << endl;  }  }; |

Write a km를 mile(마일)로 변환하는 KmToMile class that inherits from the Converter class. The main() function and execution result are as follows.

|  |  |
| --- | --- |
| 1  2  3  4 | int main() {  KmToMile toMile(1.609344); // 1마일은 1.609344 KM  toMile.run();  } |

![](https://img.sobamemil.com/posts/5/img_1.png)

<b>Objective & Hints:</b>

Creating a derived class that inherits from an abstract class.

<b>Code:</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33 | #include<iostream>  using namespace std;    class Converter {  protected:  double ratio;  virtual double convert(double src)=0; // src를 다른 단위로 변환한다.  virtual string getSourceString()=0; // src 단위 명칭  virtual string getDestString()=0; // dest 단위 명칭  public:  Converter(double ratio) { this->ratio = ratio; }  void run(){  double src;  cout << getSourceString() << "을 " << getDestString() << "로 바꿉니다. ";  cout << getSourceString() << "을 입력하세요>> ";  cin >> src;  cout << "변환 결과 : " << convert(src) << getDestString() << endl;  }  };    class KmToMile : public Converter {  double mile;  public:  KmToMile(double mile) : Converter(mile) { this->mile = mile; }  virtual double convert(double src){ return src/mile; }  virtual string getSourceString(){ return "Km"; }  virtual string getDestString() { return "Mile"; }  };    int main() {  KmToMile toMile(1.609344); // 1마일은 1.609344 KM  toMile.run();  } |
