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

# Claude Code Security Review — PR audit workflow

## Код и тесты

- Код: `action.yml`, `claudecode/github_action_audit.py`, `claudecode/prompts.py`.
- Тесты: `claudecode/test_github_action_audit.py`, `claudecode/test_workflow_integration.py`, `.github/workflows/test-claudecode.yml`.

## Алгоритм

1. GitHub Action получает diff и контекст изменённых файлов.
2. Audit prompt просит Claude Code искать exploitable data flow и control flow.
3. Ответ разбирается в findings с расположением, severity и remediation.
4. Workflow публикует результат в PR и при настройке сохраняет артефакт.

## Зависимости

GitHub Actions, Claude Code, Claude API key, Python dependencies из `claudecode/requirements.txt` и разрешение на PR comments.

## Ограничения

Анализ вероятностный и не доказывает отсутствие уязвимостей. Код и текст PR попадают в model context; недоверенный diff может содержать prompt injection.

## Вердикт

**prod только для trusted PR/advisory** — основной механизм способа №30 применим после approval gate и как дополнение, а не замена SAST и human review.

## Связи

- Репозиторий: [[repo-114-claude-code-security-review]]
