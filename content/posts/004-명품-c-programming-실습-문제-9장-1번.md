---
title: "명품 C++ programming 실습 문제 9장 1번"
date: 2019-11-20T22:55:26+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C", "C++", "programming", "명품", "소스코드", "실습문제", "실행결과", "연습문제", "프로그래밍"]
---

**문제:**

다음은 단위를 변환하는 추상 클래스 Converter이다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19 | #include<iostream>  using namespace std;    class Converter {  protected:  double ratio;  virtual double convert(double src)=0; // src를 다른 단위로 변환한다.  virtual string getSourceString()=0; // src 단위 명칭  virtual string getDestString()=0; // dest 단위 명칭  public:  Converter(double ratio) { this->ratio = ratio; }  void run(){  double src;  cout << getSourceString() << "을 " << getDestString() << "로 바꿉니다. ";  cout << getSourceString() << "을 입력하세요>> ";  cin >> src;  cout << "변환 결과 : " << convert(src) << getDestString() << endl;  }  };  [Colored by Color Scripter](http://colorscripter.com/info#e) |

Converter 클래스를 상속받아 달러를 원화로 환산하는 WonToDollar 클래스를 작성하라. main() 함수와 실행 결과는 다음과 같다.

|  |  |
| --- | --- |
| 1  2  3  4 | int main() {  WonToDollar wd(1010); // 1달러에 1010원  wd.run();  }  [Colored by Color Scripter](http://colorscripter.com/info#e) |

![](https://img.sobamemil.com/posts/4/img_1.png)

**목적 및 힌트:**

추상 클래스를 상속받는 파생 클래스 만들기

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39 | #include<iostream>  using namespace std;    class Converter {  protected:  double ratio;  virtual double convert(double src)=0; // src를 다른 단위로 변환한다.  virtual string getSourceString()=0; // src 단위 명칭  virtual string getDestString()=0; // dest 단위 명칭  public:  Converter(double ratio) { this->ratio = ratio; }  void run(){  double src;  cout << getSourceString() << "을 " << getDestString() << "로 바꿉니다. ";  cout << getSourceString() << "을 입력하세요>> ";  cin >> src;  cout << "변환 결과 : " << convert(src) << getDestString() << endl;  }  };    class WonToDollar : public Converter { // Converter class 상속  int won;  public:  WonToDollar(int won) : Converter(won) { this->won = won; } // 매개변수가 있는 Converter 생성자 호출  double convert(double src){  return src/won;  }  virtual string getSourceString(){  return "원";  }  virtual string getDestString(){  return "달러";  }  };    int main() {  WonToDollar wd(1010); // 1달러에 1010원  wd.run();  } |


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 9장 6번](/11)  (1) | 2019.11.21 |
| [명품 C++ programming 실습 문제 9장 5번](/10)  (2) | 2019.11.21 |
| [명품 C++ programming 실습 문제 9장 4번](/9)  (3) | 2019.11.21 |
| [명품 C++ programming 실습 문제 9장 3번](/8)  (2) | 2019.11.21 |
| [명품 C++ programming 실습 문제 9장 2번](/5)  (2) | 2019.11.20 |