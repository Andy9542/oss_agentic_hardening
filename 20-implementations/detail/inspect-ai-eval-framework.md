---
type: implementation-detail
parent-repo: repo-73-inspect-ai
method-id: 45
repo: https://github.com/UKGovernmentBEIS/inspect_ai
language: Python
license: MIT
verdict: prod
commit-sha: 6202670
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# Inspect AI — framework eval задач агентов/LLM

## Репозиторий

- [UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai)
- Проверенный срез: `6202670`; код проверен 2026-07-15.

## Что это за технология

**UK AISI eval framework**: `@task` registry, solvers, scorers, `TaskState`, agent loops — единый способ запускать safety/capability evals (в т.ч. cyber). Способ №45.

## Где в коде

- `src/inspect_ai/_eval/registry.py` — `@task`
- `src/inspect_ai/solver/`, `_eval/run.py` (`TaskInjection`)
- CLI `inspect eval …`

## Алгоритм

1. Define `@task` с dataset + solver + scorer.
2. `inspect eval path/to/task` with model.
3. Agent/solver produces trajectory in TaskState.
4. Scorer → metrics/logs.

## Примеры реализации

```python
@task
def my_eval():
    return Task(dataset=…, solver=…, scorer=…)
# TaskInjection / TaskState drive multi-step agent evals
```

## Пример: вход → решение

- Cyber task: agent fails exploit → score 0.
- Capability task correct → score 1.

## Детерминизм или машинное обучение

Harness детерминирован; model outcomes — нет.

## Внешние зависимости

Python; model providers; optional sandbox for agents.

## Ограничения

- Tasks live often in inspect_evals sibling.
- Learning curve API.

## Сигналы качества

- UK Gov AISI; active; widely used.

## Вердикт

**готово к продакшену** как eval platform.

## Связи

- Репозиторий: [[repo-73-inspect-ai]]
