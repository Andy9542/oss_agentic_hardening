---
type: implementation-detail
parent-repo: repo-26-agent-audit
method-id: 27
repo: https://github.com/scadastrangelove/agent-audit
language: Python
license: MIT
verdict: experimental
commit-sha: 48578c6
commit-date: 2026-05-26
verified-date: 2026-07-15
tags:
  - agent-security
---

# agent-audit — ATR rule packs для skills/MCP/сессий

## Репозиторий

- [scadastrangelove/agent-audit](https://github.com/scadastrangelove/agent-audit)
- Проверенный срез: `48578c6`; код проверен 2026-07-15.

## Что это за технология

**Forensic auditor** coding-агентов и репозиториев: сотни YAML-сигнатур (ATR — Agent Threat Rules) по категориям tool-poisoning, model-abuse и др. Сканирует session logs, configs, SKILL.md, MCP manifests. Опционально LLM cross-verify. Способ №27 («Sigma для агентов»).

## Где в коде

- Rule packs: `src/agent_audit/knowledge/rule_packs/atr/`
- OWASP maps: `data/owasp_mcp/`, `data/owasp_agentic/`
- Example: `…/tool-poisoning/ATR-2026-00012-unauthorized-tool-call-detection.yaml`

## Алгоритм

1. Собрать surfaces (home agent dirs, repo skills, MCP manifests, session traces).
2. Применить bundled ATR YAML (patterns/detectors per rule).
3. Map findings → OWASP/ASAMM/ATLAS.
4. Optional LLM verification of hits.
5. Report.

## Примеры реализации

Из ATR-2026-00012 (`unauthorized-tool-call-detection.yaml`):

```yaml
title: Unauthorized Tool Call Detection
severity_default: high
category: tool-poisoning
audit_surface: [mcp_manifest, tool_description, skill_md]
detection.conditions:
  - field: tool_args
    operator: regex
    value: '(\.{2}[/\\]){2,}|…/(etc|proc|root|sys|…)'
    # path traversal к чувствительным каталогам
  - field: tool_args
    operator: regex
    value: '(;|&&|\|\||\$\(|`)…(curl|wget|bash|rm\s+-|cat\s+/etc|…)'
    # shell metachar + dangerous commands
  - field: tool_args
    operator: regex
    value: '(?i)(process\.env\.|os\.environ|getenv\s*\()'
    # извлечение секретов из env
```

Сотни правил в `rule_packs/atr/model-abuse/` и `tool-poisoning/`.

## Пример: вход → решение

- MCP tool description с path traversal args → high finding tool-poisoning.
- Clean skill → no match.

## Детерминизм или машинное обучение

Сигнатуры детерминированы; LLM verify — опционально вероятностный.

## Внешние зависимости

Python; optional LLM CLIs/API.

## Ограничения

- Объём rules → tuning/noise.
- Experimental maturity на многих ATR.

## Сигналы качества

- ASAMM alignment; upstream ATR imports; OWASP mappings.

## Вердикт

**экспериментально** — богатейший signature corpus для agent forensics.

## Связи

- Репозиторий: [[repo-26-agent-audit]]
