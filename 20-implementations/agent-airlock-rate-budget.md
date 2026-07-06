---
type: implementation
method-id: 11
repo: https://github.com/sattyamjjain/agent-airlock
language: Python
license: MIT
verdict: prod
tags: [agent-security]
---

# agent-airlock — rate and budget

## Репозиторий

[sattyamjjain/agent-airlock](https://github.com/sattyamjjain/agent-airlock)

## Где в коде

- Policy layer: rate limits, time windows, cost/budget tracking
- Circuit breaker in resilience layer

## Алгоритм

Sliding window counters + budget accumulator on tool calls.

## Детерминизм или машинное обучение

Детерминированный.

## Внешние зависимости

OpenTelemetry export optional.

## Вердикт

**готово к продакшену** — in-process decorator pattern.

## Связи

- Способ: [[11-rate-cost-token-limits]]
