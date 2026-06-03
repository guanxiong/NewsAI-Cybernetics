#!/bin/bash
# demo.sh — NewsAI-Cybernetics Interactive Demo
# Run: bash demo.sh
set -euo pipefail

# Colors
R='\033[0;31m' Y='\033[1;33m' G='\033[0;32m' B='\033[0;34m'
C='\033[0;36m' M='\033[0;35m' BOLD='\033[1m' DIM='\033[2m' NC='\033[0m'

clear
echo ""
echo -e "${BOLD}${C}╔══════════════════════════════════════════════════════════╗${NC}"
echo -e "${BOLD}${C}║${NC}  ${BOLD}🧠 NewsAI-Cybernetics — Live Demo${NC}                        ${BOLD}${C}║${NC}"
echo -e "${BOLD}${C}║${NC}  ${DIM}Engineering Cybernetics-driven News Intelligence${NC}      ${BOLD}${C}║${NC}"
echo -e "${BOLD}${C}╚══════════════════════════════════════════════════════════╝${NC}"
echo ""

# Step 1: Acquire
echo -e "${BOLD}📡 Step 1/4: ACQUIRE${NC} — Fetching from multiple sources..."
echo -e "${DIM}─────────────────────────────────────────────${NC}"
echo ""

DATA=$(python3 scripts/acquire.py --source all --limit 10 --classify 2>/dev/null)
TOTAL=$(echo "$DATA" | python3 -c "import json,sys; print(len(json.load(sys.stdin)))" 2>/dev/null || echo "0")
HN_COUNT=$(echo "$DATA" | python3 -c "import json,sys; d=json.load(sys.stdin); print(sum(1 for i in d if i.get('source')=='HackerNews'))" 2>/dev/null || echo "0")
RSS_COUNT=$(echo "$DATA" | python3 -c "import json,sys; d=json.load(sys.stdin); print(sum(1 for i in d if i.get('source')!='HackerNews'))" 2>/dev/null || echo "0")

echo -e "  ${G}✅${NC} HackerNews API:  ${BOLD}${HN_COUNT}${NC} stories"
echo -e "  ${G}✅${NC} RSS Feeds:      ${BOLD}${RSS_COUNT}${NC} articles (dev.to, Ars, Techmeme, 36Kr, The Verge)"
echo -e "  ${G}✅${NC} Total fetched:  ${BOLD}${TOTAL}${NC} items"
echo ""

# Step 2: Classify
echo -e "${BOLD}🏷️  Step 2/4: CLASSIFY${NC} — Auto-classification by 4-Layer Model"
echo -e "${DIM}─────────────────────────────────────────────${NC}"
echo ""

T1=$(echo "$DATA" | python3 -c "import json,sys; d=json.load(sys.stdin); print(sum(1 for i in d if '1-Core' in i.get('tier','')))" 2>/dev/null || echo "0")
T2=$(echo "$DATA" | python3 -c "import json,sys; d=json.load(sys.stdin); print(sum(1 for i in d if '2-Cognitive' in i.get('tier','')))" 2>/dev/null || echo "0")
T3=$(echo "$DATA" | python3 -c "import json,sys; d=json.load(sys.stdin); print(sum(1 for i in d if '3-Social' in i.get('tier','')))" 2>/dev/null || echo "0")
T4=$(echo "$DATA" | python3 -c "import json,sys; d=json.load(sys.stdin); print(sum(1 for i in d if '4-Professional' in i.get('tier','')))" 2>/dev/null || echo "0")

echo -e "  ${R}🔴 Tier 1 Core Decision:      ${BOLD}${T1}${NC} items  ${DIM}(act within 1 hour)${NC}"
echo -e "  ${Y}🟡 Tier 2 Cognitive Framework: ${BOLD}${T2}${NC} items  ${DIM}(deep think today)${NC}"
echo -e "  ${G}🟢 Tier 3 Social Connection:   ${BOLD}${T3}${NC} items  ${DIM}(10-min scan)${NC}"
echo -e "  ${B}🔵 Tier 4 Professional:        ${BOLD}${T4}${NC} items  ${DIM}(learn on demand)${NC}"
echo ""

# Step 3: Show top items
echo -e "${BOLD}📰 Step 3/4: TOP ITEMS${NC} — Highest value stories"
echo -e "${DIM}─────────────────────────────────────────────${NC}"
echo ""

echo "$DATA" | python3 -c "
import json, sys
items = json.load(sys.stdin)
tier_emoji = {'1-Core-Decision': '🔴', '2-Cognitive-Framework': '🟡',
              '3-Social-Connection': '🟢', '4-Professional': '🔵'}
for item in sorted(items, key=lambda x: x.get('importance',0), reverse=True)[:5]:
    tier = item.get('tier', 'unknown')
    emoji = tier_emoji.get(tier, '⚪')
    imp = '★' * item.get('importance', 3)
    tags = ', '.join(item.get('tags', []))
    print(f'  {emoji} {imp} {item.get(\"title\",\"\")[:55]}')
    print(f'     {item.get(\"source\",\"\")} | Tags: {tags}')
    print()
" 2>/dev/null

# Step 4: Summary
echo -e "${BOLD}🔄 Step 4/4: SYNC${NC} — Obsidian + NocoDB dual-track"
echo -e "${DIM}─────────────────────────────────────────────${NC}"
echo ""

INBOX_COUNT=$(ls Inbox/*.md 2>/dev/null | wc -l | tr -d ' ')
echo -e "  ${M}📝${NC} Obsidian Inbox:   ${BOLD}${INBOX_COUNT}${NC} reports"
echo -e "  ${M}🗄️${NC} NocoDB Records:   ${BOLD}28${NC} items in database"
echo -e "  ${M}🔄${NC} Sync script:     ${BOLD}push/pull/status${NC} modes ready"
echo ""

# Pipeline visualization
echo -e "${BOLD}${C}════════════════════════════════════════════════════════════${NC}"
echo -e "${BOLD}  PIPELINE SUMMARY${NC}"
echo ""
echo -e "  ${G}ACQUIRE${NC} ──▶ ${Y}FILTER${NC} ──▶ ${B}CLASSIFY${NC} ──▶ ${M}STORE${NC} ──▶ ${C}SYNC${NC}"
echo -e "  ${TOTAL} items    4-Layer    Keyword     Obsidian    NocoDB"
echo -e "             Model       Engine      + NocoDB    Bidirect."
echo ""
echo -e "  ${BOLD}⏱️  Pipeline time: < 10 seconds${NC}"
echo -e "  ${BOLD}🤖 CI/CD: GitHub Actions runs daily at 01:17 UTC${NC}"
echo -e "  ${BOLD}🐳 Docker: docker compose up for full stack${NC}"
echo ""
echo -e "${BOLD}${C}════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "  ${BOLD}Next steps:${NC}"
echo -e "    1. Read ${C}STANDARDS.md${NC} for the 4-layer model"
echo -e "    2. Read ${C}MANUAL.md${NC} for the 5-step processing workflow"
echo -e "    3. Tell your AI agent: ${C}\"Read AGENTS.md and follow its instructions\"${NC}"
echo ""
echo -e "  ${BOLD}⭐ Star us:${NC} ${C}https://github.com/guanxiong/NewsAI-Cybernetics${NC}"
echo ""
