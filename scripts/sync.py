#!/usr/bin/env python3
"""
sync.py — Obsidian ↔ NocoDB sync via Agent middleware.

This script handles the Obsidian (Markdown) side. The Agent (Claude Code / Gemini CLI)
bridges to NocoDB via MCP tools. No direct NocoDB API token needed.

Usage:
  python3 sync.py push    — Parse Inbox/*.md → output JSON records for Agent to push to NocoDB
  python3 sync.py pull    — Read JSON records from stdin (exported by Agent from NocoDB) → create Inbox files
  python3 sync.py status  — Show local Obsidian Inbox stats

Architecture:
  Obsidian Markdown → [sync.py push] → JSON → [Agent MCP] → NocoDB
  NocoDB → [Agent MCP export] → JSON → [sync.py pull] → Obsidian Markdown
"""
import json, sys, os, re, glob, datetime, argparse

INBOX_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Inbox")

def parse_frontmatter(filepath):
    """Parse YAML-style frontmatter from Obsidian Markdown."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if not match:
        return {}, content
    fm_text, body = match.groups()
    props = {}
    current_key = None
    current_list = []
    for line in fm_text.split('\n'):
        stripped = line.strip()
        if stripped.startswith('- ') and current_key:
            current_list.append(stripped[2:].strip())
            continue
        if current_key and current_list:
            props[current_key] = current_list
            current_list = []
        if ':: ' in stripped:
            key, val = stripped.split(':: ', 1)
            props[key.strip()] = val.strip()
        elif ':' in stripped and not stripped.startswith('#'):
            parts = stripped.split(':', 1)
            key = parts[0].strip()
            val = parts[1].strip().strip('"').strip("'")
            if val:
                current_key = key
                current_list = []
                props[key] = val
            else:
                current_key = key
                current_list = []
    if current_key and current_list:
        props[current_key] = current_list
    return props, body

def cmd_push(args):
    """Parse Inbox Markdown files and output JSON for Agent to push to NocoDB."""
    files = sorted(glob.glob(os.path.join(INBOX_DIR, "*.md")))
    if not files:
        print('{"records": [], "message": "No files in Inbox/"}')
        return
    records = []
    for fpath in files:
        fm, body = parse_frontmatter(fpath)
        if not fm.get('title'):
            continue
        importance = fm.get('importance', '3')
        try:
            importance = int(str(importance).strip())
        except ValueError:
            importance = 3
        record = {
            "Title": fm.get('title', ''),
            "Source": fm.get('source', ''),
            "Tier": fm.get('tier', ''),
            "Status": fm.get('status', 'inbox'),
            "Importance": importance,
            "Action Taken": fm.get('action_taken', 'false') == 'true',
            "URL": fm.get('url', ''),
            "Notes": body.strip()[:2000] if body.strip() else '',
            "Date": fm.get('date', datetime.date.today().isoformat()),
            "Tags": fm.get('tags', []) if isinstance(fm.get('tags'), list) else [],
            "_source_file": os.path.basename(fpath),
        }
        records.append(record)
    output = {"records": records, "count": len(records), "message": f"Ready to push {len(records)} records to NocoDB"}
    json.dump(output, sys.stdout, indent=2, ensure_ascii=False)
    print(f"\n--- Prepared {len(records)} records from {len(files)} Inbox files ---", file=sys.stderr)

def cmd_pull(args):
    """Read JSON records from stdin and create Inbox Markdown files."""
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        print("Error: Expected JSON on stdin. Pipe NocoDB export output.", file=sys.stderr)
        sys.exit(1)
    records = data if isinstance(data, list) else data.get('records', data.get('list', []))
    created = 0
    for rec in records:
        fields = rec.get('fields', rec)
        title = fields.get('Title', '')
        if not title:
            continue
        safe_title = re.sub(r'[^\w\s-]', '', title)[:50].strip().replace(' ', '-')
        if not safe_title:
            safe_title = f"news-{datetime.date.today().isoformat()}"
        filepath = os.path.join(INBOX_DIR, f"{safe_title}.md")
        if os.path.exists(filepath):
            continue
        tags = fields.get('Tags', [])
        tags_yaml = '\n' + '\n'.join(f'  - {t}' for t in tags) if tags else ''
        tier = fields.get('Tier', '')
        importance = fields.get('Importance', 3)
        content = f"""---
title: "{title}"
date: {fields.get('Date', '')}
source: {fields.get('Source', '')}
tier: "{tier}"
status: inbox
importance: {importance}
action_taken: {"true" if fields.get('Action Taken') else "false"}
tags:{tags_yaml}
---

# {title}

## 核心摘要
> [!abstract]
> {fields.get('Notes', '')}

## 原文/附件存储
- [ ] 原始链接: {fields.get('URL', '')}
"""
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        created += 1
        print(f"  ✅ Created: {safe_title}.md", file=sys.stderr)
    print(f"\n--- Created {created} files in Inbox/ ---", file=sys.stderr)

def cmd_status(args):
    """Show local Obsidian Inbox stats."""
    files = glob.glob(os.path.join(INBOX_DIR, "*.md"))
    by_tier = {}
    by_status = {}
    for fpath in files:
        fm, _ = parse_frontmatter(fpath)
        tier = fm.get('tier', 'unknown')
        status = fm.get('status', 'unknown')
        by_tier[tier] = by_tier.get(tier, 0) + 1
        by_status[status] = by_status.get(status, 0) + 1
    print("📊 Obsidian Inbox Status")
    print(f"  Total files: {len(files)}")
    if by_tier:
        print(f"\n  By Tier:")
        for t, c in sorted(by_tier.items()):
            print(f"    {t}: {c}")
    if by_status:
        print(f"\n  By Status:")
        for s, c in sorted(by_status.items()):
            print(f"    {s}: {c}")

def main():
    parser = argparse.ArgumentParser(description="NewsAI-Cybernetics Obsidian ↔ NocoDB Sync")
    parser.add_argument("command", choices=["push", "pull", "status"],
                        help="push: MD→JSON | pull: JSON→MD | status: local stats")
    args = parser.parse_args()
    {"push": cmd_push, "pull": cmd_pull, "status": cmd_status}[args.command](args)

if __name__ == "__main__":
    main()
