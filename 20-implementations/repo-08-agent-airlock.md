---
type: repo-catalog
catalog-id: 8
method-id: 13
also-method-ids:
  - 5
  - 11
  - 12
  - 14
  - 20
  - 33
repo: https://github.com/sattyamjjain/agent-airlock
language: Python
license: ""
verdict: prod
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-sandbox-isolation
  - cluster-formal-policies
  - cluster-tool-firewall-yaml
  - cluster-llm-gateway
  - cluster-content-guardrails-mixed
---

# sattyamjjain/agent-airlock — каталог №8

## Репозиторий

[sattyamjjain/agent-airlock](https://github.com/sattyamjjain/agent-airlock)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3+4 |
| Тип | Детерм. |
| Семейства | [[cluster-sandbox-isolation]], [[cluster-formal-policies]], [[cluster-tool-firewall-yaml]], [[cluster-llm-gateway]], [[cluster-content-guardrails-mixed]] |

## Принцип работы

Декоратор для LangChain/CrewAI: валидация аргументов, RBAC, E2B-песочница

## Алгоритм

Декоратор для LangChain/CrewAI: валидация аргументов, RBAC, E2B-песочница.

Каталожная заметка: основной механизм — **способ №13**; дополнительно перекрывает: способ №33, способ №12, способ №11, способ №5.

## Вариант в семействе

Декоратор LangChain/CrewAI: валидация, RBAC и песочница. Родственные реализации — только через семейства: песочницы, формальные политики, YAML-файрволы tools, LLM-шлюзы, смешанные guardrails.


## Детерминизм или машинное обучение

Тип из каталога: **Детерм.**.

## Вердикт

**готово к продакшену** — каталожная оценка по зрелости репозитория в экосистеме.


## Детальные разборы

- [[agent-airlock-e2b-docker]]
- [[agent-airlock-pii]]
- [[agent-airlock-pydantic-validation]]
- [[agent-airlock-rate-budget]]
- [[impl-agent-airlock]]
- [[impl-agent-airlock-deny]]


## Реализуемые способы

- [[13-проверка-аргументов-по-json-схеме]] — основной
- [[05-выявление-и-маскирование-персональных-данных]]
- [[11-ограничение-токенов-расходов-и-частоты-вызовов]]
- [[12-tool-policies-yaml-rego]]
- [[14-default-deny-allowlists]]
- [[20-ghost-args-strict-typing]]
- [[33-изоляция-агента-в-микровиртуальных-машинах-и-контейнерах]]
