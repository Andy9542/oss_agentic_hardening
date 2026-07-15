---
type: implementation-detail
parent-repo: repo-112-onecli
method-id: 21
repo: https://github.com/onecli/onecli
language: TypeScript/Rust
license: Apache-2.0
verdict: experimental
upstream-sha: 32b5852b
upstream-date: 2026-07-12
tags:
  - agent-security
---

# OneCLI — ручное одобрение запроса

## Код и тесты

- Код: `apps/gateway/src/approval.rs`, `apps/gateway/src/policy.rs`, `packages/api/src/services/policy-rule-service.ts`.
- Тесты: `apps/gateway/tests/integration.rs`, `packages/api/src/services/policy-rule-service.test.ts`.

## Алгоритм

1. Policy rule помечает операцию как требующую manual approval.
2. Gateway приостанавливает исходящий запрос и создаёт состояние ожидания.
3. Решение оператора разрешает или отклоняет продолжение.
4. Credential подставляется только после положительного решения.

## Зависимости

Gateway, API и доступный операторский интерфейс; состояние approval должно сохранять привязку к исходному агенту и запросу.

## Ограничения

Одобрение не исправляет слишком широкую формулировку операции и уязвимо к усталости оператора. Необходимо проверять неизменность параметров между запросом и продолжением.

## Вердикт

**experimental** — самостоятельная реализация способа №21, пригодная как дополнительный gate для опасных операций после проверки TOCTOU-свойств.

## Связи

- Репозиторий: [[repo-112-onecli]]
