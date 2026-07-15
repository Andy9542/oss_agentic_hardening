---
type: repo-catalog
catalog-id: 4
method-id: 12
also-method-ids:
  - 35
repo: https://github.com/peg/rampart
language: Unknown
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-tool-firewall-yaml
  - cluster-sandbox-isolation
---

# peg/rampart — каталог №4

## Репозиторий

[peg/rampart](https://github.com/peg/rampart)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3 |
| Тип | Детерм. |
| Семейства | [[cluster-tool-firewall-yaml]], [[cluster-sandbox-isolation]] |

## Принцип работы

Файрвол для coding-агентов: политики на файловые и сетевые действия

## Алгоритм

Файрвол для coding-агентов: политики на файловые и сетевые действия.

Каталожная заметка: основной механизм — **способ №12**; дополнительно перекрывает: способ №35.

## Вариант в семействе

Файрвол файловых и сетевых действий coding-агента. Родственные реализации — только через семейства: YAML-файрволы tools, песочницы.


## Детерминизм или машинное обучение

Тип из каталога: **Детерм.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Детальные разборы

- [[rampart-policy-engine]]


## Реализуемые способы

- [[12-tool-policies-yaml-rego]] — основной
- [[35-уровни-исполнения-и-изоляция-рабочего-каталога]]
