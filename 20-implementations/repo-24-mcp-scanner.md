---
type: repo-catalog
catalog-id: 24
method-id: 26
also-method-ids:
  - 25
repo: https://github.com/cisco-ai-defense/mcp-scanner
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

# cisco-ai-defense/mcp-scanner — каталог №24

## Репозиторий

[cisco-ai-defense/mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 2 |
| Тип | Статич. |
| Семейства | [[cluster-supply-chain-scanners]], [[cluster-mcp-trust-runtime]] |

## Принцип работы

Анализ MCP: tools, prompts, malware, готовность к деплою

## Алгоритм

Анализ MCP: tools, prompts, malware, готовность к деплою.

Каталожная заметка: основной механизм — **способ №26**; дополнительно перекрывает: способ №25.

## Вариант в семействе

Cisco MCP scanner: tools, prompts, malware. Родственные реализации — только через семейства: сканеры supply chain, runtime trust MCP.


## Детерминизм или машинное обучение

Тип из каталога: **Статич.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Детальные разборы

- [[mcp-scanner-multi-engine]]

## Реализуемые способы

- [[26-tool-poisoning-scan]] — основной
- [[25-контроль-целостности-описаний-инструментов]]
