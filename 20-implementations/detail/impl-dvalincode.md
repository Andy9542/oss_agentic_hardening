---
type: implementation-detail
parent-repo: repo-106-dvalincode
method-id: 12
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

# DvalinCode — сужаемые политики инструментов

## Проверенная ревизия

`d47516748f2acfc75111ca150ca2eda607187f82`, дата коммита 2026-07-15; код проверен 2026-07-15.

## Где в коде

- Код: `src/core/policy.ts`, `src/tools/registry.ts`, `src/core/permissions.ts`, `src/core/context.ts`, `src/agent/session.ts`.
- Тесты: `tests/core/policy.test.ts`, `tests/core/policy-check.test.ts`, `tests/core/policy-recipes.test.ts`, `tests/policyEnforcement.test.ts`, `tests/commands/runTool.test.ts`.

## Алгоритм

1. Runtime читает machine, repository и опциональный per-run policy JSON и валидирует их строгой Zod-схемой.
2. Allowlists пересекаются, denylists объединяются, `defaultDeny` распространяется дизъюнкцией, а network level и `maxToolCalls` выбираются по наиболее строгому значению.
3. Каждая tool-реализация объявляет policy targets: имя инструмента, команду, путь или MCP server.
4. `ToolRegistry.run` проверяет targets до выполнения и пишет `policy_violation`; approval mode не может отменить организационный запрет.
5. Хеш канонической effective policy и хеши источников попадают в событие начала запуска.

## Зависимости

Bun/Node.js, TypeScript и `zod`; machine policy хранится в `~/.dvalincode/policy.json`, repository policy — в `dvalin.policy.json`. Жёсткая защита от локального администратора требует внешнего server-mediated enforcement.

## Ограничения

Отсутствующее поле означает отсутствие ограничения, а без policy files effective policy разрешающая. Повреждённый слой отмечается ошибкой и не применяется, поэтому оператор должен контролировать предупреждение. Локальный пользователь с административными правами может изменить код runtime или policy; механизм только обнаруживает подмену по хешам.

## Вердикт

**экспериментально** — цельный и тестируемый механизм способа №12 с монотонным сужением, но локальная модель доверия не обеспечивает tamper-proof enforcement.

## Связи

- Репозиторий: [[repo-106-dvalincode]]
