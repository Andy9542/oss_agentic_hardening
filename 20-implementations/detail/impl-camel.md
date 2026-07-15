---
type: implementation-detail
parent-repo: repo-56-camel-prompt-injection
method-id: 16
repo: CaMeL (Google research)
language: Python
license: ""
verdict: экспериментально
tags:
  - agent-security
---

# CaMeL — способ №16

## Репозиторий

arXiv:2503.18813 v2 — capability-based IFC, Q/P-LLM split.

## Алгоритм

Пообъектные capability-метки; policy engine перед tool_call; P-LLM планирует, Q-LLM парсит недоверенные данные без tools. AgentDojo: 77% с безопасностью vs 84% baseline.

## Детерминизм или машинное обучение

Смешанный (интерпретатор + LLM).

## Вердикт

**экспериментально** — research-grade, не drop-in prod.

## Связи

- Репозиторий: [[repo-56-camel-prompt-injection]]
