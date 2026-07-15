---
type: implementation-detail
parent-repo: repo-47-invariant-gateway
method-id: 24
repo: https://github.com/invariantlabs-ai/invariant-gateway
language: Python
license: MIT
verdict: experimental
commit-sha: 9baeade
commit-date: 2025-11-06
verified-date: 2026-07-15
tags:
  - agent-security
---

# Invariant Gateway — LLM/MCP proxy + tracing

## Репозиторий

- [invariantlabs-ai/invariant-gateway](https://github.com/invariantlabs-ai/invariant-gateway)
- Проверенный срез: `9baeade`; код проверен 2026-07-15.

## Что это за технология

**Zero-config LLM proxy** между агентом и OpenAI/Anthropic: перехват chat/completions, tool calls, computer use и **MCP** (stdio/SSE/HTTP), запись traces в Invariant Explorer. Способ №24 (MCP gateway surface) — наблюдаемость как база для политик Invariant.

## Где в коде

- README quickstart — смена `base_url` на gateway
- MCP transport support documented in README

## Алгоритм

1. Поднять gateway locally/cloud.
2. Клиент: `base_url = http://gateway/...` вместо provider.
3. Gateway forward + stream; capture messages/tools/MCP.
4. Store traces in Explorer для debug/policy analysis.

## Примеры реализации

```python
# вместо api.openai.com — Gateway base URL
client = OpenAI(base_url="https://…/api/v1", api_key=…)
```

MCP: stdio / SSE / Streamable HTTP mediated through gateway.

## Пример: вход → решение

- Agent tool call → traced in Explorer (visibility).
- Само по себе не deny — нужен Invariant policy layer поверх traces.

## Детерминизм или машинное обучение

Проксирование **детерминированное**; анализ traces — отдельно.

## Внешние зависимости

Invariant Explorer account optional; provider keys.

## Ограничения

- Observability-first; enforcement не полный firewall.
- Trust boundary: gateway sees all prompts.

## Сигналы качества

- Invariant Labs; MCP multi-transport.

## Вердикт

**экспериментально** — удобный MCP/LLM observation gateway.

## Связи

- Репозиторий: [[repo-47-invariant-gateway]]
