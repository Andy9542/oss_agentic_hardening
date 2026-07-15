---
type: repo-catalog
catalog-id: 76
method-id: 44
also-method-ids:
  - 1
repo: https://github.com/NVIDIA/garak
language: Python
license: ""
verdict: prod
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-red-team
  - cluster-content-guardrails-ml
---

# NVIDIA/garak — каталог №76

## Репозиторий

[NVIDIA/garak](https://github.com/NVIDIA/garak)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | — |
| Тип | Red team |
| Семейства | [[cluster-red-team]], [[cluster-content-guardrails-ml]] |

## Принцип работы

100+ детекторов уязвимостей LLM

## Алгоритм

100+ детекторов уязвимостей LLM.

Каталожная заметка: основной механизм — **способ №44**; дополнительно перекрывает: способ №1.

## Вариант в семействе

100+ детекторов уязвимостей LLM. Родственные реализации — только через семейства: красное тестирование, ML content guardrails.


## Детерминизм или машинное обучение

Тип из каталога: **Red team**.

## Вердикт

**готово к продакшену** — каталожная оценка по зрелости репозитория в экосистеме.


## Детальные разборы

- [[impl-garak]]


## Реализуемые способы

- [[44-red-team-regression]] — основной
- [[01-классификация-инъекций-машинным-обучением]]
