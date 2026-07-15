---
type: implementation-detail
parent-repo: repo-82-augustus
method-id: 44
repo: https://github.com/praetorian-inc/augustus
language: Go
license: Apache-2.0
verdict: experimental
commit-sha: c87844c
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# Augustus — Go scanner 210+ probes / 90+ detectors

## Репозиторий

- [praetorian-inc/augustus](https://github.com/praetorian-inc/augustus)
- Проверенный срез: `c87844c`; код проверен 2026-07-15.

## Что это за технология

**Production-oriented LLM vuln scanner** (Praetorian): 210+ probes, 47 categories, 28 providers, 90+ detectors (pattern, LLM-judge, HarmJudge), 7 buff transforms, concurrent Go binary. Вкл. agent attacks. Способ №44.

## Где в коде

- Go modules; `harnesses/` (probewise, batch, agentwise)
- CLI single/multiple probes, buffs, JSON/HTML out

## Алгоритм

1. Build/run augustus binary with provider creds.
2. Select probes / buffs / profile.
3. Concurrent scan with rate limits/retries.
4. Detectors score responses → report.

## Примеры реализации

```text
210+ probes | 47 categories
Detectors: pattern, LLM-as-judge, HarmJudge (arXiv:2511.15304), Perspective
Buffs: encoding, paraphrase, poetry, low-resource language, case
Harnesses: probewise | batch | agentwise
```

## Пример: вход → решение

- Probe jailbreak succeeds → finding in HTML/JSON.
- All detectors clean → pass profile.

## Детерминизм или машинное обучение

Pattern detectors детерминированы; HarmJudge/LLM — нет.

## Внешние зависимости

Single Go binary; provider API keys.

## Ограничения

- LLM-centric (agent harness есть, но не полный MCP corpus).
- Cost of 210+ probes.

## Сигналы качества

- Praetorian; CI; Go Report Card; vs garak table.

## Вердикт

**экспериментально** — сильный prod-minded scanner.

## Связи

- Репозиторий: [[repo-82-augustus]]
