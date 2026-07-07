---
name: obsidian-defuddle
description: >-
  Clip web pages into clean Obsidian notes for oss_agentic_hardening vault (40-sources/ or research/).
  Use when the user shares a URL, asks to save a paper/blog/docs page to the vault, mentions
  defuddle, web clip, «сохрани статью в obsidian», ingest external source, or add OWASP/arXiv
  reference. Always follow with obsidian-markdown lint and link to affected methods in Связи.
---

# Obsidian Defuddle

URL → clean markdown note in vault.

## References

- [vault-conventions.md](../obsidian-shared/references/vault-conventions.md)
- [link-rules.md](../obsidian-shared/references/link-rules.md)

## Workflow

1. **Fetch** — WebFetch or `curl` the URL
2. **Clean** — remove nav, ads, cookie banners, footer; keep title, author, date, main content
3. **Frontmatter** for `40-sources/`:

```yaml
---
type: source
tags:
  - agent-security
source_url: https://...
date: YYYY-MM-DD
---
```

4. **Filename** — `40-sources/source-<slug>.md` (kebab-case)
5. **Body** — `# Title`, summary, key quotes (blockquoted), optional structure
6. **Связи** — wikilinks to affected methods:

```markdown
## Связи

- [[02-cot-reasoning-audit]]
```

7. Update method `sources:` in YAML (slug without brackets) via **obsidian-vault**
8. **Lint**:

```bash
python .agents/skills/obsidian-shared/scripts/lint_obsidian_md.py <file>
python .agents/skills/obsidian-shared/scripts/validate_vault_note.py <file>
```

## Optional CLI

If [defuddle](https://github.com/kepano/defuddle) installed:

```bash
bash .agents/skills/obsidian-defuddle/scripts/clip_url.sh "<url>" "40-sources/source-slug.md"
```

Otherwise WebFetch + manual cleanup is the default path.

## Placement

| Content | Folder |
|---------|--------|
| Primary reference | `40-sources/` |
| Working notes / clip summary | `research/` |

Do not write into `claude/` or `preflight/` unless user explicitly asks.

## Pair with

- **obsidian-vault** — update method `sources:` fields
- **obsidian-suite** — full ingest pipeline
