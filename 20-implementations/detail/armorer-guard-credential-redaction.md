---
type: implementation-detail
parent-repo: repo-107-armorer-guard
method-id: 7
repo: https://github.com/ArmorerLabs/Armorer-Guard
language: Rust
license: MIT
verdict: экспериментально
commit-sha: 674eb1009a56b50a54bc28163ea99e55c57f9d2a
commit-date: 2026-06-22
verified-date: 2026-07-15
tags:
  - agent-security
---

# Armorer Guard — распознавание и редактирование credentials

## Проверенная ревизия

`674eb1009a56b50a54bc28163ea99e55c57f9d2a`, дата коммита 2026-06-22; код проверен 2026-07-15.

## Где в коде

- Код: `src/main.rs` (`regex_redact`, `detect_prefixed_token`, `detect_assignment_value`, `detect_telegram_token`, `detect_credentials`), `docs/CAPABILITIES.md`, `docs/SECURITY_MODEL.md`.
- Тесты: inline-модуль `tests` в `src/main.rs`, включая Notion, OpenRouter, generic assignment, redaction marker и credential data в MCP error.

## Алгоритм

1. Credential lane проверяет известные префиксы и форматы токенов Notion, GitHub, OpenRouter, OpenAI, Gemini и Telegram.
2. Отдельный parser распознаёт присваивания generic secret/API key и отбрасывает слишком короткие значения.
3. Совпадение получает provider type и предлагаемое имя environment variable.
4. Sanitizer заменяет значение типизированным marker, а policy lane запрещает disclosure на outbound/tool boundaries.
5. Сильный local allow feedback не может подавить `detected:credential` и `policy:credential_disclosure`.

## Зависимости

Только локальный Rust scanner и встроенные patterns; сетевые lookup и cloud DLP отсутствуют.

## Ограничения

Покрываются известные форматы и эвристики присваивания; произвольные, зашифрованные или фрагментированные секреты могут не распознаться. Redaction не отзывает уже раскрытый credential и не заменяет ротацию ключей.

## Вердикт

**экспериментально** — самостоятельный детерминированный механизм способа №7 с хорошей локальной интеграцией, но ограниченным словарём форматов.

## Связи

- Репозиторий: [[repo-107-armorer-guard]]
