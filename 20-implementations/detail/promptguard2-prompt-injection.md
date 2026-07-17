---
type: implementation-detail
parent-repo: repo-37-purplellama
method-id: 1
repo: https://github.com/meta-llama/PurpleLlama
language: Python
license: MIT
verdict: prod
tags:
  - agent-security
---

# PromptGuard 2 — LlamaFirewall

## Репозиторий

[meta-llama/PurpleLlama](https://github.com/meta-llama/PurpleLlama) → LlamaFirewall

## Где в коде

- `LlamaFirewall` scanners: `ScannerType.PROMPT_GUARD`
- Fine-tuned DeBERTa (BERT-family) для jailbreak/injection

## Алгоритм

Neural classifier на user input и untrusted documents; также смотрит reasoning trace.

## Детерминизм или машинное обучение

Вероятностный. Используется в prod Meta.

## Внешние зависимости

PromptGuard — локально (HuggingFace). AlignmentCheck — отдельный способ (№2).

## Метрики (Prompt Guard 2)

По [MODEL_CARD 86M](https://github.com/meta-llama/PurpleLlama/blob/main/Llama-Prompt-Guard-2/86M/MODEL_CARD.md) (private OOD benchmark Meta):

| Модель | Backbone | AUC (EN) | Recall@1% FPR (EN) | AUC (multi) | APR@3% utility |
|--------|----------|----------|--------------------|-------------|----------------|
| PG2 86M | mDeBERTa-v3 | 0.998 | 97.5% | 0.995 | 81.2% |
| PG2 22M | DeBERTa-v3-xsmall | 0.995 | 88.7% | 0.942 | 78.4% |

На том же протоколе Meta указывает APR ProtectAI **22.2%** — не путать с Acc/F1 на HF-карточке Protect AI.

## Сигналы качества

- CyberSecEval / private OOD metrics от Meta (см. выше)
- Известные слабости: multilingual/Unicode на обходах ([[description-top-20#6. PurpleLlama / LlamaFirewall]])

## Вердикт

**готово к продакшену** — сильный vendor baseline; не единственный барьер.

## Связи

- Репозиторий: [[repo-37-purplellama]]
