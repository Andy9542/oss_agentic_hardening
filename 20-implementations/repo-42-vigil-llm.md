---
type: repo-catalog
catalog-id: 42
method-id: 1
also-method-ids:
  - 3
repo: https://github.com/deadbits/vigil-llm
language: Python
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-content-guardrails-ml
---

# deadbits/vigil-llm — каталог №42

## Репозиторий

[deadbits/vigil-llm](https://github.com/deadbits/vigil-llm)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 1 |
| Тип | Вероятн. |
| Семейства | [[cluster-content-guardrails-ml]] |

## Принцип работы

YARA + векторное сходство для инъекций

## Алгоритм

YARA + векторное сходство для инъекций.

Каталожная заметка: основной механизм — **способ №1**; дополнительно перекрывает: способ №3.

## Вариант в семействе

YARA + векторное сходство для инъекций. Родственные реализации — только через семейства: ML content guardrails.


## Детерминизм или машинное обучение

Тип из каталога: **Вероятн.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Детальные разборы

- [[vigil-yara-vectordb]]

## Реализуемые способы

- [[01-классификация-инъекций-машинным-обучением]] — основной
- [[03-правила-и-шаблоны-для-выявления-инъекций]]
