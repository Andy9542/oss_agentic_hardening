---
type: implementation-detail
parent-repo: repo-02-pipelock
method-id: 3
repo: https://github.com/luckyPipewrench/pipelock
language: Go
license: Apache-2.0
verdict: prod
tags: [agent-security]
---

# Pipelock — injection heuristics

## Репозиторий

[luckyPipewrench/pipelock](https://github.com/luckyPipewrench/pipelock)

## Где в коде

- Response scanning: 25+ injection templates
- 6 normalization passes (zero-width, homoglyphs, leetspeak) перед regex
- MCP input/output layers

## Алгоритм

Normalize → pattern match → режим «закрыто при ошибке» on parse errors.

## Детерминизм или машинное обучение

Полностью детерминированный.

## Внешние зависимости

Нет. Локальный бинарник ~20 МБ.

## Сигналы качества

- режим «закрыто при ошибке» documented
- No neural networks — predictable audit

## Вердикт

**готово к продакшену** — один из сильнейших regex+normalization стеков.

## Связи

- Репозиторий: [[repo-02-pipelock]]
