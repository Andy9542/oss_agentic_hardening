---
type: implementation-detail
parent-repo: repo-30-inkog
method-id: 28
repo: https://github.com/inkog-io/inkog
language: Go
license: Apache-2.0
verdict: experimental
commit-sha: 85683e7
commit-date: 2026-06-07
verified-date: 2026-07-15
tags:
  - agent-security
---

# Inkog — pre-flight SAST для агентного кода

## Репозиторий

- [inkog-io/inkog](https://github.com/inkog-io/inkog)
- Проверенный срез: `85683e7`; код проверен 2026-07-15.

## Что это за технология

**Go SAST «pre-flight check»** специально под AI-агентный код: ловит token bombing, prompt injection sinks, missing human oversight, compliance gaps (EU AI Act / NIST / OWASP mapping) в LangChain/CrewAI/AutoGen-стиле проектов. Способ №28/№27.

## Где в коде

- Go modules в корне; CI workflow
- Dashboard report samples in docs
- README: token bombing / injection / oversight

## Алгоритм

1. `inkog scan` на репозиторий агента.
2. AST/pattern rules по framework idioms.
3. Findings с severity + compliance tags.
4. Optional cloud report UI.

## Примеры реализации

Категории детектов (продуктовые): token bombing (неограниченные LLM loops), prompt injection into tools, missing approval gates, secrets in agent graphs.

## Пример: вход → решение

- Agent loop без max_iterations + tool shell → findings oversight + RCE risk.
- Bounded graph with HITL → cleaner report.

## Детерминизм или машинное обучение

**Детерминированный** static analysis.

## Внешние зависимости

Go binary; optional inkog.io dashboard.

## Ограничения

- Нужны framework-aware rules; false positives на необычных графах.

## Сигналы качества

- Go Report Card; CI; compliance mapping screenshots.

## Вердикт

**экспериментально** — нишевый agent-code SAST.

## Связи

- Репозиторий: [[repo-30-inkog]]
