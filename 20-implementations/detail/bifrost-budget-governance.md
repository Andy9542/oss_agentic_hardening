---
type: implementation-detail
parent-repo: repo-19-bifrost
method-id: 11
repo: https://github.com/maximhq/bifrost
language: Go
license: Apache-2.0
verdict: prod
commit-sha: c0909f9
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# Bifrost — AI gateway: budgets, rate limits, governance

## Репозиторий

- [maximhq/bifrost](https://github.com/maximhq/bifrost)
- Проверенный срез: `c0909f9`; код проверен 2026-07-15.

## Что это за технология

**High-performance LLM/MCP gateway** (OpenAI-compatible): единая точка для 20+ провайдеров с failover, load balancing, **semantic cache**, MCP tools, и governance — virtual keys, **hierarchical budgets**, rate limits, access control. Способ №11 (лимиты/бюджеты) + №12.

## Где в коде

- Plugins: `plugins/governance/`, `plugins/semanticcache/`, `plugins/telemetry/`
- HTTP transport: `transports/bifrost-http/`
- Docs: docs.getbifrost.ai — Budget Management, Governance

## Алгоритм

1. Клиент бьёт в Bifrost `/v1/chat/completions` с virtual key.
2. Auth + governance plugin: проверить budget/team limits / RPM.
3. Route to provider with failover; optional semantic cache hit.
4. Log spend/metrics (Prometheus); reject if over budget.
5. MCP path: gateway mediates tool calls under same governance.

## Примеры реализации

```bash
npx -y @maximhq/bifrost
# Web UI :8080 — configure providers, budgets, virtual keys
```

Drop-in: заменить `base_url` OpenAI/Anthropic на `http://localhost:8080/openai`.

## Пример: вход → решение

- Team over monthly budget → request denied.
- Within limits → proxied to openai/gpt-4o-mini.

## Детерминизм или машинное обучение

Лимиты детерминированы; semantic cache — embedding similarity (вероятностный hit).

## Внешние зависимости

Docker/npx gateway; provider API keys.

## Ограничения

- Guardrails enterprise-tier в README; OSS фокус на gateway/governance.
- Не заменяет content injection classifier сам по себе.

## Сигналы качества

- Perf benchmarks (µs overhead); Docker pulls; codecov.

## Вердикт

**готово к продакшену** как LLM gateway с budget/RL governance.

## Связи

- Репозиторий: [[repo-19-bifrost]]
