---
title: "명품 C++ programming 실습 문제 3장 12번"
date: 2020-03-03T19:03:06+09:00
draft: false
categories: ["💻 Dev & CS"]
tags: ["C++", "CPP", "programming", "구현부", "명품", "선언부", "실습문제", "연습문제", "코딩", "프로그래밍"]
---

<b>Problem:</b>

컴퓨터의 주기억장치를 모델링하는 클래스의 Ram을 구현하려고 한다.

Ram 클래스는 데이터가 기록될 메모리 공간과 크기 정보를 가지고, 주어진 주소에 데이터를 기록하고(write), 주어진 주소로부터 데이터를 읽어 온다(read).

Ram 클래스는 다음과 같이 선언된다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | class Ram {  char mem[100 \* 1024]; // 100KB 메모리. 한 번지는 한 바이트이므로 char 타입 사용  int size;  public:  Ram(); // mem 배열을 0으로 초기화하고 size를 100\*1024로 초기화  ~Ram(); // "메모리 제거됨" 문자열 출력  char read(int address);    // address 주소의 메모리 바이트 리턴  void write(int address, char value); // address 주소에 한 바이트로 value 저장  }; |

다음 main() 함수는 100 번지에 20을 저장하고, 101 번지에 30을 저장한 후, 100 번지와 101 번지의 값을 읽고 더하여 102 번지에 저장하는 코드이다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8 | int main() {  Ram ram;  ram.write(100, 20); // 100 번지에 20 저장  ram.write(101, 30); // 101 번지에 30 저장  char res = ram.read(100) + ram.read(101); // 20 + 30 = 50  ram.write(102, res); // 102 번지에 50 저장  cout << "102 번지의 값 = " << (int)ram.read(102) << endl; // 102 번지 값 출력  } |

<b>Objective & Hints:</b>

실세계 객체를 클래스로 코딩하는 연습

<b>Execution Result:</b>

![](https://img.sobamemil.com/posts/54/img_1.png)

실행 결과를 참고하여 Ram.h, Ram.cpp, main.cpp로 헤더 파일과 cpp 파일을 분리하여 프로그램을 완성하라.

<b>Code:</b>

● Ram.h

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | class Ram {  char mem[100 \* 1024]; // 100KB 메모리. 한 번지는 한 바이트이므로 char 타입 사용  int size;  public:  Ram(); // mem 배열을 0으로 초기화하고 size를 100\*1024로 초기화  ~Ram(); // "메모리 제거됨" 문자열 출력  char read(int address);    // address 주소의 메모리 바이트 리턴  void write(int address, char value); // address 주소에 한 바이트로 value 저장  }; |

● Ram.cpp

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20 | #include<iostream>  #include<memory.h>  using namespace std;    #include "Ram.h"    Ram::Ram(){  size = 100 \* 1024;  for (int i = 0; i < size; ++i)  mem[i] = 0;  }  Ram::~Ram(){  cout << "메모리 제거됨";  }  char Ram::read(int address){  return mem[address];  }  void Ram::write(int address, char value){  mem[address] = value;  } |

● main.cpp

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13 | #include<iostream>  using namespace std;    #include "Ram.h"    int main() {  Ram ram;  ram.write(100, 20); // 100 번지에 20 저장  ram.write(101, 30); // 101 번지에 30 저장  char res = ram.read(100) + ram.read(101); // 20 + 30 = 50  ram.write(102, res); // 102 번지에 50 저장  cout << "102 번지의 값 = " << (int)ram.read(102) << endl; // 102 번지 값 출력  } |

<b>Explanation:</b>

주어진 main() 함수와 Ram 클래스의 선언부를 참고하여 Ram 클래스 멤버에 대한 구현부를 작성하는 문제입니다.


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 4장 2번](/56)  (1) | 2020.03.04 |
| [명품 C++ programming 실습 문제 4장 1번](/55)  (1) | 2020.03.04 |
| [명품 C++ programming 실습 문제 3장 11번](/53)  (1) | 2020.03.03 |
| [명품 C++ programming 실습 문제 3장 10번](/52)  (1) | 2020.03.03 |
| [명품 C++ programming 실습 문제 3장 9번](/51)  (1) | 2020.03.03 |