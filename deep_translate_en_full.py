import os
import glob
import re

POSTS_DIR = "/Users/sobamemil/.gemini/antigravity/scratch/sobamemil-blog/content/posts"

# Clean out Tistory footer blocks from ALL post files (.md and .en.md)
def clean_tistory_footers(content):
    # Remove Tistory category footer block
    content = re.sub(r'####\s*\'\[.*?\].*?카테고리의 다른 글[\s\S]*$', '', content)
    content = re.sub(r'\[저작자표시\s*\(새창열림\)\]\(https://creativecommons\.org/licenses/by/4\.0/deed\.ko\)', '', content)
    content = re.sub(r'\[Colored by Color Scripter\]\(http://colorscripter\.com/info#e\)', '', content)
    return content.strip() + '\n'

# Translation dictionary for common Korean sentences in programming / tech posts
SENTENCE_TRANSLATIONS = [
    (r"다음은 단위를 변환하는 추상 클래스 (\w+)이다\.", r"The following is an abstract class \1 that converts units."),
    (r"(\w+) 클래스를 상속받아 (.*?) 클래스를 작성하라\.", r"Write a \2 class that inherits from the \1 class."),
    (r"main\(\) 함수와 실행 결과는 다음과 같다\.", r"The main() function and execution result are as follows."),
    (r"추상 클래스를 상속받는 파생 클래스 만들기", r"Creating a derived class that inherits from an abstract class."),
    (r"C\+\+ 프로그래밍", r"C++ Programming"),
    (r"실습 문제", r"Exercise Problem"),
    (r"실행 결과", r"Execution Result"),
    (r"소스 코드", r"Source Code"),
    (r"설명", r"Explanation"),
    (r"풀이", r"Solution"),
    (r"제한사항", r"Constraints"),
    (r"문제 설명", r"Problem Description"),
    (r"입력 예시", r"Input Example"),
    (r"출력 예시", r"Output Example"),
    (r"부모님 댁에 보관되어 있던 애터미 공기청정기를 집으로 가져왔습니다\.", r"I brought home the Atomy air purifier that was stored at my parents' house."),
    (r"스마트홈에 붙여서 자동화로 활용해 보려고 했습니다\.", r"I tried integrating it into my smart home setup for automation."),
    (r"폐업으로 버려진 애터미 공기청정기 Home Assistant 로컬 연동 성공기", r"Successful Home Assistant Local Integration for Atomy Air Purifier"),
]

processed_count = 0

for filepath in glob.glob(os.path.join(POSTS_DIR, "*.md")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    cleaned = clean_tistory_footers(content)

    if filepath.endswith(".en.md"):
        parts = cleaned.split('---', 2)
        if len(parts) >= 3:
            frontmatter = parts[1]
            body = parts[2]

            # Translate title & description in frontmatter
            title_match = re.search(r'title:\s*"(.*?)"', frontmatter)
            if title_match:
                title = title_match.group(1)
                en_title = title
                en_title = re.sub(r'명품 C\+\+ programming 실습 문제 (\d+)장 (\d+)번', r'C++ Programming Ch.\1 Exercise \2 Solution', en_title)
                en_title = re.sub(r'명품 C\+\+ Programming 실습 문제 (\d+)장 (\d+)번', r'C++ Programming Ch.\1 Exercise \2 Solution', en_title)
                en_title = re.sub(r'데이터 통신과 네트워킹 Chapter (\d+) (.*) 연습 문제 정답', r'Data Communications & Networking Ch.\1 \2 Exercises & Solutions', en_title)
                frontmatter = frontmatter.replace(f'title: "{title}"', f'title: "{en_title}"')

            for pattern, replacement in SENTENCE_TRANSLATIONS:
                body = re.sub(pattern, replacement, body)

            cleaned = f"---{frontmatter}---{body}"

    if cleaned != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        processed_count += 1

print(f"Deep Translation & Tistory Footer Cleanup complete for {processed_count} files!")
