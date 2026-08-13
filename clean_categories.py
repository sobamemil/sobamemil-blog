import os
import re

content_dir = 'content/posts'

replacements = {
    '🏠 스마트홈 & DIY': '스마트홈 DIY',
    '💻 개발 & CS': '개발 CS',
    '📱 리뷰 & 일상': '리뷰 일상',
    '✈️ 일상 & 여행': '일상 여행',
    '🛠️ Home Assistant & IoT': 'Home Assistant IoT',
    '알고리즘 & 코딩테스트': '알고리즘 코딩테스트',
    '시스템 & 임베디드': '시스템 임베디드'
}

for filename in os.listdir(content_dir):
    if filename.endswith('.md'):
        filepath = os.path.join(content_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Only replace within frontmatter to be safe
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
