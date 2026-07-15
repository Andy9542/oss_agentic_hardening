---
type: repo-catalog
catalog-id: 46
method-id: 15
also-method-ids:
  - 1
  - 7
  - 28
repo: https://github.com/invariantlabs-ai/invariant
language: Python
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-content-guardrails-mixed
  - cluster-content-guardrails-ml
  - cluster-supply-chain-scanners
---

# invariantlabs-ai/invariant — каталог №46

## Репозиторий

[invariantlabs-ai/invariant](https://github.com/invariantlabs-ai/invariant)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 1+2 |
| Тип | Смешан. |
| Семейства | [[cluster-content-guardrails-mixed]], [[cluster-content-guardrails-ml]], [[cluster-supply-chain-scanners]] |

## Принцип работы

Анализ трасс агентов, политики на цепочках вызовов

## Алгоритм

Анализ трасс агентов, политики на цепочках вызовов.

Каталожная заметка: основной механизм — **способ №15**; дополнительно перекрывает: способ №1, способ №28.

## Вариант в семействе

Анализ трасс и политики на цепочках вызовов. Родственные реализации — только через семейства: смешанные guardrails, ML content guardrails, сканеры supply chain.


## Детерминизм или машинное обучение

Тип из каталога: **Смешан.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.


## Детальные разборы

- [[impl-invariant-tfa]]
- [[invariant-flow-rules]]
- [[invariant-prompt-injection]]
- [[invariant-secrets-predicate]]


## Реализуемые способы

- [[15-правила-последовательности-вызовов-и-потоков-данных]] — основной
- [[01-классификация-инъекций-машинным-обучением]]
- [[07-выявление-секретов-в-тексте]]
- [[28-toxic-flow-analysis]]
