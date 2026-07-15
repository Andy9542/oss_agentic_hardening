---
type: repo-catalog
catalog-id: 101
method-id: 30
repo: https://github.com/semgrep/semgrep
language: OCaml/Python
license: ""
verdict: prod
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-static-code-sast
---

# semgrep/semgrep — каталог №101

## Репозиторий

[semgrep/semgrep](https://github.com/semgrep/semgrep)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 4 |
| Тип | Статич. |
| Семейства | [[cluster-static-code-sast]] |

## Принцип работы

Rule-based SAST для кода, генерируемого coding-агентами

## Алгоритм

Rule-based SAST для кода, генерируемого coding-агентами.

Каталожная заметка: основной механизм — **способ №30**.

## Вариант в семействе

Зрелый SAST; эталон способа №30 (static analysis кода агента). Родственные реализации — только через семейства: static-code-sast.

## Детерминизм или машинное обучение

Тип из каталога: **Статич.**.

## Вердикт

**готово к продакшену** — каталожная оценка по зрелости репозитория в экосистеме.

## Детальные разборы

- [[impl-semgrep]]

## Реализуемые способы

- [[30-static-analysis-code]] — основной
