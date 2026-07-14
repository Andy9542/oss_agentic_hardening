---
type: method
id: 12
layer: action
method-type: D
prod-viable: true
effectiveness: high
robustness: medium
evidence-level: strong
status: reviewed
tags:
  - agent-security
sources:
  - source-progent-smt
  - source-owasp-agentic-2026
covers:
  - ASI02
  - ASI03
  - LLM06
---

# Политики на tools (YAML / Rego / Cedar)

## Определение

Декларативные **policy engines** на границе tool-call: allow/deny/require_approval по имени tool, аргументам, контексту. Семейства: YAML/JSON, OPA Rego/Cedar, Progent DSL+SMT, Invariant trace rules. CEL на gateway — способ №24, не сюда.

## Как это работает пошагово

1. Агент запрашивает tool_call.
2. Policy engine оценивает правила (Rego/Cedar/YAML/Progent DSL).
3. При deny — блок; при require_approval — эскалация.
4. Progent: SMT-солвер на каждое **обновление** политики (narrowing авто, expansion — одобрение).

## От чего защищает

- **ASI02** Tool Misuse.
- **ASI03** Identity & Privilege Abuse (confused deputy).
- Частично **LLM06** Excessive Agency.

## От чего НЕ защищает

- Ошибку/дыру в политике.
- Потоки данных без flow-правил (→ способ №16, №28).
- Семантически валидный злоупотребление в рамках allow.
- Prompt injection как текстовая атака.

### Обходы и цена

- Неполная онтология tools; expansion без SMT-контроля.
- Владелец правил; Progent: 6% обновлений потребовали одобрения на AgentDojo.

## Алгоритмы и механизмы (подробно)

- **OPA Rego / Cedar** — enterprise policy-as-code.
- **Progent v3** — DSL + SMT monotonic confinement (arXiv:2504.11703).
- **Invariant trace rules** — последовательности tool-call.

## Реализации

```dataview
TABLE verdict AS "Вердикт", repo AS "Репозиторий"
FROM "20-implementations"
WHERE method-id = this.id
SORT file.name
```

## Доказательная база

- source-progent-smt

## Покрытие рисков

| Риск | Сценарий в матрице | Уровень | Почему такая оценка |
|------|--------------------|---------|---------------------|
| ASI02 | Один опасный вызов | **выс.** | Основной enterprise-механизм слоя «Действие». |
| ASI02 | ↳ токсичная цепочка A→B | **ср.** | Trace rules; полный flow — №28/№16. |
| ASI03 | Эскалация привилегий | **выс.** | При корректной политике субъекта. |

## Оценка эффективности

**Высокая** для tool misuse при зрелой политике.

## Оценка прочности

**Средняя** — зависит от полноты политики и дисциплины обновлений.

## Дополняет

- способ №16 (IFC на данных)
- способ №28 (статический toxic flow)

## Требует

- способ №14 (default-deny)

## Не заменяет

- способ №20 (schema аргументов vs policy смысла)

## Сценический тезис

> Security-команда говорит агенту «ты можешь только это». Progent v3 — monotonic confinement: SMT на обновления, 6% изменений потребовали человека на AgentDojo. Политика с дырой — дырявая политика.

## Демо-кандидат

Policy deny `send_email` после `read_untrusted_web`; Progent narrowing vs expansion без approve — блок SMT.
