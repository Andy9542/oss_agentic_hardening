#!/usr/bin/env python3
"""Validate JSON Canvas .canvas files."""
from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED_NODE = {"id", "type", "x", "y", "width", "height"}
REQUIRED_EDGE = {"id", "fromNode", "toNode"}


def validate(data: dict) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["Root must be object"]
    nodes = data.get("nodes")
    edges = data.get("edges")
    if not isinstance(nodes, list):
        errors.append("'nodes' must be array")
        nodes = []
    if not isinstance(edges, list):
        errors.append("'edges' must be array")
        edges = []
    ids = set()
    for i, n in enumerate(nodes):
        if not isinstance(n, dict):
            errors.append(f"nodes[{i}] not object")
            continue
        missing = REQUIRED_NODE - set(n.keys())
        if missing:
            errors.append(f"nodes[{i}] missing: {missing}")
        nid = n.get("id")
        if nid in ids:
            errors.append(f"duplicate node id: {nid}")
        ids.add(nid)
    for i, e in enumerate(edges):
        if not isinstance(e, dict):
            errors.append(f"edges[{i}] not object")
            continue
        missing = REQUIRED_EDGE - set(e.keys())
        if missing:
            errors.append(f"edges[{i}] missing: {missing}")
        if e.get("fromNode") not in ids:
            errors.append(f"edges[{i}] fromNode not found")
        if e.get("toNode") not in ids:
            errors.append(f"edges[{i}] toNode not found")
    return errors


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: validate_canvas_json.py <file.canvas>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"FAIL {path}: {e}")
        return 1
    errs = validate(data)
    if errs:
        print(f"FAIL {path}:")
        for e in errs:
            print(f"  - {e}")
        return 1
    print(f"OK {path} ({len(data.get('nodes', []))} nodes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
