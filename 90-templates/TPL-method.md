---
type: method
id: 0
layer: text
method-type: D
prod-viable: unknown
effectiveness: unknown
robustness: unknown
evidence-level: unknown
status: draft
sources: []
tags:
  - agent-security
  - even-batch # для нечётных способов — odd-batch
covers: []
---

# {{название}}

## Определение

## Как это работает пошагово

## От чего защищает

## От чего НЕ защищает

Используй «способ №N», не wikilink, если ссылка только поясняющая.

## Алгоритмы и механизмы (подробно)

## Реализации

> Реализации: поле `method-id` в frontmatter (`20-implementations/`), без wikilink.

```dataview
TABLE verdict AS "Вердикт", repo AS "Репозиторий"
FROM "20-implementations"
WHERE method-id = this.id
SORT file.name
```

## Доказательная база

Список имён файлов из `sources:` в YAML, **без** `[[wikilink]]`.

## Покрытие рисков

Коды в YAML `covers:` — только **ASI01**…**ASI10** и **LLM01**…**LLM10**. Оценки согласованы со строками [[MOC — Матрица угроз]] (по **сценарию**, не только по коду OWASP).

| Риск | Сценарий в матрице | Уровень | Почему такая оценка |
|------|--------------------|---------|---------------------|
| ASI01 | краткое имя сценария | выс./ср./низ./— | Механизм способа в этом сценарии: что перекрывает и где граница. |
| LLM02 | ↳ уточнение | ср. | … |

Если способ не попадает в строку матрицы — риск не включайте в `covers:`.

## Оценка эффективности

## Оценка прочности

## Дополняет

Только «способ №N (краткое имя)» — **без wikilink**. Slug в YAML `complements:`.

## Требует

Условия или способы без wikilink. Slug в YAML `requires:`.

## Не заменяет

Способы с другой зоной ответственности — текст «способ №N», slug в YAML `not-replaces:`.
