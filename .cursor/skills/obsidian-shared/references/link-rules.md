# Правила связей (выжимка)

Полный текст: `30-mocs/Правила связей.md` в vault. **Не добавлять wikilink на этот файл** из заметок.

## Типы wikilink

| Тип | Направление | Где |
|-----|-------------|-----|
| Навигация | MOC / Home → способ | `30-mocs/` |
| Происхождение | Источник → способ / repo | `40-sources/`, раздел «Связи» |
| Каталог → способ | `repo-NN` → способ | `20-implementations/repo-*.md` |
| Каталог → семейство | `repo-NN` → `cluster-*` | поле `clusters:` |
| Деталь → каталог | `detail/*` → `repo-NN` | `20-implementations/detail/` |

**Запрещено:** прямые wikilink между двумя `repo-*`.

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

- Каталог: `type: repo-catalog`, `catalog-id`, `method-id`, `also-method-ids`, `clusters`
- Деталь: `type: implementation-detail`, `parent-repo: repo-NN-slug`, один wikilink на каталог
- Dataview в способах фильтрует только `repo-catalog` по `method-id` и `also-method-ids`

## Источники

- `sources:` в method → имена файлов из `40-sources/`
- В source note — wikilink на способы и при необходимости на `repo-*`

## Фильтр графа

```
-path:20-implementations -path:40-sources -path:90-templates
```
