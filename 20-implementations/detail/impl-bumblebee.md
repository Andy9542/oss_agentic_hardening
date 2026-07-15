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

# Bumblebee — профильная инвентаризация endpoint

## Проверенная ревизия

`d753592`, дата коммита 2026-06-25; код проверен 2026-07-15.

## Где в коде

- Код: `cmd/bumblebee/main.go`, `cmd/bumblebee/roots.go`, `internal/scanner/scanner.go`, `internal/walk/walk.go`, `internal/ecosystem/`, `internal/model/model.go`.
- Тесты: `internal/scanner/scanner_test.go`, `internal/scanner/scanner_integration_test.go`, `internal/walk/walk_test.go`, `internal/ecosystem/mcp/mcp_test.go`, `internal/ecosystem/skills/skills_test.go`, `cmd/bumblebee/main_test.go`, `cmd/bumblebee/selftest_test.go`.

## Алгоритм

1. Профиль `baseline`, `project` или `deep` определяет корни, допустимую ширину обхода и назначение снимка.
2. Walker пропускает защищённые и шумные каталоги и передаёт только распознанные metadata-файлы специализированным parser-ам.
3. Parser-ы извлекают package, extension, MCP и agent-skill identity без запуска package managers и без чтения исходников.
4. Scanner нормализует записи, ставит `profile`, `root_kind`, provenance и confidence, удаляет дубликаты и выводит NDJSON.

## Зависимости

Go 1.25+ для сборки; бинарник использует только стандартную библиотеку и не имеет runtime-зависимостей. Планировщик запуска и хранилище инвентаря внешние.

## Ограничения

Покрываются только перечисленные metadata formats; Cargo, Maven/Gradle, NuGet, Hex, Swift PM, Safari extensions и loose skill directories не поддерживаются. Наличие записи не доказывает исполнение или компрометацию.

## Вердикт

**экспериментально** — качественно протестированный сенсор способа №32; он наблюдает состояние endpoint и не предотвращает установку или запуск компонента.

## Связи

- Репозиторий: [[repo-118-bumblebee]]
