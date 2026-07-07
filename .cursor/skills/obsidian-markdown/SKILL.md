---
name: obsidian-markdown
description: >-
  Enforce correct Obsidian Markdown syntax for oss_agentic_hardening vault notes.
  Use when creating or editing any .md in 10-methods/, 20-implementations/, 40-sources/,
  30-mocs/, or when the user mentions wikilinks, callouts, frontmatter, YAML, Dataview blocks,
  «исправь синтаксис obsidian», or when links look broken in Obsidian. Use alongside
  obsidian-vault for every vault write — even small edits.
---

# Obsidian Markdown

Ensures Obsidian-flavored Markdown is valid for this vault.

## Before editing

1. [vault-conventions.md](../obsidian-shared/references/vault-conventions.md)
2. [link-rules.md](../obsidian-shared/references/link-rules.md)
3. [syntax.md](references/syntax.md) — full syntax reference

## Workflow

1. Draft or edit content
2. Check wikilinks (slug only, no paths)
3. Check YAML lists (no `[[` in complements/requires/sources)
4. Preserve ` ```dataview ` blocks in method notes
5. Run linter:

```bash
python .agents/skills/obsidian-shared/scripts/lint_obsidian_md.py <file>
```

6. Run vault validator if implementation/source:

```bash
python .agents/skills/obsidian-shared/scripts/validate_vault_note.py <file>
```

## Common fixes

| Mistake | Fix |
|---------|-----|
| `[[10-methods/12-tool-policies]]` | `[[12-tool-policies-yaml-rego]]` |
| Wikilink between two methods in body | «способ №12 (политики tools)» |
| `complements: [[16-ifc]]` | `complements:\n  - 16-ifc-capability-taint` |
| Broken callout `>[!NOTE]` | `> [!NOTE]` with space |

## Pair with

- **obsidian-vault** — file placement and templates
- **obsidian-suite** — multi-step workflows
