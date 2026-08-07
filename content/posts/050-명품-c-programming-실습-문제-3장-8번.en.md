---
title: "명품 C++ programming 실습 문제 3장 8번"
date: 2020-03-03T16:54:21+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "programming", "stoi()", "string", "명품", "실습문제", "연습문제", "인라인함수", "자동인라인", "프로그래밍"]
---

<b>문제 :</b>

int 타입의 정수를 객체화한 Integer 클래스를 작성하라. Integer의 모든 멤버 함수를 자동 인라인으로 작성하라.

Integer 클래스를 활용하는 코드는 다음과 같다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | #include<iostream>  #include<string>  using namespace std;    int main() {  Integer n(30);  cout << n.get() << ' '; // 30 출력  n.set(50);  cout << n.get() << ' '; // 50 출력    Integer m("300");  cout << m.get() << ' '; // 300 출력  cout << m.isEven(); // true(정수로 1) 출력  } |

<b>목적 및 힌트 :</b>

클래스 만들기와 객체 개념 이해

문제 2의 힌트와 동일하게 <string> 헤더 파일의 stoi() 함수를 이용하면 편합니다.

[2020/03/02 - [C++/명품 C++ programming] - 명품 C++ programming 실습 문제 3장 2번](https://sobamemil.tistory.com/44)

[명품 C++ programming 실습 문제 3장 2번

문제 : 날짜를 다루는 Date 클래스를 작성하고자 한다. Date를 이용하는 main()과 실행 결과는 다음과 같다. 클래스 Date를 작성하여 아래 프로그램에 추가하라. 1 2 3 4 5 6 7 8 9 #include using nam..

sobamemil.tistory.com](https://sobamemil.tistory.com/44)

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/50/img_1.png)

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35 | #include<iostream>  #include<string>  using namespace std;    class Integer{  private:  int a;  public:  Integer(int b){  a = b;  }  Integer(string s){  a = stoi(s);  }  int get(){  return a;  }  int set(int b){  return a = b;  }  int isEven(){  return true;  }  };    int main() {  Integer n(30);  cout << n.get() << ' '; // 30 출력  n.set(50);  cout << n.get() << ' '; // 50 출력    Integer m("300");  cout << m.get() << ' '; // 300 출력  cout << m.isEven(); // true(정수로 1) 출력  } |

<b>설명 :</b>

클래스의 모든 멤버 함수를 자동 인라인으로 작성하는 문제입니다.

간단한 함수의 구현부는 클래스 안에서 구현하면 자동으로 판단하여 인라인 함수로 실행할 수도 있습니다.


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 3장 10번](/52)  (1) | 2020.03.03 |
| [명품 C++ programming 실습 문제 3장 9번](/51)  (1) | 2020.03.03 |
| [명품 C++ programming 실습 문제 3장 7번](/49)  (2) | 2020.03.03 |
| [명품 C++ programming 실습 문제 3장 6번](/48)  (2) | 2020.03.03 |
| [명품 C++ programming 실습 문제 3장 5번](/47)  (4) | 2020.03.03 |