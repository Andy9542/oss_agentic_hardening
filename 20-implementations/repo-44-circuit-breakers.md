---
type: repo-catalog
catalog-id: 44
method-id: 22
also-method-ids:
  - 1
repo: https://github.com/GraySwanAI/circuit-breakers
language: Python
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-red-team
  - cluster-content-guardrails-ml
---

# GraySwanAI/circuit-breakers — каталог №44

## Репозиторий

[GraySwanAI/circuit-breakers](https://github.com/GraySwanAI/circuit-breakers)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 1 |
| Тип | Вероятн. |
| Семейства | [[cluster-red-team]], [[cluster-content-guardrails-ml]] |

## Принцип работы

«Автоматические выключатели» в весах модели

## Алгоритм

«Автоматические выключатели» в весах модели.

Каталожная заметка: основной механизм — **способ №22**; дополнительно перекрывает: способ №1.

## Вариант в семействе

Circuit breakers в весах модели (research). Родственные реализации — только через семейства: красное тестирование, ML content guardrails.


## Детерминизм или машинное обучение

Тип из каталога: **Вероятн.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Реализуемые способы

- [[22-kill-switch-circuit-breaker]] — основной
- [[01-классификация-инъекций-машинным-обучением]]
