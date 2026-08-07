import os
import glob
import re

POSTS_DIR = "/Users/sobamemil/.gemini/antigravity/scratch/sobamemil-blog/content/posts"

removed_tistory_tag_count = 0
fixed_bold_syntax_count = 0

for filepath in glob.glob(os.path.join(POSTS_DIR, "*.md")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = content.split('---', 2)
    if len(parts) < 3:
        continue

    frontmatter = parts[1]
    body = parts[2]
    original_body = body

    # 1. Remove '코딩은 내일부터 ;' or '**코딩은 내일부터 ;**'
    lines = body.splitlines()
    cleaned_lines = []
    for line in lines:
        stripped = line.strip()
        if "코딩은 내일부터" in stripped or "공유하기" in stripped or "게시글 관리" in stripped:
            removed_tistory_tag_count += 1
            continue
        cleaned_lines.append(line)

    body = '\n'.join(cleaned_lines)

    # 2. Fix problematic bold quotes like **'text'** or **"text"**
    # Convert **'text'** -> <b>'text'</b>
    body = re.sub(r"\*\*'([^']+)'\*\*", r"<b>'\1'</b>", body)
    body = re.sub(r'\*\*"([^"]+)"\*\*', r'<b>"\1"</b>', body)

    if body != original_body:
        fixed_bold_syntax_count += 1
        new_content = f"---{frontmatter}---{body}"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print(f"Deep Clean Complete: Removed Tistory tags from {removed_tistory_tag_count} lines, fixed bold syntax in {fixed_bold_syntax_count} files!")
