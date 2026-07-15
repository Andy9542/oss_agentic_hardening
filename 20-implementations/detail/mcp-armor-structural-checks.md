---
type: implementation-detail
parent-repo: repo-113-mcp-armor
method-id: 19
mechanism-id: mcp-armor-structural-mcp-checks
repo: https://github.com/aira-security/mcp-armor
language: Python
license: Apache-2.0
verdict: experimental
tags:
  - agent-security
---

# MCP Armor — структурные проверки MCP entities

## Проверенный срез

Upstream [`6af4cee4665ab6242f02a88952f9127b6a04922a`](https://github.com/aira-security/mcp-armor/commit/6af4cee4665ab6242f02a88952f9127b6a04922a) от 2026-03-27.

## Кодовые пути

- `src/mcp_armor/run_checks.py` — registry и async orchestration.
- `src/mcp_armor/scan_checks/command_injection.py` — аргументы и metadata с command patterns.
- `src/mcp_armor/scan_checks/cross_server_tool_shadowing.py`, `tool_name_ambiguity.py`.
- `src/mcp_armor/scan_checks/excessive_tool_permissions.py`, `hardcoded_secrets.py`.

## Алгоритм

Runner разделяет checks по configuration, tools, resources, prompts и resource templates, создаёт async task на каждую применимую проверку и объединяет результаты. Правила анализируют имена, descriptions, schemas/arguments и client configuration, затем сортируют findings по severity и вычисляют общий risk level. Exceptions отдельной проверки логируются и не останавливают остальные.

## Зависимости

FastMCP для подключения, PyYAML для конфигураций, `thefuzz` для сходства имён и Rich для вывода; ML-модель не нужна для этих структурных checks.

## Тесты

Автоматических unit/integration tests в проверенном срезе нет. `demo-mcp-server/demo_server.py` предоставляет ручные fixtures с уязвимыми tools.

## Ограничения

Проверки работают по опубликованным metadata и config, а не по реализации сервера. Исключения обрабатываются fail-open, поэтому частичный report может выглядеть завершённым; OSS не блокирует вызовы и не поддерживает custom policies.

## Вердикт

**экспериментально** — полезный набор detective checks, но без automated regression suite и runtime enforcement.

## Связи

- Репозиторий: [[repo-113-mcp-armor]]
