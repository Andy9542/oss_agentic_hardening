---
type: repo-catalog
catalog-id: 113
method-id: 25
also-method-ids:
  - 1
  - 7
  - 19
  - 26
repo: https://github.com/aira-security/mcp-armor
language: Python
license: Apache-2.0
verdict: experimental
tags:
  - agent-security
  - repo-catalog
  - review-2026
clusters:
  - cluster-supply-chain-scanners
  - cluster-mcp-trust-runtime
  - cluster-content-guardrails-ml
---

# aira-security/mcp-armor — каталог №113

## Репозиторий

- [aira-security/mcp-armor](https://github.com/aira-security/mcp-armor)
- Проверенный срез: [`6af4cee4665ab6242f02a88952f9127b6a04922a`](https://github.com/aira-security/mcp-armor/commit/6af4cee4665ab6242f02a88952f9127b6a04922a), 2026-03-27.
- Лицензия: [Apache-2.0](https://github.com/aira-security/mcp-armor/blob/6af4cee4665ab6242f02a88952f9127b6a04922a/LICENSE).

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 2 |
| Тип | Смешанный MCP scanner |
| Семейства | [[cluster-supply-chain-scanners]], [[cluster-mcp-trust-runtime]], [[cluster-content-guardrails-ml]] |

## Принцип работы

Обнаруживает конфигурации MCP-клиентов, подключается к серверам, инвентаризирует tools/resources/prompts и сравнивает их metadata с утверждённым SHA-512 baseline; параллельно выполняет структурные и ML-проверки.

## Алгоритм

`inspect` сохраняет идентичность компонентов и SHA-512-хеши описаний, схем, аргументов, URI и metadata; `scan` сопоставляет ключи `(server, entity, config)` и помечает изменённые поля как critical rug pull. Отдельные проверки ищут инъекции, shadowing, неоднозначные имена, избыточные разрешения и секреты. Основной механизм — **способ №25**; дополнительно реализуются способы №1, №7, №19 и №26.

## Вариант в семействе

В отличие от baseline SkillTotal и SkillSpector, MCP Armor фиксирует именно MCP metadata и применяет криптографический SHA-512, а не подавляет fingerprint известных findings. В отличие от Ramparts, OSS-часть ориентирована на конфигурации популярных клиентов и не предоставляет runtime enforcement; автоматических тестов в проверенном срезе нет.

## Детерминизм или машинное обучение

Baseline и structural checks детерминированы. Prompt-injection check использует локальную модель `Aira-security/FT-Llama-Prompt-Guard-2` с порогом 0,8.

## Вердикт

**экспериментально** — полезный detective control для MCP inventory и metadata drift, но без автоматических тестов и блокирующего enforcement-слоя.

## Детальные разборы

- [[impl-mcp-armor]]
- [[mcp-armor-local-prompt-classifier]]
- [[mcp-armor-structural-checks]]

## Реализуемые способы

- [[25-контроль-целостности-описаний-инструментов]] — основной
- [[01-классификация-инъекций-машинным-обучением]]
- [[07-выявление-секретов-в-тексте]]
- [[19-правила-против-инъекций-в-аргументах-инструментов]]
- [[26-tool-poisoning-scan]]
