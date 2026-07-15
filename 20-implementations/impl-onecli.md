---
type: implementation
method-id: 23
repo: "https://github.com/onecli/onecli"
language: "Rust / TypeScript"
license: "Apache-2.0"
verdict: экспериментально
tags:
  - agent-security
  - review-2026
  - egress
---

# OneCLI — credential broker для AI-агентов

## Репозиторий

https://github.com/onecli/onecli

## Где в коде

- `apps/gateway` — Rust HTTP gateway.
- Dashboard — управление agents, services и credentials.
- Конфигурация `.env.example` — опциональная OAuth/team настройка.
- Локальные порты: dashboard `10254`, gateway `10255`.

## Алгоритм

1. Реальные credentials сохраняются в vault OneCLI.
2. Агент получает placeholder key и направляет HTTP через gateway.
3. Gateway аутентифицирует агента и сопоставляет запрос с разрешённым сервисом.
4. Placeholder заменяется расшифрованным credential непосредственно перед outbound request.
5. Ответ возвращается агенту без раскрытия исходного секрета.
6. Централизованный gateway обеспечивает ротацию, отзыв и журналирование доступа.

## Детерминизм или машинное обучение

Маршрутизация, разрешения и подстановка credentials детерминированы. LLM в контуре решения не требуется.

## Внешние зависимости

Rust gateway, dashboard и хранилище credentials. Локальный single-user режим работает без OAuth; team mode использует Google OAuth. Для целевого API нужен сетевой доступ.

## Сигналы качества

- Тесты в репозитории: CI/команды разработки описаны, но публичные security benchmark и threat model в README не приведены.
- Документированные обходы: защита теряется при прямом egress в обход gateway; сам gateway не заявляет полноценные SSRF/DLP проверки.
- Зрелость: архитектура снимает секрет с агента, но проект новый и требует проверки vault, auth, TLS и tenant isolation.

## Вердикт

**экспериментально** — перспективная реализация secretless-agent паттерна; безопасна только при принудительном egress через gateway и проверенном хранилище credentials.

## Связи

- Способ: [[23-единый-прокси-исходящих-запросов-и-защита-от-ssrf]]
