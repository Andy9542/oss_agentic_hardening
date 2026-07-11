---
type: source
tags:
  - framework
---

# OWASP ASI Top 10

## Суть

Инициатива **OWASP Agentic AI Security** — десять главных рисков для **агентных** систем (редакция 2026).

## URL

https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

## Ключевые выводы

- Каркас для способ №41 и [[MOC — Матрица угроз]]
- **Сопоставление** контролей с чеклистом ≠ их реальная реализация в продакшене
- Фокус на **действиях** агента (tools, память, цепочки), а не только на тексте модели

## ASI01–ASI10 (2026)

| Код | English | Русский | Заметка |
|-----|---------|---------|---------|
| ASI01 | Agent Goal Hijack | Захват цели агента | [[ASI01-agent-goal-hijack]] |
| ASI02 | Tool Misuse and Exploitation | Злоупотребление и эксплуатация инструментов | [[ASI02-tool-misuse]] |
| ASI03 | Identity and Privilege Abuse | Злоупотребление идентичностью и привилегиями | [[ASI03-identity-privilege-abuse]] |
| ASI04 | Agentic Supply Chain Vulnerabilities | Уязвимости цепочки поставок агентных систем | [[ASI04-agentic-supply-chain]] |
| ASI05 | Unexpected Code Execution | Неожиданное исполнение кода | [[ASI05-unexpected-code-execution]] |
| ASI06 | Memory and Context Poisoning | Отравление памяти и контекста | [[ASI06-memory-context-poisoning]] |
| ASI07 | Insecure Inter-Agent Communication | Небезопасная связь между агентами | [[ASI07-insecure-inter-agent-communication]] |
| ASI08 | Cascading Failures | Каскадные сбои | [[ASI08-cascading-failures]] |
| ASI09 | Human-Agent Trust Exploitation | Эксплуатация доверия человека к агенту | [[ASI09-human-agent-trust-exploitation]] |
| ASI10 | Rogue Agents | Вредоносные (rogue) агенты | [[ASI10-rogue-agents]] |

Дополнительные сценарии vault — префикс **EXT-***. Пересечения LLM ↔ ASI — в [[MOC — Матрица угроз#ASI и LLM: кто с кем пересекается]].

## Связи

- [[41-сопоставление-защит-с-требованиями-стандартов]]
- [[source-owasp-llm-top10]]
- [[MOC — Матрица угроз]]
- [[source-owasp-agentic-2026]] — заметка чётной ветки о том же стандарте
