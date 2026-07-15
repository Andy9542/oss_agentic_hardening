---
name: obsidian-vault
description: >-
  Read, write, search, and organize notes in the oss_agentic_hardening Obsidian vault.
  Use whenever the user mentions Obsidian, vault, wikilink, 10-methods, MOC, Dataview,
  implementations, sources, «добавь в справочник», «создай заметку», or edits files under
  05-risks/, 10-methods/, 20-implementations/, 30-mocs/, 40-sources/. Also use before any
  vault file create/update even if the user only says «обнови карточку» or «добавь реализацию».
---

# Obsidian Vault (oss_agentic_hardening)

Filesystem access to the vault. No Obsidian plugin API — use Read/Write/Grep/Glob/Shell.

## Before first action

Read:

1. [vault-conventions.md](../obsidian-shared/references/vault-conventions.md)
2. [link-rules.md](../obsidian-shared/references/link-rules.md)

## Vault root

Repository root (`README.md` describes layout). Open this folder as Obsidian vault.

## Operations

| Task | How |
|------|-----|
| Find note | `Glob **/*.md`, `Grep` by title or `covers:` |
| Read | `Read` path relative to repo root |
| Create method | Copy `90-templates/TPL-method.md` → `10-methods/NN-slug.md` |
| Create repo catalog | Copy `90-templates/TPL-repo-catalog.md` → `20-implementations/repo-NN-slug.md` |
| Create detail | Copy `90-templates/TPL-implementation.md` → `20-implementations/detail/*.md` |
| Create source | `40-sources/source-*.md` with `type: source` |
| Update MOC | Edit `30-mocs/`; regen matrix if `covers:` changed |

## Do not modify without explicit request

`claude/`, `preflight/`, `research/` (pipeline archive).

## After editing `covers:` or risk ratings

```bash
python _gen_matrix.py > "30-mocs/MOC — Матрица угроз.md"
```

## Validation

After create/edit vault notes:

```bash
python .agents/skills/obsidian-shared/scripts/validate_vault_note.py <path>
python .agents/skills/obsidian-shared/scripts/lint_obsidian_md.py <path>
```

## Pair with other skills

- Syntax fixes → **obsidian-markdown**
- URL clip → **obsidian-defuddle** then write here
- Multi-step → **obsidian-suite**
