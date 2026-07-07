---
type: method
id: 16
layer: action
method-type: D
prod-viable: false
effectiveness: high
robustness: medium
evidence-level: strong
status: reviewed
tags:
  - agent-security
  - even-batch
sources:
  - source-camel-ifc
covers:
  - LLM01
  - LLM02
  - LLM06
  - ASI01
  - ASI02
complements:
  - 28-toxic-flow-analysis
requires:
  - 14-default-deny-allowlists
not-replaces:
  - 02-cot-reasoning-audit
---

# Capability / IFC / taint-метки

## Определение

Решение о допустимости по **происхождению данных**: capability-метки на значениях, IFC-propagation, policy engine перед tool_call, taint score сессии. CaMeL — пообъектная дисциплина; taint score — сессионный скаляр. Архитектурный носитель Q-LLM/P-LLM — способ №43 (нечётный, один дизайн CaMeL).

## Как это работает пошагово

1. Каждому значению присваиваются метки provenance (trusted/untrusted, sensitivity).
2. При операциях метки наследуются (IFC propagation).
3. Перед tool_call policy engine сверяет метки аргументов с политикой sink'ов.
4. При нарушении потока — inline-блокировка.

## От чего защищает

- Indirect PI → экфильтрация (LLM01→LLM02, LLM06).
- Confused deputy — недоверенные данные не меняют план.
- Часть Excessive Agency при корректной политике.
- Разрыв lethal trifecta (паттерн Q/P-LLM, №43).

## От чего НЕ защищает

- Атаку в рамках разрешённого потока.
- Ошибку/неполноту политики (незаявленный sink).
- Компрометацию Q-LLM на уровне значения.
- Reasoning-hijack без потока данных.
- Побочные каналы; memory poisoning (→ №46*).

### Обходы

- Over-tainting → коллапс полезности.
- Implicit flows; неполная онтология sink'ов.

## Алгоритмы и механизмы (подробно)

- **CaMeL** (arXiv:2503.18813 v2) — пообъектные capability, IFC, policy engine, Q/P-LLM.
- **FIDES** — IFC-развитие `[не проверено]`.
- **Janus** — сессионный taint score на SpiceDB `[проверено]` существование.

## Реализации

```dataview
TABLE verdict AS "Вердикт", repo AS "Репозиторий"
FROM "20-implementations"
WHERE method-id = this.id
SORT file.name
```

## Доказательная база

- source-camel-ifc

## Покрытие рисков

| Риск | Сценарий в матрице | Уровень | Почему такая оценка |
|------|--------------------|---------|---------------------|
| ASI01 | Захват цели (экфильтрация) | **выс.** | Блок потока недоверенных данных в sink. |
| ASI02 | ↳ токсичная цепочка | **выс.** | Рантайм-исполнение flow-ограничений. |
| LLM02 | Утечка персональных данных | **выс.** | Прямая мишень IFC на exfil paths. |

## Оценка эффективности

**Высокая** на PI-экфильтрацию — единственный класс с доказуемой гарантией на трифекту.

## Оценка прочности

**Средняя** — implicit flows, полнота политики, Q-LLM на значении.

## Дополняет

- способ №1, №2 (текстовые детекторы — другой слой)
- способ №15 (flow rules — грубый предок)
- способ №28 (статический toxic flow)

## Требует

- способ №14 (default-deny)

## Не заменяет

- способ №1, №2 (текстовый слой)

## Сценический тезис

> PI — задача контроля потоков данных, не фильтрации текста. CaMeL делает инъекцию структурно невозможной для sink'а. ~7 п.п. полезности за доказуемую безопасность в AgentDojo.

## Демо-кандидат

Флоу-граф трифекты → policy gate красный перед send_email; контраст: №1 проходит / IFC падает.
