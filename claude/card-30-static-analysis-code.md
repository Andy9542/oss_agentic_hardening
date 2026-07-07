# Карточка №30 — Static analysis кода

> Статус: **экспресс**. Слой: Код. Класс: **детективный**.
> Несущее поле: **§4**. Ось §4 пинится: OWASP Agentic Top 10 **2026** / LLM Top 10 **2025**.
> Якорь: CodeShield (LlamaFirewall) `[док]`; Semgrep `[док]`.

---

## 1. Идентификация и декомпозиция
Статический анализ **генерируемого или исполняемого кода** агента: уязвимости, опасные паттерны (Semgrep rules), regex в CodeShield. Объект — **исходный код**, не metadata tools (№26).

**Исключение:** Cisco mcp/a2a-сканеры → **№26**, не сюда (правка V2).

## 2. Статус после Этапа 0
**Подтверждён** (детективный).

## 3. Точка врезки × режим
**egress / post-model** (код от coding agent) × **inline-блокировка** или off-band в CI.

## 4. Модель угроз — несущее поле
**Закрывает:** **ASI05 Unexpected Code Execution (RCE)**; **LLM05 Improper Output Handling** для кода; частично **ASI04** в сгенерированном коде skills.

**НЕ закрывает:** prompt injection; tool metadata poisoning (№26); runtime-only exploits без статического следа.

## 5–7, 9 — схлопнутые поля
- **§5 Обходы:** обфускация; код без срабатывания правил; novel vuln без сигнатуры.
- **§6 Цена:** Semgrep CI latency; владелец — rule packs.
- **§7:** CodeShield (LlamaFirewall) `[док]`; Semgrep `[док]`.
- **§9:** сгенерировать `eval(user_input)` → finding. Hands-on `[не выполнено]`.

## 8. Сочетаемость
Для coding agents; комплемент №26 (metadata) и №28 (flows). Не путать с №42 execution rails.

## 10. Вердикт
Покрытие **M** (известные паттерны), устойчивость **L**, цена **M**.
Radar: **adopt** coding agents; **hold** general agents без кода.

## 11. Сценический тезис
> «CodeShield и Semgrep смотрят на то, что агент собирается выполнить как код — не на то, что написано в description инструмента. Для coding agents это must-have; для email-агента без кода — irrelevant.»

## 12. Кандидат в демо/пример
**Есть (короткий).** Snippet с `os.system` → Semgrep finding block.

---
*Экспресс; Cisco MCP scanners → №26.*
