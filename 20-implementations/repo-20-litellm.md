---
type: repo-catalog
catalog-id: 20
method-id: 11
also-method-ids:
  - 40
repo: https://github.com/BerriAI/litellm
language: Python
license: ""
verdict: prod
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-llm-gateway
  - cluster-observability
---

# BerriAI/litellm — каталог №20

## Репозиторий

[BerriAI/litellm](https://github.com/BerriAI/litellm)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 1+2 |
| Тип | Смешан. |
| Семейства | [[cluster-llm-gateway]], [[cluster-observability]] |

## Принцип работы

Прокси LLM с guardrails, бюджетами, логированием

## Алгоритм

Прокси LLM с guardrails, бюджетами, логированием.

Каталожная заметка: основной механизм — **способ №11**; дополнительно перекрывает: способ №40.

## Вариант в семействе

LLM-прокси с guardrails, бюджетами и логированием. Родственные реализации — только через семейства: LLM-шлюзы, наблюдаемость.


## Детерминизм или машинное обучение

Тип из каталога: **Смешан.**.

## Вердикт

**готово к продакшену** — каталожная оценка по зрелости репозитория в экосистеме.

## Реализуемые способы

- [[11-ограничение-токенов-расходов-и-частоты-вызовов]] — основной
- [[40-opentelemetry-siem]]
