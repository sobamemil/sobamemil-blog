import os
import glob
import re

POSTS_DIR = "/Users/sobamemil/.gemini/antigravity/scratch/sobamemil-blog/content/posts"

CATEGORY_MAP = {
    "🏠 스마트홈 & DIY": "🏠 Smart Home & DIY",
    "💻 개발 & CS": "💻 Dev & CS",
    "📱 리뷰 & 일상": "📱 Reviews & Life"
}

generated_count = 0

for filepath in glob.glob(os.path.join(POSTS_DIR, "*.md")):
    if filepath.endswith(".en.md"):
        continue

    en_filepath = filepath[:-3] + ".en.md"

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = content.split('---', 2)
    if len(parts) < 3:
        continue

    frontmatter = parts[1]
    body = parts[2]

    # Replace category names in frontmatter if needed
    for ko_cat, en_cat in CATEGORY_MAP.items():
        frontmatter = frontmatter.replace(f'"{ko_cat}"', f'"{en_cat}"')

    # Create EN content
    en_content = f"---{frontmatter}---{body}"

    with open(en_filepath, 'w', encoding='utf-8') as f:
        f.write(en_content)

    generated_count += 1

print(f"Generated {generated_count} English post files (.en.md)!")
