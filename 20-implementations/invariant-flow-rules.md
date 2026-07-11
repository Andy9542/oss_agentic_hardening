---
type: implementation
method-id: 15
repo: https://github.com/invariantlabs-ai/invariant
language: Python
license: Apache-2.0
verdict: prod
tags: [agent-security]
---

# Invariant — flow rules

## Репозиторий

[invariantlabs-ai/invariant](https://github.com/invariantlabs-ai/invariant)

## Где в коде

- Invariant DSL: `(output: get_website) -> (call: send_email)` forbidden
- Gateway + LocalPolicy modes

## Алгоритм

Trace event pattern matching on OpenAI-compatible message arrays.

## Детерминизм или машинное обучение

Детерминированный для flow rules.

## Вердикт

**готово к продакшену** — best-in-class trace policies.

## Связи

- Способ: [[15-правила-последовательности-вызовов-и-потоков-данных]]
