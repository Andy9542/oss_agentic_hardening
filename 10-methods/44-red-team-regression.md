---
type: method
id: 44
layer: meta
method-type: T
prod-viable: true
effectiveness: high
robustness: medium
evidence-level: strong
status: reviewed
tags:
  - agent-security
  - even-batch
sources:
  - source-t3mp3st
  - source-strix
covers: []
---

# Red team probes + regression eval

## Определение

**Тестовый контур**, не prod-защита: адверсариал-пробы (garak), regression eval (promptfoo), automation (PyRIT). Закрывает петлю обратной связи. AgentDojo → способ №45 (нечётный).

## Как это работает пошагово

1. Probe suite в CI (garak/promptfoo).
2. Regression gate: red → merge blocked.
3. офлайн-тест × off-band.

## От чего защищает

- Пробелы в покрытии других классов — **до prod**, если CI gate enforced.

## От чего НЕ защищает

- Runtime атаки; не заменяет №1–№40.

## Реализации

```dataview
TABLE verdict AS "Вердикт", repo AS "Репозиторий"
FROM "20-implementations"
WHERE method-id = this.id
SORT file.name
```

## Покрытие рисков

| Риск | Сценарий в матрице | Уровень | Почему такая оценка |
|------|--------------------|---------|---------------------|
| — | Мета: измеритель покрытия | **мета** | Не runtime-барьер; оценивает стек. |

## Оценка эффективности

**Высокая** как test process; **низкая** как runtime defense.

## Оценка прочности

**Средняя** — stale probes, narrow suite.

## Дополняет

Весь реестр чётных способов — петля обратной связи.

## Требует

CI gate для regression.

## Не заменяет

Prod-барьеры №1–№40.

## Сценический тезис

> Red team в CI — зеркало, не защита: garak и promptfoo показывают, что сломается завтра.

## Демо-кандидат

CI regression gate: probe suite red → merge blocked.
