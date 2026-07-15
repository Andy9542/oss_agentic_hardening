---
type: repo-catalog
catalog-id: 56
method-id: 43
also-method-ids:
  - 16
repo: https://github.com/google-research/camel-prompt-injection
language: Python
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-capability-camel
  - cluster-os-isolation
---

# google-research/camel-prompt-injection — каталог №56

## Репозиторий

[google-research/camel-prompt-injection](https://github.com/google-research/camel-prompt-injection)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3+4 |
| Тип | Детерм. |
| Семейства | [[cluster-capability-camel]], [[cluster-os-isolation]] |

## Принцип работы

CaMeL: capability-based контроль + разделение доверенных данных

## Алгоритм

CaMeL: capability-based контроль + разделение доверенных данных.

Каталожная заметка: основной механизм — **способ №43**; дополнительно перекрывает: способ №16.

## Вариант в семействе

CaMeL: capability-based контроль (research). Родственные реализации — только через семейства: capability (CaMeL), изоляция ОС (eBPF).


## Детерминизм или машинное обучение

Тип из каталога: **Детерм.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.


## Детальные разборы

- [[camel-dual-llm-quarantine]]
- [[impl-camel]]


## Реализуемые способы

- [[43-две-модели-с-разделением-доверия-и-карантином]] — основной
- [[16-ifc-capability-taint]]
