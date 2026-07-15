---
type: implementation-detail
parent-repo: repo-89-autodefense
method-id: 43
repo: https://github.com/XHMY/AutoDefense
language: Python
license: MIT
verdict: experimental
commit-sha: 721655c
commit-date: 2026-01-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# AutoDefense — multi-agent jailbreak detector (AutoGen)

## Репозиторий

- [XHMY/AutoDefense](https://github.com/XHMY/AutoDefense)
- Проверенный срез: `721655c`; код проверен 2026-07-15.

## Что это за технология

**Multi-agent defense** (AutoGen): response жертвы проходит через agency из 1–4 explicit detector agents + Coordinator/Output — решают, jailbreak ли ответ. Способ №43 (две модели / разделение ролей) в multi-agent форме.

## Где в коде

- `defense/explicit_detector/agency/explicit_{1,2,3,4}_agents.py`
- `defense/explicit_detector/explicit_defense_arch.py`
- `defense/run_defense_exp.py`

## Алгоритм

1. Victim LLM produces response to (possibly jailbreak) prompt.
2. TaskAgency / explicit agents debate/classify harmfulness.
3. Coordinator routes; OutputAgent emits final allow/block.
4. Measure defense ASR reduction.

## Примеры реализации

```python
# explicit_defense_arch: User_Prompt_Agent, LLM_Victim_Agent,
# Task_Agency_Agent, Output_Agent (+ Coordinator mentions exactly one agent)
strategies: explicit_1_agent, explicit_1_agent_CoT, explicit_2/3/4_agents
```

## Пример: вход → решение

- Jailbreak elicits harmful answer → detector agency → block/flag.
- Benign answer → allow.

## Детерминизм или машинное обучение

Агенты — LLM (вероятностны).

## Внешние зависимости

vLLM/AutoGen; GPU recommended.

## Ограничения

- Latency/cost of multi-agent path.
- Research experiment harness.

## Сигналы качества

- AutoGen blog; explicit strategy variants.

## Вердикт

**экспериментально** — multi-agent content quarantine pattern.

## Связи

- Репозиторий: [[repo-89-autodefense]]
