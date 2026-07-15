---
type: implementation-detail
parent-repo: repo-15-agentgate-public
method-id: 12
repo: https://github.com/ElamOlame31/agentgate-public
language: Python
license: Apache-2.0
verdict: experimental
commit-sha: 6ef46f0
commit-date: 2026-06-26
verified-date: 2026-07-15
tags:
  - agent-security
---

# AgentGate — PDP с fnmatch-политиками и time windows

## Репозиторий

- [ElamOlame31/agentgate-public](https://github.com/ElamOlame31/agentgate-public)
- Проверенный срез: `6ef46f0`, дата коммита 2026-06-26; код проверен 2026-07-15.

## Что это за технология

**Policy Decision Point до действия**: политики (DENY / ESCALATE) матчят `agent_id`, `action`, `resource` через `fnmatch`. Опциональные time windows (внутри/снаружи бизнес-часов). Plain-English → structured policy через Claude или keyword fallback. DENY бьёт ESCALATE. Способ №12 + №21.

## Где в коде

- `core/policy_engine.py` — `check_policies`, `create_policy`, time gates
- Templates: `templates/hipaa.yaml`, `gdpr.yaml`, `soc2.yaml`
- MCP proxy: `server/mcp_proxy.py`
- Integrations: LangChain / OpenAI Agents

## Алгоритм

1. Создать policy (LLM parse или fallback keywords never/deny/block…).
2. На запрос: для каждой active policy проверить time window.
3. `fnmatch(agent)`, `fnmatch(action)`, `fnmatch(resource)`.
4. Первая DENY → hard block; иначе ESCALATE → HITL; иначе no match.
5. Trust scoring (если есть) идёт **после** hard DENY.

## Примеры реализации

```python
agent_ok = policy.agent_pattern == "*" or fnmatch.fnmatch(agent_id, policy.agent_pattern)
action_ok = fnmatch.fnmatch(action.lower(), policy.action_pattern.lower())
resource_ok = fnmatch.fnmatch(resource.lower(), policy.resource_pattern.lower())
# DENY beats ESCALATE; first DENY wins
```

Fallback: слова `never|deny|block|forbid` → effect DENY.

## Пример: вход → решение

- Policy DENY `action=shell.*` `resource=*` → `shell.exec` blocked.
- ESCALATE payments outside 09:00–17:00 → require human.
- No match → continue to trust score path.

## Детерминизм или машинное обучение

Matching **детерминированный**; парсинг plain English через Claude — вероятностный (есть fallback).

## Внешние зависимости

Python; опционально Anthropic API для policy parse.

## Ограничения

- fnmatch грубее Rego; LLM parse можно обходить adversarial text (mitigated by «ignore instructions in policy text»).

## Сигналы качества

- THREAT_MODEL.md; demo_attack.py; compliance templates.

## Вердикт

**экспериментально** — наглядный PDP с time-gated policies.

## Связи

- Репозиторий: [[repo-15-agentgate-public]]
