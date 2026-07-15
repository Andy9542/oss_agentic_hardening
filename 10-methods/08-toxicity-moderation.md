---
type: method
id: 8
layer: text
method-type: V
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
  - LLM05
---

# Фильтры токсичности / модерация

## Определение

Классификаторы/LLM-судьи над вводом и выводом на **недопустимость контента**: toxicity, hate, harassment, sexual, self-harm, illicit. Объект — вредоносность контента, не механика атаки. Не PI (способ №1), не secrets/DLP (способ №6/№3).

## Как это работает пошагово

1. Ввод и/или вывод проходит классификатор.
2. При превышении порога — блок или флаг.
3. Двусторонняя модерация: pre-model + egress/post-model.
4. Inline-блокировка / off-band-флаг.

## От чего защищает

- Генерация/пропуск недопустимого контента (toxicity, hate, harassment, sexual, self-harm).
- Jailbreak, проявившийся как токсичный вывод.

## От чего НЕ защищает

- Prompt injection и goal hijack («вежливая» атака проходит).
- Всё agentic (маршрут данных, tool misuse).
- Обход классификатора адверсариал-перефразом.

## Алгоритмы и механизмы (подробно)

- **llm-guard** — Toxicity, BanTopics, NoRefusal.
- **NeMo Guardrails** — self-check.
- **ActiveFence** — enterprise moderation.

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
| LLM05 | Вредный/токсичный контент | **ср.** | Прямой домен content safety, не agentic attacks. |

## Оценка эффективности

**Средняя** для safety/compliance; **низкая** для agentic-угроз.

## Оценка прочности

**Низкая** — адверсариал-перефраз, «нетоксичная» по форме вредоносная семантика.

## Дополняет

- способ №4 (нормализация)

## Требует

—

## Не заменяет

- способ №1 (prompt injection)
- способ №16 (IFC)

## Сценический тезис

> Модерация — гигиена контента, не защита агента; пропускает вежливую экфильтрацию. В реестр агентных защит — только с ярлыком «другой домен».

## Демо-кандидат

Вежливая экфильтрация проходит №8, падает на IFC №16 (в связке с №16).
