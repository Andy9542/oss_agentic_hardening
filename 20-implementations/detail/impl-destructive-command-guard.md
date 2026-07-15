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

# destructive_command_guard — pre-execution hook

## Код и тесты

- Код: `src/hook.rs`, `src/normalize.rs`, `src/context.rs`, `src/evaluator.rs`, `src/allowlist.rs`.
- Тесты: `tests/agent_hook_output.rs`, `tests/cli_e2e.rs`, `tests/pattern_audit.rs`, `tests/security_regressions.rs`.

## Алгоритм

1. Hook adapter извлекает shell-команду из протокола coding-агента.
2. Команда нормализуется и делится на исполняемый контекст и данные.
3. Allowlist пропускает известные безопасные формы.
4. Evaluator применяет активные security packs и при совпадении возвращает deny, правило и объяснение.

## Зависимости

Локальный бинарник `dcg`, поддерживаемый hook-протокол агента и конфигурация активных packs.

## Ограничения

Hook работает fail-open при ошибках и превышении deadline; `DCG_BYPASS=1` отключает проверку. Прямые API/tool-вызовы и процессы вне hook не покрываются. Лицензия source-available и не OSI-approved.

## Вердикт

**experimental security boundary** — основной механизм способа №19 полезен как guardrail, но требует sandbox, approval и сетевых политик вокруг себя.

## Связи

- Репозиторий: [[repo-117-destructive-command-guard]]
