---
type: method
id: 10
layer: text
method-type: D
prod-viable: true
effectiveness: low
robustness: low
evidence-level: strong
status: reviewed
tags:
  - agent-security
  - even-batch
sources: []
covers:
  - LLM05
complements:
  - 12-tool-policies-yaml-rego
  - 16-ifc-capability-taint
  - 20-ghost-args-strict-typing
---

# Валидация структуры ответа (JSON / Schema)

## Определение

Проверка соответствия вывода **JSON-схеме** (типы, обязательные поля, enum, границы). Два механизма: post-model валидация (вероятностная) и constrained decoding (детерминированная форма). Смотрит форму, не семантику. Подмеханизмы: 10a валидация + 10b constrained decoding.

## Как это работает пошагово

1. Модель генерирует structured output.
2. Валидатор сверяет с JSON Schema / Pydantic (post-model) или constrained decoding ограничивает токены (at-decode).
3. При несоответствии — reject.
4. Точка врезки: egress/post-model или at-decode.

## От чего защищает

- Malformed-вывод, ломающий downstream-парсер.
- Неограниченная строка в типизированном/enum-слоте (узко LLM05).
- Constrained enum — слабая, но настоящая защита от инъекции в поле.

## От чего НЕ защищает

- Prompt injection.
- Семантически валидное-но-вредоносное значение.
- Экфильтрация через разрешённые поля.
- Злоупотребление в рамках корректной формы.

## Алгоритмы и механизмы (подробно)

- **JSON Schema** — type, properties, required, pattern, additionalProperties.
- **Pydantic V2 strict** — запрет неявного приведения типов.
- **outlines / guidance / JSON mode** — constrained decoding.

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
| ASI02 | Один опасный вызов инструмента | **ср.** | Strict typing на args; ghost args — способ №20. |
| LLM05 | Improper output handling | **ср.** | Форма вывода; семантика вне scope. |

## Оценка эффективности

**Низкая** как защита от инъекций; **высокая** как enabler для policy/IFC.

## Оценка прочности

**Низкая** — атака соблюдает схему.

## Дополняет

- способ №12 (policy engine)
- способ №16 (IFC)
- способ №19 (injection rules на args — нечётный)
- способ №20 (ghost args)

## Требует

—

## Не заменяет

Не защита — предпосылка для policy engine и валидации аргументов.

## Сценический тезис

> JSON Schema не остановит инъекцию, но без типизированного вывода нет входа для policy engine. Enum-поле — бесплатный анти-инъекционный примитив.

## Демо-кандидат

Строка в общей карте слоёв, не отдельный акт.
