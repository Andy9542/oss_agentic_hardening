---
type: implementation-detail
parent-repo: repo-80-fuzzyai
method-id: 44
repo: https://github.com/cyberark/FuzzyAI
language: Python
license: Apache-2.0
verdict: experimental
commit-sha: 8184b96
commit-date: 2026-02-06
verified-date: 2026-07-15
tags:
  - agent-security
---

# FuzzyAI — CyberArk LLM jailbreak fuzzer

## Репозиторий

- [cyberark/FuzzyAI](https://github.com/cyberark/FuzzyAI)
- Проверенный срез: `8184b96`; код проверен 2026-07-15.

## Что это за технология

**Automated LLM fuzzing** от CyberArk: CLI `fuzzyai fuzz` для поиска jailbreaks и уязвимостей API LLM. Способ №44.

## Где в коде

- Package `fuzzyai` / `src/fuzzyai`
- CLI entry `fuzzyai fuzz -h`

## Алгоритм

1. `pip install` / poetry install.
2. Configure target LLM endpoint.
3. `fuzzyai fuzz` with attack/mutation options.
4. Collect successful jailbreaks / report.

## Примеры реализации

```bash
pip install git+https://github.com/cyberark/FuzzyAI.git
fuzzyai fuzz -h
```

Mutational fuzzing over prompts to elicit policy violations.

## Пример: вход → решение

- Fuzz campaign finds payload that bypasses safety → logged finding.
- No bypass after N iters → hardened signal.

## Детерминизм или машинное обучение

Fuzz search **недетерминирован**; mutations may use heuristics/LLM.

## Внешние зависимости

Poetry/pip; target LLM.

## Ограничения

- Focus jailbreak API, not full MCP/tool graph.
- Ops cost of large campaigns.

## Сигналы качества

- CyberArk; Discord; active commits.

## Вердикт

**экспериментально** — enterprise-origin LLM fuzzer.

## Связи

- Репозиторий: [[repo-80-fuzzyai]]
