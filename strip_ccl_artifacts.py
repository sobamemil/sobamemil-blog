import os
import glob
import re

POSTS_DIR = "/Users/sobamemil/.gemini/antigravity/scratch/sobamemil-blog/content/posts"

removed_ccl_count = 0

for filepath in glob.glob(os.path.join(POSTS_DIR, "*.md")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = content.split('---', 2)
    if len(parts) < 3:
        continue

    frontmatter = parts[1]
    body = parts[2]
    original_body = body

    # 1. Remove Creative Commons License markdown links and text artifacts
    body = re.sub(r'\[저작자표시.*?\([^)]+\)', '', body, flags=re.DOTALL)
    body = re.sub(r'\(새창열림\)\]\(https://creativecommons\.org/licenses/[^)]+\)', '', body)
    body = re.sub(r'\[저작자표시[^\]]*\]', '', body)
    body = re.sub(r'https://creativecommons\.org/licenses/[^\s]+', '', body)

    # Clean up empty orphan lines left over at the bottom
    lines = body.splitlines()
    cleaned_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped in ["(새창열림)", "[저작자표시", "[저작자표시 비영리", "저작자표시"]:
            continue
        cleaned_lines.append(line)

    body = '\n'.join(cleaned_lines).strip() + '\n'

    if body != original_body:
        removed_ccl_count += 1
        new_content = f"---{frontmatter}---{body}"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print(f"Successfully stripped CCL Creative Commons artifacts from {removed_ccl_count} post files!")
