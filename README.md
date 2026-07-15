# Obsidian vault: чётные способы защиты агентов

Справочник по **23 чётным** методам защиты агентных систем (№2, 4, 6 … 44, 46*). Структура повторяет ветку `odd_protections` (нечётные способы), но содержит только чётную половину.

## Структура

| Папка | Назначение |
|-------|------------|
| `00-terms/` | Словарь терминов агентных систем |
| `03-incidents/` | Публичные инциденты и раскрытия, связанные с рисками |
| `05-risks/` | OWASP Agentic 2026 + LLM 2025 — словарь угроз |
| `10-methods/` | Заметки способов (тег `even-batch`) |
| `20-implementations/` | Реализации OSS/продуктов |
| `30-mocs/` | Home, MOC, матрица угроз, выводы |
| `40-sources/` | Первоисточники и papers |
| `90-templates/` | Шаблоны заметок |

## Pipeline (исходники исследования)

Карточки v1.1 и журнал конвейера **не удалены**:

- `all-methods-top-20.md` — таксономия способов
- `description-top-20.md` — карточки топ-20 инструментов
<<<<<<< Updated upstream
- `github-100-repo.md` — каталог 119 репозиториев
- `30-mocs/MOC — Дополнение обзора 2026.md` — 12 новых реализаций и их связь со способами
- `03-incidents/MOC — Инциденты.md` — 29 событий и disclosures, связанных со всеми 20 карточками рисков
=======
- `github-100-repo.md` — каталог 118 репозиториев
- `30-mocs/MOC — Дополнение обзора 2026.md` — 14 новых реализаций и их связь со способами
>>>>>>> Stashed changes

## Связь с odd_protections

Ветка [`odd_protections`](https://github.com/) содержит **нечётные** способы (№1, 3 … 45) в том же формате vault. Этот репозиторий — **parallel vault**: общие `05-risks/` и шаблоны, но без файлов нечётных способов. Перекрёстные ссылки на нечётные номера — текстом «способ №N», без wikilink (см. `30-mocs/Правила связей.md`).

## Матрица угроз

```bash
python _gen_matrix.py > "30-mocs/MOC — Матрица угроз.md"
```

## Открытие в Obsidian

Откройте корень репозитория как vault. Плагин Dataview нужен для таблиц реализаций в заметках способов.

## Agent skills (Obsidian)

Набор скиллов в [`.agents/skills/`](.agents/skills/) для работы агента с vault (по мотивам [DEV: Obsidian skills](https://dev.to/scorp323/building-claude-skills-that-connect-to-obsidian-a-developers-field-guide-4a2k)):

| Скилл | Назначение |
|-------|------------|
| `obsidian-suite` | Оркестратор: defuddle → vault → markdown → bases/canvas |
| `obsidian-vault` | Чтение/запись/поиск, шаблоны `90-templates/` |
| `obsidian-markdown` | Wikilinks, YAML, callouts, правила связей |
| `obsidian-bases` | Генерация `.base` (пример: `30-mocs/even-methods-by-layer.base`) |
| `obsidian-json-canvas` | Генерация `.canvas` (пример: `30-mocs/demo-dlp-chain.canvas`) |
| `obsidian-defuddle` | URL → заметка в `40-sources/` |

Общие конвенции: `.agents/skills/obsidian-shared/references/vault-conventions.md`

Валидация заметок:

```bash
python .agents/skills/obsidian-shared/scripts/lint_obsidian_md.py <file.md>
python .agents/skills/obsidian-shared/scripts/validate_vault_note.py <file.md>
```

Полный аудит графа:

```bash
python .agents/skills/obsidian-shared/scripts/audit_vault_links.py --report research/composer/audit-links-even-batch.md
```

Eval-набор: `.agents/skills/obsidian-skills-workspace/evals/evals.json`
