---
type: implementation-detail
parent-repo: repo-08-agent-airlock
method-id: 5
repo: https://github.com/sattyamjjain/agent-airlock
language: Python
license: MIT
verdict: prod
commit-sha: eb90d17
commit-date: 2026-07-14
verified-date: 2026-07-15
tags:
  - agent-security
---

# agent-airlock — PII masking на tool seam

## Репозиторий

- [sattyamjjain/agent-airlock](https://github.com/sattyamjjain/agent-airlock)
- Проверенный срез: `eb90d17`, дата коммита 2026-07-14; код проверен 2026-07-15.

## Что это за технология

Опция `@Airlock(mask_pii=True)` включает слой выявления/маскирования персональных данных на входе/выходе tool (способ №5). Типично опирается на распознаватели сущностей (email, phone, card, …) — аналогично Presidio-паттерну: найти span → заменить плейсхолдером до передачи в LLM или во внешний API.

## Где в коде

- Конфиг/core: `src/agent_airlock/core.py`, `config.py` (`mask_pii`)
- Пример: `examples/workspace_pii.py`
- Trace redaction: `trace_redaction.py` (связанный контур)

## Алгоритм

1. Перед/после tool: если `mask_pii`.
2. Прогнать текст аргументов/результата через entity detectors (~12 типов в карточке продукта).
3. Заменить найденные spans на токены `<EMAIL>`, `<PHONE>`, …
4. Продолжить pipeline (schema validation, sandbox, budget).

## Примеры реализации

Включение:

```python
@Airlock(mask_pii=True)
def lookup_customer(email: str) -> str: ...
```

Пример сценария в `examples/workspace_pii.py` — workspace текст с PII до/после маскирования.

## Пример: вход → решение

- Аргумент `email=jane.doe@contoso.com` → в логах/LLM контексте `email=<EMAIL_ADDRESS>`.
- Текст без PII → без изменений.

## Детерминизм или машинное обучение

В основном **детерминированный** regex/recognizer path (без LLM для маскирования).

## Внешние зависимости

Python Airlock; детекторы PII локально.

## Ограничения

- Не заменяет Presidio на сложных NER-именах без NLP-модели.
- Schema-valid exfil через не-PII поля не ловит.

## Сигналы качества

- Отдельный example + benchmarks blockrate в репозитории.

## Вердикт

**готово к продакшену** — удобный PII layer рядом с schema/RBAC декоратором.

## Связи

- Репозиторий: [[repo-08-agent-airlock]]
