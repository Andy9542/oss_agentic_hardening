---
type: repo-catalog
catalog-id: 13
method-id: 12
also-method-ids:
  - 14
repo: https://github.com/log-bell/avakill
language: Unknown
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-tool-firewall-yaml
---

# log-bell/avakill — каталог №13

## Репозиторий

[log-bell/avakill](https://github.com/log-bell/avakill)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3 |
| Тип | Детерм. |
| Семейства | [[cluster-tool-firewall-yaml]] |

## Принцип работы

YAML-политики, три пути enforcement

## Алгоритм

YAML-политики, три пути enforcement.

Каталожная заметка: основной механизм — **способ №12**; дополнительно перекрывает: способ №14.

## Вариант в семействе

YAML-политики с тремя путями enforcement. Родственные реализации — только через семейства: YAML-файрволы tools.


## Детерминизм или машинное обучение

Тип из каталога: **Детерм.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Детальные разборы

- [[avakill-response-scanner]]

## Реализуемые способы

- [[12-tool-policies-yaml-rego]] — основной
- [[14-default-deny-allowlists]]
