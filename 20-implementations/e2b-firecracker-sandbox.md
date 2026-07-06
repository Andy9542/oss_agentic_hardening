---
type: implementation
method-id: 33
repo: https://github.com/e2b-dev/E2B
language: Python/TS
license: Apache-2.0
verdict: prod
tags: [agent-security]
---

# E2B — Firecracker sandbox

## Где в коде

SDK → Orchestrator → Firecracker VMM → envd daemon.

## Алгоритм

microVM per session; destroy after use; optional snapshots.

## Вердикт

**готово к продакшену** — industry-standard isolation for code agents.

## Связи

- Способ: [[33-microvm-container]]
