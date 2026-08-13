import os
import re

content_dir = 'content/posts'

replacements = {
    '🏠 Smart Home & DIY': 'Smart Home DIY',
    '💻 Dev & CS': 'Dev CS',
    '📱 Reviews & Life': 'Reviews Life',
    '✈️ Life & Travel': 'Life Travel'
}

for filename in os.listdir(content_dir):
    if filename.endswith('.en.md'):
        filepath = os.path.join(content_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        frontmatter_match = re.match(r'^(---.*?---)', content, flags=re.DOTALL)
        if frontmatter_match:
            fm = frontmatter_match.group(1)
            new_fm = fm
            for old, new in replacements.items():
                new_fm = new_fm.replace(old, new)
            
            if new_fm != fm:
                new_content = content.replace(fm, new_fm)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")
