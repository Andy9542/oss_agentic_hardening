---
type: repo-catalog
catalog-id: 39
method-id: 1
also-method-ids:
  - 10
repo: https://github.com/guardrails-ai/guardrails
language: Python
license: ""
verdict: prod
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-content-guardrails-mixed
  - cluster-content-guardrails-ml
---

# guardrails-ai/guardrails — каталог №39

## Репозиторий

[guardrails-ai/guardrails](https://github.com/guardrails-ai/guardrails)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 1 |
| Тип | Смешан. |
| Семейства | [[cluster-content-guardrails-mixed]], [[cluster-content-guardrails-ml]] |

## Принцип работы

Валидаторы ввода/вывода, PII, структура

## Алгоритм

Валидаторы ввода/вывода, PII, структура.

Каталожная заметка: основной механизм — **способ №1**; дополнительно перекрывает: способ №10.

## Вариант в семействе

Python-фреймворк валидаторов ввода/вывода. Родственные реализации — только через семейства: смешанные guardrails, ML content guardrails.


## Детерминизм или машинное обучение

Тип из каталога: **Смешан.**.

## Вердикт

**готово к продакшену** — каталожная оценка по зрелости репозитория в экосистеме.

## Реализуемые способы

- [[01-классификация-инъекций-машинным-обучением]] — основной
- [[10-json-schema-constrained]]
