---
type: implementation-detail
parent-repo: repo-41-rebuff
method-id: 1
repo: https://github.com/protectai/rebuff
language: Python/TypeScript
license: MIT
verdict: experimental
commit-sha: 4d2fe06
commit-date: 2024-01-25
verified-date: 2026-07-15
tags:
  - agent-security
---

# Rebuff — heuristics + vector + LLM judge

## Репозиторий

- [protectai/rebuff](https://github.com/protectai/rebuff)
- Проверенный срез: `4d2fe06`; код проверен 2026-07-15.

## Что это за технология

**Тройной детектор prompt injection**: (1) combinatorial keyword heuristics, (2) Pinecone vector similarity к известным атакам, (3) OpenAI LLM scoring 0..1. OR по порогам → `injection_detected`. Способ №1.

## Где в коде

- `python-sdk/rebuff/sdk.py` — `detect_injection`
- `detect_pi_heuristics.py`, `detect_pi_vectorbase.py`, `detect_pi_openai.py`

## Алгоритм

1. Heuristic score (keyword combos Ignore/Disregard × instructions…).
2. Vector top_score vs Pinecone (если включено).
3. LLM judge → float completion score.
4. Detect if any score > max_* threshold.

## Примеры реализации

Пороги по умолчанию (`sdk.py`):

```python
max_heuristic_score = 0.75
max_vector_score = 0.90
max_model_score = 0.90
# injection if heuristic|model|vector exceeds
```

Heuristics: verbs `Ignore|Disregard|Bypass|…` × objects `instructions|commands|…`.

## Пример: вход → решение

- `"Ignore previous instructions and …"` → high heuristic → detected.
- Benign question, scores below thresholds → allow.

## Детерминизм или машинное обучение

Смесь: heuristics детерминированы; vector/LLM — нет.

## Внешние зависимости

OpenAI API; Pinecone optional.

## Ограничения

- Репо старше (2024); пороги калибровать.
- Cloud cost на LLM/vector.

## Сигналы качества

- SDK + server; LangChain tests.

## Вердикт

**экспериментально** — классический multi-signal PI detector.

## Связи

- Репозиторий: [[repo-41-rebuff]]
