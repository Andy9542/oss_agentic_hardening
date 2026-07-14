---
type: method
id: 42
layer: dialog
method-type: D
prod-viable: true
effectiveness: medium
robustness: medium
evidence-level: strong
status: reviewed
tags:
  - agent-security
sources: []
covers:
  - ASI09
  - ASI01
complements:
  - 08-toxicity-moderation
  - 12-tool-policies-yaml-rego
---

# Rails (Colang)

## Определение

Ядро: **dialog rails** (Colang) + canonical form matching. Не дублировать: input rails → №1; output rails → №8; execution rails → №12.

## Как это работает пошагово

1. User intent сопоставляется с canonical forms.
2. Dialog state machine ограничивает допустимые ветки.
3. Off-topic / manipulative paths — block.
4. pre-model / CoT (диалоговый план) × inline.

## От чего защищает

- **ASI09** Human-Agent Trust Exploitation (off-topic paths).
- Частично **ASI01** — удержание в dialog flow.

## От чего НЕ защищает

- Tool misuse (№12); data-flow (№16).
- Сложный PI вне dialog patterns.

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
| ASI09 | Обман оператора | **ср.** | Dialog flow constraints. |
| ASI01 | Захват цели | **низ.** | Узко через dialog, не PI в целом. |

## Оценка эффективности

**Средняя** для dialog-heavy agents.

## Оценка прочности

**Средняя** — неполный Colang coverage.

## Дополняет

- способ №1 (input), №8 (output), №12 (execution)

## Требует

—

## Не заменяет

- способ №2 (CoT-аудит — другой объект)

## Сценический тезис

> Colang rails — не ещё один фильтр токсичности; ядро — dialog flow и canonical forms.

## Демо-кандидат

Colang path: user intent → allowed branch vs blocked off-topic.
