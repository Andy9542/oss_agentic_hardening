---
type: implementation-detail
parent-repo: repo-112-onecli
method-id: 11
repo: https://github.com/onecli/onecli
language: TypeScript/Rust
license: Apache-2.0
verdict: experimental
upstream-sha: 32b5852b
upstream-date: 2026-07-12
tags:
  - agent-security
---

# OneCLI — rate limit и бюджет

## Код и тесты

- Код: `apps/gateway/src/budget.rs`, `apps/gateway/src/policy.rs`, `packages/api/src/services/policy-rule-service.ts`.
- Тесты: `apps/gateway/tests/integration.rs`, `packages/api/src/services/policy-rule-service.test.ts`.

## Алгоритм

1. Gateway определяет агента и применимое policy rule.
2. До credential injection проверяется лимит запросов или бюджет операции.
3. Превышение лимита блокирует запрос; допустимый запрос продолжает policy pipeline.
4. Учёт связывается с идентичностью агента, а не с placeholder credential.

## Зависимости

Стабильная agent identity, единое состояние счётчиков для всех экземпляров gateway и корректная конфигурация временных окон.

## Ограничения

Лимит не ограничивает ущерб одного разрешённого дорогостоящего действия. При распределённом развёртывании несогласованные счётчики допускают превышение бюджета.

## Вердикт

**experimental** — реализует способ №11 как часть gateway policy, но production-оценка требует тестов конкурентного обновления и отказоустойчивого хранения счётчиков.

## Связи

- Репозиторий: [[repo-112-onecli]]
