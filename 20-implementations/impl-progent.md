---
type: implementation
method-id: 12
repo: Progent (research)
language: ""
license: ""
verdict: экспериментально
tags:
  - agent-security
---

# Progent v3 — способ №12

## Репозиторий

arXiv:2504.11703 v3 — DSL + SMT monotonic confinement.

## Алгоритм

JSON/JSON Schema привилегий; SMT-солвер на каждое обновление политики: narrowing авто, expansion — одобрение. 6% обновлений потребовали одобрения на AgentDojo `[проверено 2026-07-07]`.

## Детерминизм или машинное обучение

Детерминированный (SMT).

## Вердикт

**экспериментально** — сильная research-реализация; не mass prod.

## Связи

- Способ: [[12-tool-policies-yaml-rego]]
