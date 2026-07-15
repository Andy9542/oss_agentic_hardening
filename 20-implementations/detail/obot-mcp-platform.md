---
type: implementation-detail
parent-repo: repo-100-obot
method-id: 24
repo: https://github.com/obot-platform/obot
language: Go
license: Apache-2.0
verdict: experimental
commit-sha: 790b2e0
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# Obot — MCP hosting + registry + gateway

## Репозиторий

- [obot-platform/obot](https://github.com/obot-platform/obot)
- Проверенный срез: `790b2e0`; код проверен 2026-07-15.

## Что это за технология

**MCP platform**: hosting servers (Docker/K8s), curated **registry**, **gateway** (auth, access control, request/response logging), chat client. OAuth 2.1. Способ №24.

## Где в коде

- Go server `main.go`, `pkg/`, Helm `chart/`
- Docker: `ghcr.io/obot-platform/obot`
- Auth via `OBOT_SERVER_ENABLE_AUTHENTICATION` + bootstrap token

## Алгоритм

1. Deploy Obot with auth enabled.
2. Register/approve MCP servers in catalog.
3. Clients (ChatGPT/Claude/LangGraph/n8n) connect via gateway.
4. Gateway enforces auth + audits MCP traffic.

## Примеры реализации

```bash
docker run -d --name obot -p 8080:8080 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -e OPENAI_API_KEY=… \
  -e OBOT_SERVER_ENABLE_AUTHENTICATION=true \
  -e OBOT_BOOTSTRAP_TOKEN=<token≥8chars> \
  ghcr.io/obot-platform/obot:latest
```

Capabilities: MCP Hosting, Registry, Gateway, standards-compliant chat.

## Пример: вход → решение

- Unapproved MCP → not in registry → unavailable to users.
- Authenticated client → proxied tool calls logged.

## Детерминизм или машинное обучение

Control plane **детерминированный**.

## Внешние зависимости

Docker/K8s; LLM keys for chat; IdP/OAuth.

## Ограничения

- Platform ops complexity.
- Security = config (auth must stay on).

## Сигналы качества

- Active platform; SECURITY.md; Helm chart.

## Вердикт

**экспериментально**/зреющий MCP control plane.

## Связи

- Репозиторий: [[repo-100-obot]]
