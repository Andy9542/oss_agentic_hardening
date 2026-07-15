---
type: implementation-detail
parent-repo: repo-31-medusa
method-id: 27
repo: https://github.com/Pantheon-Security/medusa
language: Python
license: AGPL-3.0
verdict: experimental
commit-sha: 5f217ed
commit-date: 2026-06-24
verified-date: 2026-07-15
tags:
  - agent-security
---

# MEDUSA — AI-first scanner (40k+ patterns, secrets, repo poison)

## Репозиторий

- [Pantheon-Security/medusa](https://github.com/Pantheon-Security/medusa)
- Проверенный срез: `5f217ed`; код проверен 2026-07-15.

## Что это за технология

**Офлайн AI/ML security scanner** с заявленными 40 000+ паттернами: repo poisoning (Cursor/Claude/Copilot configs), MCP tool poisoning, prompt injection, 200 CVE signatures, `medusa secrets scan` (21 issuer types API keys в chat/shell history). Parallel multi-core. Способ №27.

## Где в коде

- Package `medusa/` — config, scanners
- CLI: `medusa scan`, `medusa scan --git URL`, `medusa secrets scan`
- Config: `.medusa.yml`, `medusa/config.py`

## Алгоритм

1. Walk repo (exclude deps/vendor via config).
2. Match built-in AI/agent/CVE pattern packs.
3. Optional secrets scan of IDE/shell histories with interactive purge.
4. Cache by content hash for rescans.
5. Export JSON/HTML/SARIF/Markdown.

## Примеры реализации

Команды:

```bash
medusa scan --git <URL>
medusa secrets scan   # Anthropic/OpenAI/GitHub/AWS/… issuers
```

Config toggles `scanners.enabled/disabled`, IDE auto_scan for Claude Code.

## Пример: вход → решение

- Weaponized `.cursor/rules` with exfil → repo poisoning finding.
- `sk-ant-…` in shell history → secrets hit → optional purge.

## Детерминизм или машинное обучение

Паттерны **детерминированные** (объёмный signature DB).

## Внешние зависимости

`pip install medusa-security`; no mandatory external linters.

## Ограничения

- Huge rule set → noise; AGPL licensing.
- Marketing-scale pattern counts — verify relevant packs for your stack.

## Сигналы качества

- PyPI; cross-platform tests; rich CLI.

## Вердикт

**экспериментально** — широкий AI supply-chain scanner; калибровать severity.

## Связи

- Репозиторий: [[repo-31-medusa]]
