---
type: implementation
method-id: 14
repo: "https://github.com/onecli/onecli"
language: "Rust / TypeScript"
license: "Apache-2.0"
verdict: экспериментально
tags:
  - agent-security
  - review-2026
  - access-control
  - credential-broker
---

# OneCLI — credential broker для AI-агентов

## Репозиторий

https://github.com/onecli/onecli

## Где в коде

- `apps/gateway` — Rust HTTP gateway, который перехватывает outbound requests и подставляет credentials.
- `packages/api/src/services/policy-rule-service.ts` — правила allow/block/manual approval/rate limit, deny mode и per-agent overrides.
- `packages/api/src/apps/app-permissions/` — каталог разрешений, привязанных к HTTP method, host/path и операциям сервисов.
- Dashboard — управление agents, services, credentials и permissions.
- Конфигурация `.env.example` — опциональная OAuth/team настройка; локальные порты: dashboard `10254`, gateway `10255`.

## Алгоритм

1. Реальные credentials сохраняются в vault OneCLI.
2. Агент получает собственный access token и placeholder key, затем направляет HTTP через gateway.
3. Gateway аутентифицирует агента и сопоставляет HTTP method, host/path и операцию с policy rules.
4. В `deny` mode неразрешённая операция блокируется; для разрешённых операций доступны per-agent overrides, manual approval и rate limit.
5. Только после положительного решения placeholder заменяется расшифрованным credential непосредственно перед outbound request.
6. Ответ возвращается агенту без раскрытия исходного секрета; gateway централизует ротацию, отзыв и журналирование доступа.

## Детерминизм или машинное обучение

Маршрутизация, разрешения и подстановка credentials детерминированы. LLM в контуре решения не требуется.

## Внешние зависимости

Rust gateway, dashboard и хранилище credentials. Локальный single-user режим работает без OAuth; team mode использует Google OAuth. Для целевого API нужен сетевой доступ.

## Сигналы качества

- Тесты в репозитории: CI/команды разработки описаны, но публичные security benchmark и threat model в README не приведены.
- Документированные обходы: соответствие способу №14 появляется только при включённом `deny` mode и корректных endpoint permissions; защита теряется при прямом egress в обход gateway. Это не полноценная SSRF/DLP-защита способа №23.
- Зрелость: архитектура снимает секрет с агента, но проект новый и требует проверки vault, auth, TLS и tenant isolation.

## Вердикт

**экспериментально** — перспективное сочетание secretless-agent паттерна с разрешениями на операции. Как реализация способа №14 учитывается только в `deny` mode, при принудительном egress через gateway и проверенном хранилище credentials.

## Связи

- Способ: [[14-default-deny-allowlists]]
