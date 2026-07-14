---
type: method
id: 32
layer: supply-chain
method-type: D
prod-viable: true
effectiveness: low
robustness: low
evidence-level: strong
status: reviewed
tags:
  - agent-security
sources: []
covers:
  - ASI04
complements:
  - 26-tool-poisoning-scan
  - 28-toxic-flow-analysis
  - 40-opentelemetry-siem
---

# AIBOM / inventory

## Определение

Инвентаризация компонентов: модели, MCP-серверы, skills, plugins, конфиги — AIBOM (CycloneDX). Auto-discovery конфигов. Сам не блокирует — карта для №26/№28/аудита.

## Как это работает пошагово

1. Discovery моделей, MCP, skills в окружении.
2. Генерация AIBOM / inventory registry.
3. Обновление при изменении конфигурации.
4. pre-deploy × архитектурное свойство / офлайн.

## От чего защищает (косвенно)

- **ASI04** — visibility supply chain.

## От чего НЕ защищает

- Любую атаку напрямую.
- Устаревший BOM = ложная уверенность.

## Реализации

```dataview
TABLE verdict AS "Вердикт", repo AS "Репозиторий"
FROM "20-implementations"
WHERE method-id = this.id
SORT file.name
```

## Покрытие рисков

| Риск | Сценарий в матрице | Уровень | Почему такая оценка |
|------|--------------------|---------|---------------------|
| ASI04 | ↳ rug-pull | **выс.** | Без inventory нечего сканировать (№26). |
| ASI04 | ↳ вредонос в пакетах | **ср.** | Visibility компонентов. |

## Оценка эффективности

**Низкая** как защита; **высокая** как hygiene enabler.

## Оценка прочности

**Низкая** — shadow IT, drift без обновления.

## Дополняет

- способ №26, №28, №40

## Требует

—

## Не заменяет

Любой runtime-барьер.

## Сценический тезис

> AIBOM — SBOM для агентов: пока не знаете MCP и skills, не знаете что сканировать.

## Демо-кандидат

Строка в общей карте supply chain.
