---
type: repo-catalog
catalog-id: 77
method-id: 44
also-method-ids:
  - 1
repo: https://github.com/microsoft/PyRIT
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

# Azure/PyRIT — каталог №77

## Репозиторий

[Azure/PyRIT](https://github.com/microsoft/PyRIT)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | — |
| Тип | Red team |
| Семейства | [[cluster-red-team]], [[cluster-content-guardrails-ml]] |

## Принцип работы

Оркестрация многоходовых атак

## Алгоритм

Оркестрация многоходовых атак.

Каталожная заметка: основной механизм — **способ №44**; дополнительно перекрывает: способ №1.

## Вариант в семействе

Оркестрация многоходовых атак. Родственные реализации — только через семейства: красное тестирование, ML content guardrails.


## Детерминизм или машинное обучение

Тип из каталога: **Red team**.

## Вердикт

**готово к продакшену** — каталожная оценка по зрелости репозитория в экосистеме.

## Детальные разборы

- [[pyrit-attack-scorer-pipeline]]

## Реализуемые способы

- [[44-red-team-regression]] — основной
- [[01-классификация-инъекций-машинным-обучением]]
