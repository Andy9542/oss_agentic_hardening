# Правила связей (выжимка)

Полный текст: `30-mocs/Правила связей.md` в vault. **Не добавлять wikilink на этот файл** из заметок.

## Три типа wikilink

| Тип | Направление | Где |
|-----|-------------|-----|
| Навигация | MOC / Home → способ | `30-mocs/` |
| Происхождение | Источник → способ | `40-sources/`, раздел «Связи» |
| Реализация | Реализация → способ | `20-implementations/`, раздел «Связи» |

## Запрещено

- Wikilink между двумя заметками из `10-methods/`
- Wikilink из способа на реализацию или источник (Dataview + `sources:` достаточно)
- Wikilink на `Правила связей.md`

## YAML без скобок

```yaml
complements:
  - 16-ifc-capability-taint
requires:
  - 14-default-deny-allowlists
sources:
  - source-progent-smt
covers:
  - ASI02
  - LLM06
```

`covers:` — только ASI01…ASI10 и LLM01…LLM10.

## Prose

В тексте: **«способ №N (краткое имя)»**, не `[[wikilink]]`, если это не навигация/MOC.

## Реализации

- `method-id: <число>` в frontmatter
- Ровно **один** wikilink в «Связи»: `[[02-cot-reasoning-audit]]` (slug файла без `.md`)

## Источники

- `sources:` в method → имена файлов из `40-sources/`
- В source note — wikilink на способы в «Связи»

## Фильтр графа

```
-path:20-implementations -path:40-sources -path:90-templates
```
