#!/usr/bin/env bash
set -e
echo "=== RankHub Deploy ==="
python build.py
git add -A
git commit -m "$(date '+%Y-%m-%d %H:%M') update" || true
git push origin main
echo "✓ Done — check https://github.com/luojun0115/rankhub/actions"
