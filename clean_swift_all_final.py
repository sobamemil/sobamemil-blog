import os
import glob
import re

POSTS_DIR = "/Users/sobamemil/.gemini/antigravity/scratch/sobamemil-blog/content/posts"

for filepath in glob.glob(os.path.join(POSTS_DIR, "*swift*.en.md")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove Programmers card text blocks
    content = re.sub(r'\[프로그래머스[\s\S]*?programmers\.co\.kr\]\(.*?\)', '', content)
    content = re.sub(r'Ternary operator\(삼항 연산자\) 사용해서 문제를 해결 하였습니다\. 입련된 수를 2로 나눈 나머지가 0인지 확인하여 짝수인지 확인할 수 있습니다\.',
                     'I solved this problem using a ternary operator. By checking if the remainder when divided by 2 is 0, we can determine whether the number is even.', content)
    content = re.sub(r'\]\(\s*\)', '', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Final Swift post cleanup complete!")
