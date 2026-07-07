# Composition workflows (oss_agentic_hardening)

Orchestrate skills — read each SKILL.md, do not duplicate instructions.

## Pipeline default

```
obsidian-defuddle (optional URL)
  → obsidian-vault (create/update file)
  → obsidian-markdown (lint + link rules)
  → obsidian-bases / obsidian-json-canvas (optional views)
```

## Recipe 1: New source from URL

1. **obsidian-defuddle** — clip to `40-sources/source-<slug>.md`
2. **obsidian-vault** — add slug to method `sources:` in frontmatter
3. **obsidian-markdown** — lint both files
4. User: regen matrix if `covers:` changed

## Recipe 2: New implementation

1. **obsidian-vault** — copy `90-templates/TPL-implementation.md` → `20-implementations/impl-<name>.md`
2. Set `method-id`, fill repo/verdict; **one** wikilink in «Связи»
3. **obsidian-markdown** + **validate_vault_note.py**

## Recipe 3: Research clip + pipeline link

1. **obsidian-defuddle** — save summary to `research/<topic>.md`
2. Link in prose to `research/composer/` or `claude/card-*.md` (no wikilink into pipeline unless MOC)
3. **obsidian-markdown** lint

## Recipe 4: Demo canvas for talk

1. Pick method chain from §12 demos (e.g. №6→№10→№16)
2. **obsidian-json-canvas** — `30-mocs/demo-<name>.canvas`
3. **obsidian-vault** — optional note linking canvas from MOC

## Skill routing

| User intent | Start with |
|-------------|------------|
| Read/search vault | obsidian-vault |
| Fix wikilink/YAML | obsidian-markdown |
| Table over notes | obsidian-bases |
| Visual board | obsidian-json-canvas |
| Save URL | obsidian-defuddle |
| Multi-step / unclear | obsidian-suite (this doc) |

## Article reference

Inspired by [DEV: Building Claude Skills for Obsidian](https://dev.to/scorp323/building-claude-skills-that-connect-to-obsidian-a-developers-field-guide-4a2k) — adapted for Cursor agent tools, not slash commands.
