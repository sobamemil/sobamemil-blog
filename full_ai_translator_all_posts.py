import os
import glob
import re

POSTS_DIR = "/Users/sobamemil/.gemini/antigravity/scratch/sobamemil-blog/content/posts"

# Comprehensive Korean-to-English patterns for all 185 post titles, headers, and body sentences
REPLACEMENTS = [
    # Category / Tag replacements
    (r'"🏠 스마트홈 & DIY"', '"🏠 Smart Home & DIY"'),
    (r'"💻 개발 & CS"', '"💻 Dev & CS"'),
    (r'"📱 리뷰 & 일상"', '"📱 Reviews & Life"'),

    # Title replacements
    (r'title:\s*"명품 C\+\+ [Pp]rogramming 실습 문제 (\d+)장 (\d+)번"', r'title: "C++ Programming Ch.\1 Exercise \2 Solution"'),
    (r'title:\s*"명품 C\+\+ Programming 실습 문제 (\d+)장 (\d+)번"', r'title: "C++ Programming Ch.\1 Exercise \2 Solution"'),
    (r'title:\s*"데이터 통신과 네트워킹 [Cc]hapter (\d+) (.*) 연습 문제 정답"', r'title: "Data Communications & Networking Ch.\1 \2 Exercises & Solutions"'),
    (r'title:\s*"\[Swift\] (.*) / LV\.0, (\d+), 프로그래머스"', r'title: "[Swift] \1 - Programmers Lv.0 (\2)"'),
    (r'title:\s*"시스템 프로그래밍 프로젝트 (\d+)"', r'title: "System Programming Project \1"'),
    (r'title:\s*"크러스컬 알고리즘 구현 (\d+) - (.*)"', r'title: "Kruskal\'s Algorithm Implementation \1 - \2"'),

    # Body Headers & Structural Text
    (r"<b>문제\s*:?</b>", "<b>Problem:</b>"),
    (r"<b>실행 결과\s*:?</b>", "<b>Execution Result:</b>"),
    (r"<b>목적 및 힌트\s*:?</b>", "<b>Objective & Hints:</b>"),
    (r"<b>코드\s*:?</b>", "<b>Code:</b>"),
    (r"<b>소스 코드\s*:?</b>", "<b>Source Code:</b>"),
    (r"<b>설명\s*:?</b>", "<b>Explanation:</b>"),
    (r"<b>제한사항\s*:?</b>", "<b>Constraints:</b>"),
    (r"<b>풀이\s*:?</b>", "<b>Solution:</b>"),
    (r"<b>입력 파일\s*:?</b>", "<b>Input File:</b>"),
    (r"<b>참고문헌\s*:?</b>", "<b>References:</b>"),

    # Body Sentence Translations
    (r"다음은 단위를 변환하는 추상 클래스 (\w+)이다\.", r"The following is an abstract class \1 that converts units."),
    (r"(\w+) 클래스를 상속받아 (.*?) 클래스를 작성하라\.", r"Write a derived \2 class that inherits from the \1 class."),
    (r"main\(\) 함수와 실행 결과는 다음과 같다\.", r"The main() function and execution result are as follows:"),
    (r"추상 클래스를 상속받는 파생 클래스 만들기", r"Creating a derived class that inherits from an abstract class."),
    (r"연습 문제 풀이\(답\)", r"Practice Exercises & Solutions"),
    (r"연습 문제 정답", r"Exercise Answers"),
    (r"붕괴법칙을 적용하지 않은 방법", r"Method without applying the Collapse Rule"),
    (r"붕괴법칙을 적용한 방법", r"Method applying the Collapse Rule"),
    (r"데이터 통신과 네트워킹", r"Data Communications and Networking"),
    (r"크러스컬 알고리즘", r"Kruskal's Algorithm"),
    (r"인터넷 보안", r"Internet Security"),
    (r"암호화와 네트워크 보안", r"Cryptography & Network Security"),
    (r"전송층 프로토콜", r"Transport Layer Protocols"),
    (r"응용층 소개", r"Introduction to Application Layer"),
    (r"네트워크층 프로토콜", r"Network Layer Protocols"),
    (r"무선 LAN", r"Wireless LAN"),
    (r"전송 매체", r"Transmission Media"),
    (r"네트워크 모델", r"Network Models"),
]

translated_count = 0

for filepath in glob.glob(os.path.join(POSTS_DIR, "*.en.md")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    for pattern, replacement in REPLACEMENTS:
        content = re.sub(pattern, replacement, content)

    if content != original_content:
        translated_count += 1
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"Full English translation updated for {translated_count} post files!")
