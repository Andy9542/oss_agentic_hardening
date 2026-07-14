---
name: obsidian-bases
description: >-
  Generate Obsidian Bases (.base) database views for the oss_agentic_hardening vault.
  Use when the user wants a table view, filter, or spreadsheet over notes, mentions
  Obsidian Bases, .base files, «таблица всех способов», «view по layer/tags/method-id»,
  or database-style listing of 10-methods/20-implementations. Use after obsidian-vault
  knows which folder to index.
---

# Obsidian Bases

Generate `.base` JSON for Obsidian 1.8+.

## References

- [bases-schema.md](references/bases-schema.md)
- [vault-conventions.md](../obsidian-shared/references/vault-conventions.md)

## Workflow

1. Clarify: which folder, columns, filters, sort
2. Read [bases-schema.md](references/bases-schema.md)
3. Write `30-mocs/<name>.base` (or user path)
4. Validate:

```bash
python .agents/skills/obsidian-bases/scripts/validate_base_json.py <file.base>
```

5. User opens file in Obsidian to verify UI

## Default views for this repo

- **methods-by-layer.base** — `10-methods/`, filter `type: method`, columns layer, effectiveness, robustness
- **implementations-by-method.base** — `20-implementations/`, column method-id, verdict, repo

## Pair with

- **obsidian-markdown** — not required for .base
- **obsidian-vault** — path placement
