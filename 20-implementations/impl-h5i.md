---
type: implementation
method-id: 35
repo: "https://github.com/h5i-dev/h5i"
language: "Rust"
license: "Apache-2.0"
verdict: экспериментально
tags:
  - agent-security
  - review-2026
  - sandbox
---

# h5i — аудируемые рабочие области coding-агентов

## Репозиторий

https://github.com/h5i-dev/h5i

## Где в коде

- CLI `h5i env` — создание и управление рабочими областями.
- `h5i team` — orchestration, verify, finalize и apply.
- `refs/h5i/*` — Git-хранилище prompts, context и evidence.
- `docs/` — профили окружений, командная работа и аудит.

## Алгоритм

1. Для каждого агента создаёт отдельную Git worktree и environment profile.
2. Записывает prompt, команды, tool output, policies и reviews как Git-объекты.
3. Несколько агентов работают изолированно от файлов и веток друг друга.
4. Кандидаты взаимно рецензируются и могут пересобираться после замечаний.
5. Независимая команда verify воспроизводит проверки, например `pytest`.
6. Finalize выбирает объяснимый результат; apply переносит только прошедшего gates кандидата.

## Детерминизм или машинное обучение

Создание worktree, журналирование, replay, gates и merge детерминированы. Код и peer review создаются LLM-агентами и остаются вероятностными.

## Внешние зависимости

Rust CLI, Git и установленные agent runtimes (Claude Code, Codex и др.). Данные хранятся локально в Git; SaaS не требуется. Сила sandbox зависит от выбранного environment profile.

## Сигналы качества

- Тесты в репозитории: GitHub Actions и документированный verify flow.
- Документированные обходы: worktree предотвращает конфликты, но сама по себе не является OS security boundary; профиль должен отдельно ограничивать сеть, процессы и host FS.
- Зрелость: удобная модель evidence-in-repo, но молодой проект и сильные claims об изоляции нуждаются в threat-model review.

## Вердикт

**экспериментально** — полезный слой воспроизводимости и supervised execution; считать его containment можно только после проверки конкретного sandbox-профиля.

## Связи

- Способ: [[35-уровни-исполнения-и-изоляция-рабочего-каталога]]
