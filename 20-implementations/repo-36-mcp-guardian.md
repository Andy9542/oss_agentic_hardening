---
type: repo-catalog
catalog-id: 36
method-id: 24
also-method-ids:
  - 14
repo: https://github.com/mcp-guardian/mcp-guardian
language: Unknown
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-mcp-trust-runtime
  - cluster-mcp-gateway
  - cluster-tool-firewall-yaml
---

# mcp-guardian/mcp-guardian — каталог №36

## Репозиторий

[mcp-guardian/mcp-guardian](https://github.com/mcp-guardian/mcp-guardian)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3 |
| Тип | Детерм. |
| Семейства | [[cluster-mcp-trust-runtime]], [[cluster-mcp-gateway]], [[cluster-tool-firewall-yaml]] |

## Принцип работы

Runtime-защита MCP-серверов

## Алгоритм

Runtime-защита MCP-серверов.

Каталожная заметка: основной механизм — **способ №24**; дополнительно перекрывает: способ №14.

## Вариант в семействе

Runtime-защита MCP-серверов. Родственные реализации — только через семейства: runtime trust MCP, MCP/A2A шлюзы, YAML-файрволы tools.


## Детерминизм или машинное обучение

Тип из каталога: **Детерм.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Реализуемые способы

- [[24-mcp-gateway-rbac]] — основной
- [[14-default-deny-allowlists]]
