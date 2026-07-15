---
type: repo-catalog
catalog-id: 21
method-id: 26
also-method-ids:
  - 15
  - 28
  - 32
repo: https://github.com/snyk/agent-scan
language: Unknown
license: ""
verdict: prod
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-supply-chain-scanners
  - cluster-artifact-trust
---

# snyk/agent-scan — каталог №21

## Репозиторий

[snyk/agent-scan](https://github.com/snyk/agent-scan)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 2 |
| Тип | Статич. |
| Семейства | [[cluster-supply-chain-scanners]], [[cluster-artifact-trust]] |

## Принцип работы

Сканер агентов, MCP-серверов, навыков (преемник mcp-scan)

## Алгоритм

Сканер агентов, MCP-серверов, навыков (преемник mcp-scan).

Каталожная заметка: основной механизм — **способ №26**; дополнительно перекрывает: способ №28, способ №32.

## Вариант в семействе

Сканер агентов/MCP/навыков (линия Invariant → Snyk). Родственные реализации — только через семейства: сканеры supply chain, доверие к артефактам.


## Детерминизм или машинное обучение

Тип из каталога: **Статич.**.

## Вердикт

**готово к продакшену** — каталожная оценка по зрелости репозитория в экосистеме.


## Детальные разборы

- [[snyk-agent-scan-discovery]]
- [[snyk-toxic-flows]]



## Реализуемые способы

- [[26-tool-poisoning-scan]] — основной
- [[15-правила-последовательности-вызовов-и-потоков-данных]]
- [[28-toxic-flow-analysis]]
- [[32-aibom-inventory]]
