---
type: repo-catalog
catalog-id: 43
method-id: 1
also-method-ids:
  - 37
repo: https://github.com/whylabs/langkit
language: Python
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-content-guardrails-mixed
  - cluster-content-guardrails-ml
  - cluster-observability
---

# whylabs/langkit — каталог №43

## Репозиторий

[whylabs/langkit](https://github.com/whylabs/langkit)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 1+2 |
| Тип | Вероятн. |
| Семейства | [[cluster-content-guardrails-mixed]], [[cluster-content-guardrails-ml]], [[cluster-observability]] |

## Принцип работы

Мониторинг инъекций, дрейфа, токсичности

## Алгоритм

Мониторинг инъекций, дрейфа, токсичности.

Каталожная заметка: основной механизм — **способ №1**; дополнительно перекрывает: способ №37.

## Вариант в семействе

Мониторинг инъекций, дрейфа, токсичности. Родственные реализации — только через семейства: смешанные guardrails, ML content guardrails, наблюдаемость.


## Детерминизм или машинное обучение

Тип из каталога: **Вероятн.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Детальные разборы

- [[langkit-proactive-injection]]

## Реализуемые способы

- [[01-классификация-инъекций-машинным-обучением]] — основной
- [[37-выявление-поведенческих-отклонений]]
