---
type: implementation-detail
parent-repo: repo-112-onecli
method-id: 23
repo: https://github.com/onecli/onecli
language: Rust
license: Apache-2.0
verdict: experimental
upstream-sha: 32b5852b
upstream-date: 2026-07-12
tags:
  - agent-security
---

# OneCLI — единый egress gateway

## Код и тесты

- Код: `apps/gateway/src/connect.rs`, `apps/gateway/src/gateway.rs`, `apps/gateway/src/ca.rs`, `apps/gateway/src/auth.rs`.
- Тесты: `apps/gateway/tests/integration.rs`.

## Алгоритм

1. Agent traffic направляется на HTTP(S)-gateway.
2. Gateway аутентифицирует агента и разбирает целевые host и path.
3. CONNECT-трафик проходит через interception и общий policy pipeline.
4. Только разрешённый запрос пересылается наружу; gateway централизует журналирование и credential injection.

## Зависимости

Сетевое принуждение маршрута, доверенный CA для HTTPS interception, DNS и доступ к целевому API.

## Ограничения

Это не полная SSRF-защита: результат зависит от проверки адресов после DNS resolution, правил redirects и блокировки альтернативного egress. Компрометация gateway затрагивает все проходящие credentials.

## Вердикт

**experimental** — соответствует способу №23 как единая точка egress, но требует сетевого deny-by-default и отдельной проверки SSRF-инвариантов.

## Связи

- Репозиторий: [[repo-112-onecli]]
