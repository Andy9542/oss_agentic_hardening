---
type: implementation-detail
parent-repo: repo-23-aguara-mcp
method-id: 27
repo: https://github.com/garagon/aguara-mcp
language: Go
license: Apache-2.0
verdict: experimental
commit-sha: 6feb0f9
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# aguara-mcp — Aguara как MCP/CI tool

## Репозиторий

- [garagon/aguara-mcp](https://github.com/garagon/aguara-mcp)
- Проверенный срез: `6feb0f9`; код проверен 2026-07-15.

## Что это за технология

Обёртка, которая выставляет **Aguara scanner** как MCP-инструмент и/или CI step: агент или pipeline вызывает scan skill/repo через MCP instead of CLI. Механизм детекции тот же (patterns + rug-pull); меняется delivery surface.

## Где в коде

- README / MCP server entry в корне репозитория
- Делегирует в Aguara engine (sibling project)

## Алгоритм

1. Подключить MCP server aguara-mcp к хосту агента/CI.
2. Tool `scan` принимает path/bundle.
3. Запуск Aguara engine → JSON findings.
4. CI fail on severity threshold.

## Примеры реализации

Типовой вызов: MCP tool scan на `./skills/my-skill` → findings list с rule IDs (`RUGPULL_001`, pattern IDs).

## Пример: вход → решение

- CI PR добавляет skill с credential pattern → scan fail → block merge.

## Детерминизм или машинное обучение

Как у Aguara — в основном детерминированный.

## Внешние зависимости

Aguara binary/engine; MCP host.

## Ограничения

- Тонкий адаптер: качество = Aguara rules.

## Сигналы качества

- Парный проект к Aguara; CI-oriented.

## Вердикт

**экспериментально** — удобная MCP/CI поверхность для Aguara.

## Связи

- Репозиторий: [[repo-23-aguara-mcp]]
