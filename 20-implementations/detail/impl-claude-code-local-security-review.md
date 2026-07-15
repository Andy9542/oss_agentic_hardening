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

# Claude Code Security Review — локальная команда

## Код и тесты

- Код: `.claude/commands/security-review.md`, `claudecode/prompts.py`, `claudecode/audit.py`.
- Тесты: `claudecode/test_prompts.py`, `claudecode/test_main_function.py`, `claudecode/test_integration.py`.

## Алгоритм

1. Пользователь запускает `/security-review` в доверенной локальной checkout.
2. Команда собирает diff и направляет его в тот же класс audit prompt.
3. Модель возвращает приоритизированные security findings.
4. Разработчик проверяет рекомендации до merge.

## Зависимости

Установленный Claude Code, локальный Git checkout и доступ модели к анализируемому коду.

## Ограничения

Локальный запуск не создаёт обязательного merge gate и наследует вероятностность модели. Результат зависит от выбранного diff и полноты доступного контекста.

## Вердикт

**prod только для trusted PR/advisory** — удобный advisory-вариант способа №30 для доверенной рабочей копии; не механизм enforcement.

## Связи

- Репозиторий: [[repo-114-claude-code-security-review]]
