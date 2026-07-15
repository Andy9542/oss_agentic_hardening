---
type: implementation-detail
parent-repo: repo-08-agent-airlock
method-id: 13
repo: https://github.com/sattyamjjain/agent-airlock
language: Python
license: MIT
verdict: prod
tags: [agent-security]
---

# agent-airlock — Pydantic validation

## Репозиторий

[sattyamjjain/agent-airlock](https://github.com/sattyamjjain/agent-airlock)

## Где в коде

- Validation layer: ghost argument removal, Pydantic V2 strict typing
- `@Airlock()` decorator on tools

## Алгоритм

Schema diff → strip unknown keys → strict type check.

## Детерминизм или машинное обучение

Детерминированный.

## Вердикт

**готово к продакшену** — reference impl for ghost args.

## Связи

- Репозиторий: [[repo-08-agent-airlock]]
