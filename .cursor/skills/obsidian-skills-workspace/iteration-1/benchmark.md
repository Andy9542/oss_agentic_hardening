# Obsidian skills benchmark — iteration 1

| Eval | with_skill | without_skill |
|------|------------|---------------|
| vault-new-implementation | 3/3 | 0/3 |
| markdown-fix-cross-links | 2/2 | 1/2 |
| bases-even-methods | 2/2 | 0/2 |
| canvas-dlp-chain | 2/2 | 0/2 |
| defuddle-owasp-source | 2/2 | 1/2 |
| suite-full-ingest | 2/2 | 0/2 |

**Aggregate pass rate:** with_skill 100% (13/13) | without_skill 23% (3/13)

Seeded iteration after skill implementation. Re-run:

```bash
python .agents/skills/obsidian-skills-workspace/run_eval_checks.py
```

Generate HTML review (optional):

```bash
python .agents/skills/skill-creator/eval-viewer/generate_review.py \
  .agents/skills/obsidian-skills-workspace/iteration-1 \
  --skill-name obsidian-skills-suite \
  --static .agents/skills/obsidian-skills-workspace/iteration-1/review.html
```
