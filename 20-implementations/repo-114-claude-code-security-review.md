---
type: repo-catalog
catalog-id: 114
method-id: 30
repo: https://github.com/anthropics/claude-code-security-review
language: Python
license: MIT
verdict: prod
upstream-sha: 0c6a49f1
upstream-date: 2026-02-11
tags:
  - agent-security
  - repo-catalog
  - review-2026
clusters:
  - cluster-static-code-sast
  - cluster-content-guardrails-ml
---

# anthropics/claude-code-security-review — каталог №114

## Репозиторий

[anthropics/claude-code-security-review](https://github.com/anthropics/claude-code-security-review)

Проверенная ревизия: `0c6a49f1` от 2026-02-11.

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 2 |
| Тип | Вероятностный статический анализ |
| Семейства | [[cluster-static-code-sast]], [[cluster-content-guardrails-ml]] |

## Принцип работы

GitHub Action передаёт Claude Code diff и ограниченный контекст pull request, получает security findings, выполняет отдельный LLM-проход фильтрации и публикует результат в PR.

## Алгоритм

1. Workflow извлекает изменённые файлы и diff.
2. Audit prompt направляет модель на уязвимые data flow и control flow.
3. Находки нормализуются в структурированный результат.
4. Второй проход и жёсткие правила исключения снижают число ложных срабатываний.
5. Action публикует комментарий и артефакт; тот же prompt доступен локальной командой.

Основной и единственный сопоставленный механизм — **способ №30**.

## Вариант в семействе

LLM-рецензент анализирует семантику diff, а не только синтаксические шаблоны SAST. Цена этого варианта — вероятностность и восприимчивость audit context к prompt injection.

## Вердикт

**prod только для trusted PR/advisory** — пригоден как рекомендательный этап для доверенных изменений после approval gate. Автоматический запуск на недоверенном PR-контенте не образует безопасную production boundary.

## Детальные разборы

- [[impl-claude-code-security-review]]
- [[impl-claude-code-findings-filter]]
- [[impl-claude-code-local-security-review]]

## Реализуемые способы

- [[30-static-analysis-code]] — основной
