---
type: repo-catalog
catalog-id: 116
method-id: 44
repo: https://github.com/HiveTrace/HiveTraceRed
language: Python
license: Apache-2.0
verdict: experimental
tags:
  - agent-security
  - repo-catalog
  - review-2026
clusters:
  - cluster-red-team
  - cluster-benchmarks
---

# HiveTrace/HiveTraceRed — каталог №116

## Репозиторий

[HiveTrace/HiveTraceRed](https://github.com/HiveTrace/HiveTraceRed), проверенная ревизия `975fd99` от 2026-06-25.

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | — |
| Тип | Red team |
| Семейства | [[cluster-red-team]], [[cluster-benchmarks]] |

## Принцип работы

Multilingual red-team framework генерирует jailbreak-промпты, асинхронно опрашивает целевые модели, оценивает ответы и формирует отчёт для повторяемых проверок.

## Алгоритм

Четырёхстадийный pipeline применяет библиотеку атак к исходным промптам, собирает ответы провайдеров, классифицирует успешность обхода и строит HTML-отчёт. Основной и единственный каталожный механизм — **способ №44**.

## Вариант в семействе

HiveTraceRed ориентирован на multilingual content-level red teaming, включая русский язык. Он проверяет guardrails до релиза, но не блокирует действия агента во время исполнения.

## Детерминизм или машинное обучение

Статические преобразования и оркестрация детерминированы; model-based, iterative и conversational атаки, ответы целей и модельные evaluators вероятностны.

## Вердикт

**экспериментально** — молодой исследовательский framework с хорошим собственным test suite.

## Детальные разборы

- [[impl-hivetrace-red]]
- [[hivetrace-attack-library]]
- [[hivetrace-evaluation-reporting]]

## Реализуемые способы

- [[44-red-team-regression]] — основной
