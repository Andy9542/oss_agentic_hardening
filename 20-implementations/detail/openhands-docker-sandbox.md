---
type: implementation-detail
parent-repo: repo-55-openhands
method-id: 33
repo: https://github.com/All-Hands-AI/OpenHands
language: Python
license: MIT
verdict: prod
commit-sha: 9c5d4dc
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# OpenHands — DockerSandboxService для coding agent

## Репозиторий

- [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands)
- Проверенный срез: `9c5d4dc`; код проверен 2026-07-15.

## Что это за технология

Полноценный coding agent; security-релевантная часть — **sandbox layer**: `DockerSandboxService` / `SandboxService` поднимают контейнер на conversation, ограничивая shell/file tools агента. Способ №33.

## Где в коде

- `openhands/app_server/sandbox/docker_sandbox_service.py`
- `sandbox_service.py`, `sandbox_models.py`, `sandbox_spec_service.py`
- Wired in `live_status_app_conversation_service.py`

## Алгоритм

1. New conversation → allocate sandbox (Docker) per grouping strategy.
2. Agent actions (bash/edit) → execute inside sandbox.
3. Poll startup; enforce max conversations per sandbox.
4. Resume/stop via `/api/v1/sandboxes/…`.

## Примеры реализации

```python
from openhands.app_server.sandbox.docker_sandbox_service import DockerSandboxService
# LiveStatusAppConversationService.sandbox_service: SandboxService
# sandbox_startup_timeout, max_num_conversations_per_sandbox
```

## Пример: вход → решение

- Agent `pip install` / shell — только в container FS.
- Host repo optionally mounted read/write per spec — не весь `$HOME`.

## Детерминизм или машинное обучение

Изоляция **детерминированная**; агент — LLM.

## Внешние зависимости

Docker; OpenHands stack; LLM keys.

## Ограничения

- Продукт шире sandbox; конфиг mounts критичен.
- Не заменяет content injection filters.

## Сигналы качества

- Широко используемый OSS agent; активная разработка.

## Вердикт

**готово к продакшену** как agent+sandbox platform (при правильной конфигурации).

## Связи

- Репозиторий: [[repo-55-openhands]]
