import os
import glob
import re

POSTS_DIR = "/Users/sobamemil/.gemini/antigravity/scratch/sobamemil-blog/content/posts"

SWIFT_BODY_TRANSLATIONS = [
    # Problem 181944 (Even / Odd)
    ("자연수 n이 입력으로 주어졌을 때 만약 n이 짝수이면 \"n is even\"을, 홀수이면 \"n is odd\"를 출력하는 코드를 작성해 보세요.",
     "Given a natural number n, write code to output \"n is even\" if n is even, and \"n is odd\" if n is odd."),
    ("Ternary operator\\(삼항 연산자\\) 사용해서 문제를 해결 하였습니다. 입련된 수를 2로 나눈 나머지가 0인지 확인하여 짝수인지 확인할 수 있습니다.",
     "I solved this problem using a ternary operator. By checking if the remainder when divided by 2 is 0, we can determine whether the number is even."),
    ("이런 식으로 isMultiple\\(of:\\) 함수를 사용해서 홀짝을 판별할 수도 있습니다.",
     "Alternatively, you can also determine even/odd status using Swift's `isMultiple(of:)` function as shown above."),

    # Problem 181945 (Rotate string)
    ("문자열 str이 주어집니다. 문자열을 시계방향으로 90도 돌려서 아래 입출력 예와 같이 출력하는 코드를 작성해 보세요.",
     "Given a string str, write code to rotate it 90 degrees clockwise and print the result as shown below."),

    # Problem 181946 (Concatenate string)
    ("두 개의 문자열 str1, str2가 공백으로 구분되어 입력으로 주어집니다. 입출력 예와 같이 str1과 str2을 이어서 출력하는 코드를 작성해 보세요.",
     "Given two space-separated strings str1 and str2, write code to concatenate and print them."),

    # Problem 181949 (Swap case)
    ("영어 알파벳으로 이루어진 문자열 str이 주어집니다. 각 대소문자를 서로 바꾸어 출력하는 코드를 작성해 보세요.",
     "Given an alphabetic string str, write code to swap uppercase and lowercase characters."),

    # Problem 181948 (Special characters)
    ("다음과 같이 출력되도록 코드를 작성해 보세요.", "Write code to produce the output shown below."),

    # Problem 181947 (Addition equation)
    ("두 정수 a, b가 주어질 때 다음과 같은 형태의 계산식을 출력하는 코드를 작성해 보세요.",
     "Given two integers a and b, write code to print the equation format below."),

    # Problem 181951 (Print a and b)
    ("정수 a와 b가 주어집니다. 두 정수를 출력하는 코드를 작성해 보세요.", "Given two integers a and b, write code to print their values."),

    # Problem 181950 (Repeat string)
    ("문자열 str과 정수 n이 주어집니다. str이 n번 반복된 문자열을 출력하는 코드를 작성해 보세요.",
     "Given a string str and an integer n, write code to print str repeated n times."),

    # Problem 181952 (Print string)
    ("문자열 str이 주어집니다. str을 출력하는 코드를 작성해 보세요.", "Given a string str, write code to print it."),

    # Remove Programmers card boilerplate text
    (r"\[프로그래머스\s+코드 중심의 개발자 채용.*?programmers\.co\.kr\]\(https://school\.programmers\.co\.kr/learn/courses/30/lessons/\d+\)", ""),
]

translated_count = 0

for filepath in glob.glob(os.path.join(POSTS_DIR, "*.en.md")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    # Replace Non-Breaking Spaces (\u00a0) with normal spaces
    content = content.replace('\u00a0', ' ')

    for pattern, replacement in SWIFT_BODY_TRANSLATIONS:
        content = re.sub(pattern, replacement, content)

    # Clean up empty bracket artifacts
    content = re.sub(r'\]\(\s*\)', '', content)

    if content != original_content:
        translated_count += 1
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"Deep translated Swift post bodies and summaries in {translated_count} files!")
