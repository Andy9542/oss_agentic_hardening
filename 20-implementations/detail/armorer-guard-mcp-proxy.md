---
type: implementation-detail
parent-repo: repo-107-armorer-guard
method-id: 19
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

# Armorer Guard — pre-call MCP proxy

## Проверенная ревизия

`674eb1009a56b50a54bc28163ea99e55c57f9d2a`, дата коммита 2026-06-22; код проверен 2026-07-15.

## Где в коде

- Код: `src/main.rs` (`mcp_proxy_context`, `mcp_proxy_should_block`, `mcp_proxy_handle_line`, `mcp_proxy_error_response`), `docs/MCP_QUICKSTART.md`, `examples/mcp_proxy.md`, `examples/cursor-mcp.md`.
- Тесты: inline-модуль `tests` в `src/main.rs`: `mcp_proxy_blocks_dangerous_tools_call`, `mcp_proxy_passes_safe_tools_call`, `mcp_proxy_error_includes_credential_scan_data`.

## Алгоритм

1. Proxy запускает целевой stdio MCP server дочерним процессом и читает line-delimited JSON-RPC.
2. Для `tools/call` сериализует arguments и сканирует их с context `eval_surface=tool_call_args`, `trace_stage=action`, `policy_scope=mcp`.
3. Credential, dangerous-action, prompt-injection, exfiltration и local-block причины проверяются по hard-block allowlist причин.
4. Опасный вызов заменяется JSON-RPC error `-32001` с reasons, confidence, sanitized text и scan id; безопасный передаётся серверу без изменения.
5. Audit line фиксирует tool name, action и scanner result.

## Зависимости

Rust binary и совместимый line-delimited stdio MCP server. Интеграция требует заменить исходную команду сервера на `armorer-guard mcp-proxy -- <server>`.

## Ограничения

Proxy v1 не поддерживает Content-Length framing и не изолирует дочерний server после разрешённого вызова. Review-only причины сами по себе не блокируют. Защита исчезает, если клиент запускает MCP server в обход wrapper.

## Вердикт

**экспериментально** — ясный chokepoint способа №19 с тестами allow/block, но транспортная совместимость и обязательность wrapper пока ограничены.

## Связи

- Репозиторий: [[repo-107-armorer-guard]]
