---
type: method
id: 18
layer: action
method-type: D
prod-viable: true
effectiveness: medium
robustness: medium
evidence-level: strong
status: reviewed
tags:
  - agent-security
  - even-batch
sources: []
covers:
  - ASI03
  - ASI02
complements:
  - 12-tool-policies-yaml-rego
  - 16-ifc-capability-taint
requires:
  - 14-default-deny-allowlists
not-replaces:
  - 16-ifc-capability-taint
---

# ReBAC (SpiceDB)

## Определение

Relationship-Based Access Control: доступ к tools/ресурсам по **графу отношений** (user→agent→tool, org→project→dataset), не плоский RBAC. SpiceDB (Zanzibar); Janus — минимальная агентная интеграция. ReBAC = права в графе; IFC (№16) = метки на потоках.

## Как это работает пошагово

1. Перед tool_call — CheckPermission в SpiceDB.
2. Граф отношений определяет, имеет ли субъект право на ресурс/tool.
3. При отсутствии edge — inline deny.

## От чего защищает

- **ASI03** — агент без отношения в графе не вызывает tool.
- Частично **ASI02** — горизонтальное повышение через чужие ресурсы.

## От чего НЕ защищает

- Prompt injection и data-flow (→ №16).
- Злоупотребление разрешённым доступом.
- Ошибки в схеме отношений.
- Семантика аргументов (→ №20).

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
| ASI03 | Эскалация привилегий | **выс.** | Граф отношений на границе tool-call. |
| ASI02 | Один опасный вызов | **ср.** | Горизонтальный privilege abuse. |

## Оценка эффективности

**Средняя** — baseline для enterprise multi-tenant.

## Оценка прочности

**Средняя** — неполный граф, устаревшие tuples.

## Дополняет

- способ №12 (policy engine)
- способ №16 (IFC)

## Требует

- способ №14 (default-deny)

## Не заменяет

- способ №16 (data-flow)

## Сценический тезис

> ReBAC — «имеет ли агент право трогать tool», не «куда утекут данные». Мощный замок на двери, не видит что переносят.

## Демо-кандидат

Граф user→agent→tool; agent→чужой_tool без edge → deny.
