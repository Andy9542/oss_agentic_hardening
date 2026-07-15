---
type: implementation
method-id: 15
repo: "https://github.com/agent-defense/parallax"
language: "Rust"
license: "Apache-2.0"
verdict: экспериментально
tags:
  - agent-security
  - review-2026
  - runtime-policy
---

# Parallax — out-of-band policy engine для событий агента

## Репозиторий

https://github.com/agent-defense/parallax

## Где в коде

- `parallax.yaml` — inline evaluators и политика.
- `rules/` — библиотека правил по движкам.
- `docs/ARCHITECTURE.md` — evaluator chain и short-circuit.
- `docs/RULES.md` — формат правил.
- `integrations/openclaw` и `docs/integrations/` — хуки OpenClaw, Claude Code и Codex.

## Алгоритм

1. Интеграция отправляет события `message.before`, `params.before`, `tool.before` и `tool.after` во внешний сервис.
2. Движки выполняются от дешёвых к дорогим и завершаются сразу при `block`.
3. Regex и pattern ловят локальные сигнатуры; Sigma сопоставляет события; CEL проверяет поля.
4. SQL evaluator хранит состояние в SQLite и выявляет частоту, последовательности и временные паттерны.
5. Итог агрегируется по приоритету `block > redact > detect > allow`.
6. Решение и причины попадают в audit log/webhook.

## Детерминизм или машинное обучение

Полностью детерминированный reference-monitor слой: regex, keyword, Sigma, CEL и SQL. LLM не участвует в решении.

## Внешние зависимости

Один Rust binary и HTTP/CLI hooks. Правила локальны. Интеграции требуют поддержки lifecycle hooks; часть интеграций заявлена в roadmap.

## Сигналы качества

- Тесты в репозитории: README указывает 45 Rust-тестов.
- Документированные обходы: правила покрывают только известные поля/паттерны; корректность зависит от полноты событий и невозможности обойти hook.
- Зрелость: версия README 0.2.0, hot reload и UI ещё в roadmap.

## Вердикт

**экспериментально** — архитектурно сильный out-of-band reference monitor, но ранняя версия и неполная интеграционная поверхность не позволяют считать его зрелым production barrier.

## Связи

- Способ: [[15-правила-последовательности-вызовов-и-потоков-данных]]
