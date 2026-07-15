---
type: implementation-detail
parent-repo: repo-24-mcp-scanner
method-id: 26
repo: https://github.com/cisco-ai-defense/mcp-scanner
language: Python
license: Apache-2.0
verdict: experimental
commit-sha: f96659f
commit-date: 2026-07-14
verified-date: 2026-07-15
tags:
  - agent-security
---

# cisco mcp-scanner — YARA + LLM-judge + Cisco AI Defense

## Репозиторий

- [cisco-ai-defense/mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner)
- Проверенный срез: `f96659f`; код проверен 2026-07-15.

## Что это за технология

**Сканер MCP servers/tools**: три движка — YARA rules, LLM-as-a-judge, Cisco AI Defense Inspect API — плюс pip-audit для CVE в зависимостях. Анализирует tools, prompts, resources на malware/injection/readiness. Способ №26.

## Где в коде

- Python package `cisco-ai-mcp-scanner`
- Examples: `examples/example-malicious-servers/`, `advanced_scanning.py`
- CLI + REST API modes

## Алгоритм

1. Подключить к MCP server (stdio/SSE/HTTP) или загрузить definitions.
2. Извлечь tool schemas/descriptions/prompts.
3. Параллельно: YARA match → LLM judge → Cisco inspect.
4. Агрегировать severity; optional dependency CVE scan.
5. Report / fail CI.

## Примеры реализации

Malicious fixtures в `examples/example-malicious-servers/` (line jumping, tricky_server, behavioural malicious).

Engines configurable: use any subset independently.

## Пример: вход → решение

- Tool description с hidden «ignore previous instructions» → YARA/LLM hit → finding.
- Clean filesystem MCP → pass / low risk.

## Детерминизм или машинное обучение

YARA детерминирован; LLM/Cisco — вероятностны.

## Внешние зависимости

Python 3.11+; API keys for LLM/Cisco optional.

## Ограничения

- Cloud engines требуют сеть/ключ.
- Judge variance.

## Сигналы качества

- Cisco AI Defense branding; malicious server corpus; CI.

## Вердикт

**экспериментально** — зрелый multi-engine MCP scanner.

## Связи

- Репозиторий: [[repo-24-mcp-scanner]]
