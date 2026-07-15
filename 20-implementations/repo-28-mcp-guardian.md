---
type: repo-catalog
catalog-id: 28
method-id: 26
also-method-ids:
  - 25
repo: https://github.com/alexandriashai/mcp-guardian
language: Unknown
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-supply-chain-scanners
  - cluster-mcp-trust-runtime
---

# alexandriashai/mcp-guardian — каталог №28

## Репозиторий

[alexandriashai/mcp-guardian](https://github.com/alexandriashai/mcp-guardian)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 2 |
| Тип | Статич. |
| Семейства | [[cluster-supply-chain-scanners]], [[cluster-mcp-trust-runtime]] |

## Принцип работы

Детекция инъекций в описаниях MCP-инструментов

## Алгоритм

Детекция инъекций в описаниях MCP-инструментов.

Каталожная заметка: основной механизм — **способ №26**; дополнительно перекрывает: способ №25.

## Вариант в семействе

Детекция инъекций в описаниях MCP-инструментов. Родственные реализации — только через семейства: сканеры supply chain, runtime trust MCP.


## Детерминизм или машинное обучение

Тип из каталога: **Статич.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Детальные разборы

- [[mcp-guardian-tool-desc-scan]]


## Реализуемые способы

- [[26-tool-poisoning-scan]] — основной
- [[25-контроль-целостности-описаний-инструментов]]
