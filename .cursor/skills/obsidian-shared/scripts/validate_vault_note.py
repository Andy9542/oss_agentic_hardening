#!/usr/bin/env python3
"""Validate Obsidian vault note conventions for oss_agentic_hardening."""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore

WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|#]+)?(?:\|[^\]]+)?\]\]")
FRONTMATTER = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
METHOD_ID = re.compile(r"^method-id:\s*\d+\s*$", re.MULTILINE)


def classify(path: Path) -> str:
    parts = path.parts
    if "10-methods" in parts:
        return "method"
    if "20-implementations" in parts:
        return "implementation"
    if "40-sources" in parts:
        return "source"
    if "30-mocs" in parts:
        return "moc"
    return "other"


def parse_frontmatter(text: str) -> dict | None:
    m = FRONTMATTER.match(text)
    if not m:
        return None
    blob = m.group(1)
    if yaml is not None:
        try:
            return yaml.safe_load(blob) or {}
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML frontmatter: {e}") from e
    return {"_raw": blob}


def has_method_id(text: str, fm: dict | None) -> bool:
    if fm and "method-id" in fm:
        return True
    return bool(METHOD_ID.search(text))


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    kind = classify(path)

    try:
        fm = parse_frontmatter(text)
    except ValueError as e:
        return [str(e)]

    if fm is None and kind in ("method", "implementation", "source"):
        errors.append("Missing YAML frontmatter (--- ... ---)")

    yaml_blob = FRONTMATTER.match(text)
    body_links = WIKILINK.findall(text)
    if yaml_blob:
        body_links = WIKILINK.findall(text[yaml_blob.end() :])

    if kind == "method":
        for target in body_links:
            slug = target.split("/")[-1]
            if re.match(r"\d{2}-", slug) and slug != path.stem:
                errors.append(
                    f"Wikilink to method [[{target}]] in 10-methods/ body — use «способ №N»"
                )

    if kind == "implementation":
        section = text.split("## Связи", 1)[1] if "## Связи" in text else ""
        sec_links = WIKILINK.findall(section)
        if len(sec_links) != 1:
            errors.append(
                f"Implementation must have exactly 1 wikilink in «Связи»; found {len(sec_links)}"
            )
        if not has_method_id(text, fm):
            errors.append("Implementation missing method-id in frontmatter")

    if kind == "source":
        if "## Связи" not in text:
            errors.append("Source note should have «Связи» section with wikilinks to methods")

    return errors


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: validate_vault_note.py <note.md> [note2.md ...]", file=sys.stderr)
        return 2
    ok = True
    for arg in sys.argv[1:]:
        p = Path(arg)
        errs = validate(p)
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
