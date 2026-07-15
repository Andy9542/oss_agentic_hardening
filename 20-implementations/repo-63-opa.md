---
type: repo-catalog
catalog-id: 63
method-id: 12
also-method-ids:
  - 17
repo: https://github.com/open-policy-agent/opa
language: Go
license: ""
verdict: prod
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-formal-policies
  - cluster-tool-firewall-yaml
---

# open-policy-agent/opa — каталог №63

## Репозиторий

[open-policy-agent/opa](https://github.com/open-policy-agent/opa)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3 |
| Тип | Детерм. |
| Семейства | [[cluster-formal-policies]], [[cluster-tool-firewall-yaml]] |

## Принцип работы

Движок политик Rego для авторизации

## Алгоритм

Движок политик Rego для авторизации.

Каталожная заметка: основной механизм — **способ №12**; дополнительно перекрывает: способ №17.

## Вариант в семействе

Движок политик Rego (OPA). Родственные реализации — только через семейства: формальные политики, YAML-файрволы tools.


## Детерминизм или машинное обучение

Тип из каталога: **Детерм.**.

## Вердикт

**готово к продакшену** — каталожная оценка по зрелости репозитория в экосистеме.


## Детальные разборы

- [[impl-opa-cedar]]


## Реализуемые способы

- [[12-tool-policies-yaml-rego]] — основной
- [[17-формальная-проверка-политик-и-сужение-привилегий]]
