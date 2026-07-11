---
type: implementation
method-id: 43
repo: https://github.com/google-research/camel
language: Python
license: Apache-2.0
verdict: exp
tags: [agent-security]
---

# CaMeL — dual-LLM quarantine

## Репозиторий

Google Research CaMeL (Capability-based Machine Learning) — IFC architecture.

## Где в коде

Q-LLM (no tools) + P-LLM (planner); capability tags; policy engine pre-tool.

## Алгоритм

Information flow control on values; untrusted never reaches privileged planner raw.

## Вердикт

**экспериментально** — research-grade; high architectural robustness for indirect injection.

## Связи

- Способ: [[43-две-модели-с-разделением-доверия-и-карантином]]
