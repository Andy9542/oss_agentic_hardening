---
type: implementation-detail
parent-repo: repo-37-purplellama
method-id: 1
repo: https://github.com/meta-llama/PurpleLlama
language: Python
license: MIT
verdict: prod
tags: [agent-security]
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

## Сигналы качества

- CyberSecEval benchmarks от Meta
- Известные слабости: multilingual, Unicode ([[description-top-20#6. PurpleLlama / LlamaFirewall]])

## Вердикт

**готово к продакшену** — сильный vendor baseline; не единственный барьер.

## Связи

- Репозиторий: [[repo-37-purplellama]]
