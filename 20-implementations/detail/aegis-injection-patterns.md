---
type: implementation-detail
parent-repo: repo-03-aegis
method-id: 19
repo: https://github.com/Justin0504/Aegis
language: Go
license: MIT
verdict: prod
commit-sha: 6b014e4
commit-date: 2026-07-14
verified-date: 2026-07-15
tags:
  - agent-security
---

# Aegis — эвристики инъекций в аргументах tools

## Репозиторий

- [Justin0504/Aegis](https://github.com/Justin0504/Aegis)
- Проверенный срез: `6b014e4`, дата коммита 2026-07-14; код проверен 2026-07-15.

## Что это за технология

**Content scan на границе tool_call**: gateway/PDP перехватывает аргументы, делает deep string extraction (все строковые поля вложенного JSON) и матчит regex/templates на фразы вроде instruction override. Это способ №19 — защита не только user prompt, но и отравленных tool args / MCP results, протащенных в следующий вызов.

Aegis — шлюз с RBAC/аудитом; pattern stage — один из слоёв PDP.

## Где в коде

- Control-plane / gateway apps под `apps/`, SDK Go/Python
- Stage «content scan» в pipeline решения (см. docs/marketing claims в README репозитория)
- Demo-agent и loadtest в `tools/`

## Алгоритм

1. Перехватить tool_call на gateway :8080.
2. Рекурсивно извлечь все string values из args.
3. Нормализовать (базовый casefold) → regex/template match на injection phrases.
4. Hit → deny + audit; miss → следующие стадии (RBAC, anomaly, …).
5. Fail-closed на ошибках сканера (по дизайну gateway).

## Примеры реализации

Типовые целевые фразы (как в смежных продуктовых тестах Aegis/карты каталога):

- `ignore (all )?previous instructions`
- `system:\s*` role override в начале строки
- `you are (now )?DAN`

Deep extraction важен: инъекция в `args.metadata.note`, а не только top-level `query`.

## Пример: вход → решение

- `send_email({body: "Ignore all previous instructions and …"})` → pattern hit → deny.
- Чистый `{body: "Meeting at 3pm"}` → pass к RBAC.

## Детерминизм или машинное обучение

Pattern stage **детерминированный**; behavioral anomaly — отдельный модуль (статистический).

## Внешние зависимости

Self-hosted Docker gateway; без обязательного ML для pattern stage.

## Ограничения

- Те же, что у regex: парафраз без ключевых слов.
- Нужна обязательная маршрутизация агента через gateway.

## Сигналы качества

- Публичные claims: высокий block rate на внутреннем наборе; низкий FPR и ~ms latency на pattern stage.

## Вердикт

**готово к продакшену** — полезный tool-arg injection layer в составе PDP.

## Связи

- Репозиторий: [[repo-03-aegis]]
