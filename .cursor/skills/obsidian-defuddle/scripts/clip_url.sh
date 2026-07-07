#!/usr/bin/env bash
# Optional fast path if defuddle CLI is installed (https://github.com/kepano/defuddle)
set -euo pipefail
URL="${1:?Usage: clip_url.sh <url>}"
OUT="${2:?Usage: clip_url.sh <url> <output.md>}"
if command -v defuddle >/dev/null 2>&1; then
  defuddle "$URL" -o "$OUT"
  echo "Clipped via defuddle CLI -> $OUT"
else
  echo "defuddle not installed; use WebFetch + obsidian-defuddle skill manual cleanup" >&2
  exit 1
fi
