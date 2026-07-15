---
type: implementation-detail
parent-repo: repo-59-agent-threat-rules
method-id: 3
repo: https://github.com/panguard-ai/agent-threat-rules
language: YAML
license: MIT
verdict: experimental
commit-sha: b1f0f3d
commit-date: 2026-03-10
verified-date: 2026-07-15
tags:
  - agent-security
---

# Agent Threat Rules (ATR) — Sigma-like YAML для агентов

## Репозиторий

- [panguard-ai/agent-threat-rules](https://github.com/panguard-ai/agent-threat-rules)
- Проверенный срез: `b1f0f3d`; код проверен 2026-07-15.

## Что это за технология

**Корпус детект-правил** (не runtime сам по себе): YAML ATR с `detection.conditions` regex на `tool_args`/`tool_name`, маппинг OWASP/ATLAS. Потребители — agent-audit и сканеры. Способ №3 (pattern rules).

## Где в коде

- `rules/tool-poisoning/ATR-2026-012-unauthorized-tool-call.yaml`
- `rules/context-exfiltration/`, `spec/`, `examples/`

## Алгоритм

1. Импортировать pack в scanner/SIEM-like agent auditor.
2. На событии tool_call применить conditions (OR/AND per rule).
3. Match → finding severity + references.
4. Tune/suppress.

## Примеры реализации

ATR-2026-012:

```yaml
detection:
  conditions:
    - field: tool_args
      operator: regex
      value: "(\.\.[\/\\]){2,}|…(etc|proc|root|…)"
    - field: tool_args
      operator: regex
      value: "(;|&&|\|\||\$\(|`)…(curl|wget|bash|…)"
severity: high
tags: { category: tool-poisoning }
```

## Пример: вход → решение

- tool_args с `../../etc/passwd` → ATR-2026-012 hit.
- Clean args → no match.

## Детерминизм или машинное обучение

**Детерминированные** regex rules.

## Внешние зависимости

Engine, который исполняет ATR (agent-audit и др.).

## Ограничения

- Сами по себе rules ≠ enforcement.
- Experimental status на многих правилах.

## Сигналы качества

- Structured spec; OWASP mappings; shared with auditors.

## Вердикт

**экспериментально** — ценный shared rule corpus.

## Связи

- Репозиторий: [[repo-59-agent-threat-rules]]
