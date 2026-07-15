---
type: implementation-detail
parent-repo: repo-05-nomos
method-id: 14
repo: https://github.com/safe-agentic-world/nomos
language: Go
license: Apache-2.0
verdict: experimental
commit-sha: de46088
commit-date: 2026-05-13
verified-date: 2026-07-15
tags:
  - agent-security
---

# Nomos — YAML ALLOW/DENY/REQUIRE_APPROVAL на действиях

## Репозиторий

- [safe-agentic-world/nomos](https://github.com/safe-agentic-world/nomos)
- Проверенный срез: `de46088`, дата коммита 2026-05-13; код проверен 2026-07-15.

## Что это за технология

**Policy PDP для действий агента** (fs.read/write, process.exec, repo.apply_patch): правила в YAML с `decision: ALLOW|DENY` (и approval в расширенных профилях). Совпадение по `action_type` + glob `resource` + опционально `exec_match.argv_patterns`. Это способ №14: default-deny через явные правила, без ML.

## Где в коде

- Примеры политик: `examples/policies/safe.yaml`, `base.yaml`, `purchase.yaml`, `mcp-gateway.example.yaml`
- CLI: `cmd/nomos/`
- HTTP SDK examples: `examples/http-sdk/`

## Алгоритм

1. Загрузить набор rules (id, action_type, resource, decision, obligations?).
2. Агент запрашивает действие (например `fs.read` на `file://workspace/.env`).
3. Сопоставить resource glob и action_type; для exec — argv patterns (`["git","push","**"]`).
4. Первое/приоритетное DENY побеждает; ALLOW может нести obligations (`sandbox_mode: local`).
5. Вернуть решение клиенту (LangChain/HTTP tool wrapper).

## Примеры реализации

Из `examples/policies/safe.yaml`:

```yaml
- id: safe-deny-root-env
  action_type: fs.read
  resource: file://workspace/.env
  decision: DENY
- id: safe-deny-nested-env
  action_type: fs.read
  resource: file://workspace/**/.env
  decision: DENY
- id: safe-deny-git-push
  action_type: process.exec
  resource: file://workspace/
  decision: DENY
  exec_match:
    argv_patterns:
      - ["git", "push", "**"]
      - ["git", "push"]
- id: safe-allow-git-exec
  action_type: process.exec
  decision: ALLOW
  exec_match:
    argv_patterns: [["git", "**"], ["git"]]
  obligations: { sandbox_mode: local }
```

## Пример: вход → решение

- `fs.read` → `file://workspace/.env` → DENY.
- `fs.read` → `file://workspace/README.md` → ALLOW (`safe-read-workspace`).
- `process.exec` argv `git push origin main` → DENY.

## Детерминизм или машинное обучение

**Детерминированный**.

## Внешние зависимости

Go-бинарник Nomos; без GPU.

## Ограничения

- Нужна интеграция: агент обязан спрашивать Nomos до действия.
- Порядок/перекрытие rules нужно проектировать осторожно.

## Сигналы качества

- Примеры политик + CI smoke; DESIGN_NOTES.md.

## Вердикт

**экспериментально** — ясный YAML PDP для coding-agent actions.

## Связи

- Репозиторий: [[repo-05-nomos]]
