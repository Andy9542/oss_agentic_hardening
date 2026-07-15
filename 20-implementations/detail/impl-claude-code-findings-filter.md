---
type: implementation-detail
parent-repo: repo-114-claude-code-security-review
method-id: 30
repo: https://github.com/anthropics/claude-code-security-review
language: Python
license: MIT
verdict: prod
upstream-sha: 0c6a49f1
upstream-date: 2026-02-11
tags:
  - agent-security
---

# Claude Code Security Review — фильтрация findings

## Код и тесты

- Код: `claudecode/findings_filter.py`, `claudecode/claude_api_client.py`, `docs/custom-filtering-instructions.md`.
- Тесты: `claudecode/test_findings_conversion.py`, `claudecode/test_hard_exclusion_rules.py`, `claudecode/test_claude_runner.py`.

## Алгоритм

1. Первичные findings преобразуются в единый формат.
2. Жёсткие exclusion rules удаляют заведомо нерелевантные категории.
3. Отдельный модельный вызов оценивает exploitability и ложные срабатывания.
4. Пользовательские filtering instructions уточняют политику проекта.

## Зависимости

Claude API client, дополнительный model call и корректный структурированный вывод первичного аудита.

## Ограничения

Второй LLM-проход может удалить истинную находку или сохранить ложную. Пользовательские инструкции также входят в prompt context и требуют контроля изменений.

## Вердикт

**prod только для trusted PR/advisory** — самостоятельный механизм повышения signal-to-noise для способа №30, но не независимая проверка истинности findings.

## Связи

- Репозиторий: [[repo-114-claude-code-security-review]]
