#!/usr/bin/env python3
"""
Scrape and cache all UGREEN NAS / UGOS Pro Knowledge Center and Application Guide articles locally.
"""

import os
import sys
import json
import re
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup
from markdownify import markdownify as md

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.path.join(BASE_DIR, "knowledge_cache")
ARTICLES_DIR = os.path.join(CACHE_DIR, "articles")
os.makedirs(ARTICLES_DIR, exist_ok=True)

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '_', text)
    return text.strip('_')[:60]

def clean_markdown(html_content):
    if not html_content:
        return ""
    # Parse with BeautifulSoup to remove scripts/styles if any
    soup = BeautifulSoup(html_content, "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose()
    
    markdown_text = md(str(soup), heading_style="ATX")
    # Clean up excessive newlines
    markdown_text = re.sub(r'\n{3,}', '\n\n', markdown_text)
    return markdown_text.strip()

def main():
    print("1. Fetching catalogue tree from api.ugnas.com...")
    tree_url = "https://api.ugnas.com/api/system/v2/sa/official/catalogue/tree?language=en-US&withRel=true"
    req = urllib.request.Request(tree_url, headers={"User-Agent": "Mozilla/5.0"})
    
    with urllib.request.urlopen(req, timeout=15) as resp:
        tree_data = json.loads(resp.read().decode("utf-8"))["data"]

    all_items = []
    
    def walk_tree(node, cat_path=""):
        name = (node.get("name") or "").strip()
        current_path = f"{cat_path} > {name}" if cat_path else name
        node_id = node.get("id")
        children = node.get("children", [])
        
        if not children and node_id:
            all_items.append({
                "id": node_id,
                "title": name,
                "category_path": current_path
            })
            
        for child in children:
            walk_tree(child, current_path)

    for root_node in tree_data:
        walk_tree(root_node)

    # Deduplicate by article ID
    unique_map = {}
    for item in all_items:
        aid = item["id"]
        if aid not in unique_map:
            unique_map[aid] = item
    
    unique_articles = list(unique_map.values())
    print(f"Discovered {len(unique_articles)} unique articles across the knowledge base.")

    # Save initial catalog index
    catalog_path = os.path.join(CACHE_DIR, "catalog.json")
    with open(catalog_path, "w", encoding="utf-8") as f:
        json.dump(unique_articles, f, indent=2, ensure_ascii=False)

    print(f"2. Fetching and formatting {len(unique_articles)} articles...")

    def fetch_article(item):
        aid = item["id"]
        title = item["title"]
        cat_path = item["category_path"]
        slug = slugify(title)
        filename = f"{aid}_{slug}.md"
        filepath = os.path.join(ARTICLES_DIR, filename)

        api_url = f"https://api.ugnas.com/api/system/knowledge_center/sa/base/article/info?articleInfoId={aid}&language=en-US"
        api_req = urllib.request.Request(api_url, headers={"User-Agent": "Mozilla/5.0"})

        for attempt in range(3):
            try:
                with urllib.request.urlopen(api_req, timeout=12) as response:
                    res_json = json.loads(response.read().decode("utf-8"))
                    adata = res_json.get("data", {})
                    if not adata:
                        return aid, False, "No data", filename, 0
                    
                    real_title = (adata.get("title") or title).strip()
                    content_html = adata.get("content") or ""
                    client_list = adata.get("clientList") or []
                    client_type = adata.get("clientType") or ""
                    clients_str = client_type if client_type else (", ".join(client_list) if client_list else "All Supported Clients")
                    
                    markdown_body = clean_markdown(content_html)
                    
                    # Construct clean markdown with metadata header
                    doc_lines = [
                        f"# {real_title}",
                        "",
                        f"> **Article ID**: `{aid}`  ",
                        f"> **Category**: `{cat_path}`  ",
                        f"> **Client Compatibility**: `{clients_str}`  ",
                        f"> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/{aid}  ",
                        "",
                        "---",
                        "",
                        markdown_body,
                        ""
                    ]
                    
                    with open(filepath, "w", encoding="utf-8") as out_f:
                        out_f.write("\n".join(doc_lines))
                        
                    return aid, True, real_title, filename, len(markdown_body)
            except Exception as e:
                time.sleep(0.4 * (attempt + 1))
        return aid, False, str(e), filename, 0

    t_start = time.time()
    success_count = 0
    fail_count = 0
    cached_metadata = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(fetch_article, item): item for item in unique_articles}
        for future in as_completed(futures):
            aid, ok, title_or_err, filename, body_len = future.result()
            if ok:
                success_count += 1
                item_info = futures[future]
                cached_metadata.append({
                    "id": aid,
                    "title": title_or_err,
                    "category": item_info["category_path"],
                    "filename": filename,
                    "length": body_len,
                    "url": f"https://support.ugnas.com/knowledgecenter/#/detail/{aid}"
                })
            else:
                fail_count += 1
            
            total_done = success_count + fail_count
            if total_done % 50 == 0 or total_done == len(unique_articles):
                print(f"[{time.time() - t_start:5.1f}s] Processed {total_done}/{len(unique_articles)} ({success_count} success, {fail_count} failed)")

    print(f"Scrape completed in {time.time() - t_start:.1f}s: {success_count} saved, {fail_count} failed.")

    # Save detailed cached metadata
    metadata_path = os.path.join(CACHE_DIR, "articles_metadata.json")
    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(cached_metadata, f, indent=2, ensure_ascii=False)

    # Generate master README.md index
    print("3. Generating master README.md index...")
    # Group by top-level and second-level categories
    categories = {}
    for item in sorted(cached_metadata, key=lambda x: x["category"]):
        cat = item["category"]
        parts = [p.strip() for p in cat.split(">")]
        top = parts[0] if len(parts) > 0 else "General"
        sub = parts[1] if len(parts) > 1 else "General"
        
        if top not in categories:
            categories[top] = {}
        if sub not in categories[top]:
            categories[top][sub] = []
        categories[top][sub].append(item)

    readme_lines = [
        "# 📚 UGREEN NAS (UGOS Pro) Complete Knowledge Base & Application Guide",
        "",
        "> **Local Cache Repository**: Authoritative offline mirror of all official UGREEN NAS guides, application manuals, and troubleshooting articles.",
        f"> **Total Cached Articles**: `{success_count}`  ",
        f"> **Generated**: `{time.strftime('%Y-%m-%d %H:%M:%S')}`  ",
        "",
        "---",
        "",
        "## 🧭 Categories Index",
        ""
    ]

    for top, subs in sorted(categories.items()):
        readme_lines.append(f"### 📂 {top}")
        for sub, articles in sorted(subs.items()):
            readme_lines.append(f"\n#### 📁 {sub} ({len(articles)} articles)\n")
            for a in articles:
                readme_lines.append(f"- [{a['title']}](articles/{a['filename']}) — *ID `{a['id']}`*")
        readme_lines.append("")

    readme_path = os.path.join(CACHE_DIR, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(readme_lines))

    print(f"Master index written to {readme_path}.")

if __name__ == "__main__":
    main()
