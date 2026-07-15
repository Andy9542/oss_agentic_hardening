---
type: implementation-detail
parent-repo: repo-06-zerotrust-agents
method-id: 12
repo: https://github.com/lokeshsk/zerotrust-agents
language: Python
license: MIT
verdict: experimental
commit-sha: 1dc51b1
commit-date: 2026-06-09
verified-date: 2026-07-15
tags:
  - agent-security
---

# zerotrust-agents — gateway policy DSL (allow/deny/approve)

## Репозиторий

- [lokeshsk/zerotrust-agents](https://github.com/lokeshsk/zerotrust-agents)
- Проверенный срез: `1dc51b1`, дата коммита 2026-06-09; код проверен 2026-07-15.

## Что это за технология

**Zero-trust proxy** между агентом и LLM/MCP API: каждый tool call проверяется control plane. Политика — JSON DSL с операторами `equals` / `contains` / `regex` / AND/OR. Результат: `allow`, `deny`, `require_approval`. Fail-closed при ошибке сети/парсинга. Способ №12 + HITL.

## Где в коде

- `apps/gateway/policy_engine.py` — `evaluate_dsl`, `check_policy`
- Прокси: `apps/gateway/routers/openai_proxy.py`, `mcp_proxy.py`, `anthropic_proxy.py`
- Тесты: `apps/gateway/tests/test_policy_engine.py`
- Labs: `apps/security-labs/evaluations/`

## Алгоритм

1. Gateway получает tool_name + arguments.
2. GET control plane `/policies/{tenant}/{agent}/{tool}`.
3. Базовый `action` (allow/deny/require_approval).
4. Если allow и есть `dsl_rules` — `evaluate_dsl(rule, args)`:
   - AND/OR деревья; leaf: field.path + operator + value.
5. DSL false → deny; ошибка → deny; success → action.
6. `require_approval` → создать pending approval и ждать.

## Примеры реализации

```python
def evaluate_dsl(rule, args_dict):
    if "condition" in rule:  # AND/OR
        ...
    # leaf: field, operator, value
    if operator == "regex":
        return bool(re.search(str(expected_value), str(actual_value)))
    if operator == "contains":
        return str(expected_value).lower() in str(actual_value).lower()
```

`check_policy` при exception: `return "deny"` (fail closed).

## Пример: вход → решение

- Tool `send_email`, DSL `to contains "@evil.com"` → deny.
- Tool `web.search` без DSL, action allow → allow.
- Control plane timeout → deny.

## Детерминизм или машинное обучение

DSL **детерминированный**; labs могут включать semantic evasion evals отдельно.

## Внешние зависимости

Docker compose monorepo (gateway + API + web); httpx.

## Ограничения

- Зависит от доступности control plane.
- DSL проще Rego/Cedar — нет формальной верификации.

## Сигналы качества

- Unit tests policy engine; security_evals workflow.

## Вердикт

**экспериментально** — понятный zero-trust gateway с DSL и HITL.

## Связи

- Репозиторий: [[repo-06-zerotrust-agents]]
