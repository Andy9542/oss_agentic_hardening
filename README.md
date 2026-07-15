# Obsidian vault: способы защиты агентных систем

Справочник по **46 методам** защиты агентных систем (LLM-агентов): атомарные заметки способов, каталог реализаций, карточки рисков OWASP и сводная матрица «риск × способ». Репозиторий открывается в Obsidian как vault.

## Структура

| Папка | Назначение |
|-------|------------|
| `05-risks/` | OWASP Agentic/ASI Top 10 (2026) + LLM Top 10 (2025) — словарь угроз |
| `10-methods/` | Заметки всех 46 способов — ядро графа |
| `20-implementations/` | Реализации OSS/продуктов (связь через `method-id`) |
| `30-mocs/` | `Home`, `MOC — Способы`, матрица угроз, выводы |
| `40-sources/` | Первоисточники и papers |
| `90-templates/` | Шаблоны заметок |

Точка входа — `30-mocs/Home.md`. Навигация по всем способам — `30-mocs/MOC — Способы.md`; синтез оценок — `30-mocs/MOC — Выводы.md`.

## Канонические документы

- `all-methods-top-20.md` — таксономия способов
- `description-top-20.md` — карточки топ-20 инструментов
- `github-100-repo.md` — каталог 112 репозиториев
- `30-mocs/MOC — Дополнение обзора 2026.md` — 12 новых реализаций и их связь со способами

## Матрица угроз

Матрица генерируется скриптом; после изменения `covers:` или оценок в заметках способов:

```bash
python _gen_matrix.py > "30-mocs/MOC — Матрица угроз.md"
```

## Pipeline (архив исследования)

Карточки v1.1 и журнал конвейера **сохранены** как исторические материалы:

- `claude/card-*.md` — карточки конференции
- `preflight/` — эталоны и handoff
- `research/composer/` — аудиты батчей и полная матрица
- `even-methods-checklist.md` — чеклист просмотра

## Открытие в Obsidian

Откройте корень репозитория как vault. Плагин Dataview нужен для таблиц реализаций в заметках способов; также используются wikilink-types и graph-link-types. Граф по умолчанию скрывает реализации и источники (фильтр в настройках графа): `-path:20-implementations -path:40-sources -path:90-templates`.

## Agent skills (Obsidian)

Набор скиллов в [`.cursor/skills/`](.cursor/skills/) для работы агента с vault (по мотивам [DEV: Obsidian skills](https://dev.to/scorp323/building-claude-skills-that-connect-to-obsidian-a-developers-field-guide-4a2k)):

| Скилл | Назначение |
|-------|------------|
| `obsidian-suite` | Оркестратор: defuddle → vault → markdown → bases/canvas |
| `obsidian-vault` | Чтение/запись/поиск, шаблоны `90-templates/` |
| `obsidian-markdown` | Wikilinks, YAML, callouts, правила связей |
| `obsidian-bases` | Генерация `.base` (пример: `30-mocs/methods-by-layer.base`) |
| `obsidian-json-canvas` | Генерация `.canvas` (пример: `30-mocs/demo-dlp-chain.canvas`) |
| `obsidian-defuddle` | URL → заметка в `40-sources/` |

Общие конвенции: `.cursor/skills/obsidian-shared/references/vault-conventions.md`

Валидация заметок:

```bash
python .cursor/skills/obsidian-shared/scripts/lint_obsidian_md.py <file.md>
python .cursor/skills/obsidian-shared/scripts/validate_vault_note.py <file.md>
```
