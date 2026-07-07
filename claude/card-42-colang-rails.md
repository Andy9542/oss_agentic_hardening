# Карточка №42 — Rails (Colang)

> Статус: **полная**. Слой: Диалог. Класс: **превентивный**.
> Несущее поле: **§1**. Ось §4 пинится: OWASP Agentic Top 10 **2026** / LLM Top 10 **2025**.
> Якорь: NeMo Guardrails + ActiveFence `[док]`.

---

## 1. Идентификация и декомпозиция — несущее поле

**Ядро класса (уникальное):**
- **Dialog rails** — управление диалоговым потоком (Colang).
- **Canonical form matching** — сопоставление с каноническими формами намерений.

**Не дублировать (перекрёстные ссылки):**
- Input rails → **№1** (PI-детект).
- Output rails → **№8** (модерация).
- Execution rails → **№12** (политики на tools).

Сужение V3.7: класс не «все rails», а dialog + canonical form.

## 2. Статус после Этапа 0
**Сужен** (V3.7). Превентивный; декомпозиция — несущая.

## 3. Точка врезки и режим
**pre-model / CoT** (диалоговый план) × **inline-блокировка** + архитектурное свойство (dialog state machine).

## 4. Модель угроз

**Закрывает:**
- **ASI09 Human–Agent Trust Exploitation** — off-topic / manipulative dialog paths.
- Частично **ASI01** — удержание в допустимом dialog flow.

**НЕ закрывает:** tool misuse (№12); data-flow (№16); сложный PI вне dialog patterns.

## 5. Обходы и слепые зоны

- **Неполный Colang coverage** — novel intents проходят.
- **Dual-use phrases** — формально каноничные, семантически вредные.

## 6. Цена эксплуатации

- Владелец Colang-сценариев; поддержка canonical forms при новых use cases.

## 7. Реализации

| Реализация | Статус |
|---|---|
| NeMo Guardrails | `[док]` |
| ActiveFence integration | `[док]` |

## 8. Сочетаемость

Оркестрирует №1/№8/№12, не заменяет. Dialog layer над текстом и действием.

## 9. Проверочный протокол

- Off-topic manipulative dialog → rail block.
- Обход: intent, формально matching canonical form.
- **Статус:** `[не выполнено]`.

## 10. Вердикт

| Ось | Оценка |
|---|---|
| Покрытие (dialog hijack) | **M** |
| Устойчивость | **M** |
| Цена | **M** |

**Radar:** `trial` dialog-heavy agents; `hold` tool-only agents.

## 11. Сценический тезис

> «Colang rails — это не ещё один фильтр токсичности. Уникальное ядро — dialog flow и canonical forms: агент остаётся в коридоре намерений. Input/output/execution rails — соседи по пайплайну, не клоны №1 и №8.»

## 12. Кандидат в демо/пример

**Есть.** Colang path diagram: user intent → canonical match → allowed branch vs blocked off-topic.

---
*Полная; несущее §1; сужение V3.7.*
