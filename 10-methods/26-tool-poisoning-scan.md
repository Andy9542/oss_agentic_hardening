---
type: method
id: 26
layer: supply-chain
method-type: S
prod-viable: true
effectiveness: high
robustness: medium
evidence-level: strong
status: reviewed
tags:
  - agent-security
  - even-batch
sources:
  - source-invariant-toxic-flow
covers:
  - ASI04
  - LLM03
  - LLM01
complements:
  - 28-toxic-flow-analysis
  - 32-aibom-inventory
requires:
  - 32-aibom-inventory
---

# Tool poisoning / shadowing scan

## Определение

Скан **метаданных** инструментов: tools/list descriptions, имена, shadowing, unsafe command definitions, rug-pull. Объект = metadata; содержимое skills → способ №27 (нечётный).

## Как это работает пошагово

1. CI или watch сканирует tools/list и skill metadata.
2. Diff с baseline ловит rug-pull и shadowing.
3. SARIF/report для блокировки deploy.
4. pre-deploy + post-factum watch × off-band.

## От чего защищает

- **ASI04** — отравленные descriptions, shadowing.
- **LLM03** — компрометация tool metadata.
- Частично **LLM01** — indirect PI через tool description.

## От чего НЕ защищает

- Содержимое skill-файлов, кода, RAG (№27, №30).
- Рантайм-подмена между сканами.
- Криптоподпись (agentseal не подписывает).

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
| ASI04 | ↳ rug-pull, отравление skill/MCP | **выс.** | Прямая мишень сканера metadata. |
| ASI04 | ↳ вредонос в пакетах и CI | **выс.** | Pre-deploy скан в supply chain. |

## Оценка эффективности

**Высокая** при CI gate на onboarding MCP.

## Оценка прочности

**Средняя** — rug-pull между сканами, семантически невинные descriptions.

## Дополняет

- способ №28 (flow-граф vs metadata)
- способ №32 (inventory)

## Требует

- способ №32 (опционально, субстрат)

## Не заменяет

- способ №27 (содержимое skills)
- криптоподпись артефактов

## Сценический тезис

> Tool poisoning — вредоносность в description инструмента; rug-pull — смена после install; сканер ловит diff, watch ловит смену.

## Демо-кандидат

Benign description → malicious после update; diff подсвечен scanner.
