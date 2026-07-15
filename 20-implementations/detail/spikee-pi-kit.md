---
type: implementation-detail
parent-repo: repo-81-spikee
method-id: 44
repo: https://github.com/ReversecLabs/spikee
language: Python
license: Apache-2.0
verdict: experimental
commit-sha: 454f7a0
commit-date: 2026-07-13
verified-date: 2026-07-15
tags:
  - agent-security
---

# Spikee — generate dataset → test → results

## Репозиторий

- [ReversecLabs/spikee](https://github.com/ReversecLabs/spikee)
- Проверенный срез: `454f7a0`; код проверен 2026-07-15.

## Что это за технология

**SPIKEE** (Simple Prompt Injection Kit): modular `spikee generate` → dataset, `spikee test` against LLM/guardrail/app, `spikee results`. Targets LLMs, RAG/apps, guardrails. Способ №44.

## Где в коде

- Package `spikee/`; docs guides
- CLI: `spikee list|generate|test|results`

## Алгоритм

1. Workspace + `spikee list` modules.
2. `spikee generate` custom attack dataset.
3. `spikee test` against target (OpenAI-compatible by default).
4. Analyse results for ASR / guardrail bypass.

## Примеры реализации

```bash
spikee list
spikee generate
spikee test
spikee results
```

Architecture: generation stage + execution stage via pluggable Python modules (`any-llm` providers).

## Пример: вход → решение

- Generated PI dataset vs guardrail → bypass rate.
- Guardrail blocks → low ASR.

## Детерминизм или машинное обучение

Modules mostly детерминированы; judges may be LLM.

## Внешние зависимости

`spikee` pip; optional `spikee[all]` for Bedrock/Ollama/…

## Ограничения

- Need custom modules for exotic targets.
- Not OS sandbox.

## Сигналы качества

- Reversec Labs; modular docs; v0.9.1.

## Вердикт

**экспериментально** — чистый PI eval kit.

## Связи

- Репозиторий: [[repo-81-spikee]]
