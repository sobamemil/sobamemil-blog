import os
import glob
import re

POSTS_DIR = "/Users/sobamemil/.gemini/antigravity/scratch/sobamemil-blog/content/posts"

# Comprehensive Korean-to-English dictionary for titles & summaries
TITLE_MAP = {
    "홀짝 구분하기": "Checking Even or Odd",
    "문자열 돌리기": "Rotating String 90 Degrees",
    "문자열 붙여서 출력하기": "Concatenating and Printing Strings",
    "대소문자 바꿔서 출력하기": "Swapping Upper and Lowercase",
    "특수문자 출력하기": "Printing Special Characters",
    "덧셈식 출력하기": "Printing Addition Equation",
    "a와 b 출력하기": "Printing a and b",
    "문자열 출력하기": "Printing a String",
    "문자열 반복해서 출력하기": "Printing Repeated Strings",
    "수어 통역 Application 동작 시연 영상": "Sign Language Interpretation App Demo Video",
    "삽입 정렬(Insertion Sort) 알고리즘": "Insertion Sort Algorithm",
    "합병 정렬(Merge Sort) 알고리즘": "Merge Sort Algorithm",
    "이원 탐색 트리(Binary Search Tree) 배열 만들기": "Binary Search Tree Array Implementation",
    "크러스컬(Kruskal) 알고리즘": "Kruskal's Minimum Spanning Tree Algorithm",
}

SUMMARY_BODY_MAP = [
    (r"자연수 n이 입력으로 주어졌을 때 만약 n이 짝수이면 \"n is even\"을, 홀수이면 \"n is odd\"를 출력하는 코드를 작성해 보세요\.",
     "Given a natural number n, write code to print \"n is even\" if n is even, and \"n is odd\" if n is odd."),
    (r"문자열 str이 주어집니다\. 문자열을 시계방향으로 90도 돌려서 아래 입출력 예와 같이 출력하는 코드를 작성해 보세요\.",
     "Given a string str, write code to rotate it 90 degrees clockwise and print the result."),
    (r"두 개의 문자열 str1, str2가 공백으로 구분되어 입력으로 주어집니다\. 입출력 예와 같이 str1과 str2을 이어서 출력하는 코드를 작성해 보세요\.",
     "Given two space-separated strings str1 and str2, write code to concatenate and print them."),
    (r"영어 알파벳으로 이루어진 문자열 str이 주어집니다\. 각 대소문자를 서로 바꾸어 출력하는 코드를 작성해 보세요\.",
     "Given an alphabetic string str, write code to swap uppercase and lowercase characters."),
    (r"다음과 같이 출력되도록 코드를 작성해 보세요\.", "Write code to print the output as shown below."),
    (r"두 정수 a, b가 주어질 때 다음과 같은 형태의 계산식을 출력하는 코드를 작성해 보세요\.", "Given two integers a and b, write code to print the equation format below."),
    (r"정수 a와 b가 주어집니다\. 두 정수를 출력하는 코드를 작성해 보세요\.", "Given two integers a and b, write code to print their values."),
    (r"문자열 str과 정수 n이 주어집니다\. str이 n번 반복된 문자열을 출력하는 코드를 작성해 보세요\.", "Given a string str and an integer n, write code to print str repeated n times."),
    (r"문자열 str이 주어집니다\. str을 출력하는 코드를 작성해 보세요\.", "Given a string str, write code to print it."),
]

translated_files = 0

for filepath in glob.glob(os.path.join(POSTS_DIR, "*.en.md")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Translate Korean Titles
    title_match = re.search(r'title:\s*"(.*?)"', content)
    if title_match:
        title = title_match.group(1)
        new_title = title

        for ko_t, en_t in TITLE_MAP.items():
            new_title = new_title.replace(ko_t, en_t)

        # Replace remaining Korean title patterns
        new_title = re.sub(r'\[Swift\] (.*) - Programmers Lv\.0 \((\d+)\)', r'[Swift] \1 - Programmers Lv.0 (\2)', new_title)
        
        if new_title != title:
            content = content.replace(f'title: "{title}"', f'title: "{new_title}"')

    # 2. Translate Korean Summaries and Body Text
    for pattern, replacement in SUMMARY_BODY_MAP:
        content = re.sub(pattern, replacement, content)

    if content != original_content:
        translated_files += 1
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"Translated titles & summaries in {translated_files} .en.md files!")
