# Конвенции vault oss_agentic_hardening

Корень vault = корень репозитория. Открывать в Obsidian как vault.

## Карта папок

| Папка | Назначение |
|-------|------------|
| `05-risks/` | OWASP ASI01–ASI10, LLM01–LLM10 |
| `10-methods/` | Все 46 способов защиты (тег `agent-security`) |
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

## Набор способов

- ID: 1 … 45 и 46* (расширение набора)
- Имена файлов: slug без папки в wikilink; исторически часть slug русские (`01-классификация-инъекций-машинным-обучением.md`), часть английские (`02-cot-reasoning-audit.md`)
- Перекрёстные упоминания между способами — только текст «способ №N», без wikilink
