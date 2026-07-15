---
type: implementation-detail
parent-repo: repo-42-vigil-llm
method-id: 1
repo: https://github.com/deadbits/vigil-llm
language: Python
license: GPL-3.0
verdict: experimental
commit-sha: f2b4c13
commit-date: 2024-01-31
verified-date: 2026-07-15
tags:
  - agent-security
---

# Vigil — YARA + vectordb + canary tokens

## Репозиторий

- [deadbits/vigil-llm](https://github.com/deadbits/vigil-llm)
- Проверенный срез: `f2b4c13`; код проверен 2026-07-15.

## Что это за технология

**LLM security scanner/service**: scanners YARA (heuristics), Chroma vectordb (embeddings known jailbreaks), transformer models, canary tokens на утечку system prompt. Способ №1 (+ secrets №7).

## Где в коде

- `data/yara/*.yar` — instruction_bypass, apitokens, mdexfil, …
- Docs: `docs/detections.md`, `docs/canarytokens.md`

## Алгоритм

1. Prompt → configured scanners.
2. YARA match rulesets; vectordb similarity > threshold → flag.
3. Optional canary: embed token in system prompt; check response.
4. Aggregate detections.

## Примеры реализации

`instruction_bypass.yar`:

```yara
$bypass_phrase = /(Ignore|Disregard|Skip|Forget|…)\s*(prior|previous|…)?\s*(instructions|commands|…)/
```

`apitokens.yar`: AWS `AKIA…`, Slack `xox…`, Stripe `sk_live_…`, Google `AIza…`.

Canary: token in response → leak; missing expected canary → goal hijack signal.

## Пример: вход → решение

- `"Ignore previous instructions"` → YARA InstructionBypass.
- Response repeats canary unexpectedly → leak alert.

## Детерминизм или машинное обучение

YARA детерминирован; vectordb/transformer — вероятностны.

## Внешние зависимости

YARA; Chroma; optional HF embeddings / Docker.

## Ограничения

- GPL; возраст датасетов.
- Threshold tuning.

## Сигналы качества

- Явные YARA corpora; detection docs.

## Вердикт

**экспериментально** — полезный YARA+vector stack.

## Связи

- Репозиторий: [[repo-42-vigil-llm]]
