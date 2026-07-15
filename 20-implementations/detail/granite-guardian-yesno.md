---
type: implementation-detail
parent-repo: repo-49-granite-guardian
method-id: 1
repo: https://github.com/ibm-granite/granite-guardian
language: Python
license: Apache-2.0
verdict: experimental
commit-sha: a409be8
commit-date: 2026-05-04
verified-date: 2026-07-15
tags:
  - agent-security
---

# Granite Guardian — yes/no risk judge models

## Репозиторий

- [ibm-granite/granite-guardian](https://github.com/ibm-granite/granite-guardian)
- Проверенный срез: `a409be8`; код проверен 2026-07-15.

## Что это за технология

Семейство **IBM Granite Guardian** моделей: chat template с блоком `<guardian>` (criteria) → ответ **yes/no** (и optional think-trace) о риске текста/документов/tool schemas. Использовать строго в scoring mode. Способ №1 (ML moderation/risk).

## Где в коде

- README cookbooks + `build_guardian_block`
- HF models: granite-guardian-4.1-8b / 3.2 / HAP-*.

## Алгоритм

1. Собрать messages + criteria в `<guardian>…</guardian>`.
2. `tokenizer.apply_chat_template` (optional `documents=`, `available_tools=`).
3. Generate; parse score yes/no (+ trace if think).
4. Gate: yes risk → block/escalate.

## Примеры реализации

```python
def build_guardian_block(criteria, think=False):
    return f"<guardian>{judge_instruction}\n\n{criteria}...</guardian>"
# parse score_match → yes|no
# agentic: available_tools= in apply_chat_template; prefer no-think for latency
```

## Пример: вход → решение

- Hallucinated answer vs docs + groundedness criteria → `yes` risk → block.
- Clean answer → `no`.

## Детерминизм или машинное обучение

**ML classifier** (LLM-as-judge семейство).

## Внешние зависимости

GPU/vLLM или HF inference; model weights.

## Ограничения

- Только prescribed scoring template.
- Latency/cost vs regex guards.

## Сигналы качества

- IBM docs; multiple model sizes; HF Spaces.

## Вердикт

**экспериментально**/зреющий prod-candidate для risk gating.

## Связи

- Репозиторий: [[repo-49-granite-guardian]]
