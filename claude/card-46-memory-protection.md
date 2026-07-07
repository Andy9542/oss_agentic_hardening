# Карточка №46* — Защита памяти агента

> Статус: **полная**. Слой: Память / RAG. Класс: **превентивный/детективный**.
> Несущее поле: **§4**. Ось §4 пинится: OWASP Agentic Top 10 **2026** / LLM Top 10 **2025**.
> Якорь: ASI06 Memory & Context Poisoning `[проверено]` stage0; AgentPoison arXiv:2407.12784 `[проверено 2026-07-08]`; Progent на AgentPoison `[проверено]` handoff.

---

## 1. Идентификация и декомпозиция

Защита **долговременной памяти агента** и **RAG knowledge base**: валидация записей, provenance, anti-poisoning при retrieve, TTL/верификация источников. Крупнейший пробел V5 — вне периметра №16 (пофлоу одной сессии).

**Подмеханизмы:**
- **Pre-write validation** — проверка перед записью в memory store.
- **Retrieval-time filtering** — score/trust при retrieve из RAG.
- **Provenance / TTL** — метаданные источника, срок жизни записи.

**Граница с context poisoning:** in-session in-context PI — №1/№16; **persistent** store — №46*.

## 2. Статус после Этапа 0
**Добавлен** (решение B6). Нумерация со звёздочкой — вне исходных 45.

## 3. Точка врезки и режим
- **pre-write** (перед commit в memory) × inline-блокировка.
- **retrieval-time** (при RAG retrieve) × inline-блокировка / off-band score.
- **pre-deploy** (provenance policy) × архитектурное свойство.

## 4. Модель угроз — несущее поле

**Закрывает:**
- **ASI06 Memory & Context Poisoning** — отравленные записи в long-term memory / RAG KB.
- **LLM04 Data and Model Poisoning** (компонент KB poisoning).
- Backdoor через trigger в memory (класс атак AgentPoison [1]).

**НЕ закрывает:**
- **In-session PI** без персистентной записи (№1, №16).
- **Poison ниже детекционного порога** — AgentPoison <0.1% ratio [1].
- **Runtime tool misuse** без опоры на poisoned memory (№12).
- **Model training poisoning** — вне скоупа (model-level исключён).

## 5. Обходы и слепые зоны

- **Stealthy triggers** — optimized embedding triggers (AgentPoison) обходят naive filters [1].
- **Slow poisoning** — мало записей за длительный период.
- **Benign-looking poison** — семантически нормальный текст с backdoor trigger.

## 6. Цена эксплуатации

- Latency на retrieve validation; хранилище provenance metadata.
- Владелец — data governance + security; живая политика trust sources.
- Trade-off utility vs paranoia на retrieve.

## 7. Реализации со статусом проверки

| Реализация | Что даёт | Статус |
|---|---|---|
| AgentPoison (attack benchmark) | ASR >80%, poison <0.1% [1] | `[проверено 2026-07-08]` arXiv:2407.12784 |
| Progent | Тестируется на AgentPoison | `[проверено]` handoff |
| Production memory guards | Зрелые OSS-реализации | `[не проверено]` — класс в формировании |

## 8. Сочетаемость

- **Не заменяет №16** — session IFC vs persistent memory.
- **Комплемент №32** — inventory знает, какие KB подключены.
- **№44** — red-team на memory poisoning (AgentPoison-style probes).

## 9. Проверочный протокол

- **Каноничная атака:** poisoned RAG entry с trigger → retrieve → adversarial action (AgentPoison template).
- **Обход:** poison без trigger в query — depends on retrieval design.
- **Статус:** `[не выполнено]` → experiments-todo.

## 10. Вердикт

| Ось | Оценка | Обоснование |
|---|---|---|
| Покрытие ASI06 | **M** | Класс определён; prod митигации слабы |
| Устойчивость | **L** | AgentPoison показывает обход naive defenses [1] |
| Цена | **M** | Provenance на каждую запись |

**Radar:** `assess` — критический пробел; `trial` point solutions.

## 11. Сценический тезис

> «Память агента — это доверенная база, пока кто-то не положил туда 0.1% poisoned записей с триггером. AgentPoison показал 80%+ success при почти невидимом poison rate — IFC одной сессии это не видит. ASI06 существует именно потому, что persistent store — новый периметр.»

## 12. Кандидат в демо/пример

**Есть (сильный).** Poisoned memory entry → benign queries OK → query с trigger → retrieve poison → wrong tool action.

---
*Полная карточка нового класса; ASI06; AgentPoison arXiv:2407.12784.*
