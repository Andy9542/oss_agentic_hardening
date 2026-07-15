---
type: implementation-detail
parent-repo: repo-79-agentic-security
method-id: 44
repo: https://github.com/msoedov/agentic_security
language: Python
license: MIT
verdict: experimental
commit-sha: 42615e5
commit-date: 2026-06-23
verified-date: 2026-07-15
tags:
  - agent-security
---

# Agentic Security — fuzzer LLM/агентов по датасетам

## Репозиторий

- [msoedov/agentic_security](https://github.com/msoedov/agentic_security)
- Проверенный срез: `42615e5`; код проверен 2026-07-15.

## Что это за технология

**Vulnerability scanner/fuzzer**: multimodal + multi-step jailbreaks, CSV/`prompt` datasets, HF jailbreak sets, HTTP probe spec `<<PROMPT>>`, thresholds low/medium/high. Способ №44.

## Где в коде

- `agentic_security/probe_data/`, `probe_actor/fuzzer.py`
- `attack_rules/`, CLI `agentic_security`
- Readme.md config YAML modules

## Алгоритм

1. Define LLM HTTP spec with `<<PROMPT>>` placeholder.
2. Load modules/datasets (CSV or HF).
3. Fuzzer single-shot / multi-step scan.
4. Score vs thresholds (`max_th`, low/medium/high).

## Примеры реализации

```yaml
general:
  llmSpec: |
    POST http://0.0.0.0:8718/v1/self-probe
    {"prompt": "<<PROMPT>>"}
  max_th: 0.3
modules:
  aya-23-8B_advbench_jailbreak:
    dataset_name: simonycl/aya-23-8B_advbench_jailbreak
thresholds: { low: 0.15, medium: 0.3, high: 0.5 }
```

## Пример: вход → решение

- Jailbreak dataset prompt → model complies → high risk hit.
- Below threshold → pass module.

## Детерминизм или машинное обучение

Датасеты фиксированы; RL-based attacks optional (probabilistic).

## Внешние зависимости

pip; optional HF datasets; target API.

## Ограничения

- UI/docs sprawl; calibrate thresholds.
- Multimodal needs extra setup.

## Сигналы качества

- Active fuzz_chain; many HF datasets wired.

## Вердикт

**экспериментально** — flexible LLM fuzzer.

## Связи

- Репозиторий: [[repo-79-agentic-security]]
