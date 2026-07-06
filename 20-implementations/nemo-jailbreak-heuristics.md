---
type: implementation
method-id: 3
repo: https://github.com/NVIDIA-NeMo/Guardrails
language: Python
license: Apache-2.0
verdict: prod
tags: [agent-security]
---

# NeMo — jailbreak heuristics

## Репозиторий

[NVIDIA-NeMo/Guardrails](https://github.com/NVIDIA-NeMo/Guardrails)

## Где в коде

- Input rails: jailbreak heuristics в Colang flows
- `config.yml` + `.co` files

## Алгоритм

Keyword/heuristic matching + Colang dialog flows; часть self-check на LLM.

## Детерминизм или машинное обучение

Смешанный: heuristics — Д; self-check — В.

## Внешние зависимости

LLM для rails; ActiveFence опционально.

## Сигналы качества

- NVIDIA production guardrails
- Gap: tool messages не проходят input rails

## Вердикт

**готово к продакшену** для dialog bots; tool-heavy — добавить execution rails.

## Связи

- Способ: [[03-heuristics-regex-injection]]
