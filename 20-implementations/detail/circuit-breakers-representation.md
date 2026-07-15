---
type: implementation-detail
parent-repo: repo-44-circuit-breakers
method-id: 22
repo: https://github.com/GraySwanAI/circuit-breakers
language: Python
license: MIT
verdict: experimental
commit-sha: a1ba1a5
commit-date: 2024-09-24
verified-date: 2026-07-15
tags:
  - agent-security
---

# Circuit Breakers — representation-level refusal training

## Репозиторий

- [GraySwanAI/circuit-breakers](https://github.com/GraySwanAI/circuit-breakers)
- Проверенный срез: `a1ba1a5`; код проверен 2026-07-15.

## Что это за технология

**Метод выравнивания модели**: на выбранных слоях (`target_layers`) обучают «circuit breaker» — вредные запросы уводят представления в refusal, benign retain. Не runtime kill-switch продукта, а **model-internal** short-circuit (способ №22 по смыслу прерывания опасного поведения на уровне модели).

## Где в коде

- `src/args.py` — `target_layers`, `transform_layers`
- `src/cb_train_dataset.py` — circuit_breaker vs retain splits
- `data/circuit_breakers_train.json`, notebooks `train_cb_*.ipynb`
- `harmfulness_probe/`

## Алгоритм

1. Датасет: harmful request+response (`<SEPARATOR>`) + retain/refusal.
2. Train с loss на representations выбранных слоёв.
3. Inference: harmful inputs trigger internal circuit → refuse.
4. Evaluate probes / harmfulness.

## Примеры реализации

```python
# args: target_layers="10,12,14,16,18,20"
cb_request, cb_response = circuit_breaker_orig.split('<SEPARATOR>')
# combine tokenized request+response as CB sample
```

## Пример: вход → решение

- Jailbreak harm request → model refuses (internal CB).
- Benign QA → retain path.

## Детерминизм или машинное обучение

**ML training** метода; после fine-tune поведение модели.

## Внешние зависимости

GPU; HF models (Llama3/Mistral notebooks).

## Ограничения

- Нужен retrain/finetune; не drop-in proxy.
- Не покрывает tool misuse вне текста модели.

## Сигналы качества

- Research code + evaluation harness.

## Вердикт

**экспериментально** — research defense в весах модели.

## Связи

- Репозиторий: [[repo-44-circuit-breakers]]
