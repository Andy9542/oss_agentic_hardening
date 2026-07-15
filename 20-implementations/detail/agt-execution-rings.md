---
type: implementation-detail
parent-repo: repo-01-agent-governance-toolkit
method-id: 35
repo: https://github.com/microsoft/agent-governance-toolkit
language: Go
license: MIT
verdict: prod
commit-sha: 789963c
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# AGT — уровни исполнения (execution rings)

## Репозиторий

- [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit)
- Проверенный срез: `789963c`, дата коммита 2026-07-15; код проверен 2026-07-15.

## Что это за технология

**Execution rings** — модель привилегий как у колец защиты CPU (ring 0…3): каждому агенту назначается кольцо, каждому кольцу — список разрешённых действий (`data.read`, `system.shutdown`, …). Запрос действия проверяется через `CheckAccess(agent, action)` без LLM. Это способ №35 (уровни исполнения): least privilege на уровне identity агента.

## Где в коде

- API: `agent-governance-golang/packages/agentmesh/rings.go` (`NewRingEnforcer`, `Assign`, `CheckAccess`, `SetRingPermissions`)
- Пример: `agent-governance-golang/examples/execution-rings/main.go` + `README.md`

## Алгоритм

1. Создать `RingEnforcer`.
2. Назначить permissions кольцам: Admin=`*`, Standard=`data.read+write`, Restricted=`data.read`, Sandboxed=`[]`.
3. `Assign(agentID, ring)`.
4. На tool/action: `CheckAccess(agent, action)` → bool.
5. Агент без кольца → **deny by default**.

## Примеры реализации

```go
enforcer.SetRingPermissions(agentmesh.RingAdmin, []string{"*"})
enforcer.SetRingPermissions(agentmesh.RingStandard, []string{"data.read", "data.write"})
enforcer.SetRingPermissions(agentmesh.RingRestricted, []string{"data.read"})
enforcer.SetRingPermissions(agentmesh.RingSandboxed, []string{})
enforcer.Assign("readonly-agent", agentmesh.RingRestricted)
enforcer.CheckAccess("readonly-agent", "data.write") // false
```

Ожидаемая сетка из README: admin — всё true; sandboxed — всё false; unassigned — всё false.

## Пример: вход → решение

- `worker-agent` + `data.write` → allow (RingStandard).
- `readonly-agent` + `system.shutdown` → deny.
- `unassigned-agent` + `data.read` → deny.

## Детерминизм или машинное обучение

Полностью **детерминированный**.

## Внешние зависимости

Go SDK agentmesh; без GPU. Политики могут дополняться YAML/OPA в соседних примерах.

## Ограничения

- Кольца не заменяют аргументную валидацию и sandbox OS.
- Нужно явно маппить domain-actions на строки permissions.

## Сигналы качества

- Официальный example + expected output; часть Microsoft AGT.

## Вердикт

**готово к продакшену** — ясная least-privilege модель для multi-agent.

## Связи

- Репозиторий: [[repo-01-agent-governance-toolkit]]
