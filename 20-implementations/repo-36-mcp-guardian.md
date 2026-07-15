---
type: repo-catalog
catalog-id: 36
method-id: 24
also-method-ids:
  - 14
  - 21
repo: https://github.com/eqtylab/mcp-guardian
language: Rust
license: Apache-2.0
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-mcp-trust-runtime
  - cluster-mcp-gateway
  - cluster-tool-firewall-yaml
---

# eqtylab/mcp-guardian — каталог №36

## Репозиторий

[eqtylab/mcp-guardian](https://github.com/eqtylab/mcp-guardian)

Каталожный URL `mcp-guardian/mcp-guardian` на 2026-07-15 был недоступен (404). Канонический OSS-проект с брендом **MCP Guardian** (runtime proxy + approvals): `eqtylab/mcp-guardian`.

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3 |
| Тип | Детерм. |
| Семейства | [[cluster-mcp-trust-runtime]], [[cluster-mcp-gateway]], [[cluster-tool-firewall-yaml]] |

## Принцип работы

Runtime-прокси MCP: логирование, human approval tool calls, управление коллекциями серверов.

## Алгоритм

Хост LLM → `mcp-guardian-proxy` → upstream MCP server; сообщения могут ждать approve/deny.

Каталожная заметка: основной механизм — **способ №24**; дополнительно: способ №14, способ №21 (HITL).

## Вариант в семействе

Runtime-защита MCP-серверов (EQTY Lab). Не путать со сканером описаний tools alexandriashai/mcp-guardian (каталог №28).

## Детерминизм или машинное обучение

Тип из каталога: **Детерм.** (HITL + proxy).

## Вердикт

**экспериментально** — полезный HITL MCP proxy; automated scans в README ещё «Coming Soon».

## Детальные разборы

- [[mcp-guardian-proxy]]

## Реализуемые способы

- [[24-mcp-gateway-rbac]] — основной
- [[14-default-deny-allowlists]]
- [[21-одобрение-опасных-действий-человеком]]
