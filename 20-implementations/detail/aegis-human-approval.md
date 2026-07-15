---
type: implementation-detail
parent-repo: repo-03-aegis
method-id: 21
repo: https://github.com/Justin0504/Aegis
language: Go
license: MIT
verdict: prod
tags:
  - agent-security
---

# Aegis — human approval

## Репозиторий

[Justin0504/Aegis](https://github.com/Justin0504/Aegis)

## Где в коде

- Policy stage: block / pending / allow
- Compliance Cockpit :3000 — approval queue, kill switch

## Алгоритм

State machine: tool_call → pending → human decision → resume.

## Вердикт

**готово к продакшену** — full HITL UX.

## Связи

- Репозиторий: [[repo-03-aegis]]
