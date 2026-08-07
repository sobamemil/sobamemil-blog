#!/usr/bin/env python3
import os
import sys
import re
import json
import time
import random
import urllib.parse
import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup
import markdownify

BLOG_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(BLOG_DIR, "content", "posts")
STATIC_IMG_DIR = os.path.join(BLOG_DIR, "static", "images", "posts")
PROGRESS_FILE = os.path.join(BLOG_DIR, ".migration_progress.json")
REPORT_FILE = os.path.join(BLOG_DIR, "migration_report.md")

os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(STATIC_IMG_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
}

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
    return {"completed": [], "failed": [], "stats": {"total": 0, "images": 0}}

def save_progress(progress):
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)

def map_category(raw_cat):
    if not raw_cat:
        return "💻 개발 & CS"
    raw = raw_cat.strip()
    if any(k in raw for k in ["스마트홈", "DIY", "Home Assistant", "IoT", "하드웨어"]):
        return "🏠 스마트홈 & DIY"
    elif any(k in raw for k in ["개발", "CS", "C++", "네트워크", "임베디드", "알고리즘", "코딩테스트", "iOS"]):
        return "💻 개발 & CS"
    elif any(k in raw for k in ["리뷰", "내돈내산", "일상", "여행"]):
        return "📱 리뷰 & 일상"
    elif raw.startswith("🏠"):
        return "🏠 스마트홈 & DIY"
    elif raw.startswith("💻"):
        return "💻 개발 & CS"
    elif raw.startswith("📱"):
        return "📱 리뷰 & 일상"
    return "💻 개발 & CS"

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text).strip('-')
    return text[:50] if text else "post"

def download_image(img_url, post_id, idx):
    if not img_url:
        return None
    if img_url.startswith('//'):
        img_url = 'https:' + img_url
    elif not img_url.startswith('http'):
        return None

    post_img_dir = os.path.join(STATIC_IMG_DIR, str(post_id))
    os.makedirs(post_img_dir, exist_ok=True)

    # Determine file extension
    ext = '.png'
    parsed = urllib.parse.urlparse(img_url)
    path = parsed.path
    if '.' in path.split('/')[-1]:
        possible_ext = os.path.splitext(path.split('/')[-1])[1].lower()
        if possible_ext in ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp']:
            ext = possible_ext

    filename = f"img_{idx+1}{ext}"
    file_path = os.path.join(post_img_dir, filename)
    local_url = f"/images/posts/{post_id}/{filename}"

    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        return local_url

    try:
        r = requests.get(img_url, headers=HEADERS, timeout=10)
        if r.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(r.content)
            return local_url
    except Exception as e:
        print(f"    ⚠️ Warning: Failed to download image {img_url}: {e}")
    return img_url

def fetch_post_ids():
    url = 'https://sobamemil.tistory.com/sitemap.xml'
    print(f"🔍 Fetching sitemap from {url}...")
    r = requests.get(url, headers=HEADERS, timeout=10)
    post_ids = set()
    if r.status_code == 200:
        found = re.findall(r'https://sobamemil\.tistory\.com/(\d+)', r.text)
        for pid in found:
            post_ids.add(int(pid))
    print(f"✅ Found {len(post_ids)} distinct post IDs in sitemap.")
    return sorted(list(post_ids))

