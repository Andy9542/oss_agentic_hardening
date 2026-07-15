---
type: implementation-detail
parent-repo: repo-39-guardrails
method-id: 1
repo: https://github.com/guardrails-ai/guardrails
language: Python
license: Apache-2.0
verdict: prod
commit-sha: 762c7e6
commit-date: 2026-06-19
verified-date: 2026-07-15
tags:
  - agent-security
---

# Guardrails AI — validators + OnFailAction

## Репозиторий

- [guardrails-ai/guardrails](https://github.com/guardrails-ai/guardrails)
- Проверенный срез: `762c7e6`; код проверен 2026-07-15.

## Что это за технология

**Framework структурных и content-валидаторов** вокруг LLM output: RegexMatch, ValidLength, ValidChoices, custom `Validator` → `PassResult`/`FailResult`, политика `on_fail` (EXCEPTION, FILTER, REASK, FIX, REFRAIN, NOOP). Способ №1 (и соседние content rails).

## Где в коде

- Package `guardrails/` — Guard, validators, `types/on_fail`
- Tests: `tests/integration_tests/test_streaming.py`, `test_guard.py`

## Алгоритм

1. Описать schema/validators на поля ответа.
2. LLM generate → validate каждый field.
3. На FailResult применить OnFailAction (reask/fix/exception…).
4. Вернуть validated output или escalate.

## Примеры реализации

```python
RegexMatch(regex="^(?:[A-Z][^\s]*\s?)+$", on_fail="noop")
ValidLength(1, 100, on_fail="noop")
ValidChoices(["Some Name", …], on_fail="noop")
LowerCase(on_fail=OnFailAction.FIX)   # или FILTER / REFRAIN
```

Custom validator returns `FailResult(...)` → streaming path уважает on_fail.

## Пример: вход → решение

- Output не match regex + `on_fail=REASK` → повторный prompt.
- `on_fail=EXCEPTION` → raise.

## Детерминизм или машинное обучение

Validators часто детерминированы; hub может тянуть ML validators.

## Внешние зависимости

Python; optional Hub validators / LLM для reask.

## Ограничения

- Качество = выбранные validators.
- Latency на reask loops.

## Сигналы качества

- Зрелый OSS; богатые integration tests.

## Вердикт

**готово к продакшену** как validation layer.

## Связи

- Репозиторий: [[repo-39-guardrails]]
