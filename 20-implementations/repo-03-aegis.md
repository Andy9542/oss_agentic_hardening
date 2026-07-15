---
type: repo-catalog
catalog-id: 3
method-id: 12
also-method-ids:
  - 1
  - 3
  - 19
  - 21
  - 37
  - 39
repo: https://github.com/Justin0504/Aegis
language: Go
license: ""
verdict: prod
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-tool-firewall-pdp
  - cluster-tool-firewall-yaml
  - cluster-governance-platform
  - cluster-content-guardrails-ml
  - cluster-observability
---

# Justin0504/Aegis — каталог №3

## Репозиторий

[Justin0504/Aegis](https://github.com/Justin0504/Aegis)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3 |
| Тип | Детерм. |
| Семейства | [[cluster-tool-firewall-pdp]], [[cluster-tool-firewall-yaml]], [[cluster-governance-platform]], [[cluster-content-guardrails-ml]], [[cluster-observability]] |

## Принцип работы

Шлюз с PDP: перехват вызовов, RBAC, аудит, SDK на Go/Python

## Алгоритм

Шлюз с PDP: перехват вызовов, RBAC, аудит, SDK на Go/Python.

Каталожная заметка: основной механизм — **способ №12**; дополнительно перекрывает: способ №21, способ №39, способ №1, способ №37.

## Вариант в семействе

PDP-шлюз с RBAC и аудитом на границе tool-call. Родственные реализации — только через семейства: PDP-шлюзы, YAML-файрволы tools, платформы governance, ML content guardrails, наблюдаемость.


## Детерминизм или машинное обучение

Тип из каталога: **Детерм.**.

## Вердикт

**готово к продакшену** — каталожная оценка по зрелости репозитория в экосистеме.


## Детальные разборы

- [[aegis-behavioral-anomaly]]
- [[aegis-hash-chain-audit]]
- [[aegis-human-approval]]
- [[aegis-injection-patterns]]
- [[aegis-injection-scanner]]


## Реализуемые способы

- [[12-tool-policies-yaml-rego]] — основной
- [[01-классификация-инъекций-машинным-обучением]]
- [[03-правила-и-шаблоны-для-выявления-инъекций]]
- [[19-правила-против-инъекций-в-аргументах-инструментов]]
- [[21-одобрение-опасных-действий-человеком]]
- [[37-выявление-поведенческих-отклонений]]
- [[39-неизменяемый-журнал-с-цепочкой-хешей-и-подписями]]
