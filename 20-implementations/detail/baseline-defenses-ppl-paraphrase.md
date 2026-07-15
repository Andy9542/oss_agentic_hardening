---
type: implementation-detail
parent-repo: repo-91-baseline-defenses
method-id: 1
repo: https://github.com/neelsjain/baseline-defenses
language: Python
license: Unknown
verdict: experimental
commit-sha: 53d637f
commit-date: 2023-10-26
verified-date: 2026-07-15
tags:
  - agent-security
---

# Baseline Defenses — perplexity filter + paraphrase

## Репозиторий

- [neelsjain/baseline-defenses](https://github.com/neelsjain/baseline-defenses)
- Проверенный срез: `53d637f`; код проверен 2026-07-15.

## Что это за технология

Paper code (arXiv 2309.00614): **detection** via perplexity / windowed perplexity; **preprocessing** via GPT paraphrase; retokenization via BPE-dropout (описано). Способ №1.

## Где в коде

- `perplexity_filter.py` — `PerplexityFilter`
- `paraphrase.py` — `gpt_paraphrase`

## Алгоритм

1. Encode prompt; compute CE loss / windowed -log PPL.
2. If PPL below threshold (adversarial gibberish often low/high depending setting) → filter.
3. Optional: paraphrase with GPT before model sees input.
4. Optional: BPE-dropout retokenization.

## Примеры реализации

```python
class PerplexityFilter:
    def __init__(self, model, tokenizer, threshold, window_size=10):
        self.cn_loss = torch.nn.CrossEntropyLoss(reduction='none')
    def get_log_perplexity(self, sequence):
        loss = self.model(input_ids, labels=input_ids).loss
        return loss.item()
```

```python
paraphrase_query = prompt + original_text  # GPT rewrite
```

## Пример: вход → решение

- GCG suffix → anomalous window PPL → filtered.
- Paraphrase destroys adversarial suffix → attack fails.

## Детерминизм или машинное обучение

PPL filter **детерминирован** на fixed model; paraphrase — LLM.

## Внешние зависимости

PyTorch HF model; OpenAI for paraphrase.

## Ограничения

- Threshold calibration hard; utility cost of paraphrase.
- 2023 baselines vs modern attacks.

## Сигналы качества

- Peer-reviewed paper companion.

## Вердикт

**экспериментально** — классические baseline defenses.

## Связи

- Репозиторий: [[repo-91-baseline-defenses]]
