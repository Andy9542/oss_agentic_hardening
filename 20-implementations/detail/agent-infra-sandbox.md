---
type: implementation-detail
parent-repo: repo-52-sandbox
method-id: 33
repo: https://github.com/agent-infra/sandbox
language: TypeScript/Go
license: Apache-2.0
verdict: experimental
commit-sha: f2ebdba
commit-date: 2026-07-03
verified-date: 2026-07-15
tags:
  - agent-security
---

# agent-infra/sandbox — изолированный runtime для агентов

## Репозиторий

- [agent-infra/sandbox](https://github.com/agent-infra/sandbox)
- Проверенный срез: `f2ebdba`; код проверен 2026-07-15.

## Что это за технология

**Sandbox infrastructure** для выполнения кода/инструментов агента вне хоста: контейнерная изоляция, ограниченная сеть/FS. Способ №33.

## Где в коде

- README architecture; service packages under repo tree
- Docker-oriented runtime APIs

## Алгоритм

1. Создать sandbox session для агента.
2. Выполнять commands/files внутри изоляции.
3. Network/FS limits по политике sandbox.
4. Destroy/timeout session.

## Примеры реализации

Агент не получает raw host shell: tool `exec` → sandbox API → container → stdout обратно агенту.

## Пример: вход → решение

- `rm -rf /` в sandbox → ущерб только ephemeral FS.
- Host secrets вне mount → недоступны.

## Детерминизм или машинное обучение

**Детерминированная** изоляция.

## Внешние зависимости

Docker/container runtime.

## Ограничения

- Не microVM по умолчанию (зависит от backend).
- Misconfigured mounts ломают модель угроз.

## Сигналы качества

- Active 2026 commits; infra-focused repo size.

## Вердикт

**экспериментально** — agent sandbox building block.

## Связи

- Репозиторий: [[repo-52-sandbox]]
