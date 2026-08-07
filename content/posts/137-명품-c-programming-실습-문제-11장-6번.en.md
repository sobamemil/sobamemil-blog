---
title: "명품 C++ programming 실습 문제 11장 6번"
date: 2020-03-27T15:55:33+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "formatflag", "manipulator", "programming", "명품", "실습문제", "연습문제", "조작자", "포맷플래그", "프로그래밍"]
---

**문제 :**

다음과 같이 정수, 제곱, 제곱근의 값을 형식에 맞추어 출력하는 프로그램을 작성하라.

필드의 간격은 총 15칸이고 제곱근의 유효 숫자는 총 3자리로 한다.

빈칸은 모두 underline(\_) 문자로 삽입한다.

**실행 결과 :**

![](https://img.sobamemil.com/posts/137/img_1.png)

**목적 및 힌트 :**

cout으로 포맷 출력 응용 연습

제곱근을 구하려면 <cmath> 헤더 파일을 include 하고 sqrt(double x) 함수를 호출하면 됩니다.

**코드 :**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25 | #include <iostream>  #include <cmath>  #include <iomanip>  using namespace std;    void showNumber(const double &num){  cout << setw(15) << setfill('\_') << num;  }    void showSqrt(const double &num){  cout << setprecision(3) << setw(15) << setfill('\_') << sqrt(num) << endl;  }    int main() {  cout.setf(ios::left);  cout << setw(15) << "Number";  cout << setw(15) << "Square";  cout << setw(15) << "Square Root" << endl;  for(double i=0; i<=45; i+=5){  cout.precision(4);  showNumber(i); // Number 출력  showNumber(i\*i); // Square 출력  showSqrt(i); // Square Root 출력  }  } |

**설명 :**

포맷 함수와 포맷 플래그, 조작자에 대해 알고 있으면 문제를 푸는데 어려움이 없습니다.

포맷 플래그와 조작자에 대한 내용은 너무 광범위 해 링크로 대체하겠습니다.

포맷 플래그 :

<http://www.cplusplus.com/reference/ios/ios_base/fmtflags/>

[ios\_base::fmtflags - C++ Reference

public member type Type for stream format flags Bitmask type to represent stream format flags. This type is used as its parameter and/or return value by the member functions flags, setf and unsetf. The values passed and retrieved by these

www.cplusplus.com](http://www.cplusplus.com/reference/ios/ios_base/fmtflags/)

조작자 :

<http://www.cplusplus.com/reference/library/manipulators/>

[manipulators - C++ Reference

www.cplusplus.com](http://www.cplusplus.com/reference/library/manipulators/)

**코딩은 내일부터 ;**

[저작자표시 비영리
(새창열림)](https://creativecommons.org/licenses/by-nc/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 11장 8번](/139)  (1) | 2020.04.02 |
| [명품 C++ programming 실습 문제 11장 7번](/138)  (1) | 2020.04.02 |
| [명품 C++ programming 실습 문제 11장 5번](/136)  (3) | 2020.03.27 |
| [명품 C++ programming 실습 문제 11장 4번](/135)  (1) | 2020.03.27 |
| [명품 C++ programming 실습 문제 11장 3번](/134)  (3) | 2020.03.27 |