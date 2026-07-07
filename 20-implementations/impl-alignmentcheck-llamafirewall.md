---
type: implementation
method-id: 2
repo: meta-llama/PurpleLlama (LlamaFirewall)
language: Python
license: ""
verdict: экспериментально
tags:
  - agent-security
---

# AlignmentCheck — способ №2

## Репозиторий

https://github.com/meta-llama/PurpleLlama — модуль LlamaFirewall, AlignmentCheck.

## Где в коде

LlamaFirewall: AlignmentCheck auditor над CoT/plan trace.

## Алгоритм

Few-shot-аудитор сравнивает план агента с исходной целью пользователя; флагует расхождения. Бэкенд: Llama 3.3 70B / Llama 4 Maverick. Together API для хостинга `[док]`.

## Детерминизм или машинное обучение

Вероятностный (LLM-судья).

## Внешние зависимости

Крупная модель-бэкенд; Together API опционально.

## Сигналы качества

- Eval: 577 кейсов × 6 моделей
- Документированные обходы: unfaithful CoT, ~63% в AgentDojo (с бэкендом)
- Зрелость: экспериментальная фича `[проверено 2026-07-07]`

## Вердикт

**экспериментально** — сильный сигнал второго эшелона; чувствительность к модели-бэкенду (factcheck OPEN №2).

## Связи

- Способ: [[02-cot-reasoning-audit]]
