---
type: implementation-detail
parent-repo: repo-11-janus
method-id: 13
repo: https://github.com/Agentic-AI-Risk-Mitigation/Janus
language: Python
license: Apache-2.0
verdict: prod
tags: [agent-security]
---

# Janus — JSON Schema on tool args

## Репозиторий

[Agentic-AI-Risk-Mitigation/Janus](https://github.com/Agentic-AI-Risk-Mitigation/Janus)

## Где в коде

- Policy boundary: JSON Schema validation on tool invocation
- Optional SpiceDB ReBAC

## Алгоритм

JSON Schema draft validation + default-deny policies.

## Детерминизм или машинное обучение

Детерминированный.

## Вердикт

**готово к продакшену** — policy at tool boundary.

## Связи

- Репозиторий: [[repo-11-janus]]
