import os
import re

BLOG_DIR = '/Users/sobamemil/.gemini/antigravity/scratch/sobamemil-blog'
POSTS_DIR = os.path.join(BLOG_DIR, 'content', 'posts')

def infer_subcategory(title, tags, main_cat, is_en):
    title_lower = title.lower()
    tags_lower = [t.lower() for t in tags]
    
    if main_cat.startswith("🏠"):
        # 스마트홈 & DIY
        if any(k in title_lower for k in ["ha", "home assistant", "iot", "공기청정기", "tuya"]) or any(k in tags_lower for k in ["ha", "home assistant", "iot", "tuya"]):
            return "🛠️ Home Assistant & IoT" if not is_en else "🛠️ Home Assistant & IoT"
        else:
            return "하드웨어 & DIY" if not is_en else "Hardware & DIY"
            
    elif main_cat.startswith("💻"):
        # 개발 & CS
        if "c++" in title_lower or "c++" in tags_lower or "명품" in title_lower:
            return "C++ 프로그래밍" if not is_en else "C++ Programming"
        elif any(k in title_lower for k in ["통신", "네트워크", "network", "데이터링크", "ip "]) or any(k in tags_lower for k in ["network", "통신", "데이터링크"]):
            return "네트워크 & 통신" if not is_en else "Network & Comm"
        elif any(k in title_lower for k in ["시스템", "system", "임베디드"]) or any(k in tags_lower for k in ["system", "시스템"]):
            return "시스템 & 임베디드" if not is_en else "System & Embedded"
        elif any(k in title_lower for k in ["알고리즘", "코딩테스트", "프로그래머스", "정렬", "탐색"]) or any(k in tags_lower for k in ["algorithm", "알고리즘", "프로그래머스", "백준"]):
            return "알고리즘 & 코딩테스트" if not is_en else "Algorithm & Coding Test"
        elif any(k in title_lower for k in ["swift", "ios"]) or any(k in tags_lower for k in ["swift", "ios"]):
            return "iOS & 기타" if not is_en else "iOS & Others"
        elif "오픈소스" in title_lower or "opensource" in tags_lower:
            return "오픈소스 & 프로젝트" if not is_en else "Open Source & Projects"
        else:
            return "iOS & 기타" if not is_en else "iOS & Others" # Fallback
            
    elif main_cat.startswith("📱"):
        # 리뷰 & 일상
        if any(k in title_lower for k in ["리뷰", "내돈내산"]) or any(k in tags_lower for k in ["리뷰", "내돈내산"]):
            return "📦 내돈내산 리뷰" if not is_en else "📦 Real Reviews"
        else:
            return "✈️ 일상 & 여행" if not is_en else "✈️ Life & Travel"
            
    return None

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # match front matter
    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not match:
        return

    front_matter = match.group(1)
    body = match.group(2)
    
    is_en = file_path.endswith('.en.md')

    # extract title
    title_match = re.search(r'^title:\s*"(.*?)"', front_matter, re.MULTILINE)
    title = title_match.group(1) if title_match else ""

    # extract tags
    tags_match = re.search(r'^tags:\s*\[(.*?)\]', front_matter, re.MULTILINE)
    tags = []
    if tags_match:
        tag_str = tags_match.group(1)
        tags = [t.strip().strip('"\'') for t in tag_str.split(',') if t.strip()]

    # extract categories
    cats_match = re.search(r'^categories:\s*\[(.*?)\]', front_matter, re.MULTILINE)
    if not cats_match:
        return
        
    cats_str = cats_match.group(1)
    existing_cats = [c.strip().strip('"\'') for c in cats_str.split(',') if c.strip()]
    
    if len(existing_cats) == 0:
        main_cat = "💻 Dev & CS" if is_en else "💻 개발 & CS"
    else:
        main_cat = existing_cats[0]
        
    # Already nested?
    if len(existing_cats) >= 2:
        return

    sub_cat = infer_subcategory(title, tags, main_cat, is_en)
    
    if sub_cat:
        new_cats_line = f'categories: ["{main_cat}", "{sub_cat}"]'
        new_front_matter = re.sub(r'^categories:\s*\[.*?\]', new_cats_line, front_matter, flags=re.MULTILINE)
        
        new_content = f'---\n{new_front_matter}\n---\n{body}'
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(file_path)}: {main_cat} > {sub_cat}")


for root, _, files in os.walk(POSTS_DIR):
    for file in files:
        if file.endswith('.md'):
            process_file(os.path.join(root, file))
