---
type: implementation-detail
parent-repo: repo-83-deepteam
method-id: 44
repo: https://github.com/confident-ai/deepteam
language: Python
license: Apache-2.0
verdict: experimental
commit-sha: 6ceb27d
commit-date: 2026-07-09
verified-date: 2026-07-15
tags:
  - agent-security
---

# DeepTeam — red_team(vulnerabilities, attacks)

## Репозиторий

- [confident-ai/deepteam](https://github.com/confident-ai/deepteam)
- Проверенный срез: `6ceb27d`; код проверен 2026-07-15.

## Что это за технология

**Confident AI red-teaming library**: `red_team(model_callback, vulnerabilities=[…], attacks=[…])` — симулирует атаки на типы уязвимостей (prompt_leakage, excessive_agency, exploit_tool_agent, PII, hallucination, …) и оценивает risk. Способ №44.

## Где в коде

- `deepteam/red_team.py` — public API
- `deepteam/vulnerabilities/*`, `deepteam/attacks/`
- `deepteam/frameworks/risk_category.py`

## Алгоритм

1. Provide `model_callback` for target.
2. Select vulnerability classes + attack strategies.
3. Simulator model generates attacks_per_vulnerability_type.
4. Evaluation model scores → risk_assessment.

## Примеры реализации

```python
def red_team(model_callback, vulnerabilities=None, attacks=None,
             simulator_model="gpt-4o-mini", evaluation_model="gpt-4o-mini",
             attacks_per_vulnerability_type=1, …):
    return RedTeamer(…).red_team(…)
```

Vuln modules: `excessive_agency`, `exploit_tool_agent`, `prompt_leakage`, `pii_leakage`, `autonomous_agent_drift`, …

## Пример: вход → решение

- `excessive_agency` attacks → model over-acts → failed metric.
- Refusals / scoped tools → pass.

## Детерминизм или машинное обучение

Симуляция/оценка — **LLM-driven**.

## Внешние зависимости

deepeval models; OpenAI-compatible APIs.

## Ограничения

- Simulator refusals if guardrailed (documented error).
- Cost of many vuln×attack combos.

## Сигналы качества

- Confident AI; rich vuln taxonomy; tests.

## Вердикт

**экспериментально** — API-first agent/LLM red team.

## Связи

- Репозиторий: [[repo-83-deepteam]]
