---
type: implementation-detail
parent-repo: repo-108-parallax
method-id: 12
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

# Parallax — цепочка YAML evaluators

## Проверенная ревизия

`c9c28face1e7426bb67ab03aa18f772ff7050fc5`, дата коммита 2026-06-05; код и GitHub tree проверены 2026-07-15.

## Где в коде

- Код: `src/config/loader.rs`, `src/config/schema.rs`, `src/engine/chain.rs`, `src/engine/result.rs`, `src/evaluators/mod.rs`, `parallax.yaml`, `docs/ARCHITECTURE.md`.
- Тесты: inline-модули в `src/config/loader.rs`, `src/engine/chain.rs`, `src/engine/result.rs` и `src/evaluators/*.rs`; CI — `.github/workflows/build.yaml`.

## Алгоритм

1. Loader читает server/reporting settings, inline evaluators и YAML files из `rules/`, присваивая им stages.
2. Event нормализуется в `EvalContext` с message, tool name, arguments, result, model params и session identity.
3. Chain сортирует engines по стоимости: regex, pattern, Sigma, CEL, SQL, затем потенциальные ML/LLM.
4. Каждый применимый evaluator возвращает action, reason, confidence, redacted value и metadata; первый `block` прекращает цепочку.
5. При отсутствии block результаты агрегируются с приоритетом `redact > detect > allow`; panic evaluator превращается в `detect`, а не в разрешение.

## Зависимости

Rust 1.70+, Tokio/Axum, Serde YAML/JSON, regex, CEL parser и rusqlite. Server mode требует, чтобы agent runtime синхронно вызывал HTTP endpoint; proxy и hooks имеют собственные интеграционные crates.

## Ограничения

YAML rules корректны лишь для полей, которые передала интеграция. Реализованные Sigma conditions и CEL expressions — ограниченные подмножества соответствующих языков. Ошибка evaluator даёт `detect`, поэтому fail-closed поведение требует внешней политики на такие события.

## Вердикт

**экспериментально** — прозрачный и тестируемый механизм способа №12, но гарантии зависят от hook coverage и трактовки внутренних ошибок вызывающим runtime.

## Связи

- Репозиторий: [[repo-108-parallax]]
