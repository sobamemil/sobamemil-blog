---
title: "명품 C++ programming 실습 문제 8장 7번"
date: 2020-03-09T14:04:17+09:00
draft: false
categories: ["💻 개발 & CS"]
tags: ["C++", "programming", "RAM", "ROM", "명품", "상속", "실습문제", "연습문제", "프로그래밍"]
---

<b>문제 :</b>

아래와 같은 BaseMemory 클래스를 상속받는 ROM(Read Only Memory), RAM 클래스를 작성하라.

BaseMemory에 필요한 코드를 수정 추가하여 적절히 완성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5 | class BaseMemory{  char \*mem;  protected:  BaseMemory(int size) { mem = new char [size]; }  }; |

ROM은 읽기 전용 메모리이므로 작동 중에 값을 쓸 수가 없기 때문에, 공장에서 생산할 때 생산자가 요청한 데이터로 초기화 하는데 이 작업을 굽는다(burn)라고 한다. 그러므로 ROM은 반드시 생성자에서 burn 작업이 일어나야 한다.

다음은 ROM과 RAM 메모리를 생성하고 사용하는 사례이다.

ROM의 0번지에서 4번지까지 읽어 RAM 메모리의 0~4번지에 쓰고, 다시 RAM 메모리의 값을 화면에 출력한다.

전체 프로그램을 완성하라.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7 | char x[5] = {'h', 'e', 'l', 'l', 'o'};  ROM biosROM(1024\*10, x, 5); // 10KB의 ROM 메모리. 배열 x로 초기화됨  RAM mainMemory(1024\*1024); // 1MB의 ROM 메모리    // 0 번지에서 4번지까지 biosRom에서 읽어 mainMemory에 복사  for(int i=0; i<5; i++) mainMemory.write(i, biosROM.read(i));  for(int i=0; i<5; i++) cout << mainMemory.read(i); |

<b>실행 결과 :</b>

![](https://img.sobamemil.com/posts/108/img_1.png)

<b>목적 및 힌트 :</b>

기본 클래스와 파생 클래스로 나누어 응용 작성

<b>코드 :</b>

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50 | #include<iostream>  using namespace std;    class BaseMemory{  char \*mem;  protected:  BaseMemory(int size) { mem = new char [size]; }  void set\_mem(char \*x){  mem = x;  }  void put\_mem(int i, char copy){  mem[i] = copy;  }  char get\_mem(int i){  return mem[i];  }  };    class ROM : public BaseMemory {  public:  ROM(long int mem\_size, char \*x, int arr\_size) : BaseMemory(mem\_size) {  set\_mem(x);  }  char read(int i){  char mem = get\_mem(i);  return mem;  }  };    class RAM : public BaseMemory {  public:  RAM(int mem\_size) : BaseMemory(mem\_size){;}  void write(int i, char rom\_mem){  put\_mem(i, rom\_mem);  }  char read(int i){  char mem = get\_mem(i);  return mem;  }  };    int main() {  char x[5] = {'h', 'e', 'l', 'l', 'o'};  ROM biosROM(1024\*10, x, 5); // 10KB의 ROM 메모리. 배열 x로 초기화됨  RAM mainMemory(1024\*1024); // 1MB의 ROM 메모리    // 0 번지에서 4번지까지 biosRom에서 읽어 mainMemory에 복사  for(int i=0; i<5; i++) mainMemory.write(i, biosROM.read(i));  for(int i=0; i<5; i++) cout << mainMemory.read(i);  } |


[저작자표시
(새창열림)](https://creativecommons.org/licenses/by/4.0/deed.ko)

#### '[💻 개발 & CS](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS) > [C++ 프로그래밍](/category/%F0%9F%92%BB%20%EA%B0%9C%EB%B0%9C%20%26%20CS/C%2B%2B%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)' 카테고리의 다른 글

|  |  |
| --- | --- |
| [명품 C++ programming 실습 문제 8장 9번](/110)  (4) | 2020.03.09 |
| [명품 C++ programming 실습 문제 8장 8번](/109)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 8장 6번](/107)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 8장 5번](/106)  (1) | 2020.03.09 |
| [명품 C++ programming 실습 문제 8장 4번](/105)  (3) | 2020.03.09 |