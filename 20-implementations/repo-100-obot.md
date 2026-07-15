---
type: repo-catalog
catalog-id: 100
method-id: 24
also-method-ids:
  - 39
repo: https://github.com/obot-platform/obot
language: Unknown
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-mcp-gateway
  - cluster-governance-platform
---

# obot-platform/obot — каталог №100

## Репозиторий

[obot-platform/obot](https://github.com/obot-platform/obot)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 4 |
| Тип | Архит. |
| Семейства | [[cluster-mcp-gateway]], [[cluster-governance-platform]] |

## Принцип работы

MCP-шлюз с контролем доступа и аудитом

## Алгоритм

MCP-шлюз с контролем доступа и аудитом.

Каталожная заметка: основной механизм — **способ №24**; дополнительно перекрывает: способ №39.

## Вариант в семействе

MCP-шлюз с ACL и аудитом. Родственные реализации — только через семейства: MCP/A2A шлюзы, платформы governance.


## Детерминизм или машинное обучение

Тип из каталога: **Архит.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Реализуемые способы

- [[24-mcp-gateway-rbac]] — основной
- [[39-неизменяемый-журнал-с-цепочкой-хешей-и-подписями]]
