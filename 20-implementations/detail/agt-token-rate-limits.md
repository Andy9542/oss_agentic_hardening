---
type: implementation-detail
parent-repo: repo-01-agent-governance-toolkit
method-id: 11
repo: https://github.com/microsoft/agent-governance-toolkit
language: Python
license: MIT
verdict: prod
tags:
  - agent-security
---

# AGT — token and rate limits

## Репозиторий

[microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit)

## Где в коде

- `GovernancePolicy` — token limits, blocked patterns
- Agent SRE — circuit breakers, SLO

## Алгоритм

Declarative YAML/JSON/Rego limits per agent/session.

## Детерминизм или машинное обучение

Детерминированный.

## Внешние зависимости

OPA optional; core local.

## Вердикт

**готово к продакшену** — enterprise policy kernel.

## Связи

- Репозиторий: [[repo-01-agent-governance-toolkit]]
