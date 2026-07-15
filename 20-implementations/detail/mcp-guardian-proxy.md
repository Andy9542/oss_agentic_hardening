---
type: implementation-detail
parent-repo: repo-36-mcp-guardian
method-id: 21
repo: https://github.com/eqtylab/mcp-guardian
language: Rust
license: Apache-2.0
verdict: experimental
commit-sha: 54395bf
commit-date: 2025-04-10
verified-date: 2026-07-15
tags:
  - agent-security
---

# MCP Guardian — прокси MCP с human approval

## Репозиторий

- [eqtylab/mcp-guardian](https://github.com/eqtylab/mcp-guardian)
- Проверенный срез: `54395bf`, дата коммита 2025-04-10; код проверен 2026-07-15.

## Что это за технология

**MCP proxy + approval UI**: между хостом LLM и MCP server встаёт `mcp-guardian-proxy`, логирует сообщения и может поставить tool call на **approve/deny человеком** в realtime (CLI/GUI). Это способ №21 (HITL) для MCP без изменения серверов.

## Где в коде

- Proxy: `mcp-guardian-core/src/proxy.rs` (`proxy_mcp_server`)
- Approvals: `mcp-guardian-core/src/message_approval.rs` (`deny_message`, approve)
- Apps: `mcp-guardian-cli/`, Tauri GUI `mcp-guardian/`
- Docs: `docs/src/tutorial/index.md`

## Алгоритм

1. Сконфигурировать collection MCP servers через CLI/GUI.
2. Хост указывает proxy вместо прямого server command.
3. Proxy запускает upstream (`program` + args), стыкует stdio/SSE.
4. Каждое tool call message может требовать approval → UI pending list.
5. Approve → forward; deny → `deny_message(id)` → ошибка клиенту.
6. Логи traces всей активности.

## Примеры реализации

```rust
// message_approval.rs
pub async fn deny_message(id: String) -> Result<()> { … }
```

Build: `nix develop` → `just build-release` → `_build/bin/mcp-guardian-proxy`.

Automated message scans («Coming Soon» в README) — будущий слой; сейчас HITL+logging.

## Пример: вход → решение

- Tool `delete_repo` в pending → оператор Deny → агент получает отказ.
- Read-only `list_files` в auto-allow профиле → pass-through + log.

## Детерминизм или машинное обучение

HITL/proxy **детерминированные**.

## Внешние зависимости

Rust toolchain / nix; Node для GUI.

## Ограничения

- Automated scans ещё не готовы.
- Latency HITL; нужен внимательный оператор.

## Сигналы качества

- Чёткий product docs на mcp-guardian.org; Rust monorepo.

## Вердикт

**экспериментально** — полезный HITL MCP proxy; зрелость автоматики низкая.

## Связи

- Репозиторий: [[repo-36-mcp-guardian]]
