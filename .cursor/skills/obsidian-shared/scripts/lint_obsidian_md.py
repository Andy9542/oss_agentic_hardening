#!/usr/bin/env python3
"""Lint Obsidian Markdown syntax and project link rules."""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

FRONTMATTER = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
WIKILINK_FULL = re.compile(r"\[\[([^\]]+)\]\]")
WIKILINK = re.compile(r"\[\[([^\]|#]+)")


def wikilink_target(raw: str) -> str:
    """Target part of a wikilink body: strip alias (incl. escaped \\|) and anchor."""
    return re.split(r"\\\||\|", raw)[0].split("#")[0].strip().rstrip("\\")


def lint(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    rel = str(path)

    for m in WIKILINK_FULL.finditer(text):
        if "/" in wikilink_target(m.group(1)):
            errors.append(
                f"Wikilink target contains path separator — use [[slug]] not [[folder/slug]]: [[{m.group(1)}]]"
            )
            break

    if "10-methods" in rel:
        for m in WIKILINK.finditer(text):
            target = m.group(1).strip()
            if re.match(r"\d{2}-", target) and target != path.stem:
                errors.append(f"Cross-method wikilink [[{target}]] in 10-methods/ — forbidden")

    fm = FRONTMATTER.match(text)
    if fm:
        blob = fm.group(1)
        if yaml:
            try:
                data = yaml.safe_load(blob)
            except yaml.YAMLError as e:
                errors.append(f"Invalid YAML: {e}")
                data = None
            if data and "10-methods" in rel:
                for field in ("complements", "requires", "not-replaces", "sources"):
                    val = data.get(field)
                    if isinstance(val, list):
                        for item in val:
                            if isinstance(item, str) and ("[[" in item or "/" in item):
                                errors.append(
                                    f"{field} must be slug without [[ or /]: {item!r}"
                                )
        if "10-methods" in rel and "agent-security" not in blob:
            errors.append("Method note should have tag agent-security")

    return errors


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: lint_obsidian_md.py <file.md> ...", file=sys.stderr)
        return 2
    ok = True
    for arg in sys.argv[1:]:
        p = Path(arg)
        errs = lint(p)
        if errs:
            ok = False
            print(f"FAIL {p}:")
            for e in errs:
                print(f"  - {e}")
        else:
            print(f"OK {p}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
