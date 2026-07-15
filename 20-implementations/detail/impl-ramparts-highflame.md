---
type: implementation-detail
parent-repo: repo-115-ramparts
method-id: 26
mechanism-id: ramparts-mcp-yara-llm-scan
repo: https://github.com/highflame-ai/ramparts
language: Rust
license: Apache-2.0
verdict: experimental
tags:
  - agent-security
---

# Ramparts — YARA и LLM-анализ MCP

## Проверенный срез

Upstream [`8fc73b56f124e10c5f58d553573d7faf74fde133`](https://github.com/highflame-ai/ramparts/commit/8fc73b56f124e10c5f58d553573d7faf74fde133) от 2026-06-23.

## Кодовые пути

- `src/mcp_client.rs`, `src/scanner.rs` — MCP probe и единый scan pipeline.
- `src/security/mod.rs` — batch LLM analysis и парсинг issues.
- `rules/pre/*.yar`, `build.rs` — YARA-X rules и build-time embedding.
- `src/taxonomy.rs`, `src/sarif.rs`, `src/utils.rs` — OWASP tags и renderers.

## Алгоритм

Scanner получает tools/resources/prompts через stdio или streamable HTTP, создаёт локальное представление и прогоняет descriptions/schemas/content через YARA-X. При настроенном API key security scanner пакетно отправляет entities LLM с temperature 0,1 и извлекает typed issues; без LLM остаются YARA/structural findings. Результаты получают OWASP MCP tags и объединяются в terminal, JSON, Markdown или SARIF.

## Зависимости

Rust 2021, Tokio, RMCP, Reqwest/rustls, serde и YARA-X feature по умолчанию; LLM endpoint и credential опциональны. В workspace YARA-X закреплён на commit `664cdfe...`.

## Тесты

Inline unit tests в `src/security/mod.rs`, `src/scanner.rs` и других modules; `src/integration_tests.rs` проверяет интеграционный pipeline. GitHub Actions запускает test/lint workflows.

## Ограничения

LLM findings вероятностны и требуют внешней передачи metadata; без ключа semantic checks отсутствуют. Scanner анализирует объявленные MCP surfaces и не является proxy, который блокирует последующие вызовы.

## Вердикт

**экспериментально** — сильный multi-signal scanner для предварительного допуска, но не runtime enforcement и не полностью offline в максимальном режиме.

## Связи

- Репозиторий: [[repo-115-ramparts]]
