---
type: implementation
method-id: 19
repo: https://github.com/luckyPipewrench/pipelock
language: Go
license: Apache-2.0
verdict: prod
tags: [agent-security]
---

# Pipelock — shell rules

## Репозиторий

[luckyPipewrench/pipelock](https://github.com/luckyPipewrench/pipelock)

## Где в коде

- MCP wrapper: 17 dangerous command rules, shell obfuscation detection
- Path traversal layer

## Алгоритм

Pattern match on command strings after normalization.

## Вердикт

**готово к продакшену**

## Связи

- Способ: [[19-injection-rules-args]]
