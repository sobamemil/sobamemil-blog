import os
import glob
import re

POSTS_DIR = "/Users/sobamemil/.gemini/antigravity/scratch/sobamemil-blog/content/posts"

fixed_count = 0

for filepath in glob.glob(os.path.join(POSTS_DIR, "*.md")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = content.split('---', 2)
    if len(parts) < 3:
        continue

    frontmatter = parts[1]
    body = parts[2]
    original_body = body

    # Replace **'text'** or **‘text’** or **"text"** or **text** with <b>text</b>
    body = re.sub(r"\*\*['‘“]?([^'\n*”’]+)['’”]?\*\*", r"<b>\1</b>", body)

    if body != original_body:
        fixed_count += 1
        new_content = f"---{frontmatter}---{body}"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print(f"Forced replace of raw asterisks to <b> HTML tags in {fixed_count} files!")
