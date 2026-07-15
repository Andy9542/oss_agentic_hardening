---
type: repo-catalog
catalog-id: 41
method-id: 1
also-method-ids:
  - 7
repo: https://github.com/protectai/rebuff
language: Python
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-content-guardrails-ml
---

# protectai/rebuff — каталог №41

## Репозиторий

[protectai/rebuff](https://github.com/protectai/rebuff)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 1 |
| Тип | Вероятн. |
| Семейства | [[cluster-content-guardrails-ml]] |

## Принцип работы

Эвристики + LLM-классификатор + canary-токены

## Алгоритм

Эвристики + LLM-классификатор + canary-токены.

Каталожная заметка: основной механизм — **способ №1**; дополнительно перекрывает: способ №7.

## Вариант в семействе

Эвристики + LLM-классификатор + canary-токены. Родственные реализации — только через семейства: ML content guardrails.


## Детерминизм или машинное обучение

Тип из каталога: **Вероятн.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Детальные разборы

- [[rebuff-triple-detection]]

## Реализуемые способы

- [[01-классификация-инъекций-машинным-обучением]] — основной
- [[07-выявление-секретов-в-тексте]]
