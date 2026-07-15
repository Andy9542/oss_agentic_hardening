---
type: implementation-detail
parent-repo: repo-117-destructive-command-guard
method-id: 30
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
---

# destructive_command_guard — repository scan

## Код и тесты

- Код: `src/scan.rs`, `src/sarif.rs`, `action/action.yml`.
- Тесты: `tests/scan_extractor_integration.rs`, `tests/scan_extractor_docs.rs`, `tests/golden_json_tests.rs`.

## Алгоритм

1. `dcg scan` выбирает staged files, paths или Git diff.
2. Форматные extractors находят только исполняемые фрагменты в shell, workflow, Dockerfile, package scripts и других поддерживаемых файлах.
3. Извлечённые команды проходят тот же evaluator и packs, что и runtime hook.
4. Findings выводятся для CI, включая структурированный или SARIF-формат.

## Зависимости

Git checkout, включённые security packs и extractor для конкретного формата файла; для CI используется action или локальный бинарник.

## Ограничения

Scanner не является general-purpose SAST: он не строит межпроцедурный data flow и пропускает команды, сформированные динамически или в неподдерживаемом формате. Allowlist и неполный набор packs уменьшают покрытие.

## Вердикт

**experimental security boundary** — отдельная реализация способа №30 для опасных команд в репозитории, полезная как CI-check, но не замена полноценному SAST.

## Связи

- Репозиторий: [[repo-117-destructive-command-guard]]
