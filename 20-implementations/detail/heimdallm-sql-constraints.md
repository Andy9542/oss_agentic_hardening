---
type: implementation-detail
parent-repo: repo-48-heimdallm
method-id: 1
repo: https://github.com/amoffat/HeimdaLLM
language: Python
license: MIT
verdict: experimental
commit-sha: 7d097ae
commit-date: 2024-07-16
verified-date: 2026-07-15
tags:
  - agent-security
---

# HeimdaLLM — SQL AST constraints для LLM-generated queries

## Репозиторий

- [amoffat/HeimdaLLM](https://github.com/amoffat/HeimdaLLM)
- Проверенный срез: `7d097ae`; код проверен 2026-07-15.

## Что это за технология

**Bifrost pipeline**: LLM порождает SQL → parse AST → **ConstraintValidator** (allowlist колонок/JOIN/обязательные WHERE) → optional reconstruction → исполнять только если constraints pass. Защита от SQL misuse агентом (способ №1 / tool-arg safety).

## Где в коде

- `heimdallm/bifrost.py` — try validators until one succeeds
- `heimdallm/bifrosts/sql/` — SQL bifrost, reconstruct, exc
- `heimdallm/constraints.py`

## Алгоритм

1. LLM output SQL SELECT.
2. Parse tree; для каждого ConstraintValidator: validate / reconstruct.
3. Exceptions: `Column … is not allowed in SELECT`, missing required constraint, forbidden JOIN.
4. Только validated SQL идёт дальше.

## Примеры реализации

```text
# exc.py
Column `{column}` is not allowed in SELECT
Missing required constraint `{column}`=:{placeholder}
# Forbidden join specs similarly raised
```

Pipeline: parse → reconstruct (strip forbidden) → re-validate.

## Пример: вход → решение

- `SELECT * FROM users` без allowlist `*` → reject.
- `SELECT id, email FROM users WHERE tenant_id=:tid` при required tenant constraint → allow.

## Детерминизм или машинное обучение

Constraints **детерминированные**; генерация SQL — LLM.

## Внешние зависимости

Python; SQL dialect parsers в bifrosts.

## Ограничения

- Фокус на SELECT; не полный DBMS firewall.
- Нужно аккуратно задать validators под схему.

## Сигналы качества

- Явная exception taxonomy; reconstruct path.

## Вердикт

**экспериментально** — сильная идея SQL allowlist для LLM.

## Связи

- Репозиторий: [[repo-48-heimdallm]]
