---
type: implementation-detail
parent-repo: repo-12-agentgateway
method-id: 11
repo: https://github.com/agentgateway/agentgateway
language: Go
license: Apache-2.0
verdict: prod
commit-sha: 114f77f
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# agentgateway — rate limiting и RBAC на MCP/A2A

## Репозиторий

- [agentgateway/agentgateway](https://github.com/agentgateway/agentgateway)
- Проверенный срез: `114f77f`, дата коммита 2026-07-15; код проверен 2026-07-15.

## Что это за технология

**API/MCP gateway** с политиками: JWT/API keys, **CEL-based RBAC**, local/global **rate limits**. Rate limiting — ограничение частоты запросов (токены/вызовы) по ключу (user, route, tool), чтобы сдержать runaway-агента и cost abuse (способ №11). CEL (Common Expression Language) — выражения вида `request.auth.principal == "…"` для authz.

## Где в коде

- CRD типы политик: `controller/api/v1alpha1/agentgateway/agentgateway_policy_types.go` (`RateLimits`, `LocalRateLimit`, `GlobalRateLimit`, `RateLimitsOrConditional`)
- Архитектура CEL: `architecture/cel.md`
- README: Auth, RBAC, rate limiting, OTel

## Алгоритм

1. Запрос MCP/A2A проходит gateway.
2. Auth (JWT/API key) → identity в context.
3. CEL RBAC на identity (без полного payload на этапе authz, см. cel.md).
4. Rate limit: local counters и/или global external service; conditional policies по выражениям.
5. При превышении — reject; иначе proxy к upstream MCP/LLM.

## Примеры реализации

Структура из API types (смысл полей):

```go
type RateLimits struct {
    Local  []LocalRateLimit  // in-process windows
    Global *GlobalRateLimit  // external limiter service
}
type RateLimitsOrConditional struct {
    Local       []LocalRateLimit
    Global      *GlobalRateLimit
    Conditional []RateLimitsConditional // CEL-gated policy selection
}
```

CEL используется и для выбора измерений rate limit (какие поля request считать ключом).

## Пример: вход → решение

- 121-й tool call/min при local limit 120 → deny/429.
- Principal без RBAC на `tools/call:shell` → deny до rate limit.

## Детерминизм или машинное обучение

**Детерминированный** (счётчики + CEL).

## Внешние зависимости

Kubernetes CRDs опционально; можно self-host gateway. Global RL — внешний сервис.

## Ограничения

- Не анализирует семантику промпта — только infra controls.
- Неверные CEL → дыры или lockout.

## Сигналы качества

- Зрелый gateway-проект с controller API и docs.

## Вердикт

**готово к продакшену** — инфраструктурный слой лимитов/RBAC для MCP.

## Связи

- Репозиторий: [[repo-12-agentgateway]]
