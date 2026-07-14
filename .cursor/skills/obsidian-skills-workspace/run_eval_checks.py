#!/usr/bin/env python3
"""Run obsidian-skills eval assertions against iteration-1 outputs."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[2]  # .agents/skills/workspace -> repo root


def run_validator(script: str, path: Path) -> bool:
    r = subprocess.run(
        [sys.executable, str(REPO / ".agents/skills/obsidian-shared/scripts" / script), str(path)],
        capture_output=True,
        text=True,
    )
    return r.returncode == 0


def main() -> int:
    results = []
    impl = ROOT / "iteration-1/eval-vault-new-implementation/with_skill/outputs/impl-progent-eval-draft.md"
    results.append(("vault_impl_validate", run_validator("validate_vault_note.py", impl)))

    method = REPO / "10-methods/02-cot-reasoning-audit.md"
    results.append(("method_lint", run_validator("lint_obsidian_md.py", method)))

    base = REPO / "30-mocs/methods-by-layer.base"
    r = subprocess.run(
        [sys.executable, str(REPO / ".agents/skills/obsidian-bases/scripts/validate_base_json.py"), str(base)],
        capture_output=True,
    )
    results.append(("base_valid", r.returncode == 0))

    canvas = REPO / "30-mocs/demo-dlp-chain.canvas"
    r = subprocess.run(
        [sys.executable, str(REPO / ".agents/skills/obsidian-json-canvas/scripts/validate_canvas_json.py"), str(canvas)],
        capture_output=True,
    )
    results.append(("canvas_valid", r.returncode == 0))

    source = REPO / "40-sources/source-progent-smt.md"
    results.append(("source_validate", run_validator("validate_vault_note.py", source)))

    passed = sum(1 for _, ok in results if ok)
    report = {"passed": passed, "total": len(results), "checks": dict(results)}
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
