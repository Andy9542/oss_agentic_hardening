---
type: implementation-detail
parent-repo: repo-20-litellm
method-id: 11
repo: https://github.com/BerriAI/litellm
language: Python
license: MIT
verdict: prod
commit-sha: f1f33f5
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# LiteLLM — proxy hooks: budget, rate limit, guardrails

## Репозиторий

- [BerriAI/litellm](https://github.com/BerriAI/litellm)
- Проверенный срез: `f1f33f5` (sparse); код/ARCHITECTURE проверены 2026-07-15.

## Что это за технология

**LLM proxy/gateway**: единый API ко многим провайдерам + production hooks — virtual keys, **max_budget_limiter**, parallel request limiter, spend tracking (Redis→Postgres), guardrails per project. Способ №11 (+ observability №40).

## Где в коде

- ARCHITECTURE.md: request path Auth → hooks → provider → spend writer
- Hooks: `proxy/hooks/max_budget_limiter.py`, parallel_request_limiter
- Spend: `proxy/db/db_spend_update_writer.py`
- Redis for RPM/TPM; Postgres for keys/teams/spend logs

## Алгоритм

1. Request with virtual key → Redis key info + spend limits.
2. Hooks: `max_budget_limiter`, `parallel_request_limiter` — deny if exceeded.
3. Optional guardrails/logging per project.
4. Call upstream model; queue spend increment to Redis.
5. Background job flushes spend to Postgres (~60s); budget reset jobs.

## Примеры реализации

Из ARCHITECTURE:

```text
Auth → max_budget_limiter, parallel_request_limiter → Provider
DBSpendUpdateWriter → Redis spend queue → Postgres batch
Jobs: update_spend 60s, reset_budget 10-12min
```

## Пример: вход → решение

- Key over max_budget → blocked before provider call.
- Under budget → completion + spend logged.

## Детерминизм или машинное обучение

Budget/RL **детерминированные**; guardrail plugins могут быть ML.

## Внешние зависимости

Redis + Postgres for full gateway; provider keys.

## Ограничения

- Огромный monorepo — подключать только proxy features.
- Guardrail quality depends on configured validators.

## Сигналы качества

- Widely deployed OSS gateway; clear spend pipeline docs.

## Вердикт

**готово к продакшену** для budget/rate governance LLM traffic.

## Связи

- Репозиторий: [[repo-20-litellm]]
