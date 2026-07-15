---
type: implementation-detail
parent-repo: repo-54-sandboxai
method-id: 33
repo: https://github.com/substratusai/sandboxai
language: Go/Python
license: Apache-2.0
verdict: experimental
commit-sha: 606cdc0
commit-date: 2025-02-05
verified-date: 2026-07-15
tags:
  - agent-security
---

# SandboxAI — API песочницы для agent code exec

## Репозиторий

- [substratusai/sandboxai](https://github.com/substratusai/sandboxai)
- Проверенный срез: `606cdc0`; код проверен 2026-07-15.

## Что это за технология

**SandboxAI**: сервис/API для безопасного выполнения кода, порождаемого LLM/агентом — изолированные среды вместо local exec. Способ №33.

## Где в коде

- README quickstart; server/SDK packages
- Container-backed execution

## Алгоритм

1. Клиент создает sandbox / box id.
2. Send code/command → remote isolated runner.
3. Capture stdout/stderr/files.
4. Teardown.

## Примеры реализации

Agent tool `run_python` → HTTP to SandboxAI → container exec → result JSON.

## Пример: вход → решение

- Malicious `os.system('curl …')` ограничен сетью/политикой sandbox.
- Host FS не смонтирован → нет чтения `~/.ssh`.

## Детерминизм или машинное обучение

**Детерминированная** изоляция.

## Внешние зависимости

SandboxAI server + container runtime.

## Ограничения

- Нужен деплой сервиса.
- Политика сети по умолчанию проверить.

## Сигналы качества

- Substratus; compact focused repo.

## Вердикт

**экспериментально** — простой sandbox API.

## Связи

- Репозиторий: [[repo-54-sandboxai]]
