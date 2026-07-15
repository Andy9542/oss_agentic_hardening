---
type: implementation-detail
parent-repo: repo-108-parallax
method-id: 7
repo: https://github.com/agent-defense/parallax
language: Rust
license: Apache-2.0
verdict: экспериментально
commit-sha: c9c28face1e7426bb67ab03aa18f772ff7050fc5
commit-date: 2026-06-05
verified-date: 2026-07-15
tags:
  - agent-security
---

# Parallax — regex-redaction секретов

## Проверенная ревизия

`c9c28face1e7426bb67ab03aa18f772ff7050fc5`, дата коммита 2026-06-05; код и GitHub tree проверены 2026-07-15.

## Где в коде

- Код: `src/evaluators/regex_eval.rs`, `src/engine/context.rs`, `src/engine/result.rs`, `rules/regex/secrets.yaml`, `docs/RULES.md`.
- Тесты: inline-модуль в `src/evaluators/regex_eval.rs`, включая `test_redact`, field targeting, multi-pattern AND и negation.

## Алгоритм

1. YAML rule задаёт один или несколько regex, action, stages и опциональные target fields.
2. Engine компилирует patterns при загрузке; невалидное правило пропускается с warning.
3. На событии evaluator проверяет выбранные поля либо весь searchable text и поддерживает режимы `any`, `all` и negation.
4. Для action `redact` все положительные совпадения заменяются строкой `[REDACTED]`.
5. Shipped rules редактируют AWS keys, GitHub tokens и generic API keys, а PEM private key block полностью блокируют.

## Зависимости

Rust crate `regex`, YAML loader и переданные integration fields. Внешний secret manager или сетевой detector не требуется.

## Ограничения

Список shipped patterns конечен и не ловит произвольные, разбитые или кодированные значения. Невалидный regex отключает правило вместо отказа запуска. Возвращённый redacted text должен фактически использовать вызывающий runtime, иначе исходный payload продолжит обработку.

## Вердикт

**экспериментально** — самостоятельная реализация способа №7 с тестируемой redaction, но ограниченная сигнатурами и соблюдением verdict интеграцией.

## Связи

- Репозиторий: [[repo-108-parallax]]
