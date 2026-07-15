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

# Bumblebee — сопоставление с exposure catalog

## Проверенная ревизия

`d753592`, дата коммита 2026-06-25; код проверен 2026-07-15.

## Где в коде

- Код: `internal/exposure/exposure.go`, `internal/scanner/scanner.go`, `internal/osv/osv.go`, `tools/osvcatalog/main.go`, `docs/schema/v0.1.0/exposure-catalog.schema.json`, `threat_intel/`.
- Тесты: `internal/exposure/exposure_test.go`, `internal/scanner/findings_test.go`, `internal/osv/osv_test.go`, `tools/osvcatalog/main_test.go`.

## Алгоритм

1. Оператор передаёт JSON-файл или каталог файлов с общей `schema_version`.
2. Loader нормализует package names и строит индекс по паре ecosystem и name.
3. Каждая дедуплицированная inventory-запись сопоставляется по точной версии со всеми подходящими entries.
4. Для каждого совпадения scanner создаёт отдельный finding с catalog ID, severity, provenance и evidence.
5. `tools/osvcatalog` может преобразовать offline OSV records о malicious packages в совместимый каталог.

## Зависимости

Внешний exposure catalog обязателен для findings; встроенного автоматического advisory feed и сетевых lookups нет. OSV-конвертер принимает локальные JSON или ZIP.

## Ограничения

Сопоставление точное и не интерпретирует version ranges. Finding подтверждает присутствие metadata, а не запуск, сетевую активность, file hash или persistence. Качество результата ограничено полнотой внешнего каталога.

## Вердикт

**экспериментально** — самостоятельная корреляция inventory по способу №32, полезная для incident response, но не preventive control.

## Связи

- Репозиторий: [[repo-118-bumblebee]]
