---
type: repo-catalog
catalog-id: 14
method-id: 25
also-method-ids:
  - 24
repo: https://github.com/MaazAhmed47/Interlock
language: Unknown
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-mcp-trust-runtime
  - cluster-mcp-gateway
---

# MaazAhmed47/Interlock — каталог №14

## Репозиторий

[MaazAhmed47/Interlock](https://github.com/MaazAhmed47/Interlock)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3 |
| Тип | Детерм. |
| Семейства | [[cluster-mcp-trust-runtime]], [[cluster-mcp-gateway]] |

## Принцип работы

Слой доверия MCP в рантайме

## Алгоритм

Слой доверия MCP в рантайме.

Каталожная заметка: основной механизм — **способ №25**; дополнительно перекрывает: способ №24.

## Вариант в семействе

Runtime trust layer для MCP. Родственные реализации — только через семейства: runtime trust MCP, MCP/A2A шлюзы.


## Детерминизм или машинное обучение

Тип из каталога: **Детерм.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Детальные разборы

- [[interlock-mcp-drift]]

## Реализуемые способы

- [[25-контроль-целостности-описаний-инструментов]] — основной
- [[24-mcp-gateway-rbac]]
