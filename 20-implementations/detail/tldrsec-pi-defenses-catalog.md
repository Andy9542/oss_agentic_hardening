---
type: implementation-detail
parent-repo: repo-62-prompt-injection-defenses
method-id: 3
repo: https://github.com/tldrsec/prompt-injection-defenses
language: Markdown
license: Unknown
verdict: experimental
commit-sha: 423a2f3
commit-date: 2025-02-22
verified-date: 2026-07-15
tags:
  - agent-security
---

# tl;dr sec — каталог защит от prompt injection

## Репозиторий

- [tldrsec/prompt-injection-defenses](https://github.com/tldrsec/prompt-injection-defenses)
- Проверенный срез: `423a2f3`; код проверен 2026-07-15.

## Что это за технология

**Курируемый каталог** практических/proposed defenses (не код продукта): blast radius, paraphrasing, guardrails, taint tracking, dual LLM, ensemble, instructional defense, preflight injection test, papers/critiques. Способ №3 как taxonomy паттернов.

## Где в коде

- Единый `README.md` TOC

## Алгоритм

1. Читать категорию защиты.
2. Сопоставить со своим stack (rails / dual-LLM / taint…).
3. Выбрать кандидатов для PoC.
4. Сверить critiques of controls.

## Примеры реализации

Секции TOC:

```text
Blast Radius Reduction
Input Pre-processing (Paraphrasing, Retokenization)
Guardrails & Overseers, Firewalls & Filters
Taint Tracking
Secure Threads / Dual LLM
Ensemble Decisions / Mixture of Experts
Prompt Engineering / Instructional Defense
Preflight "injection test"
```

## Пример: вход → решение

- Нужен quarantine untrusted content → Dual LLM section.
- Нужен CI smoke → Preflight injection test.

## Детерминизм или машинное обучение

Документация — **детерминированный** каталог ссылок.

## Внешние зависимости

Нет.

## Ограничения

- Не executable controls.
- Нужно самому внедрять.

## Сигналы качества

- Широко цитируемый curated list.

## Вердикт

**экспериментально**/reference — map идей защит.

## Связи

- Репозиторий: [[repo-62-prompt-injection-defenses]]
