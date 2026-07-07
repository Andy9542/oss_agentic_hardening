#!/usr/bin/env python3
"""Validate Obsidian .base JSON files (minimal schema)."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def validate(data: dict) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["Root must be a JSON object"]
    if "views" not in data:
        errors.append("Missing 'views' array")
    else:
        views = data["views"]
        if not isinstance(views, list) or len(views) == 0:
            errors.append("'views' must be a non-empty array")
        else:
            for i, v in enumerate(views):
                if not isinstance(v, dict):
                    errors.append(f"views[{i}] must be object")
                    continue
                if "name" not in v:
                    errors.append(f"views[{i}] missing 'name'")
                if "type" not in v:
                    errors.append(f"views[{i}] missing 'type'")
    return errors


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: validate_base_json.py <file.base>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"FAIL {path}: invalid JSON: {e}")
        return 1
    errs = validate(data)
    if errs:
        print(f"FAIL {path}:")
        for e in errs:
            print(f"  - {e}")
        return 1
    print(f"OK {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
