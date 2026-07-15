---
type: repo-catalog
catalog-id: 12
method-id: 24
also-method-ids:
  - 11
repo: https://github.com/agentgateway/agentgateway
language: Rust/Go
license: ""
verdict: prod
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-mcp-gateway
  - cluster-llm-gateway
---

# agentgateway/agentgateway — каталог №12

## Репозиторий

[agentgateway/agentgateway](https://github.com/agentgateway/agentgateway)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 4 |
| Тип | Архит. |
| Семейства | [[cluster-mcp-gateway]], [[cluster-llm-gateway]] |

## Принцип работы

Шлюз MCP/A2A: маршрутизация, аутентификация, ограничение поверхностей

## Алгоритм

Шлюз MCP/A2A: маршрутизация, аутентификация, ограничение поверхностей.

Каталожная заметка: основной механизм — **способ №24**; дополнительно перекрывает: способ №11.

## Вариант в семействе

Шлюз MCP/A2A: маршрутизация, auth, rate limits. Родственные реализации — только через семейства: MCP/A2A шлюзы, LLM-шлюзы.


## Детерминизм или машинное обучение

Тип из каталога: **Архит.**.

## Вердикт

**готово к продакшену** — каталожная оценка по зрелости репозитория в экосистеме.


## Детальные разборы

- [[agentgateway-rate-limiting]]
- [[impl-agentgateway]]


## Реализуемые способы

- [[24-mcp-gateway-rbac]] — основной
- [[11-ограничение-токенов-расходов-и-частоты-вызовов]]
