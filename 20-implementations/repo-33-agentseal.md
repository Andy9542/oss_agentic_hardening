---
type: repo-catalog
catalog-id: 33
method-id: 31
also-method-ids:
  - 4
  - 26
repo: https://github.com/getagentseal/agentseal
language: Unknown
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-artifact-trust
---

# getagentseal/agentseal — каталог №33

## Репозиторий

[getagentseal/agentseal](https://github.com/getagentseal/agentseal)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 2 |
| Тип | Статич. |
| Семейства | [[cluster-artifact-trust]] |

## Принцип работы

Подпись и верификация артефактов агентов

## Алгоритм

Подпись и верификация артефактов агентов.

Каталожная заметка: основной механизм — **способ №31**; дополнительно перекрывает: способ №4.

## Вариант в семействе

Подпись и верификация артефактов агентов. Родственные реализации — только через семейства: доверие к артефактам.


## Детерминизм или машинное обучение

Тип из каталога: **Статич.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.


## Детальные разборы

- [[impl-agentseal]]
- [[impl-agentseal-unicode]]


## Реализуемые способы

- [[31-допуск-артефактов-и-отзыв-по-чёрному-списку]] — основной
- [[04-unicode-normalization]]
- [[26-tool-poisoning-scan]]
