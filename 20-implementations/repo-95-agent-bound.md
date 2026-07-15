---
type: repo-catalog
catalog-id: 95
method-id: 12
also-method-ids:
  - 14
repo: https://github.com/ElPaisano/agent-bound
language: Unknown
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-tool-firewall-pdp
  - cluster-tool-firewall-yaml
---

# ElPaisano/agent-bound — каталог №95

## Репозиторий

[ElPaisano/agent-bound](https://github.com/ElPaisano/agent-bound)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3 |
| Тип | Детерм. |
| Семейства | [[cluster-tool-firewall-pdp]], [[cluster-tool-firewall-yaml]] |

## Принцип работы

Ограничение границ действий агента

## Алгоритм

Ограничение границ действий агента.

Каталожная заметка: основной механизм — **способ №12**; дополнительно перекрывает: способ №14.

## Вариант в семействе

Ограничение границ действий агента. Родственные реализации — только через семейства: PDP-шлюзы, YAML-файрволы tools.


## Детерминизм или машинное обучение

Тип из каталога: **Детерм.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Реализуемые способы

- [[12-tool-policies-yaml-rego]] — основной
- [[14-default-deny-allowlists]]
