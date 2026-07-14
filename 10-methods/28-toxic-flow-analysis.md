---
type: method
id: 28
layer: supply-chain
method-type: D
prod-viable: true
effectiveness: high
robustness: medium
evidence-level: strong
status: reviewed
tags:
  - agent-security
sources:
  - source-invariant-toxic-flow
  - source-owasp-agentic-2026
covers:
  - ASI01
  - ASI02
  - LLM02
---

# Toxic flow / dataflow analysis

## Определение

Статический анализ **флоу-графа**: узлы = tools/источники, рёбра = переходы данных; trust, sensitivity, sink; скоринг токсичных последовательностей (lethal trifecta). Триада: №15 (rules) / №28 (статика) / №16 (рантайм).

## Как это работает пошагово

1. Построение графа агента из конфигурации tools.
2. Аннотация trust/sensitivity/sink на узлах.
3. Поиск токсичных путей (недоверенный ввод → привилегированный sink).
4. pre-deploy / design-time × офлайн CI.

## От чего защищает

- **ASI01** — пути недоверенного ввода к sink.
- **ASI02** — токсичные последовательности tool-call.
- **LLM02** — пути exfil в графе.

## От чего НЕ защищает

- Рантайм-обход при ветвлении.
- Неполный граф (незаявленный tool).
- Reasoning-hijack без data-flow.

## Реализации

```dataview
TABLE verdict AS "Вердикт", repo AS "Репозиторий"
FROM "20-implementations"
WHERE method-id = this.id
SORT file.name
```

## Доказательная база

- source-invariant-toxic-flow

## Покрытие рисков

| Риск | Сценарий в матрице | Уровень | Почему такая оценка |
|------|--------------------|---------|---------------------|
| ASI01 | Захват цели | **выс.** | Статика lethal trifecta paths. |
| ASI02 | ↳ токсичная цепочка A→B | **выс.** | Скоринг последовательностей. |
| ASI02 | Один опасный вызов | **ср.** | Частично, если путь в графе. |

## Оценка эффективности

**Высокая** в CI для high-risk агентов.

## Оценка прочности

**Средняя** — неполная модель, динамические MCP tools.

## Дополняет

- способ №16 (рантайм IFC)
- способ №15 (декларативные flow rules)
- способ №32 (узлы графа)

## Требует

Актуальная карта tools и trust-модель.

## Не заменяет

- способ №16 (рантайм IFC)

## Сценический тезис

> TFA смотрит на агента как на граф до первого запуска: где приватные данные и недоверенный контент могут встретиться у сетевого выхода.

## Демо-кандидат

Флоу-граф GitHub-MCP-кейса: toxic path подсвечен; D3/постер.
