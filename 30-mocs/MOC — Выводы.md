# Выводы по чётным способам защиты

Синтез настольного исследования по 23 способам (22 чётных + №46*). Подробности — в `10-methods/`.

## Лидеры по эффективности и прочности

| Способ | Эффект. | Прочн. | Почему |
|--------|---------|--------|--------|
| [[12-tool-policies-yaml-rego]] | высокая | средняя | Enterprise policy на tool-call; Progent SMT на обновления |
| [[16-ifc-capability-taint]] | высокая | средняя | Доказуемая гарантия на data-flow exfil (CaMeL); цена архитектуры |
| [[26-tool-poisoning-scan]] | высокая | средняя | Rug-pull, shadowing в metadata MCP |
| [[28-toxic-flow-analysis]] | высокая | средняя | Статика lethal trifecta до рантайма |
| [[34-os-sandbox-openshell]] | высокая | средняя | Последний рубеж containment |
| [[14-default-deny-allowlists]] | средняя | средняя | Обязательный baseline слоя «Действие» |

## Средний уровень (полезны с оговорками)

| Способ | Оговорка |
|--------|----------|
| [[02-cot-reasoning-audit]] | Только видимый в CoT; unfaithful reasoning |
| [[06-content-dlp-inspection]] | Обход дроблением/перефразом |
| [[08-toxicity-moderation]] | Content safety, не agentic attacks |
| [[18-rebac-spicedb]] | Права в графе, не data-flow |
| [[24-mcp-gateway-rbac]] | Граница сети, не in-process policy |
| [[36-crypto-agent-identity]] | Multi-agent mesh; не PI |
| [[42-colang-dialog-rails]] | Dialog-heavy агенты |
| [[46-memory-protection]] | Критический пробел; prod-зрелость низкая |

## Поддерживающий слой (enablers)

| Способ | Роль |
|--------|------|
| [[04-unicode-normalization]] | Гигиена для текстовых детекторов |
| [[10-json-schema-constrained]] | Вход для policy и ghost args |
| [[20-ghost-args-strict-typing]] | Гигиена typed tool-calling |
| [[32-aibom-inventory]] | Карта для №26/№28 |

## Аудит / тесты / реактивные (не prod-барьеры)

| Способ | Вердикт |
|--------|---------|
| [[40-opentelemetry-siem]] | **Только аудит** — обязателен, но не блокирует |
| [[38-skill-attribution]] | Форензика при OTel |
| [[44-red-team-regression]] | **Мета** — CI mirror, не runtime |
| [[22-kill-switch-circuit-breaker]] | Страховка после факта / по порогу |

## Открытые factcheck

См. `experiments/factcheck-todo.md`: agent-airlock (#1), defenseclaw↔OpenShell (#4), Pipelock (#6), AGT Flight Recorder (#7), backend sensitivity №2.

## Связь с нечётными способами

Полный стек 45+1 методов требует merge с веткой `odd_protections`. Перекрёстные ссылки на нечётные номера — текстом «способ №N», без wikilink ([[Правила связей]]).
