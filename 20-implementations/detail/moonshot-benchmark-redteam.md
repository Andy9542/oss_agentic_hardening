---
type: implementation-detail
parent-repo: repo-84-moonshot
method-id: 44
repo: https://github.com/aiverify-foundation/moonshot
language: Python
license: Apache-2.0
verdict: experimental
commit-sha: 03e9344
commit-date: 2026-02-05
verified-date: 2026-07-15
tags:
  - agent-security
---

# Moonshot — cookbooks + recipes + attack modules

## Репозиторий

- [aiverify-foundation/moonshot](https://github.com/aiverify-foundation/moonshot)
- Проверенный срез: `03e9344`; код проверен 2026-07-15.

## Что это за технология

**AI Verify Foundation platform**: benchmark tests (datasets/metrics, IMDA starter kit cookbooks) + red-team attack modules; recipes = dataset + template + metric + grading. Web UI + CLI. Способ №44/№45.

## Где в коде

- Moonshot packages; docs for cookbooks/recipes/attack_modules
- Web UI + interactive CLI

## Алгоритм

1. Connect endpoint (LLM app).
2. Select cookbook/recipe or attack module.
3. Run benchmark or adversarial campaign.
4. HTML/JSON report with grades.

## Примеры реализации

```text
Cookbooks: pre-built IMDA starter workflows
Recipes: custom input-target pairs + metrics + grading scales
Attack modules: algorithmic / generative adversarial prompts
```

## Пример: вход → решение

- Toxicity cookbook → fail grade on unsafe outputs.
- Attack module finds jailbreak → red-team finding.

## Детерминизм или машинное обучение

Datasets фиксированы; generative attacks — LLM.

## Внешние зависимости

Moonshot install; model endpoints.

## Ограничения

- Platform weight vs thin CLI fuzzers.
- Singapore IMDA-oriented defaults.

## Сигналы качества

- AI Verify Foundation; rich docs; UI+CLI.

## Вердикт

**экспериментально** — unified benchmark+redteam platform.

## Связи

- Репозиторий: [[repo-84-moonshot]]
