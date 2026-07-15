---
type: implementation-detail
parent-repo: repo-74-inspect-evals
method-id: 45
repo: https://github.com/UKGovernmentBEIS/inspect_evals
language: Python
license: MIT
verdict: prod
commit-sha: 3fda7b0
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# inspect_evals — готовые eval suites (cyber/agents)

## Репозиторий

- [UKGovernmentBEIS/inspect_evals](https://github.com/UKGovernmentBEIS/inspect_evals)
- Проверенный срез: `3fda7b0`; код проверен 2026-07-15.

## Что это за технология

**Библиотека задач** для Inspect AI: agent company, web agents, CyberSecEval 3, CyberGym, CVE exploit suites и др. Способ №45 — конкретные regression packs.

## Где в коде

- `src/inspect_evals/*` — per-benchmark packages
- README catalog с `uv run inspect eval inspect_evals/…`

## Алгоритм

1. Install inspect_ai + inspect_evals.
2. Pick suite (e.g. `cyberseceval_3`, `theagentcompany`).
3. `inspect eval inspect_evals/<name> --model …`.
4. Track metrics over time / models.

## Примеры реализации

```bash
uv run inspect eval inspect_evals/theagentcompany
# Also: cyberseceval_3, cybergym, CVE-based agent exploit benches
```

## Пример: вход → решение

- Agent completes synthetic company multi-tool task → scored.
- Unsafe cyber assist → risk metric flagged.

## Детерминизм или машинное обучение

Задачи фиксированы; scoring зависит от suite.

## Внешние зависимости

Inspect AI; heavy suites may need sandboxes/data.

## Ограничения

- Some challenges excluded for license (noted in README).
- Large compute for agent suites.

## Сигналы качества

- AISI maintained; many contributors.

## Вердикт

**готово к продакшену** как suite pack к Inspect.

## Связи

- Репозиторий: [[repo-74-inspect-evals]]
