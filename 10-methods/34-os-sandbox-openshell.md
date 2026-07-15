---
type: method
id: 34
layer: infra
method-type: D
prod-viable: false
effectiveness: high
robustness: medium
evidence-level: medium
status: reviewed
tags:
  - agent-security
  - even-batch
sources: []
covers:
  - ASI05
  - ASI02
  - ASI08
complements:
  - 12-tool-policies-yaml-rego
  - 16-ifc-capability-taint
---

# OS-level sandbox (OpenShell)

## Определение

Изоляция на уровне ОС: hardware-enforced network / FS / syscall policy. OpenShell = NVIDIA. Граница с №33 (microVM) и №35 (rings — не OS isolation).

## Как это работает пошагово

1. Агент исполняется в sandbox с ограниченными syscall/network/FS.
2. Попытка escape или запрещённого syscall — deny.
3. pre-tool-call (исполнение) × архитектурное свойство + inline block.

## От чего защищает

- **ASI05** containment escape / RCE.
- **ASI02** — ограничение side-effects tool.
- Частично **ASI08** — изоляция сбоев.

## От чего НЕ защищает

- Prompt injection; exfil через разрешённые egress.
- Sandbox escape 0-days; логику вне sandbox.

### Обходы

- Over-permissive egress; DNS-туннелирование.
- defenseclaw→OpenShell integration `[не проверено]`.

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
| ASI05 | Побег / неожиданное исполнение | **выс.** | Последний рубеж containment. |
| ASI02 | ↳ SSRF через tool | **ср.** | Сетевая политика внутри sandbox. |

## Оценка эффективности

**Высокая** при hardware-enforced isolation.

## Оценка прочности

**Средняя** — egress misconfig, integration gaps.

## Дополняет

- способ №12, №16 (in-process policy)

## Требует

—

## Не заменяет

- способ №35 (rings — не OS isolation)
- in-process политики

## Сценический тезис

> OS-level sandbox — последний рубеж: даже если политика и IFC проспали, агент не должен иметь syscall и сеть всей машины.

## Демо-кандидат

DNS/FS/syscall trace; попытка escape → deny.
