---
type: implementation
method-id: 11
repo: https://github.com/agentgateway/agentgateway
language: Rust
license: Apache-2.0
verdict: prod
tags: [agent-security]
---

# agentgateway — rate limiting

## Репозиторий

[agentgateway/agentgateway](https://github.com/agentgateway/agentgateway)

## Где в коде

- Gateway middleware: rate limiting, TLS, CORS
- CEL policies on MCP tools

## Алгоритм

Token-bucket / rate limit at proxy layer.

## Детерминизм или машинное обучение

Детерминированный.

## Вердикт

**готово к продакшену** — MCP/A2A gateway scale.

## Связи

- Способ: [[11-ограничение-токенов-расходов-и-частоты-вызовов]]
