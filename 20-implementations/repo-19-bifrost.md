---
type: repo-catalog
catalog-id: 19
method-id: 11
also-method-ids:
  - 1
  - 12
repo: https://github.com/maximhq/bifrost
language: Unknown
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-llm-gateway
  - cluster-content-guardrails-ml
  - cluster-tool-firewall-yaml
---

# maximhq/bifrost — каталог №19

## Репозиторий

[maximhq/bifrost](https://github.com/maximhq/bifrost)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 1+3 |
| Тип | Смешан. |
| Семейства | [[cluster-llm-gateway]], [[cluster-content-guardrails-ml]], [[cluster-tool-firewall-yaml]] |

## Принцип работы

AI-шлюз с встроенными барьерами и лимитами

## Алгоритм

AI-шлюз с встроенными барьерами и лимитами.

Каталожная заметка: основной механизм — **способ №11**; дополнительно перекрывает: способ №1, способ №12.

## Вариант в семействе

AI-шлюз с встроенными барьерами и лимитами. Родственные реализации — только через семейства: LLM-шлюзы, ML content guardrails, YAML-файрволы tools.


## Детерминизм или машинное обучение

Тип из каталога: **Смешан.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Реализуемые способы

- [[11-ограничение-токенов-расходов-и-частоты-вызовов]] — основной
- [[01-классификация-инъекций-машинным-обучением]]
- [[12-tool-policies-yaml-rego]]
