---
type: implementation-detail
parent-repo: repo-106-dvalincode
method-id: 39
repo: https://github.com/arthurpanhku/dvalincode
language: TypeScript
license: MIT
verdict: экспериментально
commit-sha: d47516748f2acfc75111ca150ca2eda607187f82
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# DvalinCode — hash-chained audit JSONL

## Проверенная ревизия

`d47516748f2acfc75111ca150ca2eda607187f82`, дата коммита 2026-07-15; код проверен 2026-07-15.

## Где в коде

- Код: `src/audit/log.ts`, `src/audit/hash.ts`, `src/audit/report.ts`, `src/audit/taps.ts`, `src/sessions/journal.ts`, `src/evidence/pack.ts`.
- Тесты: `tests/audit/log.test.ts`, `tests/audit/report.test.ts`, `tests/sessions/journal.test.ts`, `tests/evidence/evidence.test.ts`.

## Алгоритм

1. Для запуска создаётся JSONL-файл и genesis hash `SHA-256(runId)`.
2. Каждое событие получает монотонный `seq`, timestamp и `prevHash`; новый chain head равен SHA-256 канонического JSON текущей записи.
3. Журнал фиксирует policy provenance, tool calls, provider/MCP requests, file operations, shell execution, approvals и итог запуска; длинные свободные поля обрезаются.
4. Проверка заново вычисляет genesis и каждый link, выявляя изменение, удаление, вставку или перестановку строк.
5. Session journal сохраняет chain head, а Evidence Pack может повторно проверить вложенные записи без доступа к исходному файлу.

## Зависимости

Node.js filesystem и crypto primitives; журнал по умолчанию хранится в `~/.dvalincode/audit`. Криптографической подписи, внешнего timestamping и защищённого append-only storage нет.

## Ограничения

Запись best-effort: ошибки append накапливаются как warnings и не останавливают agent loop. SHA-256 chain обнаруживает последующую подмену только при наличии доверенного checkpoint; локальный атакующий может заменить весь файл вместе с genesis-derived цепочкой.

## Вердикт

**экспериментально** — корректно протестированный tamper-evident журнал способа №39, но без подписи и внешнего якоря он не является неизменяемым хранилищем.

## Связи

- Репозиторий: [[repo-106-dvalincode]]
