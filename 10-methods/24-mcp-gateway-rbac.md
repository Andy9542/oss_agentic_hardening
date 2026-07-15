---
type: method
id: 24
layer: network
method-type: D
prod-viable: true
effectiveness: medium
robustness: medium
evidence-level: strong
status: reviewed
tags:
  - agent-security
  - even-batch
sources: []
covers:
  - ASI03
  - ASI07
---

# MCP/LLM gateway с RBAC

## Определение

Enforcement point на границе MCP/LLM: auth (JWT/OAuth/OIDC), authz (CEL на claims), multi-tenant session routing, rate limits. CEL на gateway vs in-process policy (№12) — разные точки врезки.

## Как это работает пошагово

1. Клиент подключается к gateway с JWT.
2. CEL-политика проверяет claims и tenant.
3. Session routing изолирует tenants.
4. pre-model / network boundary × inline block.

## От чего защищает

- **ASI03** — JWT/OIDC, tenant isolation.
- Частично **ASI07** на границе.
- Confused deputy при корректной конфигурации.

## От чего НЕ защищает

- Prompt injection; content DLP (№6).
- Tool policy in-process (№12).

## Реализации

```dataview
TABLE verdict AS "Вердикт", repo AS "Репозиторий"
FROM "20-implementations"
WHERE type = "repo-catalog" AND (method-id = this.id OR contains(also-method-ids, this.id))
SORT catalog-id ASC
```

## Покрытие рисков

| Риск | Сценарий в матрице | Уровень | Почему такая оценка |
|------|--------------------|---------|---------------------|
| ASI02 | ↳ SSRF через tool | **выс.** | Сетевая граница и egress policy на gateway. |
| ASI03 | Эскалация привилегий | **ср.** | RBAC на входе в MCP-сессию. |
| ASI07 | Межагентная связь | **ср.** | Tenant isolation на границе. |

## Оценка эффективности

**Средняя** — adopt для multi-tenant MCP.

## Оценка прочности

**Средняя** — token theft, misconfigured CEL.

## Дополняет

- способ №12 (in-process policy)
- способ №40 (OTel на gateway)

## Требует

—

## Не заменяет

- способ №6 (egress-DLP)

## Сценический тезис

> Gateway решает, какой tenant и JWT имеет право подключиться к MCP-сессии; CEL на claims — RBAC на входе, не политика на каждый tool внутри агента.

## Демо-кандидат

JWT → CEL allow → routed session; blocked cross-tenant.
