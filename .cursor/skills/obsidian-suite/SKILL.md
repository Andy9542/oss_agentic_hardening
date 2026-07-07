---
name: obsidian-suite
description: >-
  Orchestrate Obsidian skills for oss_agentic_hardening vault: defuddle → vault → markdown →
  bases/canvas. Use when the user wants a multi-step vault workflow, full ingest pipeline,
  «добавь источник и свяжи со способом», «создай реализацию и проверь», research clip plus
  method update, or any task touching 2+ of: URL clip, new note, lint, base view, canvas.
  Start here when unsure which obsidian-* skill to use first.
---

# Obsidian Suite

Router and composition layer for vault work.

## Read first

[composition-workflows.md](references/composition-workflows.md)

## Child skills

| Skill | Role |
|-------|------|
| [obsidian-vault](../obsidian-vault/SKILL.md) | Read/write/search |
| [obsidian-markdown](../obsidian-markdown/SKILL.md) | Syntax + link rules |
| [obsidian-defuddle](../obsidian-defuddle/SKILL.md) | URL → note |
| [obsidian-bases](../obsidian-bases/SKILL.md) | .base views |
| [obsidian-json-canvas](../obsidian-json-canvas/SKILL.md) | .canvas maps |

Shared: [vault-conventions.md](../obsidian-shared/references/vault-conventions.md)

## Default algorithm

1. Classify intent (single vs multi-step)
2. If URL involved → **obsidian-defuddle**
3. File ops → **obsidian-vault**
4. Always lint → **obsidian-markdown** + validate scripts
5. Optional visualization → bases or canvas skill

## Do not

- Edit `claude/`, `preflight/` without explicit user request
- Skip validators on new implementation/source notes
