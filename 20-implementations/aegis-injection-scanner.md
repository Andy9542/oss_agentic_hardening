---
type: implementation
method-id: 19
repo: https://github.com/Justin0504/Aegis
language: Go
license: MIT
verdict: prod
tags: [agent-security]
---

# Aegis — injection scanner (args)

## Репозиторий

[Justin0504/Aegis](https://github.com/Justin0504/Aegis)

## Где в коде

- 3-stage pipeline: extract → scan (SQL/shell/path/injection) → policy
- SDK patches 14 frameworks

## Алгоритм

Regex/signatures on all strings in tool arguments.

## Детерминизм или машинное обучение

Детерминированный.

## Вердикт

**готово к продакшену** — published attack block stats.

## Связи

- Способ: [[19-injection-rules-args]]