def process_post(post_id):
    url = f"https://sobamemil.tistory.com/{post_id}"
    r = requests.get(url, headers=HEADERS, timeout=10)
    if r.status_code != 200:
        print(f"❌ Failed to fetch post {post_id} (HTTP {r.status_code})")
        return False, 0

    soup = BeautifulSoup(r.text, 'html.parser')

    # Title
    og_title = soup.find('meta', property='og:title')
    title = og_title.get('content') if og_title else None
    if not title:
        title_el = soup.find(class_='title') or soup.find('h1') or soup.find('h2')
        title = title_el.get_text(strip=True) if title_el else f"Post {post_id}"

    # Clean title
    title = title.replace('"', '\\"').strip()

    # Published Date
    meta_date = soup.find('meta', property='article:published_time') or soup.find('meta', property='og:regDate')
    pub_date = meta_date.get('content') if meta_date else None
    if not pub_date:
        date_el = soup.find(class_='date') or soup.find(class_='created_at')
        if date_el:
            raw_d = date_el.get_text(strip=True)
            # Example format: 2019. 11. 20. 22:55 -> 2019-11-20T22:55:00+09:00
            m = re.search(r'(\d{4})\.\s*(\d{1,2})\.\s*(\d{1,2})\.\s*(\d{1,2}):(\d{2})', raw_d)
            if m:
                pub_date = f"{m.group(1)}-{int(m.group(2)):02d}-{int(m.group(3)):02d}T{int(m.group(4)):02d}:{m.group(5)}:00+09:00"
    if not pub_date:
        pub_date = "2020-01-01T00:00:00+09:00"

    # Category
    cat_el = soup.find(class_='category') or soup.find(class_='cat')
    raw_cat = cat_el.get_text(strip=True) if cat_el else ""
    final_cat = map_category(raw_cat)

    # Tags
    tags = []
    tag_els = soup.find_all(class_='tag') or soup.find_all('a', href=re.compile(r'/tag/'))
    for tel in tag_els:
        t_text = tel.get_text(strip=True).replace('#', '').strip()
        if t_text and t_text not in tags and len(t_text) < 30:
            tags.append(t_text)

    # Main content container
    container = soup.find(class_='entry-content') or soup.find(class_='tt_article_useless_p_margin') or soup.find(class_='article-view')
    if not container:
        print(f"⚠️ Warning: Could not find main content container for post {post_id}")
        return False, 0

    # Process Images
    imgs = container.find_all('img')
    img_count = 0
    for idx, img in enumerate(imgs):
        src = img.get('src') or img.get('data-origin-src') or img.get('data-filename')
        if src:
            local_src = download_image(src, post_id, idx)
            if local_src:
                img['src'] = local_src
                img_count += 1

    # Convert HTML to Markdown
    md_content = markdownify.markdownify(str(container), heading_style="ATX", code_language="cpp")
    md_content = re.sub(r'\n{3,}', '\n\n', md_content).strip()

    # Format Frontmatter
    tags_fmt = json.dumps(tags, ensure_ascii=False)
    cats_fmt = json.dumps([final_cat], ensure_ascii=False)

    file_slug = slugify(title)
    filename = f"{post_id:03d}-{file_slug}.md"
    file_path = os.path.join(POSTS_DIR, filename)

    frontmatter = f"""---
title: "{title}"
date: {pub_date}
draft: false
categories: {cats_fmt}
tags: {tags_fmt}
---

{md_content}
"""

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter)

    print(f"  ✅ Saved Post [{post_id}] | Category: {final_cat} | Date: {pub_date[:10]} | Imgs: {img_count} | Title: {title[:40]}")
    return True, img_count

def main():
    print("🚀 Starting Tistory to Hugo Migration...")
    progress = load_progress()

    post_ids = fetch_post_ids()

    # Filter out already completed
    pending = [pid for pid in post_ids if pid not in progress["completed"]]
    print(f"📊 Total Posts: {len(post_ids)} | Already Completed: {len(progress['completed'])} | Pending: {len(pending)}")

    total_imgs = progress["stats"].get("images", 0)

    for idx, pid in enumerate(pending, 1):
        print(f"[{idx}/{len(pending)}] Processing Post {pid}...")
        try:
            success, img_c = process_post(pid)
            if success:
                progress["completed"].append(pid)
                total_imgs += img_c
                progress["stats"]["images"] = total_imgs
                save_progress(progress)
            else:
                progress["failed"].append(pid)
                save_progress(progress)
        except Exception as e:
            print(f"❌ Error processing post {pid}: {e}")
            progress["failed"].append(pid)
            save_progress(progress)

        # Rate limiting delay
        time.sleep(random.uniform(0.4, 0.7))

    print("\n🎉 Migration Complete!")
    print(f"Total Successfully Converted: {len(progress['completed'])} / {len(post_ids)}")

    # Generate Summary Report
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write(f"""# 📊 Tistory to Hugo Migration Report

- **Total Posts Found**: {len(post_ids)}
- **Successfully Converted**: {len(progress['completed'])}
- **Failed**: {len(progress['failed'])}
- **Total Local Images Downloaded**: {total_imgs}
- **Output Post Directory**: `content/posts/`
- **Output Static Image Directory**: `static/images/posts/`
""")
    print(f"📄 Report written to {REPORT_FILE}")

if __name__ == "__main__":
    main()
