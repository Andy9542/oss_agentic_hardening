---
type: method
id: 46
layer: memory
method-type: S
prod-viable: false
effectiveness: medium
robustness: low
evidence-level: strong
status: reviewed
tags:
  - agent-security
  - even-batch
sources:
  - source-agentpoison-arxiv
  - source-owasp-llm-2025
  - source-owasp-agentic-2026
covers:
  - ASI06
  - LLM04
---

# Защита памяти агента

## Определение

Защита **long-term memory** и RAG KB: pre-write validation, retrieval-time filtering, provenance/TTL. Расширение чётного набора (№46*). In-session PI → №1/№16; persistent store → здесь.

## Как это работает пошагово

1. **Pre-write:** валидация перед commit в memory/KB.
2. **Retrieval-time:** score/trust filter при RAG retrieve.
3. **Provenance/TTL:** политика источников и срока жизни записей.
4. pre-write / retrieval × inline/off-band.

## От чего защищает

- **ASI06** Memory & Context Poisoning.
- **LLM04** Data Model Poisoning / KB poisoning.
- Backdoor через trigger (AgentPoison benchmark).

## От чего НЕ защищает

- In-session PI без персистентной записи (№1, №16).
- Poison ниже порога (<0.1% в AgentPoison).
- Runtime tool misuse без poisoned memory (№12).

## Алгоритмы и механизмы (подробно)

- **AgentPoison** (arXiv:2407.12784) — attack benchmark: ASR >80%, poison <0.1%.
- Production memory guards — класс в формировании `[не проверено]`.
- Progent тестируется на AgentPoison `[проверено]` handoff.

## Реализации

```dataview
TABLE verdict AS "Вердикт", repo AS "Репозиторий"
FROM "20-implementations"
WHERE type = "repo-catalog" AND (method-id = this.id OR contains(also-method-ids, this.id))
SORT catalog-id ASC
```

## Доказательная база

- source-agentpoison-arxiv

## Покрытие рисков

| Риск | Сценарий в матрице | Уровень | Почему такая оценка |
|------|--------------------|---------|---------------------|
| ASI06 | Отравление памяти и контекста | **выс.** | Критический пробел; целевой класс. |
| ASI04 | ↳ отравление обучения/артефактов | **ср.** | KB poisoning, не training. |

## Оценка эффективности

**Средняя** — критический пробел, зрелые prod-решения ограничены.

## Оценка прочности

**Низкая** — stealthy triggers, slow poisoning.

## Дополняет

- способ №32 (inventory KB)
- способ №44 (red-team probes AgentPoison-style)

## Требует

—

## Не заменяет

- способ №16 (session IFC vs persistent memory)

## Сценический тезис

> Память — доверенная база, пока не положили 0.1% poisoned записей с триггером; AgentPoison 80%+ success; IFC одной сессии не видит.

## Демо-кандидат

Poisoned memory entry → benign queries OK → trigger query → wrong tool action.
