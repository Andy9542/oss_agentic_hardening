---
type: implementation-detail
parent-repo: repo-115-ramparts
method-id: 27
mechanism-id: ramparts-agentskills-bundle-scan
repo: https://github.com/highflame-ai/ramparts
language: Rust
license: Apache-2.0
verdict: experimental
tags:
  - agent-security
---

# Ramparts — сканирование agentskills.io bundles

## Проверенный срез

Upstream [`8fc73b56f124e10c5f58d553573d7faf74fde133`](https://github.com/highflame-ai/ramparts/commit/8fc73b56f124e10c5f58d553573d7faf74fde133) от 2026-06-23.

## Кодовые пути

- `src/skills.rs` — frontmatter parser, discovery и skill heuristics.
- `rules/pre/*.yar` — prompt injection, Unicode, credential и payload signatures.
- `tests/fixtures/agentskills/my-skill/` — bundle fixture с `SKILL.md`, script и reference.
- `src/main.rs`, `src/utils.rs` — CLI и отчёты.

## Алгоритм

Парсер принимает skill file или auto-discovered roots, отделяет YAML frontmatter и превращает body в synthetic MCP prompt для общего YARA/LLM pipeline. Дополнительно проверяются `allowed-tools`, vague/generic triggers, name collisions, sensitive `@path` references и payload blobs. Для точного `SKILL.md` scanner проходит на один уровень `scripts/` и `references/` с лимитом 256 файлов на каталог, YARA-сканирует содержимое и валидирует имя/поля спецификации.

## Зависимости

Rust binary с serde_yaml, regex и YARA-X; LLM опционален. Дополнительных interpreters для bundled scripts не требуется, поскольку они не исполняются.

## Тесты

Fixture `tests/fixtures/agentskills/my-skill/` и unit tests внутри `src/skills.rs` проверяют parsing, grants, embedded payloads, collisions, bundle validation и discovery roots.

## Ограничения

Bundle walk ограничен одним уровнем, числом и размером файлов; binaries и глубоко вложенные payloads могут быть пропущены. Эвристики frontmatter не доказывают вредоносность, а LLM-фаза зависит от provider.

## Вердикт

**экспериментально** — конкретная реализация pre-install проверки skill bundle, но покрытие ограничено статически доступными файлами и известными шаблонами.

## Связи

- Репозиторий: [[repo-115-ramparts]]
