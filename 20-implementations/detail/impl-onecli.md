---
type: implementation-detail
parent-repo: repo-112-onecli
method-id: 14
repo: https://github.com/onecli/onecli
language: TypeScript/Rust
license: Apache-2.0
verdict: experimental
upstream-sha: 32b5852b
upstream-date: 2026-07-12
tags:
  - agent-security
---

# OneCLI — credential broker и default deny

## Код и тесты

- Код: `apps/gateway/src/policy.rs`, `apps/gateway/src/inject.rs`, `apps/gateway/src/secret_inject.rs`, `packages/api/src/services/policy-rule-service.ts`.
- Тесты: `apps/gateway/tests/integration.rs`, `packages/api/src/services/policy-rule-service.test.ts`.

## Алгоритм

1. Агент аутентифицируется access token и отправляет через gateway запрос с placeholder.
2. Gateway сопоставляет endpoint и операцию с scoped policy rules.
3. В deny mode отсутствие разрешения завершает запрос до доступа к credential.
4. Разрешённый запрос получает расшифрованный секрет только в модуле injection и уходит во внешний API.

## Зависимости

Rust gateway, TypeScript API, PostgreSQL и ключ шифрования; для HTTPS interception нужен доверенный локальный CA.

## Ограничения

Прямой egress в обход gateway раскрывает агенту альтернативный путь. Эффект default deny зависит от deny mode, полноты endpoint permissions, защиты agent token и tenant isolation.

## Вердикт

**experimental** — основной механизм способа №14 архитектурно обоснован, но требует принудительной маршрутизации и отдельной проверки auth, TLS и secret store.

## Связи

- Репозиторий: [[repo-112-onecli]]
