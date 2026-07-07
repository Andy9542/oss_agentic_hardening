# Карточка №34 — OS-level sandbox (OpenShell)

> Статус: **полная**. Слой: Инфра. Класс: **превентивный (архитектурный)**.
> Несущее поле: **§4+§5**. Ось §4 пинится: OWASP Agentic Top 10 **2026** / LLM Top 10 **2025**.
> Якорь: NVIDIA OpenShell `[проверено]` существование; defenseclaw→OpenShell `[не проверено]` (#4 OPEN).

---

## 1. Идентификация и декомпозиция
**Изоляция на уровне ОС:** hardware-enforced network / FS / syscall policy. OpenShell = NVIDIA. Граница: №33 microVM/container — гранулярность; №35 rings — не OS isolation (V3.8).

Escape-поверхность — несущее §5.

## 2. Статус после Этапа 0
**Подтверждён** (архитектурный превентивный). Атрибуция OpenShell=NVIDIA исправлена.

## 3. Точка врезки и режим
**pre-tool-call** (исполнение в sandbox) × **архитектурное свойство** + inline syscall/network block.

## 4. Модель угроз

**Закрывает:**
- **ASI05 Unexpected Code Execution** — containment escape attempts.
- **ASI02** — ограничение side-effects tool (FS, network).
- Частично **ASI08** — изоляция сбоев.

**НЕ закрывает:** prompt injection; data exfil через **разрешённые** egress channels; sandbox escape 0-days; логику агента вне sandbox.

## 5. Обходы и слепые зоны — несущее поле

- **Over-permissive egress** — sandbox есть, но сеть открыта.
- **DNS-туннелирование / side channels** — эмпирика Docker-sandbox (Habr).
- **Shared kernel** vs hardware-enforced — разная сила гарантии.
- **Integration gaps** — defenseclaw→OpenShell не подтверждена.

## 6. Цена эксплуатации

- Смена runtime architecture; latency; ops complexity.
- Владелец — platform/infra.

## 7. Реализации

| Реализация | Статус |
|---|---|
| NVIDIA OpenShell | `[проверено]` существование |
| defenseclaw integration | `[не проверено]` #4 OPEN |
| E2B / Firecracker (№33 контекст) | `[док]` смежный |

## 8. Сочетаемость

Комплемент №12/№16 in-process; sandbox — последняя физическая граница. Демо-потенциал: DNS/FS/syscall trace.

## 9. Проверочный протокол

- Попытка `curl attacker.com` из sandbox → block.
- Обход: exfil через разрешённый webhook.
- **Статус:** `[не выполнено]`.

## 10. Вердикт

| Ось | Оценка |
|---|---|
| Покрытие (containment) | **H** |
| Устойчивость | **M** |
| Цена | **H** |

**Radar:** `assess` OpenShell; `trial` container sandboxes.

## 11. Сценический тезис

> «OS-level sandbox — последний рубеж: даже если политика и IFC проспали, агент не должен иметь syscall и сеть всей машины. OpenShell обещает hardware-enforced границы — но egress policy внутри sandbox всё равно ваша ответственность.»

## 12. Кандидат в демо/пример

**Есть (сильный).** DNS/FS/syscall trace; попытка escape → deny.

---
*Полная; escape §5; defenseclaw caveat.*
