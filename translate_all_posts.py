import os
import glob
import re

POSTS_DIR = "/Users/sobamemil/.gemini/antigravity/scratch/sobamemil-blog/content/posts"

CATEGORY_MAP = {
    "🏠 스마트홈 & DIY": "🏠 Smart Home & DIY",
    "💻 개발 & CS": "💻 Dev & CS",
    "📱 리뷰 & 일상": "📱 Reviews & Life"
}

TERM_TRANSLATIONS = [
    (r"문제\s*:", "Problem:"),
    (r"입력 파일\s*:", "Input File:"),
    (r"실행 결과\s*:", "Execution Result:"),
    (r"목적 및 힌트\s*:", "Objective & Hints:"),
    (r"코드\s*:", "Code:"),
    (r"소스 코드\s*:", "Source Code:"),
    (r"설명\s*:", "Explanation:"),
    (r"제한사항\s*:", "Constraints:"),
    (r"풀이\s*:", "Solution:"),
    (r"참고문헌\s*:", "References:"),
    (r"연습 문제\s*", "Practice Exercises"),
    (r"정답\s*", "Answers & Solutions"),
    (r"단원\s*", "Chapter "),
    (r"데이터 통신과 네트워킹", "Data Communications & Networking"),
    (r"명품 C\+\+ Programming", "Essential C++ Programming"),
    (r"시스템 프로그래밍", "Systems Programming"),
]

updated_count = 0

for filepath in glob.glob(os.path.join(POSTS_DIR, "*.en.md")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = content.split('---', 2)
    if len(parts) < 3:
        continue

    frontmatter = parts[1]
    body = parts[2]
    original_content = content

    # 1. Update Category Names in Frontmatter
    for ko_cat, en_cat in CATEGORY_MAP.items():
        frontmatter = frontmatter.replace(f'"{ko_cat}"', f'"{en_cat}"')

    # 2. Update Frontmatter Title & Description if Korean
    title_match = re.search(r'title:\s*"(.*?)"', frontmatter)
    if title_match:
        title = title_match.group(1)
        # Translate title terms
        en_title = title
        en_title = re.sub(r'명품 C\+\+ Programming 실습 문제 (\d+)장 (\d+)번', r'C++ Programming Chapter \1 Exercise \2 Solution', en_title)
        en_title = re.sub(r'데이터 통신과 네트워킹 chapter (\d+) (.*) 연습 문제 정답', r'Data Communications & Networking Chapter \1 \2 Practice Exercises & Answers', en_title)
        en_title = re.sub(r'\[Swift\] (.*) / LV\.0, (\d+), 프로그래머스', r'[Swift] \1 - Programmers Lv.0 (\2)', en_title)
        en_title = re.sub(r'\[HA / DIY\] (.*)', r'[Smart Home / DIY] \1', en_title)
        
        frontmatter = frontmatter.replace(f'title: "{title}"', f'title: "{en_title}"')

    # 3. Translate common Korean headers and terms in body
    for pattern, replacement in TERM_TRANSLATIONS:
        body = re.sub(pattern, replacement, body)

    new_content = f"---{frontmatter}---{body}"

    if new_content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_count += 1

print(f"Successfully updated translation structures for {updated_count} English post files (.en.md)!")
