---
type: implementation
method-id: 14
repo: agent-airlock
language: Python
license: ""
verdict: экспериментально
tags:
  - agent-security
---

# agent-airlock — способ №14 (default-deny)

## Репозиторий

agent-airlock — deny-by-default для capabilities.

## Алгоритм

Агент стартует с минимальным allowlist; каждый tool вне списка блокируется.

## Детерминизм или машинное обучение

Детерминированный.

## Вердикт

**экспериментально** — подтверждено по описанию репо `[проверено]`.

## Связи

- Способ: [[14-default-deny-allowlists]]
