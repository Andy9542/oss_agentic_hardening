---
type: implementation-detail
parent-repo: repo-117-destructive-command-guard
method-id: 19
repo: https://github.com/Dicklesworthstone/destructive_command_guard
language: Rust
license: MIT with OpenAI/Anthropic rider
license-class: source-available
osi-approved: false
verdict: experimental
upstream-sha: 80969f63
upstream-date: 2026-07-15
tags:
  - agent-security
---

# destructive_command_guard — heredoc и inline scripts

## Код и тесты

- Код: `src/heredoc.rs`, `src/ast_matcher.rs`, `src/context.rs`.
- Тесты: `tests/debug_heredoc_extraction.rs`, `tests/regression_heredoc_masking.rs`, `tests/repro_inline_bypass.rs`, `fuzz/fuzz_targets/fuzz_heredoc_extract.rs`.

## Алгоритм

1. Быстрый trigger stage определяет heredoc или inline-script candidate.
2. Извлекатель отделяет тело и определяет язык.
3. AST matcher классифицирует исполняемые конструкции.
4. Вложенные команды повторно проходят packs; timeout и parse error обрабатываются согласно fallback-настройкам.

## Зависимости

`ast-grep`, tree-sitter grammars для поддерживаемых языков и отдельный временной бюджет heredoc pipeline.

## Ограничения

Неподдерживаемый язык, динамически собранная строка или parse error могут оставить обход. Hook defaults допускают fail-open при timeout; глубина и число heredoc ограничены ради latency.

## Вердикт

**experimental security boundary** — самостоятельное усиление способа №19 против вложенных команд, но не полный shell interpreter и не доказательство отсутствия обходов.

## Связи

- Репозиторий: [[repo-117-destructive-command-guard]]
