---
type: repo-catalog
catalog-id: 47
method-id: 24
also-method-ids:
  - 1
  - 15
repo: https://github.com/invariantlabs-ai/invariant-gateway
language: Python
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-mcp-gateway
  - cluster-content-guardrails-mixed
  - cluster-content-guardrails-ml
---

# invariantlabs-ai/invariant-gateway — каталог №47

## Репозиторий

[invariantlabs-ai/invariant-gateway](https://github.com/invariantlabs-ai/invariant-gateway)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 1+3 |
| Тип | Смешан. |
| Семейства | [[cluster-mcp-gateway]], [[cluster-content-guardrails-mixed]], [[cluster-content-guardrails-ml]] |

## Принцип работы

Шлюз с политиками для агентных трасс

## Алгоритм

Шлюз с политиками для агентных трасс.

Каталожная заметка: основной механизм — **способ №24**; дополнительно перекрывает: способ №15, способ №1.

## Вариант в семействе

Шлюз с политиками для агентных трасс. Родственные реализации — только через семейства: MCP/A2A шлюзы, смешанные guardrails, ML content guardrails.


## Детерминизм или машинное обучение

Тип из каталога: **Смешан.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Реализуемые способы

- [[24-mcp-gateway-rbac]] — основной
- [[01-классификация-инъекций-машинным-обучением]]
- [[15-правила-последовательности-вызовов-и-потоков-данных]]
