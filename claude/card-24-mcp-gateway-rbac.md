# Карточка №24 — MCP/LLM gateway с RBAC

> Статус: **экспресс**. Слой: Сеть. Класс: **превентивный**.
> Несущее поле: **§3**. Ось §4 пинится: OWASP Agentic Top 10 **2026** / LLM Top 10 **2025**.
> Якорь: agentgateway (CEL, JWT/OIDC, multi-tenant session routing) `[док]`.

---

## 1. Идентификация и декомпозиция
**Enforcement point** на границе MCP/LLM: аутентификация (JWT/OAuth/OIDC), авторизация (CEL на claims), multi-tenant session routing, rate limits. Confused deputy на уровне gateway — сюда же.

**Развязка с №6/№23:** egress-DLP и контентная инспекция — другие классы; gateway = **кто и какой session**, не **что внутри строки**.

**Развязка с №12:** CEL на gateway (№24) vs in-process policy engine (№12).

## 2. Статус после Этапа 0
**Подтверждён** (превентивный). «Multi-tenant isolation» (VI) — сюда.

## 3. Точка врезки и режим — несущее поле
**pre-model / pre-tool-call** (граница сети) × **inline-блокировка** + архитектурное свойство (session isolation).

## 4. Модель угроз
**Закрывает:** **ASI03 Identity & Privilege Abuse** (JWT/OIDC, tenant isolation); частично **ASI07 Insecure Inter-Agent Communication** на границе; confused deputy при корректной конфигурации.

**НЕ закрывает:** prompt injection; content DLP (№6); tool policy in-process (№12); Pipelock confused deputy `[не проверено]` (#6 PARTIAL).

## 5–7, 9 — схлопнутые поля
- **§5 Обходы:** token theft; misconfigured CEL; tenant bleed при ошибке routing.
- **§6 Цена:** инфра gateway; владелец — platform/SRE.
- **§7:** agentgateway `[док]`; Pipelock proxy `[док]` без смешения с DLP.
- **§9:** запрос без valid JWT → 401; cross-tenant session → deny. Hands-on `[не выполнено]`.

## 8. Сочетаемость
Перед №12/№16 в сетевом контуре; OTel от №40 на gateway. Не дублировать №6.

## 10. Вердикт
Покрытие **M** (auth boundary), устойчивость **M**, цена **M**.
Radar: **adopt** multi-tenant MCP; **trial** single-tenant.

## 11. Сценический тезис
> «Gateway — это где вы решаете, какой tenant и какой JWT имеет право вообще подключиться к MCP-сессии. CEL на claims — это RBAC на входе, не политика на каждый tool внутри агента. Без gateway вы пытаетесь лечить confused deputy на уровне промпта.»

## 12. Кандидат в демо/пример
**Есть.** Gateway diagram: JWT → CEL allow → routed session; blocked cross-tenant.

---
*Экспресс; несущее §3; CEL здесь, не в №12.*
