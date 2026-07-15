---
type: implementation
method-id: 25
repo: "https://github.com/aira-security/mcp-armor"
language: "Python"
license: "Apache-2.0"
verdict: экспериментально
tags:
  - agent-security
  - review-2026
  - mcp-security
---

# MCP Armor — инвентаризация и baseline drift для MCP

## Репозиторий

https://github.com/aira-security/mcp-armor

## Где в коде

- CLI `mcp-armor inspect` — inventory и baseline.
- CLI `mcp-armor scan` — security checks и сравнение baseline.
- `demo-mcp-server/` — намеренно уязвимые MCP fixtures.
- `logs/mcp_armor.log` — локальный audit log.

## Алгоритм

1. Обнаруживает MCP-конфигурации Claude Desktop, Cursor, Windsurf, VS Code и других клиентов.
2. Подключается к серверам и инвентаризирует tools, resources и prompts.
3. Inspect сохраняет утверждённый baseline компонентов и metadata.
4. Scan ищет prompt injection, poisoning, cross-server shadowing, ambiguity и опасные описания.
5. Повторное сканирование сравнивает состояние с baseline и выявляет rug pull/drift.
6. Формирует JSON или Markdown report и локальный audit trail.

## Детерминизм или машинное обучение

Inventory, baseline diff и большинство structural checks детерминированы. Prompt-injection проверка использует локальную модель FT-Llama-Prompt-Guard-2 и вероятностна.

## Внешние зависимости

Python package и локальные MCP clients/servers. Hugging Face нужен для первоначальной загрузки открытой модели; после загрузки анализ выполняется локально. Enterprise-функции не входят в OSS.

## Сигналы качества

- Тесты в репозитории: намеренно уязвимый demo MCP server.
- Документированные обходы: OSS ограничен configuration scanning; runtime enforcement и custom policies отнесены к enterprise.
- Зрелость: pip package и полный scan flow есть, но открытая версия не является блокирующим gateway.

## Вердикт

**экспериментально** — хороший detective control для inventory и rug-pull, но без отдельного admission/enforcement слоя находки остаются рекомендациями.

## Связи

- Способ: [[25-контроль-целостности-описаний-инструментов]]
