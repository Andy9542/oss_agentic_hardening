# MOC — Чётные способы защиты

Тег `even-batch`. Нечётные способы (№1, 3 … 45) — в ветке `odd_protections`.

**№46*** — расширение набора (защита памяти / RAG), вне исходных 45 пунктов.

## Текст

| № | Способ | Класс | Эффект. | Прочн. |
|---|--------|-------|---------|--------|
| 2 | [[02-cot-reasoning-audit\|CoT-аудит]] | детективный | ср. | низ. |
| 4 | [[04-unicode-normalization\|Unicode]] | поддерживающий | низ. | низ. |
| 6 | [[06-content-dlp-inspection\|DLP]] | детективный | ср. | низ. |
| 8 | [[08-toxicity-moderation\|Модерация]] | детективный | ср. | низ. |
| 10 | [[10-json-schema-constrained\|JSON Schema]] | поддерживающий | низ. | низ. |

## Действие

| № | Способ | Класс | Эффект. | Прочн. |
|---|--------|-------|---------|--------|
| 12 | [[12-tool-policies-yaml-rego\|Политики tools]] | превентивный | выс. | ср. |
| 14 | [[14-default-deny-allowlists\|Default-deny]] | превентивный | ср. | ср. |
| 16 | [[16-ifc-capability-taint\|IFC / taint]] | превентивный | выс. | ср. |
| 18 | [[18-rebac-spicedb\|ReBAC]] | превентивный | ср. | ср. |
| 20 | [[20-ghost-args-strict-typing\|Ghost args]] | превентивный | низ. | низ. |
| 22 | [[22-kill-switch-circuit-breaker\|Kill switch / breaker]] | реактивный | низ. | ср. |

## Сеть / Supply chain / Код

| № | Способ | Класс | Эффект. | Прочн. |
|---|--------|-------|---------|--------|
| 24 | [[24-mcp-gateway-rbac\|MCP gateway]] | превентивный | ср. | ср. |
| 26 | [[26-tool-poisoning-scan\|Tool poisoning scan]] | детективный | выс. | ср. |
| 28 | [[28-toxic-flow-analysis\|Toxic flow]] | детективный | выс. | ср. |
| 30 | [[30-static-analysis-code\|Static analysis]] | детективный | ср. | низ. |
| 32 | [[32-aibom-inventory\|AIBOM]] | поддерживающий | низ. | низ. |

## Инфра / Идентичность / Поведение / Аудит / Диалог / Тесты / Память

| № | Способ | Класс | Эффект. | Прочн. |
|---|--------|-------|---------|--------|
| 34 | [[34-os-sandbox-openshell\|OS sandbox]] | превентивный | выс. | ср. |
| 36 | [[36-crypto-agent-identity\|Crypto identity]] | превентивный | ср. | ср. |
| 38 | [[38-skill-attribution\|Skill attribution]] | детективный | низ. | ср. |
| 40 | [[40-opentelemetry-siem\|OTel / SIEM]] | аудит | низ. | низ. |
| 42 | [[42-colang-dialog-rails\|Colang rails]] | превентивный | ср. | ср. |
| 44 | [[44-red-team-regression\|Red team CI]] | тестовый | выс.* | ср. |
| 46* | [[46-memory-protection\|Защита памяти]] | прев./детект. | ср. | низ. |

\* №44 — высокая эффективность **процесса тестирования**, не runtime-защиты.

## Чеклист

См. `even-methods-checklist.md` в корне репозитория — 23/23 `[x]`.
