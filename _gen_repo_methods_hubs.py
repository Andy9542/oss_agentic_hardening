#!/usr/bin/env python3
"""Sync «Реализуемые способы» wikilinks into repo catalog notes (direct, no *-methods hubs)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent
METHODS_DIR = ROOT / "10-methods"
REPO_DIR = ROOT / "20-implementations"
DETAIL_DIR = REPO_DIR / "detail"

FRONTMATTER = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
EXTRA_METHODS = re.compile(
    r"дополнительно перекрывает:\s*(.+?)(?:\n|$)", re.IGNORECASE
)
METHOD_NUM = re.compile(r"способ\s*№(\d+)")
METHODS_SECTION = re.compile(
    r"## Реализуемые способы\n(?:.*?\n)*?(?=\n## |\Z)", re.MULTILINE
)
SVIAZI_SECTION = re.compile(r"\n## Связи\n(?:.*?\n)*?(?=\n## |\Z)")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def load_method_slugs() -> dict[int, str]:
    mapping: dict[int, str] = {}
    for path in sorted(METHODS_DIR.glob("*.md")):
        m = re.match(r"^(\d+)-", path.stem)
        if m:
            mapping[int(m.group(1))] = path.stem
    return mapping


def parse_frontmatter(text: str) -> dict:
    m = FRONTMATTER.match(text)
    if not m:
        return {}
    return yaml.safe_load(m.group(1)) or {}


def detail_method_ids(parent_stem: str) -> set[int]:
    ids: set[int] = set()
    for path in DETAIL_DIR.glob("*.md"):
        fm = parse_frontmatter(read_text(path))
        if fm.get("parent-repo") == parent_stem:
            mid = fm.get("method-id")
            if isinstance(mid, int):
                ids.add(mid)
    return ids


def catalog_extra_ids(text: str) -> set[int]:
    m = EXTRA_METHODS.search(text)
    if not m:
        return set()
    chunk = m.group(1)
    if chunk.strip() in ("—", "-", "–"):
        return set()
    return {int(x) for x in METHOD_NUM.findall(chunk)}


def patch_frontmatter(text: str, also_ids: list[int]) -> str:
    m = FRONTMATTER.match(text)
    if not m:
        return text
    fm_lines = m.group(1).splitlines()
    new_lines: list[str] = []
    skip_also = False
    inserted = False
    for line in fm_lines:
        if line.startswith("also-method-ids:"):
            skip_also = True
            continue
        if skip_also and line.startswith("  - "):
            continue
        skip_also = False
        new_lines.append(line)
        if line.startswith("method-id:") and also_ids and not inserted:
            new_lines.append("also-method-ids:")
            for aid in also_ids:
                new_lines.append(f"  - {aid}")
            inserted = True
    body = "\n".join(new_lines)
    return text[: m.start(1)] + body + text[m.end(1) :]


def render_methods_section(
    method_ids: list[int], primary_id: int, method_slugs: dict[int, str]
) -> str:
    lines = ["## Реализуемые способы", ""]
    for mid in method_ids:
        slug = method_slugs.get(mid)
        if not slug:
            raise KeyError(f"No method file for id {mid}")
        suffix = " — основной" if mid == primary_id else ""
        lines.append(f"- [[{slug}]]{suffix}")
    lines.append("")
    return "\n".join(lines)


def update_catalog_body(
    text: str,
    method_ids: list[int],
    primary_id: int,
    method_slugs: dict[int, str],
) -> str:
    section = render_methods_section(method_ids, primary_id, method_slugs)
    text = SVIAZI_SECTION.sub("", text)
    if METHODS_SECTION.search(text):
        text = METHODS_SECTION.sub(section, text, count=1)
    elif "## Детальные разборы" in text:
        text = re.sub(
            r"(## Детальные разборы\n(?:.*?\n)*?)(\n## |\Z)",
            r"\1\n" + section + r"\2",
            text,
            count=1,
        )
    else:
        text = text.rstrip() + "\n\n" + section
    return text


def collect_method_ids(text: str, repo_stem: str, primary_id: int) -> list[int]:
    ids: set[int] = {int(primary_id)}
    ids |= catalog_extra_ids(text)
    ids |= detail_method_ids(repo_stem)
    return [int(primary_id)] + sorted(ids - {int(primary_id)})


def process_repo(path: Path, method_slugs: dict[int, str], write: bool) -> list[int]:
    text = read_text(path)
    fm = parse_frontmatter(text)
    repo_stem = path.stem
    primary_id = fm.get("method-id")
    if primary_id is None:
        raise ValueError(f"{path.name}: missing method-id")

    ordered = collect_method_ids(text, repo_stem, int(primary_id))
    also = ordered[1:]
    updated = patch_frontmatter(text, also)
    updated = update_catalog_body(updated, ordered, int(primary_id), method_slugs)

    if write and updated != text:
        path.write_text(updated, encoding="utf-8")

    return ordered


def delete_hubs(write: bool) -> int:
    hubs = list(REPO_DIR.glob("repo-*-methods.md"))
    if write:
        for hub in hubs:
            hub.unlink()
    return len(hubs)


def main() -> int:
    write = "--write" in sys.argv
    method_slugs = load_method_slugs()
    repos = sorted(
        p for p in REPO_DIR.glob("repo-*.md") if not p.stem.endswith("-methods")
    )

    for path in repos:
        ids = process_repo(path, method_slugs, write)
        action = "updated" if write else "dry-run"
        print(f"{action}: {path.name}  methods={ids}")

    hub_count = delete_hubs(write)
    action = "deleted" if write else "would delete"
    print(f"\n{action} {hub_count} hub notes (*-methods.md)", file=sys.stderr)

    if not write:
        print("Re-run with --write to apply.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
