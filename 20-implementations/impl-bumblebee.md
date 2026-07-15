---
type: implementation
method-id: 32
repo: "https://github.com/perplexityai/bumblebee"
language: "Go"
license: "Apache-2.0"
verdict: экспериментально
tags:
  - agent-security
  - savedtg
  - supply-chain
---

# Bumblebee — инвентаризация developer endpoints

## Репозиторий

https://github.com/perplexityai/bumblebee

## Где в коде

- `cmd/bumblebee/` — CLI.
- `internal/` — профили обхода, parsers и формирование записей.
- `threat_intel/` — exposure catalogs.
- `tools/osvcatalog/` — подготовка каталога из OSV.
- `docs/inventory-sources.md` — поддерживаемые источники метаданных.

## Алгоритм

1. Профиль `baseline`, `project` или `deep` задаёт корни и глубину обхода.
2. Сканер читает lock-файлы, package metadata, manifests расширений и поддерживаемые JSON-конфиги MCP.
3. Компоненты нормализуются в NDJSON с идентификатором endpoint, профилем, ecosystem и provenance.
4. Exposure catalog задаёт известные package/version indicators; точные совпадения превращаются в findings.
5. `scan_summary` позволяет принимающей системе решить, можно ли считать запуск актуальным состоянием.

## Детерминизм или машинное обучение

Полностью детерминированный read-only scanner. Модели и LLM-анализ не используются.

## Внешние зависимости

Go 1.25+ для сборки; бинарник заявлен без сторонних runtime-зависимостей. Планирование запусков и хранение current state остаются задачей внешней системы.

## Сигналы качества

- Apache-2.0, тесты и встроенный `selftest` без сетевых обращений.
- Документированы scope и ограничения, включая неподдерживаемые Codex TOML и Continue YAML в v0.1.
- Проект молодой и решает только inventory/exposure matching, не анализируя исходники и поведение пакетов.

## Вердикт

**экспериментально** — полезный сенсор для incident response и AIBOM-подобной инвентаризации endpoint-состояния; не является самостоятельным preventive control.

## Связи

- Способ: [[32-aibom-inventory]]
- Источник: [[source-bumblebee]]
