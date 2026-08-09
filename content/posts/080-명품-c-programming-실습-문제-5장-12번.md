---
title: "명품 C++ programming 실습 문제 5장 12번"
date: 2020-03-05T16:24:50+09:00
draft: false
categories: ["💻 개발 & CS", "C++ 프로그래밍"]
tags: ["C++", "programming", "깊은복사생성자", "명품", "실습문제", "실행시간오류", "연습문제", "참조", "참조연산자", "프로그래밍"]
---

**문제 :**

다음은 학과를 나타내는 Dept 클래스와 이를 활용하는 main()을 보여 준다.

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | class Dept {  int size; // scores 배열의 크기  int\* scores; // 동적 할당 받을 정수 배열의 주소  public:  Dept(int size) { // 생성자  this->size = size;  scores = new int[size];  }  Dept(const Dept& dept); // 복사 생성자  ~Dept(); // 소멸자  int getSize() { return size; }  void read(); // size 만큼 키보드에서 정수를 읽어 scores 배열에 저장  bool isOver60(int index); // index의 학생의 성적이 60보다 크면 true 리턴  }; |

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | int countPass(Dept dept) { // dept 학과에 60점 이상으로 통과하는 학생의 수 리턴  int count = 0;  for (int i = 0; i < dept.getSize(); i++) {  if (dept.isOver60(i)) count++;  }  return count;  }    int main() {  Dept com(10); // 총 10명이 있는 학과 com  com.read();  // 총 10명의 학생들의 성적을 키보드로부터 읽어 scores 배열에 저장  int n = countPass(com); // com 학과에 60점 이상으로 통과한 학생의 수를 리턴  cout << "60점 이상은 " << n << "명";  } |

(1) main()의 실행 결과가 다음과 같이 되도록 Dept 클래스에 멤버들을 모두 구현하고, 전체 프로그램을 완성하라.

![](https://img.sobamemil.com/posts/80/img_1.png)

(2) Dept 클래스에 복사 생성자 Dept(const Dept& dept); 가 작성되어 있지 않은 경우, 컴파일은 되지만 프로그램 실행 끝에 실행 시간 오류가 발생한다(복사 생성자를 뺀 채 실행해보라).

위의 코드 어느 부분이 실행될 때 복사 생성자가 호출되는지 설명하고, 복사 생성자가 없으면 왜 실행 오류가 발생하는지 설명하라.

(3) Dept 클래스에 복사 생성자를 제거하라. 복사 생성자가 없는 상황에서도 실행 오류가 발생하지 않게 하려면 어느 부분을 수정하면 될까? 극히 일부분의 수정으로 해결된다.

코드를 수정해보라.

<b>목적 및 힌트 :</b>

C++ 프로그램의 실행 과정과 복사 생성자, 참조 매개 변수에 대한 이해

<b>코드 :</b>

● 문제 (1)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56 | #include<iostream>  using namespace std;    class Dept {  int size; // scores 배열의 크기  int\* scores; // 동적 할당 받을 정수 배열의 주소  public:  Dept(int size) { // 생성자  this->size = size;  scores = new int[size];  }  Dept(Dept& dept); // 복사 생성자  ~Dept(); // 소멸자  int getSize() { return size; }  void read(); // size 만큼 키보드에서 정수를 읽어 scores 배열에 저장  bool isOver60(int index); // index의 학생의 성적이 60보다 크면 true 리턴  };    int countPass(Dept dept) { // dept 학과에 60점 이상으로 통과하는 학생의 수 리턴  int count = 0;  for (int i = 0; i < dept.getSize(); i++) {  if (dept.isOver60(i)) count++;  }  return count;  }    Dept::Dept(Dept& dept) {  this->size = dept.size;  this->scores = new int[this->size];  for (int i=0; i<this->size; i++){  this->scores[i] = dept.scores[i];  }  }  Dept::~Dept() {  delete[] scores;  }    void Dept::read() {  cout << size <<"개 점수 입력>> ";  for (int i = 0; i < size; ++i) {  cin >> scores[i];  }  }  bool Dept::isOver60(int index) {  if (scores[index]>60)  return true;  else  return false;  }    int main() {  Dept com(10); // 총 10명이 있는 학과 com  com.read();  // 총 10명의 학생들의 성적을 키보드로부터 읽어 scores 배열에 저장  int n = countPass(com); // com 학과에 60점 이상으로 통과한 학생의 수를 리턴  cout << "60점 이상은 " << n << "명";  } |

● 문제 (2)

복사 생성자는 main() 함수의 int n = countPass(com); 부분에서 호출이 된다.   
  
Dept 클래스에서 복사 생성자 Dept(const Dept& dept); 가 작성되어 있지 않은 경우 디폴트 복사 생성자가 호출되는데    
이때 기존 클래스 멤버 변수들이 복사된 객체 멤버 변수로 얕은 복사가 되기 때문에 동일한 메모리를 가르키게 되고, 소멸자에 의해 소멸될 때 나중에 생성된 객체가 먼저 메모리를 반환한다.

그리고 먼저 생성된 객체가 그 다음에 소멸되는데 이때 먼저 생성된 객체와 나중에 생성된 객체는 같은 메모리를 가르키고 있으므로 이미 반환한 메모리를 다시 반환하게 된다. 따라서 실행 시간 오류가 발생하고 프로그램이 비정상 종료되기 때문에 동적할당 시에는 깊은 복사를 사용해야 한다.

● 문제 (3)

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48 | #include<iostream>  using namespace std;    class Dept {  int size;  int\* scores;  public:  Dept(int size) {  this->size = size;  scores = new int[size];  }  ~Dept();  int getSize() { return size; }  void read();  bool isOver60(int index);  };    int countPass(Dept& dept) { // 참조에 의한 호출로 변경  int count = 0;  for (int i = 0; i < dept.getSize(); i++) {  if (dept.isOver60(i))  count++;  }  return count;  }    Dept::~Dept() {  delete[] scores;  }  void Dept::read() {  cout << size <<"개 점수 입력>> ";  for (int i = 0; i < size; ++i) {  cin >> scores[i];  }  }  bool Dept::isOver60(int index) {  if (scores[index]>60)  return true;  else  return false;  }    int main() {  Dept com(10);  com.read();  int n = countPass(com);  cout << "60점 이상은 " << n << "명";  } |

<b>설명 :</b>

문제 (3)에서 int countPass(Dept& dept); 처럼 참조 연산자만 추가하여 참조에 의한 호출을 사용하면 복사 생성자를 제거하여도 실행 오류가 발생하지 않게 됩니다.
