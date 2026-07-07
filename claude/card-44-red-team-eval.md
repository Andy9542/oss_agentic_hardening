# Карточка №44 — Red team probes + regression eval

> Статус: **экспресс**. Слой: Тесты. Класс: **тестовый, не prod-защита** (понижен V4).
> Несущее поле: **§8**. Ось §4 пинится: OWASP Agentic Top 10 **2026** / LLM Top 10 **2025**.
> Якорь: garak, promptfoo, PyRIT `[док]`; garak+YARA **снято** `[не найдено 2026-07-07]`.

---

## 1. Идентификация и декомпозиция
**Тестовый контур:** адверсариал-пробы (garak), regression eval (promptfoo), automation (PyRIT). Закрывает петлю обратной связи для всех остальных классов — **не барьер в prod**.

**Не включать:** garak+YARA (CLOSED-NEG #3). garak = probes/detectors/evaluators.

AgentDojo — №45 (не наш); дедуп Invariant линия.

## 2. Статус после Этапа 0
**Понижен** (V4): тестовый класс.

## 3. Точка врезки × режим
**офлайн-тест** / CI × **off-band** (не inline).

## 4. Модель угроз (мета)
**Закрывает:** пробелы в покрытии других классов — **до prod**, если CI gate enforced.

**НЕ закрывает:** runtime атаки; не заменяет №1–№40.

## 5–7, 9 — схлопнутые поля
- **§5:** stale probes; green CI на narrow suite.
- **§6:** CI time; probe maintenance.
- **§7:** garak (NVIDIA) `[док]`; promptfoo `[док]`; PyRIT `[док]`.
- **§9:** новый jailbreak → regression fails until fix. Hands-on `[не выполнено]`.

## 8. Сочетаемость — несущее поле
Петля для всего реестра; без regression защиты деградируют silently.

## 10. Вердикт
Покрытие **H** (как test process), **L** (как runtime defense), устойчивость **M**, цена **M**.
Radar: **adopt** CI red-team; **hold** as only security.

## 11. Сценический тезис
> «Red team в CI — это не защита, это зеркало: garak и promptfoo показывают, что сломается завтра, а не блокируют сегодня. Связку garak+YARA мы сняли — YARA у garak нет. Без regression gate весь ваш стек — вера.»

## 12. Кандидат в демо/пример
**Есть.** CI regression gate: probe suite red → merge blocked.

---
*Экспресс тестовый; garak+YARA снято.*
