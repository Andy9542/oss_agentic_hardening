---
type: method
id: 30
layer: code
method-type: S
prod-viable: true
effectiveness: medium
robustness: low
evidence-level: strong
status: reviewed
tags:
  - agent-security
  - even-batch
sources: []
covers:
  - ASI05
  - LLM05
  - ASI04
---

# Static analysis кода

## Определение

Статический анализ **генерируемого/исполняемого кода**: уязвимости, опасные паттерны (Semgrep), regex в CodeShield. Объект — исходный код, не metadata tools (№26).

## Как это работает пошагово

1. Coding agent генерирует код.
2. Semgrep/CodeShield сканирует перед исполнением или в CI.
3. При finding — block или flag.
4. egress / post-model × inline или CI.

## От чего защищает

- **ASI05** RCE.
- **LLM05** improper output handling для кода.
- Частично **ASI04** в сгенерированном коде skills.

## От чего НЕ защищает

- Prompt injection; tool metadata poisoning (№26).
- Runtime-only exploits.

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
| ASI05 | Побег из песочницы / RCE | **ср.** | Статика опасных паттернов; не runtime sandbox. |
| ASI04 | ↳ вредонос в пакетах | **ср.** | Код в supply chain artifacts. |

## Оценка эффективности

**Средняя** для coding agents.

## Оценка прочности

**Низкая** — обфускация, novel vuln.

## Дополняет

- способ №26 (metadata)
- способ №28 (flows)

## Требует

—

## Не заменяет

- способ №42 (execution rails)

## Сценический тезис

> CodeShield и Semgrep смотрят на код, который агент собирается выполнить — не на description инструмента.

## Демо-кандидат

Snippet с `os.system` → Semgrep finding block.
