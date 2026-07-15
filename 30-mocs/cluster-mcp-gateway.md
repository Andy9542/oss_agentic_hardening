---
type: moc
tags:
  - cluster
  - repo-catalog
---

# cluster-mcp-gateway

## MCP/A2A шлюзы и реестры

> [!NOTE] Общая суть
> Маршрутизация MCP, аутентификация, RBAC, rate limits на mesh агентов.

Несколько репозиториев реализуют **одну идею** разными способами (язык, точка встраивания, зрелость). Каждый вариант — отдельная заметка `repo-NN-*`; связь на графе: **кластер → реализация → способ**.

## Связанные способы

- способ №24 (24-mcp-gateway-rbac)
- способ №11 (11-ограничение-токенов-расходов-и-частоты-вызовов)
- способ №39 (39-неизменяемый-журнал-с-цепочкой-хешей-и-подписями)

## Варианты реализации (6)

- [[repo-100-obot]] — obot-platform/obot: MCP-шлюз с контролем доступа и аудитом
- [[repo-12-agentgateway]] — agentgateway/agentgateway: Шлюз MCP/A2A: маршрутизация, аутентификация, ограничение поверхностей
- [[repo-14-interlock]] — MaazAhmed47/Interlock: Слой доверия MCP в рантайме
- [[repo-36-mcp-guardian]] — eqtylab/mcp-guardian: Runtime-защита MCP-серверов
- [[repo-47-invariant-gateway]] — invariantlabs-ai/invariant-gateway: Шлюз с политиками для агентных трасс
- [[repo-58-mcp-gateway-registry]] — agentic-community/mcp-gateway-registry: Реестр и шлюз MCP с контролем доступа


## Навигация

- [[github-100-repo]] — полный каталог 118 репозиториев
- [[MOC — Кластеры репозиториев]] — все семейства
