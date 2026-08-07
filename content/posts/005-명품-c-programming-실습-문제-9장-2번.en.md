---
title: "명품 C++ programming 실습 문제 9장 2번"
date: 2019-11-20T23:09:20+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["2019", "2020", "converter", "KM", "Mile", "public", "단위변환", "추상클래스", "파생클래스", "프로그래밍"]
---

**문제 :**

다음은 단위를 변환하는 추상 클래스 Converter이다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16 | class Converter {  protected:  double ratio;  virtual double convert(double src)=0; // src를 다른 단위로 변환한다.  virtual string getSourceString()=0; // src 단위 명칭  virtual string getDestString()=0; // dest 단위 명칭  public:  Converter(double ratio) { this->ratio = ratio; }  void run(){  double src;  cout << getSourceString() << "을 " << getDestString() << "로 바꿉니다. ";  cout << getSourceString() << "을 입력하세요>> ";  cin >> src;  cout << "변환 결과 : " << convert(src) << getDestString() << endl;  }  }; |

Converter 클래스를 상속받아 km를 mile(마일)로 변환하는 KmToMile 클래스를 작성하라. main() 함수와 실행 결과는 다음과 같다.

|  |  |
| --- | --- |
| 1  2  3  4 | int main() {  KmToMile toMile(1.609344); // 1마일은 1.609344 KM  toMile.run();  } |

![](https://img.sobamemil.com/posts/5/img_1.png)

**목적 및 힌트 :**

추상 클래스를 상속받는 파생 클래스 만들기

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33 | #include<iostream>  using namespace std;    class Converter {  protected:  double ratio;  virtual double convert(double src)=0; // src를 다른 단위로 변환한다.  virtual string getSourceString()=0; // src 단위 명칭  virtual string getDestString()=0; // dest 단위 명칭  public:  Converter(double ratio) { this->ratio = ratio; }  void run(){  double src;  cout << getSourceString() << "을 " << getDestString() << "로 바꿉니다. ";  cout << getSourceString() << "을 입력하세요>> ";  cin >> src;  cout << "변환 결과 : " << convert(src) << getDestString() << endl;  }  };    class KmToMile : public Converter {  double mile;  public:  KmToMile(double mile) : Converter(mile) { this->mile = mile; }  virtual double convert(double src){ return src/mile; }  virtual string getSourceString(){ return "Km"; }  virtual string getDestString() { return "Mile"; }  };    int main() {  KmToMile toMile(1.609344); // 1마일은 1.609344 KM  toMile.run();  } |


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 9장 6번](/11)  (1) | 2019.11.21 |
| [명품 C++ programming 실습 문제 9장 5번](/10)  (2) | 2019.11.21 |
| [명품 C++ programming 실습 문제 9장 4번](/9)  (3) | 2019.11.21 |
| [명품 C++ programming 실습 문제 9장 3번](/8)  (2) | 2019.11.21 |
| [명품 C++ programming 실습 문제 9장 1번](/4)  (1) | 2019.11.20 |