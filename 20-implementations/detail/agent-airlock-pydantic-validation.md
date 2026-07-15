---
type: implementation-detail
parent-repo: repo-08-agent-airlock
method-id: 13
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

# agent-airlock — строгая Pydantic-валидация аргументов

## Репозиторий

- [sattyamjjain/agent-airlock](https://github.com/sattyamjjain/agent-airlock)
- Проверенный срез: `eb90d17`, дата коммита 2026-07-14; код проверен 2026-07-15.

## Что это за технология

**Pydantic** — библиотека runtime-валидации данных по type hints / JSON Schema. Airlock оборачивает tool-функции: перед вызовом аргументы проходят `validate_call` в строгом режиме (без тихой coercion), плюс детекция **ghost args** — ключей, которых нет в сигнатуре (способ №13 + №20).

LLM часто «додумывает» лишние поля (`admin=true`); strict schema это отсекает.

## Где в коде

- `src/agent_airlock/validator.py` — `detect_ghost_arguments`, `strip_ghost_arguments`, `GhostArgumentError`, Pydantic `validate_call`
- `src/agent_airlock/unknown_args.py` — режимы BLOCK / STRIP_AND_LOG / STRIP_SILENT
- `src/agent_airlock/core.py` — декоратор `Airlock`

## Алгоритм

1. Перехватить kwargs tool call.
2. `detect_ghost_arguments`: сравнить keys с `inspect.signature`; если нет `**kwargs` — лишние = ghosts.
3. Strict: `GhostArgumentError`; иначе strip + log.
4. `pydantic.validate_call` / schema model — типы, bounds, forbidden extras (`ConfigDict` strict).
5. При ошибке — structured `AirlockResponse` для self-heal LLM, а не сырой traceback.

## Примеры реализации

```python
def detect_ghost_arguments(func, kwargs):
    valid_params, accepts_kwargs = get_valid_parameters(func)
    if accepts_kwargs:
        return set()
    return set(kwargs.keys()) - valid_params
```

Режимы unknown args: `UnknownArgsMode.BLOCK` | `STRIP_AND_LOG` | `STRIP_SILENT`.

## Пример: вход → решение

- Tool `send_email(to: str, body: str)`; call с `{to, body, bcc_admin: true}` → ghost `bcc_admin` → **block** в strict.
- `{to: 123}` при `to: str` → ValidationError → deny + repair hint.

## Детерминизм или машинное обучение

**Детерминированный**.

## Внешние зависимости

Python, `pydantic`, `structlog`. Без GPU.

## Ограничения

- Не ловит семантически опасные, но schema-valid аргументы (`to=attacker@evil.com` при типе str).
- Нужны хорошие аннотации типов у tools.

## Сигналы качества

- Обширные tests/smoke scripts в репозитории.

## Вердикт

**готово к продакшену** — базовый слой schema+ghost-args для LangChain/CrewAI tools.

## Связи

- Репозиторий: [[repo-08-agent-airlock]]
