---
type: implementation-detail
parent-repo: repo-21-agent-scan
method-id: 26
repo: https://github.com/snyk/agent-scan
language: Python
license: Apache-2.0
verdict: experimental
commit-sha: 6b55d52
commit-date: 2026-07-14
verified-date: 2026-07-15
tags:
  - agent-security
---

# Snyk Agent Scan — discovery MCP/skills + issue codes

## Репозиторий

- [snyk/agent-scan](https://github.com/snyk/agent-scan)
- Проверенный срез: `6b55d52`; код проверен 2026-07-15.

## Что это за технология

**Discovery + scan** локальных агентных компонентов (MCP servers, skills, agent configs) на prompt injection и уязвимости. Direct scan URIs: `npm:`, `pypi:`, `oci:`, `sse:`, `streamable-http:`. Преемник mcp-scan; связан с Invariant/Evo platform. Способ №26.

## Где в коде

- `src/agent_scan/direct_scanner.py` — parse direct scan paths
- `src/agent_scan/models.py` — issue types / codes (`skill_scan_error` → X002)
- CLI package `snyk-agent-scan`

## Алгоритм

1. Discover agents/MCP/skills on machine or accept direct URI.
2. Connect/fetch server metadata or skill bundle.
3. Run analyzers → structured issues (experimental codes).
4. Output CLI report (schema may change) / optional platform upload.

## Примеры реализации

```python
# direct_scanner.py
if scan_type == "npm": ...
elif scan_type == "pypi": ...
elif scan_type == "oci": ...
elif scan_type == "sse": ...
elif scan_type == "streamable-http": ...
```

Issue taxonomy in `models.py` includes skill scan errors and related codes.

## Пример: вход → решение

- `snyk-agent-scan` на poisoned skill → injection findings.
- Unreachable MCP → `skill_scan_error` / connection issue code.

## Детерминизм или машинное обучение

Смешанный (статические проверки + возможные ML/platform backends).

## Внешние зависимости

Python; Snyk platform optional for enterprise.

## Ограничения

- CLI output explicitly experimental / unstable schema.
- Enterprise path may differ from CLI.

## Сигналы качества

- Snyk maintenance; skills threat report; tests.

## Вердикт

**экспериментально** — enterprise-backed agent/MCP discovery scanner.

## Связи

- Репозиторий: [[repo-21-agent-scan]]
