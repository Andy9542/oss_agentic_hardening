---
type: implementation-detail
parent-repo: repo-113-mcp-armor
method-id: 25
mechanism-id: mcp-armor-sha512-metadata-baseline
repo: https://github.com/aira-security/mcp-armor
language: Python
license: Apache-2.0
verdict: experimental
tags:
  - agent-security
---

# MCP Armor — SHA-512 baseline MCP metadata

## Проверенный срез

Upstream [`6af4cee4665ab6242f02a88952f9127b6a04922a`](https://github.com/aira-security/mcp-armor/commit/6af4cee4665ab6242f02a88952f9127b6a04922a) от 2026-03-27.

## Кодовые пути

- `src/mcp_armor/baseline.py` — immutable baseline records, SHA-512 и JSON persistence.
- `src/mcp_armor/scan_checks/baseline_deviation.py` — сравнение tools, resources, prompts и templates.
- `src/mcp_armor/cli.py` — `inspect` и `scan --baseline`.
- `src/mcp_armor/security_utils.py` — bounds для безопасного чтения baseline.

## Алгоритм

`inspect` инвентаризирует MCP entities и сохраняет timestamp, config files и SHA-512-хеши. Для tool отдельно хешируются description, sorted metadata (`input_schema`, `output_schema`, tags) и input properties; для resources, prompts и templates — соответствующие descriptions, URI, MIME, arguments и metadata. Scan сопоставляет entity по server/name/config и выдаёт critical rug-pull finding со списком изменённых полей.

## Зависимости

Python 3.10–3.15, FastMCP и PyYAML; baseline использует stdlib `hashlib`/`json`. Для inventory требуется запуск или подключение к настроенным MCP-серверам.

## Тесты

Автоматических тестов и test workflow в проверенном срезе нет. `demo-mcp-server/` содержит намеренно уязвимый сервер для ручной проверки, но не является automated regression suite.

## Ограничения

Baseline не подписан и хранится локально: атакующий с write-доступом может заменить и файл, и ожидаемые хеши. Новые/удалённые entities не обрабатываются этим кодом так же явно, как модификации совпавших ключей; operational approval остаётся внешним.

## Вердикт

**экспериментально** — конкретная криптографическая детекция metadata drift, но отсутствие automated tests, подписи baseline и enforcement не позволяет считать её самостоятельным trust anchor.

## Связи

- Репозиторий: [[repo-113-mcp-armor]]
