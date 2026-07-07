# Карточка №26 — Tool poisoning / shadowing scan

> Статус: **полная**. Слой: Supply chain. Класс: **детективный**.
> Несущее поле: **§4**. Ось §4 пинится: OWASP Agentic Top 10 **2026** / LLM Top 10 **2025**.
> Якорь: Invariant tool poisoning / rug-pull `[проверено]`; snyk agent-scan (mcp-scan) `[проверено]`.

---

## 1. Идентификация и декомпозиция

Скан **метаданных инструментов** (не содержимого skills/артефактов — то №27): descriptions в tools/list, имена, shadowing, unsafe command definitions, rug-pull (смена описания после install).

**Граница A4=a:** объект = metadata tools/list; «PI в skills» → №27.

**Термины Invariant:** tool poisoning, rug-pull — `[проверено]`.

## 2. Статус после Этапа 0
**Подтверждён** (детективный). agentseal = **сканер, не подпись** (factcheck #5 CLOSED).

## 3. Точка врезки и режим
**pre-deploy** + **post-factum** (watch) × **off-band-детекция** / офлайн-тест (CI, SARIF).

## 4. Модель угроз — несущее поле

**Закрывает:**
- **ASI04 Agentic Supply Chain Vulnerabilities** — отравленные descriptions, shadowing.
- **LLM03 Supply Chain** — компрометация tool metadata.
- Частично **LLM01** — indirect PI через tool description.

**НЕ закрывает:**
- **Содержимое** skill-файлов, кода, RAG-документов (№27, №30).
- **Рантайм-подмену** после прохождения скана (rug-pull между сканами — нужен watch).
- **Криптоподпись** — agentseal не подписывает артефакты.

## 5. Обходы и слепые зоны

- **Rug-pull между сканами** — description меняется после baseline.
- **Семантически невинное** описание с вредоносным эффектом при вызове.
- **Локальные tools** вне CI-скана.

## 6. Цена эксплуатации

- CI-интеграция; владелец — security pipeline.
- Watch-режим (agentseal) — операционный оверхед.

## 7. Реализации со статусом проверки

| Реализация | Что даёт | Статус |
|---|---|---|
| snyk agent-scan / mcp-scan | Tool metadata poisoning | `[проверено]` |
| defenseclaw / Cisco scanners | MCP/A2A metadata | `[проверено]` существование |
| getagentseal/agentseal (~292★) | Скан skills/MCP, rug-pull, shadowing, XFLOW, SARIF; **без подписи** | `[проверено 2026-07-07]` |
| AGT mcp-scan | Упом. в AGT | `[док]` |

## 8. Сочетаемость

- **Субстрат №32** — inventory/AIBOM даёт список артефактов для скана.
- **Не №30** — static code analysis кода, не metadata.
- **Дополняет №28** — metadata vs flow-граф.

## 9. Проверочный протокол

- **Каноничная атака:** tool description с hidden instruction «ignore previous…» → detect в diff с baseline.
- **Обход:** poison только в runtime response tools/list без сохранения.
- **Статус:** `[не выполнено]`.

## 10. Вердикт

| Ось | Оценка | Обоснование |
|---|---|---|
| Покрытие (supply chain metadata) | **H** | Прямой класс ASI04 |
| Устойчивость | **M** | Rug-pull, обход CI |
| Цена | **L** | Офлайн/CI |

**Radar:** `adopt` в MCP onboarding; `trial` без watch.

## 11. Сценический тезис

> «Tool poisoning — это когда вредоносность сидит не в коде, а в описании инструмента, которое модель читает при выборе action. Rug-pull — когда описание меняется после того, как вы один раз сказали „ок“. Сканер ловит diff; watch ловит смену; подпись артефактов — другой класс, и agentseal её не даёт.»

## 12. Кандидат в демо/пример

**Есть.** Side-by-side: benign description → malicious description после update; diff подсвечен scanner.

---
*Полная карточка; agentseal без подписи; граница metadata vs content.*
