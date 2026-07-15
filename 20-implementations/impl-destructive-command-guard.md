---
type: implementation
method-id: 19
repo: "https://github.com/Dicklesworthstone/destructive_command_guard"
language: "Rust"
license: "MIT with OpenAI/Anthropic rider"
verdict: экспериментально
tags:
  - agent-security
  - savedtg
  - runtime
---

# destructive_command_guard — блокировка опасных команд coding-агентов

## Репозиторий

https://github.com/Dicklesworthstone/destructive_command_guard

## Где в коде

- `src/` — CLI, hook-протоколы и движок правил.
- `examples/packs/` и `docs/packs/` — модульные наборы правил и конфигурация.
- `tests/` и `fuzz/` — тесты протоколов, паттернов и fuzzing.
- `agent_baseline/` — базовые профили агентов.
- `action/` — интеграция с GitHub Actions.

## Алгоритм

1. Hook получает команду от coding-агента до исполнения.
2. Команда нормализуется и разбирается с учётом shell-контекста, heredoc и inline-скриптов.
3. Allowlist отделяет известные безопасные формы; контекстный анализ различает исполняемую команду и строку данных.
4. Активные security packs сопоставляют команду с правилами для Git, файловой системы, БД, контейнеров, Kubernetes, облаков и IaC.
5. При совпадении hook возвращает запрет, причину и безопасную альтернативу; режим `scan` применяет правила в CI.

## Детерминизм или машинное обучение

Детерминированный Rust-движок: парсинг, allowlist и правила. LLM для решения не используется.

## Внешние зависимости

Локальный бинарник и hook-механизм конкретного coding-агента. Специализированные packs сверх базового ядра включаются конфигурацией.

## Сигналы качества

- Большой набор тестов, fuzzing, CI и версионированные releases.
- Документированы allow-once, постоянный allowlist и явный bypass через `DCG_BYPASS=1`.
- Fail-open при ошибках и неполное покрытие прямых API/tool-вызовов не позволяют считать инструмент жёсткой security boundary.
- Лицензионный rider ограничивает круг получателей прав и требует отдельной проверки.

## Вердикт

**экспериментально** как элемент agent-hardening: полезный и зрелый guardrail от известных разрушительных shell-команд, но не замена sandbox, default-deny policy и approval для необратимых действий.

## Связи

- Способ: [[19-правила-против-инъекций-в-аргументах-инструментов]]
- Источник: [[source-destructive-command-guard]]
