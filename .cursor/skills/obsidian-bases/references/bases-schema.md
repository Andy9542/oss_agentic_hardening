# Obsidian Bases (.base) — схема

Obsidian 1.8+ database views stored as `.base` JSON files.

## Минимальная структура

```json
{
  "filters": {
    "and": [
      { "field": "tags", "operator": "contains", "value": "even-batch" }
    ]
  },
  "properties": {
    "layer": { "type": "text" },
    "effectiveness": { "type": "text" }
  },
  "views": [
    {
      "name": "Чётные по слою",
      "type": "table",
      "order": ["layer", "file.name", "effectiveness"],
      "sort": [{ "field": "layer", "direction": "asc" }]
    }
  ]
}
```

> Формат эволюцирует с версией Obsidian. При ошибках открытия в UI — сверить с актуальной документацией Obsidian Bases.

## Примеры для этого vault

| View | Папка | Filter |
|------|-------|--------|
| Methods by layer | `10-methods/` | `tags` contains `even-batch` |
| Implementations | `20-implementations/` | `method-id` exists |
| Sources | `40-sources/` | `type` = `source` |

## Размещение

По умолчанию: `30-mocs/*.base` рядом с MOC.

## Validate

```bash
python .agents/skills/obsidian-bases/scripts/validate_base_json.py <file.base>
```
