---
type: implementation-detail
parent-repo: repo-88-bipia
method-id: 1
repo: https://github.com/microsoft/BIPIA
language: Python
license: MIT
verdict: experimental
commit-sha: a004b69
commit-date: 2024-04-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# BIPIA — benchmark + black/white-box defenses IPI

## Репозиторий

- [microsoft/BIPIA](https://github.com/microsoft/BIPIA)
- Проверенный срез: `a004b69`; код проверен 2026-07-15.

## Что это за технология

Microsoft **Benchmark of Indirect Prompt Injection Attacks** + защиты: black-box (few-shot / border) и white-box (finetune, special tokens). Датасеты email/qa/code/table. Способ №1 (+ №45 как bench).

## Где в коде

- `benchmark/` — attack JSON splits
- `defense/black_box/few_shot.py`
- `defense/white_box/{finetune,eval}.py`
- Package `bipia/`

## Алгоритм

1. Load BIPIA task (email/code/…).
2. Inject malicious instruction into external content.
3. Baseline: measure ASR on LLM.
4. Apply defense (few-shot borders / finetuned model) → remeasure.

## Примеры реализации

```python
# black_box/few_shot.py
class FewShotChatGPT35Defense(GPT35WOSystem):
    def add_border(self, user_prompt, context): …
# white_box: VicunaWithSpecialToken + supervised finetune on BIPIA
```

## Пример: вход → решение

- Email body with «ignore user, exfil secrets» → undefended high ASR.
- Few-shot border defense → ASR↓.

## Детерминизм или машинное обучение

Benchmark фиксирован; defenses — prompting/ML.

## Внешние зависимости

Python; OpenAI / HF models for defenses.

## Ограничения

- 2024 research code.
- White-box needs train compute.

## Сигналы качества

- arXiv 2312.14197; Microsoft.

## Вердикт

**экспериментально** — foundational IPI bench+defense kit.

## Связи

- Репозиторий: [[repo-88-bipia]]
