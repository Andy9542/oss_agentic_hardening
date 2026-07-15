---
type: implementation-detail
parent-repo: repo-46-invariant
method-id: 15
repo: https://github.com/invariantlabs-ai/invariant
language: Python
license: Apache-2.0
verdict: experimental
commit-sha: 2340fe2
commit-date: 2026-01-12
verified-date: 2026-07-15
tags:
  - agent-security
---

# Invariant Guardrails — правила потоков tool→tool

## Репозиторий

- [invariantlabs-ai/invariant](https://github.com/invariantlabs-ai/invariant)
- Проверенный срез: `2340fe2`, дата коммита 2026-01-12; код проверен 2026-07-15.

## Что это за технология

**Rule-based guardrails** с Python-подобным DSL: правила матчят сообщения и **последовательности tool calls** (`(call: ToolCall) -> (call2: ToolCall)`). Это способ №15 (правила последовательности вызовов): ловят toxic flows вроде «прочитай inbox → отправь на внешний email», которые поодиночке выглядят легитимно.

Развёртывается как MCP/LLM proxy без правок агента.

## Где в коде

- Пакет `invariant/`
- Примеры правил в README
- Docs: invariantlabs guardrails reference (внешний)

## Алгоритм

1. Записать guardrail rules (raise "…" if: …).
2. Proxy видит stream messages / tool calls.
3. Pattern-match события на переменные правил (`msg`, `call`, `call2`).
4. Условия как Python-выражения + библиотека предикатов (`is tool:send_email({to: regex})`).
5. Match → raise/block запрос к LLM или MCP.

## Примеры реализации

```python
raise "External email to unknown address" if:
    (call: ToolCall) -> (call2: ToolCall)
    call is tool:get_inbox
    call2 is tool:send_email({
      to: ".*@[^ourcompany.com$].*"
    })
```

Простое content-правило:

```python
raise "The one who must not be named" if:
    (msg: Message)
    "voldemort" in msg.content.lower() or "tom riddle" in msg.content.lower()
```

## Пример: вход → решение

- Flow `get_inbox` → `send_email(to=attacker@evil.com)` → raise block.
- `get_inbox` → `send_email(to=user@ourcompany.com)` → allow (regex domain).

## Детерминизм или машинное обучение

**Детерминированный** matching DSL (если без ML-предикатов).

## Внешние зависимости

Python package; proxy deployment.

## Ограничения

- Нужно покрыть toxic flows правилами вручную.
- Regex в условиях хрупки к обфускации адресов.

## Сигналы качества

- Публичная документация Invariant Labs; ясный DSL.

## Вердикт

**экспериментально** — сильная идея flow rules; внедрение = качество правил.

## Связи

- Репозиторий: [[repo-46-invariant]]
