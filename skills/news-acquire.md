---
name: news-acquire
description: Auto-acquire news from configured sources, classify by 4-Layer model, and store to Obsidian Inbox + NocoDB. Trigger: user says "acquire news", "fetch news", "采集新闻", "获取新闻".
---

# News Acquire Skill

## Overview
Automated news acquisition pipeline:
1. Fetch headlines from configured sources (RSS, HN, Google News)
2. LLM classifies each item by Tier (1-4) and Importance (1-5)
3. High-value items (Importance ≥ 3) are written to:
   - Obsidian `Inbox/` as Markdown (using TEMPLATE.md)
   - NocoDB `News Items` table
4. Low-value items are logged but skipped
5. Processing Log records each step

## Configuration
Read `AGENTS.md` for system rules and NocoDB connection info.

## Source Configuration
Sources are stored in NocoDB `Sources` table (Active=true).

### Default Sources
| Source | Type | Tier | Method |
|--------|------|------|--------|
| Hacker News | API | 4-Professional | `https://hacker-news.firebaseio.com/v0/topstories.json` |
| Google News | RSS | 1-Core-Decision | WebFetch/RSS parser |
| 36Kr | RSS | 2-Cognitive-Framework | RSS feed |
| Reuters | RSS | 2-Cognitive-Framework | RSS feed |

## Execution Steps

### Step 1: Fetch
For each active source in NocoDB `Sources` table:
- If API source: call API, parse JSON response
- If RSS source: fetch and parse RSS/Atom feed
- Extract: title, URL, source, date, description/snippet

### Step 2: LLM Classification
For each fetched item, use the LLM to classify:

```
Given this news item:
Title: {title}
Source: {source}
Snippet: {snippet}

Classify using these criteria:
- Tier 1 (Core-Decision): Directly affects survival, safety, or major personal interests in the next 3 months
- Tier 2 (Cognitive-Framework): Shapes worldview, long-term trends, but no immediate action needed
- Tier 3 (Social-Connection): Social currency, entertainment, emotional content
- Tier 4 (Professional): Solves a specific professional problem or builds skills

Also rate Importance (1-5):
5 = Urgent and important, requires immediate action
4 = Important, requires deep thinking today
3 = Moderate value, batch process
2 = Low value, social currency only
1 = Almost no value

Return JSON: {"tier": "N-TierName", "importance": N, "tags": ["tag1"], "summary": "one-line Chinese summary"}
```

### Step 3: Filter
Skip items where:
- Importance ≤ 1 → eliminated immediately
- Duplicate URL already exists in NocoDB

### Step 4: Store High-Value Items
For items with Importance ≥ 2:

**Obsidian**: Create file in `Inbox/` using TEMPLATE.md format:
```markdown
---
title: "{title}"
date: {date}
source: "{source}"
tier: "{tier}"
status: "inbox"
importance: {importance}
action_taken: false
tags:
  - news/{tier_short}
---

# {title}

## 核心摘要
> [!abstract]
> {LLM-generated one-line summary}

## 原文/附件存储
- [ ] 原始链接: {url}
```

**NocoDB**: Insert record into `News Items` table with all fields.

### Step 5: Log Processing
Write to NocoDB `Processing Log`:
- Step: 1-Acquire
- Action: "Fetched N items from {source}. Classified: T1={n1} T2={n2} T3={n3} T4={n4}. Stored={n5}. Eliminated={n6}."
- Executor: Agent
- Timestamp: now()

## Output Format
Report to user:
```
📰 News Acquire Complete
- Sources: {N} active
- Fetched: {total} items
- Classified:
  - 🔴 Tier 1: {n} items
  - 🟡 Tier 2: {n} items
  - 🟢 Tier 3: {n} items
  - 🔵 Tier 4: {n} items
- Stored to Inbox: {n} items
- Eliminated: {n} items
- ⚡ Action required: {n} Tier-1 items need immediate attention!
```
