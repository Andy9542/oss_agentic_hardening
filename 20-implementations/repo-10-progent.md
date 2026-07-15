---
type: repo-catalog
catalog-id: 10
method-id: 17
also-method-ids:
  - 12
  - 21
repo: https://github.com/sunblaze-ucb/progent
language: Python
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-formal-policies
  - cluster-tool-firewall-yaml
---

# sunblaze-ucb/progent — каталог №10

## Репозиторий

[sunblaze-ucb/progent](https://github.com/sunblaze-ucb/progent)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3 |
| Тип | Детерм. |
| Семейства | [[cluster-formal-policies]], [[cluster-tool-firewall-yaml]] |

## Принцип работы

Модульные политики привилегий + SMT-проверка

## Алгоритм

Модульные политики привилегий + SMT-проверка.

Каталожная заметка: основной механизм — **способ №17**; дополнительно перекрывает: способ №12.

## Вариант в семействе

Модульные политики привилегий с SMT-проверкой. Родственные реализации — только через семейства: формальные политики, YAML-файрволы tools.


## Детерминизм или машинное обучение

Тип из каталога: **Детерм.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.


## Детальные разборы

- [[impl-progent]]
- [[progent-expansion-approval]]
- [[progent-smt-monotonic]]


## Реализуемые способы

- [[17-формальная-проверка-политик-и-сужение-привилегий]] — основной
- [[12-tool-policies-yaml-rego]]
- [[21-одобрение-опасных-действий-человеком]]
