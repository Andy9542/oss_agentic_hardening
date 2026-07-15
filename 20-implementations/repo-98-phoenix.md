---
type: repo-catalog
catalog-id: 98
method-id: 40
also-method-ids:
  - 9
  - 37
repo: https://github.com/Arize-AI/phoenix
language: Python
license: ""
verdict: prod
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-observability
  - cluster-content-guardrails-mixed
---

# Arize-AI/phoenix — каталог №98

## Репозиторий

[Arize-AI/phoenix](https://github.com/Arize-AI/phoenix)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 2 |
| Тип | Наблюд. |
| Семейства | [[cluster-observability]], [[cluster-content-guardrails-mixed]] |

## Принцип работы

Трассировка, eval RAG, галлюцинации

## Алгоритм

Трассировка, eval RAG, галлюцинации.

Каталожная заметка: основной механизм — **способ №40**; дополнительно перекрывает: способ №9, способ №37.

## Вариант в семействе

Трассировка, eval RAG, галлюцинации. Родственные реализации — только через семейства: наблюдаемость, смешанные guardrails.


## Детерминизм или машинное обучение

Тип из каталога: **Наблюд.**.

## Вердикт

**готово к продакшену** — каталожная оценка по зрелости репозитория в экосистеме.

## Реализуемые способы

- [[40-opentelemetry-siem]] — основной
- [[09-проверка-фактической-точности-и-галлюцинаций]]
- [[37-выявление-поведенческих-отклонений]]
