import os
import glob
import re

POSTS_DIR = "/Users/sobamemil/.gemini/antigravity/scratch/sobamemil-blog/content/posts"

PATTERNS_TO_REMOVE = [
    r'공유하기\s*',
    r'게시글 관리\s*',
    r'카카오스토리\s*',
    r'트위터\s*',
    r'페이스북\s*',
    r'클립보드 복사\s*',
    r'https?://[^\s]+/tistory[^\s]*',
]

cleaned_count = 0

for filepath in glob.glob(os.path.join(POSTS_DIR, "*.md")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split frontmatter
    parts = content.split('---', 2)
    if len(parts) < 3:
        continue

    frontmatter = parts[1]
    body = parts[2]

    original_body = body
    for pattern in PATTERNS_TO_REMOVE:
        body = re.sub(pattern, '', body)

    # Clean up trailing empty lines or redundant Tistory artifacts at the end of body
    lines = body.splitlines()
    cleaned_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped in ["공유하기", "게시글 관리", "카카오스토리", "트위터", "페이스북"]:
            continue
        cleaned_lines.append(line)

    new_body = '\n'.join(cleaned_lines)

    if new_body != original_body:
        new_content = f"---{frontmatter}---{new_body}"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        cleaned_count += 1

print(f"Cleaned Tistory boilerplate from {cleaned_count} posts!")
