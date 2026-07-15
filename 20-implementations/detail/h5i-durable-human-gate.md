---
type: implementation-detail
parent-repo: repo-111-h5i
method-id: 21
repo: https://github.com/h5i-dev/h5i
language: Rust
license: Apache-2.0
verdict: экспериментально
commit-sha: c33cf7308169b95b6e68464e74b693bde7b60b9d
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# h5i — durable human и peer review gates

## Проверенная ревизия

`c33cf7308169b95b6e68464e74b693bde7b60b9d`, дата коммита 2026-07-15; код проверен 2026-07-15.

## Где в коде

- Код: `crates/h5i-core/src/team.rs`, orchestration CLI `h5i team`, журналы submissions/reviews в `refs/h5i/*`.
- Тесты: `tests/cli_integration.rs`, сценарии review → verify → finalize → apply.

## Алгоритм

1. Несколько агентов работают в отдельных worktree и фиксируют кандидатов как Git-объекты.
2. Кандидаты проходят взаимный peer review; замечания могут запускать пересборку.
3. Независимая команда verify воспроизводит проверки, например `pytest`, и записывает evidence.
4. Finalize выбирает объяснимый результат; apply переносит в целевую ветку только кандидата, прошедшего gates.
5. Журналы submissions, reviews и durable gates остаются в Git-хранилище `refs/h5i/*`.

## Зависимости

Rust CLI, Git и установленные agent runtimes. SaaS не требуется. Сила gate зависит от того, что verify реально проверяет в профиле.

## Ограничения

Peer review и summaries создаются LLM и остаются вероятностными. Gate не заменяет OS confinement: без сильного isolation tier это supervised workflow, а не security boundary. Apply требует явного шага; обход возможен, если оператор применяет изменения вне `h5i`.

## Вердикт

**экспериментально** — полезная реализация способа №21 для coding-агентов с воспроизводимым evidence trail, но молодой проект и зависимость от внешнего verify.

## Связи

- Репозиторий: [[repo-111-h5i]]
