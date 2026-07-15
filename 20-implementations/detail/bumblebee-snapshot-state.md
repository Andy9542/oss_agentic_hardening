---
type: implementation-detail
parent-repo: repo-118-bumblebee
method-id: 32
repo: https://github.com/perplexityai/bumblebee
language: Go
license: Apache-2.0
verdict: экспериментально
commit-sha: d753592
commit-date: 2026-06-25
verified-date: 2026-07-15
tags:
  - agent-security
---

# Bumblebee — завершённые снимки и current state

## Проверенная ревизия

`d753592`, дата коммита 2026-06-25; код проверен 2026-07-15.

## Где в коде

- Код: `internal/model/model.go`, `internal/output/output.go`, `internal/output/httpsink.go`, `cmd/bumblebee/sink.go`, `docs/state-model.md`, `docs/transport.md`, `docs/schema/v0.1.0/scan-summary.schema.json`.
- Тесты: `internal/model/model_test.go`, `internal/output/output_test.go`, `internal/output/httpsink_test.go`, `cmd/bumblebee/main_test.go`.

## Алгоритм

1. Запуск получает случайный `run_id`, а записи — стабильный content-addressed `record_id`.
2. Emitter дедуплицирует пакетные записи внутри запуска и отправляет packages, findings и diagnostics.
3. После обхода создаётся единственный `scan_summary` со статусом, roots, counts, timeout и delivery counters.
4. Получатель повышает снимок до current state только при `status=complete`; partial, error и запуск без summary остаются сырыми свидетельствами.
5. Текущий inventory строится отдельно для `baseline` и `project`, а `deep` не используется для вывода об удалении пакетов.

## Зависимости

Локальный file/stdout sink либо HTTPS sink; долговременное хранение, дедупликация между запусками и promotion logic реализуются принимающей системой.

## Ограничения

Сам Bumblebee не хранит историю и не планирует запуски. Устаревший endpoint без свежего полного снимка нельзя считать чистым. Счётчики доставки в summary не включают финальный flush самого summary.

## Вердикт

**экспериментально** — самостоятельный протокол целостности снимка для способа №32, уменьшающий риск ложного current state, но не обеспечивающий preventive enforcement.

## Связи

- Репозиторий: [[repo-118-bumblebee]]
