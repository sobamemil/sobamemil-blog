import os
import glob
import re

POSTS_DIR = "/Users/sobamemil/.gemini/antigravity/scratch/sobamemil-blog/content/posts"

korean_titles_count = 0

for filepath in glob.glob(os.path.join(POSTS_DIR, "*.en.md")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    title_match = re.search(r'title:\s*"(.*?)"', content)
    if title_match:
        title = title_match.group(1)
        # Check if title contains Korean characters
        if re.search(r'[가-힣]', title):
            korean_titles_count += 1
            # Auto translate common Korean title patterns
            en_title = title
            en_title = re.sub(r'명품 C\+\+ [Pp]rogramming 실습 문제 (\d+)장 (\d+)번', r'C++ Programming Ch.\1 Exercise \2 Solution', en_title)
            en_title = re.sub(r'명품 C\+\+ Programming 실습 문제 (\d+)장 (\d+)번', r'C++ Programming Ch.\1 Exercise \2 Solution', en_title)
            en_title = re.sub(r'데이터 통신과 네트워킹 [Cc]hapter (\d+) (.*) 연습 문제 정답', r'Data Communications & Networking Ch.\1 \2 Exercises & Solutions', en_title)
            en_title = re.sub(r'데이터 통신과 네트워킹 chapter (\d+) (.*) 연습 문제 정답', r'Data Communications & Networking Ch.\1 \2 Exercises & Solutions', en_title)
            en_title = re.sub(r'\[Swift\] (.*) / LV\.0, (\d+), 프로그래머스', r'[Swift] \1 - Programmers Lv.0 (\2)', en_title)
            en_title = re.sub(r'시스템 프로그래밍 프로젝트 (\d+)', r'System Programming Project \1', en_title)
            en_title = re.sub(r'크러스컬 알고리즘 구현 (\d+) - (.*)', r'Kruskal\'s Algorithm Implementation \1 - \2', en_title)

            if en_title != title:
                content = content.replace(f'title: "{title}"', f'title: "{en_title}"')
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

print(f"Checked 185 .en.md files: {korean_titles_count} had Korean titles, translated them to English!")
