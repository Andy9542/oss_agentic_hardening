---
type: implementation
method-id: 46
repo: AgentPoison (benchmark)
language: ""
license: ""
verdict: экспериментально
tags:
  - agent-security
---

# AgentPoison — способ №46 (benchmark / mitigation research)

## Репозиторий

arXiv:2407.12784 — attack benchmark для memory poisoning.

## Алгоритм

ASR >80% при poison rate <0.1%; stealthy embedding triggers. Mitigation refs в формировании `[не проверено]`.

## Вердикт

**экспериментально** — attack benchmark, не prod guard `[проверено 2026-07-08]`.

## Связи

- Способ: [[46-memory-protection]]
