---
type: repo-catalog
catalog-id: 7
method-id: 14
also-method-ids:
  - 12
repo: https://github.com/SecAI-Hub/agent-tool-firewall
language: Unknown
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-tool-firewall-yaml
---

# SecAI-Hub/agent-tool-firewall — каталог №7

## Репозиторий

[SecAI-Hub/agent-tool-firewall](https://github.com/SecAI-Hub/agent-tool-firewall)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3 |
| Тип | Детерм. |
| Семейства | [[cluster-tool-firewall-yaml]] |

## Принцип работы

Default-deny YAML-политики на вызовах инструментов

## Алгоритм

Default-deny YAML-политики на вызовах инструментов.

Каталожная заметка: основной механизм — **способ №14**; дополнительно перекрывает: способ №12.

## Вариант в семействе

Default-deny YAML-политики на вызовах инструментов. Родственные реализации — только через семейства: YAML-файрволы tools.


## Детерминизм или машинное обучение

Тип из каталога: **Детерм.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Детальные разборы

- [[agent-tool-firewall-default-deny]]


## Реализуемые способы

- [[14-default-deny-allowlists]] — основной
- [[12-tool-policies-yaml-rego]]
