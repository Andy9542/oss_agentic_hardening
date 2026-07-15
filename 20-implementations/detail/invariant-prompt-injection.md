---
type: implementation-detail
parent-repo: repo-46-invariant
method-id: 1
repo: https://github.com/invariantlabs-ai/invariant
language: Python
license: Apache-2.0
verdict: exp
tags:
  - agent-security
---

# Invariant — prompt_injection()

## Репозиторий

[invariantlabs-ai/invariant](https://github.com/invariantlabs-ai/invariant)

## Где в коде

- Встроенный предикат `prompt_injection(text, threshold=0.7)` в DSL правил
- `LocalPolicy` — offline; Gateway — proxy mode

## Алгоритм

ML-классификатор внутри декларативного правила; порог настраивается.

## Детерминизм или машинное обучение

Смешанный: правило детерминировано, классификатор — нет.

## Внешние зависимости

Invariant Cloud API опционально (`INVARIANT_API_KEY`).

## Сигналы качества

- Сильная сторона — flow rules, не ML
- ML injection — вспомогательный предикат

## Вердикт

**экспериментально** как ML-barrier; **готово к продакшену** в связке со способом №15 (flow rules).

## Связи

- Репозиторий: [[repo-46-invariant]]
