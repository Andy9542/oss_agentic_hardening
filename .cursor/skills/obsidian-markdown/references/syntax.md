# Obsidian Markdown — синтаксис

Канон для vault oss_agentic_hardening. Vanilla LLM output is wrong ~60% of the time on Obsidian extensions.

## Wikilinks

```
[[02-cot-reasoning-audit]]
[[02-cot-reasoning-audit|CoT-аудит]]
[[02-cot-reasoning-audit#Покрытие рисков]]
```

- Slug = filename without `.md`, **no folder prefix**
- Never `[[10-methods/02-...]]`

## Callouts

```markdown
> [!NOTE] Заголовок
> Текст callout.
```

Types: NOTE, TIP, WARNING, IMPORTANT, CAUTION, INFO, ABSTRACT, SUMMARY, TODO, FAQ, etc.

## Frontmatter

Valid YAML between `---` fences. Method example:

```yaml
type: method
id: 2
tags:
  - agent-security
covers:
  - ASI01
complements:
  - 16-ifc-capability-taint
```

List values in `complements`/`requires`/`sources` — plain slugs, no `[[ ]]`.

## Embeds

```markdown
![[02-cot-reasoning-audit]]
```

## Mermaid

Fenced block in note body; for complex diagrams prefer **mermaid** skill inline, or **obsidian-json-canvas** for `.canvas` files.

## Dataview (preserve)

Method notes contain:

````markdown
```dataview
TABLE verdict AS "Вердикт", repo AS "Репозиторий"
FROM "20-implementations"
WHERE method-id = this.id
SORT file.name
```
````

Do not remove or break when editing method bodies.

## Project rules (10-methods/)

- Cross-method references in prose: «способ №16 (IFC)», not wikilink
- Tag `agent-security` on all method notes in this vault
- `covers:` only ASI01–ASI10, LLM01–LLM10

## Lint

```bash
python .agents/skills/obsidian-shared/scripts/lint_obsidian_md.py <file.md>
```
