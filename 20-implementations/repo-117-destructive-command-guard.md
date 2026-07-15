---
type: repo-catalog
catalog-id: 117
method-id: 19
also-method-ids:
  - 30
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
  - repo-catalog
  - savedtg
  - review-2026
clusters:
  - cluster-runtime-hooks
  - cluster-static-code-sast
---

# Dicklesworthstone/destructive_command_guard — каталог №117

## Репозиторий

[Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard)

Проверенная ревизия: `80969f63` от 2026-07-15.

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3 |
| Тип | Детерминированный runtime hook и scanner |
| Семейства | [[cluster-runtime-hooks]], [[cluster-static-code-sast]] |

## Принцип работы

`dcg` перехватывает shell-команду coding-агента до исполнения, нормализует и классифицирует контекст, применяет allowlist и security packs, затем возвращает allow или deny с объяснением. Отдельный scan mode проверяет исполняемые фрагменты в репозитории.

## Алгоритм

1. Адаптер hook-протокола извлекает команду из события агента.
2. Нормализация, контекстный анализ и heredoc/inline-script pipeline выделяют исполняемые фрагменты.
3. Allowlist отсекает разрешённые формы, после чего packs сопоставляют опасные операции.
4. Совпадение формирует запрет, идентификатор правила и безопасную альтернативу.
5. Ошибка или превышение hook deadline приводит к fail-open; `DCG_BYPASS=1` явно отключает защиту.

Основной механизм — **способ №19**; scan mode дополнительно реализует способ №30.

## Вариант в семействе

Локальный guardrail для нескольких coding-agent hook-протоколов. Вариант ориентирован на известные опасные shell-формы и не заменяет sandbox или policy enforcement для прямых API/tool-вызовов.

## Лицензионный статус

Лицензия обозначена upstream как `MIT with OpenAI/Anthropic rider`. Дополнительное ограничение делает проект source-available, но не OSI-approved OSS; перед использованием требуется отдельная юридическая проверка.

## Вердикт

**experimental security boundary** — полезен как defense-in-depth, но fail-open, явный bypass и неполное покрытие путей исполнения не позволяют считать `dcg` самостоятельной границей безопасности.

## Детальные разборы

- [[impl-destructive-command-guard]]
- [[impl-destructive-command-guard-heredoc]]
- [[impl-destructive-command-guard-scan]]

## Реализуемые способы

- [[19-правила-против-инъекций-в-аргументах-инструментов]] — основной
- [[30-static-analysis-code]]
