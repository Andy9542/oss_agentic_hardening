---
type: implementation-detail
parent-repo: repo-03-aegis
method-id: 3
repo: https://github.com/Justin0504/Aegis
language: Go
license: MIT
verdict: prod
tags: [agent-security]
---

# Aegis — injection patterns in args

## Репозиторий

[Justin0504/Aegis](https://github.com/Justin0504/Aegis)

## Где в коде

- Stage 2 content scan: «ignore instructions» patterns в аргументах tool_call
- SDK + Gateway :8080

## Алгоритм

Deep string extraction из args → regex/template match.

## Детерминизм или машинное обучение

Детерминированный.

## Внешние зависимости

самостоятельный хостинг Docker.

## Сигналы качества

- Claim: 48/48 attacks blocked, 1.2% FPR, ~8.3ms median
- Часть способа №19 (injection-rules-args)

## Вердикт

**готово к продакшену** — patterns на границе tool, не только prompt.

## Связи

- Репозиторий: [[repo-03-aegis]]
