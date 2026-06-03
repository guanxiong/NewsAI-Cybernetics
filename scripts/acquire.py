#!/usr/bin/env python3
"""
acquire.py — Multi-source news acquisition + auto-classification engine.
Usage: python3 acquire.py [--source hn|rss|all] [--limit N] [--classify]
Output: JSON array to stdout, summary to stderr.

Sources:
  hn  — Hacker News API (top stories)
  rss — RSS feeds (36Kr, Reuters, Google News, V2EX, Hacker News RSS)

Classification engine (v1 — keyword-weight rules, no LLM API needed):
  Scans title + description against weighted keyword dictionaries per Tier.
  Outputs: tier, importance (1-5), tags, summary (zh-CN).
"""
import json, sys, os, re, urllib.request, concurrent.futures, datetime, argparse
from xml.etree import ElementTree

# ─── Configuration ───────────────────────────────────────────────

RSS_FEEDS = [
    {"name": "HN RSS",        "url": "https://hnrss.org/frontpage",                             "default_tier": "4-Professional",          "lang": "en"},
    {"name": "dev.to",        "url": "https://dev.to/feed",                                      "default_tier": "4-Professional",          "lang": "en"},
    {"name": "Ars Technica",  "url": "https://feeds.arstechnica.com/arstechnica/technology-lab", "default_tier": "2-Cognitive-Framework",   "lang": "en"},
    {"name": "Techmeme",      "url": "https://www.techmeme.com/feed.xml",                        "default_tier": "2-Cognitive-Framework",   "lang": "en"},
    {"name": "36Kr",          "url": "https://36kr.com/feed",                                    "default_tier": "2-Cognitive-Framework",   "lang": "zh"},
    {"name": "The Verge",     "url": "https://www.theverge.com/rss/index.xml",                   "default_tier": "4-Professional",          "lang": "en"},
]

# ─── Classification Engine ───────────────────────────────────────

TIER_KEYWORDS = {
    "1-Core-Decision": {
        "keywords": [
            # Security
            (r"\bhack\w*\b|\bexploit\w*\b|\bvulnerabilit\w+\b|\bsecurit\w+\b|\bbreach\b|\bmalware\b|\bransomware\b",
             "安全预警"),
            (r"漏洞|攻击|入侵|勒索|数据泄露|安全风险", "安全预警"),
            # Policy
            (r"\btariff\b|\bsanction\b|\bregulation\b|\blegislation\b|\bfda\b|\bban\b", "政策法规"),
            (r"关税|制裁|法规|监管|禁令|政策调整|个税|医保|社保|利率", "政策法规"),
            # Emergency
            (r"\bearthquake\b|\btsunami\b|\bhurricane\b|\bpandemic\b|\bemergency\b", "安全预警"),
            (r"地震|台风|暴雨|传染病|紧急|预警|食品安全", "安全预警"),
        ],
        "weight": 10,
    },
    "2-Cognitive-Framework": {
        "keywords": [
            # Macro
            (r"\beconomy\b|\brecession\b|\binflation\b|\binterest rate\b|\bfed\b|\bgdp\b", "宏观经济"),
            (r"经济|通胀|利率|央行|GDP|楼市|就业|衰退|美联储", "宏观经济"),
            # Geopolitics
            (r"\bgeopolitic\b|\bdiplomacy\b|\bsanction\b|\bwar\b|\bconflict\b", "宏观经济"),
            # AI trends
            (r"\bartificial intelligence\b|\bAI\b|\bllm\b|\bgpt\b|\bclaude\b|\bgemini\b|\bmodel\b", "AI/ML"),
            (r"AI|大模型|GPT|Claude|Gemini|人工智能|机器学习|深度学习|大语言模型", "AI/ML"),
            # Science
            (r"\bquantum\b|\bfusion\b|\bclimate\b|\bresearch\b|\bbreakthrough\b", "科技趋势"),
            (r"量子|核聚变|气候|科研|突破|科学发现", "科技趋势"),
        ],
        "weight": 5,
    },
    "4-Professional": {
        "keywords": [
            # Dev tools
            (r"\bframework\b|\blibrary\b|\bapi\b|\bcompiler\b|\bruntime\b|\bdebug\b|\bdeploy\b", "产品工具"),
            (r"框架|库|编译器|运行时|调试|部署|工具|教程|文档|插件", "产品工具"),
            # Languages
            (r"\bpython\b|\bjavascript\b|\brust\b|\bgo\b|\belixir\b|\bzig\b|\btypescript\b", "科技趋势"),
            (r"Python|Rust|Go|Elixir|Zig|TypeScript|编程|代码|开发", "科技趋势"),
            # Product
            (r"\brelease\b|\bupdate\b|\blaunch\b|\bopen.?source\b|\bgit", "产品工具"),
            (r"发布|更新|上线|开源|版本", "产品工具"),
        ],
        "weight": 3,
    },
}

def classify_item(title, description="", source_default_tier=None):
    """Classify a news item by tier, importance, tags using keyword rules."""
    text = f"{title} {description}".lower()
    scores = {}
    tags_set = set()

    for tier, config in TIER_KEYWORDS.items():
        score = 0
        for pattern, tag in config["keywords"]:
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                score += config["weight"] * len(matches)
                tags_set.add(tag)
        scores[tier] = score

    # Determine tier
    if max(scores.values()) == 0:
        tier = source_default_tier or "3-Social-Connection"
    else:
        tier = max(scores, key=scores.get)

    # Determine importance based on engagement signals
    importance = 3  # default
    if tier == "1-Core-Decision":
        importance = 5
    elif tier == "2-Cognitive-Framework":
        importance = 4
    elif tier == "4-Professional":
        importance = 3
    else:
        importance = 2

    if not tags_set:
        if "1-Core" in tier:
            tags_set.add("安全预警")
        elif "2-Cognitive" in tier:
            tags_set.add("科技趋势")
        elif "4-Professional" in tier:
            tags_set.add("产品工具")
        else:
            tags_set.add("社会文化")

    return {
        "tier": tier,
        "importance": importance,
        "tags": sorted(list(tags_set)),
    }

