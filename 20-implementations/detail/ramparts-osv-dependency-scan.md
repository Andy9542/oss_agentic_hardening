---
type: implementation-detail
parent-repo: repo-115-ramparts
method-id: 29
mechanism-id: ramparts-osv-stdio-dependency-scan
repo: https://github.com/highflame-ai/ramparts
language: Rust
license: Apache-2.0
verdict: experimental
tags:
  - agent-security
---

# Ramparts — OSV-проверка зависимостей stdio MCP

## Проверенный срез

Upstream [`8fc73b56f124e10c5f58d553573d7faf74fde133`](https://github.com/highflame-ai/ramparts/commit/8fc73b56f124e10c5f58d553573d7faf74fde133) от 2026-06-23.

## Кодовые пути

- `src/osv.rs` — parsing package specs, OSV query и mapping advisories.
- `src/scanner.rs` — параллельный запуск OSV рядом с основным scan.
- `src/types.rs` — `YaraScanResult` для унифицированного finding.
- `src/sarif.rs`, `src/utils.rs` — вывод CVE/GHSA, installed и fixed versions.

## Алгоритм

Для stdio command scanner консервативно извлекает npm package из `npx` или PyPI package из `uvx`, поддерживая scoped npm и точное `==` для PyPI. POST к `https://api.osv.dev/v1/query` имеет timeout 5 секунд. Ответ преобразуется в `VulnerableDependency`: CVE/GHSA aliases, summary, CVSS-derived severity, установленная версия и первая подходящая fixed version попадают в общий YARA-compatible результат.

## Зависимости

Reqwest с rustls и доступ к OSV.dev; API key не требуется. Tokio используется для асинхронного запроса.

## Тесты

Unit tests в `src/osv.rs` покрывают parsing `npx`/`uvx`, scoped packages, request body, CVSS mapping и fixed-version extraction; интеграция проверяется scanner tests.

## Ограничения

Поддерживаются только распознаваемые `npx` и `uvx`; shell wrappers, другие runners и транзитивный lockfile graph не анализируются. Любая network/HTTP/JSON ошибка fail-soft возвращает пустой список, поэтому отсутствие finding не означает отсутствие уязвимости.

## Вердикт

**экспериментально** — полезный сетевой enrichment для типовых MCP launch commands, но не полный dependency scanner и не fail-closed gate.

## Связи

- Репозиторий: [[repo-115-ramparts]]
