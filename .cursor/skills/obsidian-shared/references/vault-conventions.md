# Конвенции vault oss_agentic_hardening

Корень vault = корень репозитория. Открывать в Obsidian как vault.

## Карта папок

| Папка | Назначение |
|-------|------------|
| `05-risks/` | OWASP ASI01–ASI10, LLM01–LLM10 |
| `10-methods/` | Способы защиты (тег `even-batch`, 23 чётных) |
| `20-implementations/` | OSS/продуктовые реализации |
| `30-mocs/` | Home, MOC, матрица угроз, выводы |
| `40-sources/` | Первоисточники и papers |
| `90-templates/` | `TPL-method.md`, `TPL-implementation.md` |

## Pipeline (не трогать без явного запроса)

- `claude/` — карточки v1.1
- `preflight/` — эталоны, handoff
- `research/` — аудиты батчей

## Плагины Obsidian

- **Dataview** — таблицы реализаций в method notes; не удалять блоки ` ```dataview ` при правках
- wikilink-types, graph-link-types

## Шаблоны

- Новый способ: `90-templates/TPL-method.md` → `10-methods/NN-slug.md`
- Новая реализация: `90-templates/TPL-implementation.md` → `20-implementations/impl-*.md`
- Новый источник: frontmatter `type: source`, раздел «Связи» с wikilink на способы

## Матрица угроз

После изменения `covers:` или оценок в method notes:

```bash
python _gen_matrix.py > "30-mocs/MOC — Матрица угроз.md"
```

## Чётный набор

- ID: 2, 4, 6 … 44, 46* (расширение)
- Имена файлов: `02-cot-reasoning-audit.md` (slug без папки в wikilink)
- Нечётные способы (№1, 3 … 45) — в ветке `odd_protections`, в этом vault только текст «способ №N»

## Связь с odd_protections

Parallel vault: общие `05-risks/` и шаблоны, без файлов нечётных способов.
