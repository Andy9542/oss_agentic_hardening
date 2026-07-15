---
type: repo-catalog
catalog-id: 92
method-id: 3
also-method-ids:
  - 1
repo: https://github.com/MukundaKatta/prompt-injection-shield-py
language: Python
license: MIT
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-content-guardrails-ml
---

# MukundaKatta/prompt-injection-shield — каталог №92

## Репозиторий

Исходный JS-репозиторий [MukundaKatta/prompt-injection-shield](https://github.com/MukundaKatta/prompt-injection-shield) на 2026-07-16 недоступен (404).

Рабочий порт правил 1:1: [MukundaKatta/prompt-injection-shield-py](https://github.com/MukundaKatta/prompt-injection-shield-py) — на него указывает поле `repo` карточки.

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 1 |
| Тип | Детерм. |
| Семейства | [[cluster-content-guardrails-ml]] |

## Принцип работы

Взвешенные regex-правила: `scan(text)` → score / safe при threshold 0.7; `strip_dangerous_lines`.

## Алгоритм

Сумма весов matched rules (clip 1.0) vs threshold. Основной механизм — **способ №3**; в кластере соседствует с ML-гардрейлами (способ №1).

## Вариант в семействе

Щит от инъекций для untrusted text (RAG/tool output). Родственные: agentvet, agentguard (тот же автор).

## Детерминизм или машинное обучение

**Детерм.** regex (не ML-классификатор).

## Вердикт

**экспериментально** — локальный zero-dep pre-filter.

## Детальные разборы

- [[prompt-injection-shield-weighted-rules]]

## Доступность исходников

JS-оригинал удалён/приватный; разбор выполнен по Python-порту `fcfe38c` (2026-06-12).

## Реализуемые способы

- [[03-правила-и-шаблоны-для-выявления-инъекций]] — основной
- [[01-классификация-инъекций-машинным-обучением]]
