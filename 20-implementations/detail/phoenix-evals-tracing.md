---
type: implementation-detail
parent-repo: repo-98-phoenix
method-id: 40
repo: https://github.com/Arize-AI/phoenix
language: Python
license: Elastic-2.0
verdict: prod
commit-sha: ddd049d
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# Arize Phoenix — tracing + phoenix-evals (hallucination/…)

## Репозиторий

- [Arize-AI/phoenix](https://github.com/Arize-AI/phoenix)
- Проверенный срез: `ddd049d`; код проверен 2026-07-15.

## Что это за технология

**OSS observability + evals**: OpenTelemetry/OpenInference spans для LLM/агентов; `phoenix-evals` метрики (Faithfulness/HallucinationEvaluator, toxicity, …); filter DSL `evals['Hallucination'].score`. Способ №40 (+ content quality signals).

## Где в коде

- `packages/phoenix-evals/` — HallucinationEvaluator → FaithfulnessEvaluator
- `src/phoenix/trace/dsl/filter.py` — eval filters
- `packages/phoenix-otel/`, phoenix-client

## Алгоритм

1. Instrument app with Phoenix OTEL.
2. Collect spans for LLM/tool calls.
3. Run evaluators offline/online → annotations.
4. Query/filter spans by eval scores; alert.

## Примеры реализации

```python
# filter DSL
evals['Hallucination'].label == 'correct' or evals['Hallucination'].score < 0.5
# metrics package
HallucinationEvaluator(llm=llm)  # deprecated alias → FaithfulnessEvaluator
```

## Пример: вход → решение

- Span with high hallucination score → flagged in UI / cron eval.
- Clean grounded answer → pass.

## Детерминизм или машинное обучение

Tracing детерминирован; evaluators часто LLM-as-judge.

## Внешние зависимости

Phoenix server/UI; optional Arize cloud.

## Ограничения

- Evals ≠ hard deny unless you wire them.
- Elastic License nuances.

## Сигналы качества

- Large OSS; phoenix-evals package; active.

## Вердикт

**готово к продакшену** для LLM observability+evals.

## Связи

- Репозиторий: [[repo-98-phoenix]]
