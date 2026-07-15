---
type: implementation-detail
parent-repo: repo-08-agent-airlock
method-id: 20
repo: agent-airlock (verify owner)
language: Python
license: ""
verdict: экспериментально
tags:
  - agent-security
---

# agent-airlock — способ №20 (ghost args)

## Репозиторий

agent-airlock (~10★) — in-process Pydantic strict validation.

## Где в коде

Pydantic models для tool args; deny-by-default для capabilities (см. также method-id 14).

## Алгоритм

Strict typing: лишние поля (ghost args) отбрасываются или reject; без неявного приведения типов.

## Детерминизм или машинное обучение

Детерминированный.

## Внешние зависимости

In-process Python; Firecracker/Docker-атрибуции `[не проверено]` — не использовать.

## Сигналы качества

- Существование репо `[проверено]`; полнота README `[factcheck #1 OPEN]`
- Зрелость: маленький проект

## Вердикт

**экспериментально** — единственный подтверждённый носитель класса ghost args; factcheck #1 открыт.

## Связи

- Репозиторий: [[repo-08-agent-airlock]]
