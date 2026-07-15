---
type: implementation-detail
parent-repo: repo-72-jailbreakbench
method-id: 45
repo: https://github.com/JailbreakBench/jailbreakbench
language: Python
license: MIT
verdict: experimental
commit-sha: 23dbdf6
commit-date: 2025-03-31
verified-date: 2026-07-15
tags:
  - agent-security
---

# JailbreakBench — JBB-Behaviors + judges

## Репозиторий

- [JailbreakBench/jailbreakbench](https://github.com/JailbreakBench/jailbreakbench)
- Проверенный срез: `23dbdf6`; код проверен 2026-07-15.

## Что это за технология

**NeurIPS 2024 benchmark** jailbreaks: 200 behaviors (benign+misuse), leaderboard, artifacts repo, classifiers (`Llama3JailbreakJudge`, `Llama3RefusalJudge`, `StringClassifier`). Способ №45.

## Где в коде

- `src/jailbreakbench/` — classifier, config, submission API
- `examples/submit.py`

## Алгоритм

1. Load JBB-Behaviors / submitted jailbreak strings.
2. Query target model with jailbreaks.
3. Judge success via Classifier.
4. Optional `create_submission` for leaderboard.

## Примеры реализации

```python
from jailbreakbench import Classifier, Llama3JailbreakJudge, StringClassifier
jbb.create_submission(method_name="GCG", attack_type="white_box", method_params=…)
```

## Пример: вход → решение

- Jailbreak elicits prohibited content → judge = jailbreak success.
- Model refuses → refusal judge pass / attack fail.

## Детерминизм или машинное обучение

Dataset фиксирован; judges — ML/string.

## Внешние зависимости

HF datasets; judge model access.

## Ограничения

- LLM jailbreak focus (не tool/MCP).
- Judge disagreements possible.

## Сигналы качества

- NeurIPS D&B; public leaderboard.

## Вердикт

**экспериментально** — стандарт сравнения jailbreak attacks/defenses.

## Связи

- Репозиторий: [[repo-72-jailbreakbench]]
