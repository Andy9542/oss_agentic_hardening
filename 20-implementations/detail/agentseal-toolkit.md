---
type: implementation-detail
parent-repo: repo-33-agentseal
method-id: 31
repo: https://github.com/getagentseal/agentseal
language: Python
license: FSL-1.1-Apache-2.0
verdict: experimental
commit-sha: 7c2a228
commit-date: 2026-06-11
verified-date: 2026-07-15
tags:
  - agent-security
---

# AgentSeal — toolkit: MCP poison, skills, toxic flows, probes

## Репозиторий

- [getagentseal/agentseal](https://github.com/getagentseal/agentseal) / AgentSeal org
- Проверенный срез: `7c2a228`; код проверен 2026-07-15.

## Что это за технология

**Security toolkit** для агентов: red-team prompts, MCP poisoning detection, skill file scan, toxic data-flow tracing; заявлены 225+ tests across 28 agents. Также admission/signing артефактов (способ №31) и Unicode-related checks (also-method 4). PyPI + npm.

## Где в коде

- `python/agentseal/`, `js/`
- `PROBES.md` — probe catalog
- Tests under `python/tests`

## Алгоритм

1. Выбрать режим: scan skill / scan MCP / trace flows / run probes.
2. Static + probe suite against target agent config.
3. Findings: poison descriptors, unsafe flows, unicode tricks.
4. Optional seal/verify artifact hashes for admission.

## Примеры реализации

Продуктовые поверхности: MCP Registry integration, dashboard, probe list в PROBES.md.

## Пример: вход → решение

- MCP tool with hidden instruction in description → poison finding.
- Skill with credentials→network flow → toxic flow finding.

## Детерминизм или машинное обучение

Сканы/пробы в основном детерминированы; некоторые probes зависят от модели.

## Внешние зависимости

PyPI `agentseal` / npm; optional cloud dashboard.

## Ограничения

- FSL license nuances; breadth vs depth per agent.

## Сигналы качества

- Large probe matrix; dual language SDKs.

## Вердикт

**экспериментально** — широкий toolkit; выбирать нужные модули.

## Связи

- Репозиторий: [[repo-33-agentseal]]
