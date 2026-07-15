---
type: implementation-detail
parent-repo: repo-50-agentshield
method-id: 12
repo: https://github.com/AdityaBelhekar/AgentShield
language: Python
license: MIT
verdict: experimental
commit-sha: 702a203
commit-date: 2026-04-25
verified-date: 2026-07-15
tags:
  - agent-security
---

# AgentShield (Belhekar) — runtime policy wrapper

## Репозиторий

- [AdityaBelhekar/AgentShield](https://github.com/AdityaBelhekar/AgentShield)
- Проверенный срез: `702a203`; код проверен 2026-07-15.

## Что это за технология

**Runtime SDK** `shield(agent, policy=…)` для LangChain/LlamaIndex/AutoGen/OpenAI: перехват tool chains, goal drift, exfil. Presets `monitor_only` / `no_exfiltration` / `strict` или YAML. Не путать с affaan-m AgentShield (config auditor). Способ №12.

## Где в коде

- `agentshield/policy/` — compiler, evaluator, models
- QUICKSTART.md / README presets
- `backend/` — optional service

## Алгоритм

1. `protected = shield(agent, tools=tools, policy="strict")`.
2. На каждом tool call: policy evaluator (blocked tools, read→send chains).
3. Action: allow / block / alert per severity.
4. Optional `agentshield certify` offline.

## Примеры реализации

```python
protected = shield(agent, policy="no_exfiltration")
# read→send chain → blocked

# YAML
# tool_names: [bash, shell, execute_code]  # deny/restrict
policy="./my_policy.yaml"
```

Presets: monitor_only (log), no_exfiltration, strict (medium drift blocks).

## Пример: вход → решение

- Agent: read file → email contents → `no_exfiltration` blocks.
- `monitor_only` → allow + alert.

## Детерминизм или машинное обучение

Политики в основном **детерминированные**; drift detection может быть смешанным.

## Внешние зависимости

Python; framework agent object.

## Ограничения

- Нужна интеграция wrapper’ом.
- Молодой SDK — калибровать FP.

## Сигналы качества

- Multi-framework claims; certify CLI; tests/backend.

## Вердикт

**экспериментально** — runtime policy shield.

## Связи

- Репозиторий: [[repo-50-agentshield]]
