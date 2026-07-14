---
type: method
id: 38
layer: behavior
method-type: V
prod-viable: false
effectiveness: medium
robustness: medium
evidence-level: medium
status: reviewed
tags:
  - agent-security
sources: []
covers:
  - ASI04
  - ASI10
complements:
  - 26-tool-poisoning-scan
requires:
  - 40-opentelemetry-siem
---

# Skill attribution

## Определение

Форензика: **какой skill** инициировал действие. Owner GoPlusSecurity/agentguard — всегда указывать. Не enforcement — attribution после факта при доверенной телеметрии.

## Как это работает пошагово

1. Tool_call исполняется с контекстом skill_id.
2. Телеметрия (OTel) записывает provenance.
3. Post-incident: trace span skill_id → action.
4. post-factum × off-band.

## От чего защищает (visibility)

- **ASI04** supply chain forensics.
- **ASI10** rogue agent investigation.

## От чего НЕ защищает

- Атаку превентивно; подмену attribution без trusted telemetry.

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
| ASI04 | Supply chain | **ср.** | Forensics: какой skill в цепочке. |
| ASI10 | Rogue agent | **ср.** | Visibility post-incident. |

## Оценка эффективности

**Низкая** превентивно; **средняя** для форензики.

## Оценка прочности

**Средняя** — зависит от полноты трасс.

## Дополняет

- способ №26 (inventory skills)
- способ №40 (телеметрия)

## Требует

- способ №40 (OTel/SIEM)

## Не заменяет

Превентивную защиту.

## Сценический тезис

> Attribution отвечает «какой skill это сделал» — только при доверенной телеметрии.

## Демо-кандидат

Trace span: skill_id → tool_call (после №40).
