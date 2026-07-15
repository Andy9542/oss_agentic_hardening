---
type: method
id: 40
layer: meta
method-type: A
prod-viable: true
effectiveness: low
robustness: low
evidence-level: strong
status: reviewed
tags:
  - agent-security
  - even-batch
sources:
  - source-microsoft-agt
covers:
  - ASI08
  - ASI10
---

# OpenTelemetry / SIEM

## Определение

**Наблюдаемость**, не защита: трассы, метрики, логи tool-call, token cost tracking. SIEM для форензики и алертинга. Блокировка по бюджету → №22/№12.

## Как это работает пошагово

1. Инструментация агента OTel SDK.
2. Экспорт traces/metrics/logs в SIEM.
3. Алерты и дашборды post-factum.
4. post-factum × off-band.

## От чего защищает (visibility)

- Расследование **ASI08, ASI10** post-incident.
- Материал для способа №2 (CoT-аудит) и №38 (attribution).

## От чего НЕ защищает

- Ничего превентивно без enforcement.

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
| ASI08 | Каскадные сбои | **ср.** | Visibility для расследования; не блок. |
| ASI10 | Rogue agent | **низ.** | Аудит, не барьер. |

## Оценка эффективности

**Низкая** как security control; **высокая** как audit enabler.

## Оценка прочности

**Низкая** — log injection, неполное покрытие.

## Дополняет

- способ №2, №38

## Требует

—

## Не заменяет

Детекторы и enforcement.

## Сценический тезис

> Телеметрия не останавливает атаку — объясняет, что агент сделал после. На сцене честно: аудит, не защита.

## Демо-кандидат

Pipeline diagram в общей карте слоёв.
