---
type: implementation
method-id: 19
repo: https://github.com/GoPlusSecurity/agentguard
language: Go
license: MIT
verdict: prod
tags: [agent-security]
---

# agentguard — runtime hooks

## Репозиторий

[GoPlusSecurity/agentguard](https://github.com/GoPlusSecurity/agentguard)

## Где в коде

- Runtime hooks: path traversal, webhook exfil URLs, skill scan
- Static + runtime mix

## Алгоритм

Deterministic rules on tool invocations and skill files.

## Вердикт

**готово к продакшену** — OpenClaw-family focus.

## Связи

- Способ: [[19-правила-против-инъекций-в-аргументах-инструментов]]
