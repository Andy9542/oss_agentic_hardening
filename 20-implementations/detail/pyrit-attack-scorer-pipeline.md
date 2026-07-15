---
type: implementation-detail
parent-repo: repo-77-pyrit
method-id: 44
repo: https://github.com/microsoft/PyRIT
language: Python
license: MIT
verdict: prod
commit-sha: 0eb5364
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# PyRIT — converters + attacks + scorers

## Репозиторий

- [microsoft/PyRIT](https://github.com/microsoft/PyRIT) (Azure/PyRIT — redirect stub)
- Проверенный срез: `0eb5364`; код проверен 2026-07-15.

## Что это за технология

**Microsoft red-team framework** для GenAI: Prompt converters, attack executors/scenarios, scorers (SelfAskRefusal и др.), memory, multi-provider targets. Способ №44.

## Где в коде

- `pyrit/converter/`, `pyrit/executor/attack/`, `pyrit/score/`
- `pyrit/registry/components/{converter,scorer}_registry.py`
- `pyrit/prompt_target/`

## Алгоритм

1. Configure prompt target (OpenAI/Azure/…).
2. Apply converters (encoding, paraphrase, …).
3. Run attack strategy/orchestrator against objective.
4. Scorer judges success; store in memory for reporting.

## Примеры реализации

```text
AttackConverterConfig + ConverterRegistry
ScorerRegistry (e.g. SelfAskRefusalScorer)
prompt_target → normalizer → attack executor → score
```

## Пример: вход → решение

- Objective «bypass refusal» + converters → model complies → scorer = success.
- Hardened model refuses → scorer failure (good).

## Детерминизм или машинное обучение

Converters часто детерминированы; scorers часто LLM.

## Внешние зависимости

Python; provider keys; optional Azure stack.

## Ограничения

- Broad surface — pick modules carefully.
- Catalog `repo` may still point Azure stub URL.

## Сигналы качества

- Microsoft maintained; rich registries; docs.

## Вердикт

**готово к продакшену** как enterprise red-team toolkit.

## Связи

- Репозиторий: [[repo-77-pyrit]]
