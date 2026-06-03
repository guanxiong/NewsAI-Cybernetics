#!/bin/bash
# acquire-hn.sh — Fetch top Hacker News stories and output as JSON for Agent processing
# Usage: bash acquire-hn.sh [limit]
# Output: JSON array of {id, title, url, score, by, time}

set -euo pipefail

LIMIT="${1:-30}"
HN_API="https://hacker-news.firebaseio.com/v0"

# Fetch top story IDs
STORY_IDS=$(curl -s "${HN_API}/topstories.json" | python3 -c "
import json, sys
ids = json.load(sys.stdin)[:${LIMIT}]
print(json.dumps(ids))
")

echo '[' > /tmp/hn-items.json
FIRST=true

for ID in $(echo "$STORY_IDS" | python3 -c "import json,sys;[print(i) for i in json.load(sys.stdin)]"); do
    ITEM=$(curl -s "${HN_API}/item/${ID}.json")
    if [ "$FIRST" = true ]; then
        FIRST=false
    else
        echo ',' >> /tmp/hn-items.json
    fi
    echo "$ITEM" | python3 -c "
import json, sys, datetime
item = json.load(sys.stdin)
if item.get('type') != 'story' or not item.get('url'):
    sys.exit(0)
ts = datetime.datetime.fromtimestamp(item.get('time', 0)).strftime('%Y-%m-%d')
out = {
    'id': item.get('id'),
    'title': item.get('title', ''),
    'url': item.get('url', ''),
    'score': item.get('score', 0),
    'author': item.get('by', ''),
    'date': ts,
    'descendants': item.get('descendants', 0),
    'source': 'HackerNews'
}
print(json.dumps(out, ensure_ascii=False))
" >> /tmp/hn-items.json
done

echo ']' >> /tmp/hn-items.json

# Pretty print
python3 -c "
import json
with open('/tmp/hn-items.json') as f:
    items = json.load(f)
print(json.dumps(items, indent=2, ensure_ascii=False))
print(f'\n--- Fetched {len(items)} HN stories ---', file=sys.stderr)
" 1>&2

cat /tmp/hn-items.json
