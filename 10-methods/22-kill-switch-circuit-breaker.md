---
type: method
id: 22
layer: action
method-type: D
prod-viable: true
effectiveness: low
robustness: medium
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

# Kill switch / circuit breaker

## Определение

**22a Kill switch** — ручная аварийная остановка агента (процессный, реактивный). **22b Circuit breaker** — автоматическое ограничение при росте ошибок/error budget (Agent SRE). Не предотвращает первую атаку — ограничивает ущерб и каскад.

## Как это работает пошагово

1. **Kill switch:** оператор останавливает runtime агента on-demand.
2. **Circuit breaker:** мониторинг error budget; при превышении — блок новых вызовов.
3. post-factum / continuous monitoring.

## От чего защищает

- **ASI08** Cascading Failures — breaker обрывает каскад.
- Частично **ASI10** Rogue Agents — kill switch после детекции.

## От чего НЕ защищает

- Первичную атаку, prompt injection.
- Data exfiltration до срабатывания порога.
- Медленную экфильтрацию ниже порога breaker.

## Реализации

```dataview
TABLE verdict AS "Вердикт", repo AS "Репозиторий"
FROM "20-implementations"
WHERE method-id = this.id
SORT file.name
```

## Доказательная база

- source-microsoft-agt

## Покрытие рисков

| Риск | Сценарий в матрице | Уровень | Почему такая оценка |
|------|--------------------|---------|---------------------|
| ASI08 | Зацикливание / исчерпание ресурсов | **выс.** | Breaker по error budget. |
| ASI08 | Каскадные сбои | **выс.** | Обрыв цепной реакции. |
| ASI10 | Rogue agent | **ср.** | Kill switch после детекции. |

## Оценка эффективности

**Низкая** как превентив; **высокая** как страховка от runaway.

## Оценка прочности

**Средняя** — зависит от калибровки порогов.

## Дополняет

- способ №40 (наблюдаемость для триггеров)

## Требует

—

## Не заменяет

Превентивные слои №1–№16.

## Сценический тезис

> Kill switch ≠ circuit breaker: красная кнопка оператора vs автоматический предохранитель. Не защита от инъекции — страховка от «агент уже поехал».

## Демо-кандидат

Split-screen: оператор kill switch → runtime stopped; граф ошибок → breaker open.
