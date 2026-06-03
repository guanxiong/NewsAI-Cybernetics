#!/usr/bin/env python3
"""
acquire.py — Fetch top stories from multiple sources, output JSON for Agent processing.
Usage: python3 acquire.py [--source hn|googlenews|all] [--limit N]
Output: JSON array to stdout, summary to stderr
"""
import json, sys, urllib.request, concurrent.futures, datetime, argparse

def fetch_json(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": "NewsAI-Cybernetics/0.4"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())

def fetch_hn(limit=20):
    """Fetch top Hacker News stories."""
    ids = fetch_json("https://hacker-news.firebaseio.com/v0/topstories.json")[:limit]
    items = []
    def get_one(sid):
        try:
            d = fetch_json(f"https://hacker-news.firebaseio.com/v0/item/{sid}.json")
            if d.get("type") == "story" and d.get("url"):
                return {"id": d["id"], "title": d.get("title",""), "url": d.get("url",""),
                        "score": d.get("score",0), "author": d.get("by",""),
                        "date": datetime.datetime.fromtimestamp(d.get("time",0)).strftime("%Y-%m-%d"),
                        "comments": d.get("descendants",0), "source": "HackerNews"}
        except: pass
        return None
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
        results = list(ex.map(get_one, ids))
    return [r for r in results if r]

def main():
    parser = argparse.ArgumentParser(description="NewsAI-Cybernetics acquire")
    parser.add_argument("--source", default="hn", choices=["hn","all"])
    parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args()

    items = []
    if args.source in ("hn", "all"):
        items.extend(fetch_hn(args.limit))

    json.dump(items, sys.stdout, indent=2, ensure_ascii=False)
    print(f"\n--- Fetched {len(items)} items from {args.source} ---", file=sys.stderr)

if __name__ == "__main__":
    main()
