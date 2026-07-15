---
type: implementation-detail
parent-repo: repo-58-mcp-gateway-registry
method-id: 24
repo: https://github.com/agentic-community/mcp-gateway-registry
language: Python/TypeScript
license: Apache-2.0
verdict: experimental
commit-sha: 7cea0f0
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# MCP Gateway Registry — реестр + gateway для MCP servers

## Репозиторий

- [agentic-community/mcp-gateway-registry](https://github.com/agentic-community/mcp-gateway-registry)
- Проверенный срез: `7cea0f0`; код проверен 2026-07-15.

## Что это за технология

**Community registry + gateway** для MCP: централизованная регистрация серверов, discovery, auth/RBAC-ориентированный доступ агентов к tools вместо прямого stdio к произвольным MCP. Способ №24.

## Где в коде

- README architecture; gateway/registry services
- Large monorepo with examples/configs

## Алгоритм

1. Зарегистрировать MCP server в registry (metadata, endpoints).
2. Agent → gateway (auth) → resolve allowed servers.
3. Proxy tool calls; deny unregistered/unauthorized.
4. Audit access.

## Примеры реализации

Типовой flow: client connects to gateway URL → token/RBAC → allowlisted MCP backends only.

## Пример: вход → решение

- Unregistered malicious MCP → not in registry → unreachable.
- Authorized server tool → proxied.

## Детерминизм или машинное обучение

**Детерминированный** registry/RBAC control.

## Внешние зависимости

Deploy registry/gateway stack; IdP optional.

## Ограничения

- Ops overhead; trust in who can register.
- Не сканирует tool descriptions сам по себе (нужен scanner рядом).

## Сигналы качества

- agentic-community; active 2026.

## Вердикт

**экспериментально** — enterprise-ish MCP control plane.

## Связи

- Репозиторий: [[repo-58-mcp-gateway-registry]]