# ─── Source Fetchers ─────────────────────────────────────────────

def fetch_json(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": "NewsAI-Cybernetics/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())

def fetch_hn(limit=20):
    """Fetch top Hacker News stories via API."""
    try:
        ids = fetch_json("https://hacker-news.firebaseio.com/v0/topstories.json")[:limit]
    except Exception as e:
        print(f"  ⚠️  HN API failed: {e}", file=sys.stderr)
        return []
    items = []
    def get_one(sid):
        try:
            d = fetch_json(f"https://hacker-news.firebaseio.com/v0/item/{sid}.json")
            if d.get("type") == "story" and d.get("url"):
                return {"id": d["id"], "title": d.get("title",""), "url": d.get("url",""),
                        "score": d.get("score",0), "author": d.get("by",""),
                        "date": datetime.datetime.fromtimestamp(d.get("time",0)).strftime("%Y-%m-%d"),
                        "comments": d.get("descendants",0), "source": "HackerNews",
                        "description": ""}
        except: pass
        return None
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
        results = list(ex.map(get_one, ids))
    return [r for r in results if r]

def fetch_rss(feed_config, limit=10):
    """Fetch and parse an RSS/Atom feed."""
    items = []
    try:
        req = urllib.request.Request(feed_config["url"],
                                     headers={"User-Agent": "NewsAI-Cybernetics/1.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            tree = ElementTree.fromstring(r.read())
        # Handle both RSS and Atom
        entries = tree.findall('.//item') or tree.findall('.//{http://www.w3.org/2005/Atom}entry')
        for entry in entries[:limit]:
            title_el = entry.find('title') or entry.find('{http://www.w3.org/2005/Atom}title')
            link_el = entry.find('link') or entry.find('{http://www.w3.org/2005/Atom}link')
            desc_el = entry.find('description') or entry.find('{http://www.w3.org/2005/Atom}summary')
            date_el = entry.find('pubDate') or entry.find('{http://www.w3.org/2005/Atom}published')
            title = title_el.text if title_el is not None and title_el.text else ""
            link = ""
            if link_el is not None:
                link = link_el.text if link_el.text else link_el.get("href", "")
            desc = desc_el.text if desc_el is not None and desc_el.text else ""
            date_str = ""
            if date_el is not None and date_el.text:
                try:
                    from email.utils import parsedate_to_datetime
                    date_str = parsedate_to_datetime(date_el.text).strftime("%Y-%m-%d")
                except:
                    date_str = datetime.date.today().isoformat()
            if title:
                # Clean HTML from description
                clean_desc = re.sub(r'<[^>]+>', '', desc)[:500]
                items.append({
                    "title": title.strip(),
                    "url": link.strip(),
                    "source": feed_config["name"],
                    "date": date_str or datetime.date.today().isoformat(),
                    "description": clean_desc,
                    "score": 0,
                    "comments": 0,
                    "default_tier": feed_config.get("default_tier", ""),
                })
    except Exception as e:
        print(f"  ⚠️  RSS {feed_config['name']} failed: {e}", file=sys.stderr)
    return items

def fetch_all_rss(limit_per_feed=10):
    """Fetch all configured RSS feeds in parallel."""
    all_items = []
    def get_feed(feed):
        return fetch_rss(feed, limit=limit_per_feed)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
        results = list(ex.map(get_feed, RSS_FEEDS))
    for items in results:
        all_items.extend(items)
    return all_items

# ─── Main ────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="NewsAI-Cybernetics Multi-Source Acquire")
    parser.add_argument("--source", default="all", choices=["hn","rss","all"])
    parser.add_argument("--limit", type=int, default=15)
    parser.add_argument("--classify", action="store_true", help="Auto-classify items")
    args = parser.parse_args()

    items = []
    if args.source in ("hn", "all"):
        hn_items = fetch_hn(args.limit)
        for item in hn_items:
            item["default_tier"] = "4-Professional"
        items.extend(hn_items)
        print(f"  📡 HN: {len(hn_items)} items", file=sys.stderr)

    if args.source in ("rss", "all"):
        rss_items = fetch_all_rss(args.limit)
        items.extend(rss_items)
        print(f"  📡 RSS: {len(rss_items)} items from {len(RSS_FEEDS)} feeds", file=sys.stderr)

    # Auto-classify
    if args.classify:
        classified = 0
        for item in items:
            result = classify_item(item.get("title",""), item.get("description",""),
                                   item.get("default_tier"))
            item["tier"] = result["tier"]
            item["importance"] = result["importance"]
            item["tags"] = result["tags"]
            classified += 1
        print(f"  🏷️  Classified: {classified} items", file=sys.stderr)

    # Output
    json.dump(items, sys.stdout, indent=2, ensure_ascii=False)

    # Summary
    tier_counts = {}
    for item in items:
        t = item.get("tier", "unclassified")
        tier_counts[t] = tier_counts.get(t, 0) + 1
    summary = f"\n--- Acquired {len(items)} items from {args.source} ---"
    for t, c in sorted(tier_counts.items()):
        summary += f"\n  {t}: {c}"
    print(summary, file=sys.stderr)

if __name__ == "__main__":
    main()
