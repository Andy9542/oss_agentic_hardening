---
type: repo-catalog
catalog-id: 58
method-id: 24
also-method-ids:
  - 31
repo: https://github.com/agentic-community/mcp-gateway-registry
language: Unknown
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-mcp-gateway
  - cluster-artifact-trust
---

# agentic-community/mcp-gateway-registry — каталог №58

## Репозиторий

[agentic-community/mcp-gateway-registry](https://github.com/agentic-community/mcp-gateway-registry)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 4 |
| Тип | Архит. |
| Семейства | [[cluster-mcp-gateway]], [[cluster-artifact-trust]] |

## Принцип работы

Реестр и шлюз MCP с контролем доступа

## Алгоритм

Реестр и шлюз MCP с контролем доступа.

Каталожная заметка: основной механизм — **способ №24**; дополнительно перекрывает: способ №31.

## Вариант в семействе

Реестр и шлюз MCP с контролем доступа. Родственные реализации — только через семейства: MCP/A2A шлюзы, доверие к артефактам.


## Детерминизм или машинное обучение

Тип из каталога: **Архит.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Детальные разборы

- [[mcp-gateway-registry]]

## Реализуемые способы

- [[24-mcp-gateway-rbac]] — основной
- [[31-допуск-артефактов-и-отзыв-по-чёрному-списку]]
