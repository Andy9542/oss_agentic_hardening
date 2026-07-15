---
type: repo-catalog
catalog-id: 102
method-id: 18
repo: https://github.com/authzed/spicedb
language: Go
license: ""
verdict: prod
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-formal-policies
  - cluster-tool-firewall-pdp
---

# authzed/spicedb — каталог №102

## Репозиторий

[authzed/spicedb](https://github.com/authzed/spicedb)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3 |
| Тип | Детерм. |
| Семейства | [[cluster-formal-policies]], [[cluster-tool-firewall-pdp]] |

## Принцип работы

Google Zanzibar-style ReBAC: CheckPermission на графе user→agent→tool

## Алгоритм

Google Zanzibar-style ReBAC: CheckPermission на графе user→agent→tool.

Каталожная заметка: основной механизм — **способ №18**.

## Вариант в семействе

Enterprise ReBAC; эталон способа №18; опциональный backend в Janus. Родственные реализации — только через семейства: formal-policies, tool-firewall-pdp.

## Детерминизм или машинное обучение

Тип из каталога: **Детерм.**.

## Вердикт

**готово к продакшену** — каталожная оценка по зрелости репозитория в экосистеме.

## Детальные разборы

- [[impl-spicedb]]

## Реализуемые способы

- [[18-rebac-spicedb]] — основной
