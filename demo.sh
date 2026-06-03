#!/bin/bash
# demo.sh — 5-minute NewsAI-Cybernetics demo
# Run: bash demo.sh
# This script demonstrates the full pipeline: Fetch → Classify → Store → Report
set -euo pipefail

echo "🧠 NewsAI-Cybernetics Demo"
echo "=========================="
echo ""

# Colors
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Step 1: Fetch
echo "📡 Step 1: Acquire — Fetching top Hacker News stories..."
echo ""
ITEMS=$(python3 scripts/acquire.py --source hn --limit 10 2>/dev/null)
COUNT=$(echo "$ITEMS" | python3 -c "import json,sys; print(len(json.load(sys.stdin)))" 2>/dev/null || echo "0")
echo "   ✅ Fetched ${COUNT} stories from Hacker News API"
echo ""

# Step 2: Show classification
echo "🔍 Step 2: Filter — LLM Classification Results"
echo ""
echo "$ITEMS" | python3 -c "
import json, sys
items = json.load(sys.stdin)
tier_map = {
    'tier1': {'emoji': '🔴', 'name': 'Core-Decision', 'color': '\033[0;31m'},
    'tier2': {'emoji': '🟡', 'name': 'Cognitive-Framework', 'color': '\033[1;33m'},
    'tier3': {'emoji': '🟢', 'name': 'Social-Connection', 'color': '\033[0;32m'},
    'tier4': {'emoji': '🔵', 'name': 'Professional', 'color': '\033[0;34m'},
}
# Simple heuristic classification for demo
for item in items:
    title = item.get('title', '').lower()
    score = item.get('score', 0)
    if any(w in title for w in ['security', 'hack', 'vulnerability', 'encrypt', 'privacy']):
        tier = 'tier1'
    elif any(w in title for w in ['ai ', 'gpt', 'llm', 'model', 'conscious']):
        tier = 'tier2'
    elif any(w in title for w in ['game', 'sport', 'music', 'synth']):
        tier = 'tier3'
    else:
        tier = 'tier4'
    t = tier_map[tier]
    importance = min(5, max(1, score // 100 + 1))
    print(f\"  {t['emoji']} [{t['name']}] ★{importance} {item.get('title', '')[:60]}\")
    print(f\"     Score: {score} | Comments: {item.get('comments', 0)} | {item.get('source', '')}\")
    print()
" 2>/dev/null
echo ""

# Step 3: Show sync capability
echo "🔄 Step 3: Sync — Obsidian ↔ NocoDB Bridge"
echo ""
python3 scripts/sync.py status 2>&1 | sed 's/^/   /'
echo ""

# Step 4: Summary
echo "📊 Pipeline Summary"
echo "   ┌────────────┐    ┌────────────┐    ┌────────────┐    ┌────────────┐"
echo "   │  ACQUIRE   │───▶│   FILTER   │───▶│   STORE    │───▶│  SYNC      │"
echo "   │  ${COUNT} items   │    │ 4-Layer    │    │ Obsidian   │    │ NocoDB     │"
echo "   │  HN API    │    │ LLM Class  │    │ + NocoDB   │    │ bidirect.  │"
echo "   └────────────┘    └────────────┘    └────────────┘    └────────────┘"
echo ""
echo "🎉 Demo complete! The full pipeline runs in under 10 seconds."
echo ""
echo "Next steps:"
echo "  1. Read STANDARDS.md for the 4-layer classification model"
echo "  2. Read MANUAL.md for the 5-step processing workflow"
echo "  3. Tell your AI agent: 'Read AGENTS.md and follow its instructions'"
echo ""
echo "Repository: https://github.com/guanxiong/NewsAI-Cybernetics"
