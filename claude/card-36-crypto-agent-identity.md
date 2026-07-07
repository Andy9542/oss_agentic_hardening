# Карточка №36 — Crypto agent identity + A2A trust

> Статус: **экспресс**. Слой: Идентичность. Класс: **превентивный**.
> Несущее поле: **§4**. Ось §4 пинится: OWASP Agentic Top 10 **2026** / LLM Top 10 **2025**.
> Якорь: Microsoft AGT AgentMesh blog 02.04.2026 `[проверено]` — DID+Ed25519, IATP (Signal X3DH+Double Ratchet), trust score 0–1000.

---

## 1. Идентификация и декомпозиция
Криптографическая **идентичность агента** и **доверие agent-to-agent**: DID, Ed25519, IATP на Signal protocol, trust score / decay. **Не cloud IAM** (V5.7 вне скоупа).

## 2. Статус после Этапа 0
**Подтверждён** (превентивный).

## 3. Точка врезки × режим
**pre-tool-call** (межагентные сообщения) × **inline-блокировка** при низком trust.

## 4. Модель угроз — несущее поле
**Закрывает:** **ASI07 Insecure Inter-Agent Communication**; **ASI03** при spoofing агента; частично **ASI10** rogue agents.

**НЕ закрывает:** prompt injection; compromised legitimate agent; cloud IAM путаница.

## 5–7, 9 — схлопнутые поля
- **§5:** stolen keys; trust score gaming; downgrade attacks.
- **§6:** key management; trust policy owner.
- **§7:** AGT AgentMesh `[проверено 2026-07-06]` blog.
- **§9:** untrusted agent handshake → reject. Hands-on `[не выполнено]`.

## 8. Сочетаемость
Комплемент №24 gateway auth; не №18 ReBAC (другой слой).

## 10. Вердикт
Покрытие **M**, устойчивость **M**, цена **H**.
Radar: **trial** multi-agent; **hold** single agent.

## 11. Сценический тезис
> «Crypto identity — это паспорт агента в mesh: Ed25519, trust score, decay. Это не замена IAM облака и не ловит prompt injection — это ответ на вопрос „этот агент вообще тот, за кого себя выдаёт“.»

## 12. Кандидат в демо/пример
**Есть.** Trust handshake diagram; score drop → block.

---
*Экспресс; не cloud IAM.*
