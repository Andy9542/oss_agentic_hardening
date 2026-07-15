---
type: implementation
method-id: 30
repo: "https://github.com/anthropics/claude-code-security-review"
language: "Python / GitHub Actions"
license: "MIT"
verdict: готово к продакшену
tags:
  - agent-security
  - review-2026
  - code-review
---

# Claude Code Security Reviewer — LLM security review для pull request

## Репозиторий

https://github.com/anthropics/claude-code-security-review

## Где в коде

- GitHub Action workflow — запуск на PR.
- `claudecode/prompts.py` — audit prompt templates.
- `claudecode/findings_filter.py` — фильтрация false positives.
- `claudecode/claude_api_client.py` — второй вызов модели для filtering.
- `claudecode/evals/` — evaluation tooling.
- `.claude/commands/security-review.md` — локальная `/security-review` команда.

## Алгоритм

1. Action извлекает diff и контекст изменённых файлов.
2. Claude Code анализирует semantic intent и опасные data/control flows.
3. Findings получают описание, severity и remediation.
4. Отдельный filtering pass удаляет низкоценные и вероятные false positives.
5. Action публикует PR comment и машинные outputs; инструкции можно дополнить политиками организации.
6. Та же логика доступна локально через `/security-review`.

## Детерминизм или машинное обучение

Анализ и filtering выполняются LLM и вероятностны. Workflow, ограничение diff и формат результатов детерминированы.

## Внешние зависимости

GitHub Actions, Claude API key с доступом к Claude Code; для локального режима нужен Claude Code. Код PR передаётся модели согласно выбранной конфигурации.

## Сигналы качества

- Тесты в репозитории: `pytest claudecode -v`, eval framework на PR.
- Документированные обходы: README прямо предупреждает, что action не hardened против prompt injection и должен запускаться только после approval внешнего PR.
- Зрелость: официальный проект Anthropic, понятная CI-интеграция; не заменяет классический SAST и review.

## Вердикт

**готово к продакшену** — готов для production-процесса на доверенных изменениях при approval gate; небезопасен как автоматический scanner недоверенного PR-контента.

## Связи

- Способ: [[30-static-analysis-code]]
