---
type: implementation-detail
parent-repo: repo-45-plexiglass
method-id: 44
repo: https://github.com/kortex-labs/plexiglass
language: Python
license: Apache-2.0
verdict: experimental
commit-sha: 54bf161
commit-date: 2026-02-04
verified-date: 2026-07-15
tags:
  - agent-security
---

# Plexiglass — red-team harness для LLM/агентов

## Репозиторий

- [kortex-labs/plexiglass](https://github.com/kortex-labs/plexiglass)
- Проверенный срез: `54bf161`; код проверен 2026-07-15.

## Что это за технология

**Оффенсивный/eval harness** (не защитный proxy): прогоняет атаки/пробы против LLM или агента, собирает успех jailbreak/injection. Способ №44 (red team regression).

## Где в коде

- Package/CLI в корне; examples/attacks
- README — attack modules / scan flows

## Алгоритм

1. Указать target (API/agent endpoint).
2. Выбрать attack suite / probes.
3. Execute prompts; score success/fail.
4. Report для regression CI.

## Примеры реализации

Типовой цикл: load attack prompts → call model → judge whether policy broken → aggregate ASR (attack success rate).

## Пример: вход → решение

- Suite jailbreak → 30% ASR → fail quality gate if > threshold.
- Hardened model → ASR↓ → pass.

## Детерминизм или машинное обучение

Атаки детерминированы; judge может быть LLM.

## Внешние зависимости

Target LLM API.

## Ограничения

- Это оружие тестирования, не runtime control.
- Coverage зависит от suites.

## Сигналы качества

- Kortex labs; structured attack modules.

## Вердикт

**экспериментально** — red-team companion к защитам.

## Связи

- Репозиторий: [[repo-45-plexiglass]]
