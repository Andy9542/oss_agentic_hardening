---
type: implementation
method-id: 15
repo: https://github.com/snyk/agent-scan
language: TypeScript
license: Apache-2.0
verdict: exp
tags: [agent-security]
---

# snyk/agent-scan — toxic flows

## Репозиторий

[snyk/agent-scan](https://github.com/snyk/agent-scan)

## Где в коде

- Toxic flow analysis: dangerous tool chains in static config
- Requires Snyk API for full semantic scan

## Алгоритм

Graph of tools → co-occurrence / flow rules (static, pre-deploy).

## Детерминизм или машинное обучение

Смешанный: local rules Д, cloud API В.

## Вердикт

**экспериментально** — static only; runtime needs Invariant.

## Связи

- Способ: [[15-flow-rules]]
