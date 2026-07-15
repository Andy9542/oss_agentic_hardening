# Конвенции vault oss_agentic_hardening

Корень vault = корень репозитория. Открывать в Obsidian как vault.

## Карта папок

| Папка | Назначение |
|-------|------------|
| `05-risks/` | OWASP ASI01–ASI10, LLM01–LLM10 |
| `10-methods/` | Все 46 способов защиты (тег `agent-security`) |
| `20-implementations/` | Каталог `repo-NN-*` + детали `detail/` |
| `30-mocs/` | Home, MOC, матрица угроз, выводы, кластеры |
| `40-sources/` | Первоисточники и papers |
| `90-templates/` | `TPL-method.md`, `TPL-repo-catalog.md`, `TPL-implementation.md` |

## Pipeline (не трогать без явного запроса)

- `claude/` — карточки v1.1
- `preflight/` — эталоны, handoff
- `research/` — аудиты батчей

## Плагины Obsidian

- **Dataview** — таблицы реализаций в method notes; не удалять блоки ` ```dataview ` при правках
- wikilink-types, graph-link-types

## Шаблоны

- Новый способ: `90-templates/TPL-method.md` → `10-methods/NN-slug.md`
- Новый репозиторий в каталоге: `90-templates/TPL-repo-catalog.md` → `20-implementations/repo-NN-slug.md`
- Новый детальный разбор: `90-templates/TPL-implementation.md` → `20-implementations/detail/*.md`
- Новый источник: frontmatter `type: source`, раздел «Связи» с wikilink на способы и/или `repo-*`
- Корневые `20-implementations/impl-*.md` не создавать

## Глубина detail-заметок

`detail/*` — педагогический слой: не только имя технологии, но объяснение «что это», пошаговый алгоритм, конкретные артефакты из кода (regex, правило политики, порог модели, AST-паттерн) и мини-пример «вход → решение». Ориентир 80–180 строк на один механизм. Каталог `repo-*` остаётся кратким обзором со ссылками на detail.

## Матрица угроз

После изменения `covers:` или оценок в method notes:

```bash
python _gen_matrix.py > "30-mocs/MOC — Матрица угроз.md"
```

## Набор способов

- ID: 1 … 45 и 46* (расширение набора)
- Имена файлов: slug без папки в wikilink; исторически часть slug русские (`01-классификация-инъекций-машинным-обучением.md`), часть английские (`02-cot-reasoning-audit.md`)
- Перекрёстные упоминания между способами — только текст «способ №N», без wikilink
