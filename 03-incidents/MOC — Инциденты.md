---
type: moc
tags:
  - agent-security
  - incidents
  - risks
---

# MOC — Инциденты

Каталог связывает публично подтверждаемые события с карточками OWASP ASI 2026 и LLM 2025 из 05-risks. Это evidence layer, а не утверждение, что каждый случай полностью совпадает с формальным сценарием OWASP.

## Правила отбора

- Для каждого риска — не более двух инцидентов.
- Cross-link допустим: один инцидент может показывать несколько рисков одной exploit chain.
- Подтверждённый operational incident отделён от vulnerability disclosure без известной эксплуатации.
- Для каждого события дана первичная или официальная ссылка и, где возможно, независимое подтверждение.
- Лабораторные PoC без production-компонента в этот каталог не включены.

## Инциденты

| Дата | Карточка | Тип доказательства | Риски |
|------|----------|--------------------|-------|
| 2026-01-31 | [[incident-moltbook-agent-database-exposure]] | раскрытие и подтверждённый доступ, исправлено | ASI03, ASI07, ASI10, LLM02 |
| 2025-07-18 | [[incident-replit-production-database-deletion]] | production incident, данные восстановлены | ASI02, ASI05, ASI08, ASI09, ASI10, LLM06, LLM09 |
| 2025-07-09 | [[incident-mcp-remote-rce-cve-2025-6514]] | CVE, нет известной эксплуатации | ASI04, ASI05, LLM03 |
| 2025-06-11 | [[incident-echoleak-m365-copilot]] | CVE/exploit chain, нет подтверждённого customer breach | ASI01, ASI02, ASI06, LLM01, LLM02, LLM05, LLM06, LLM08 |
| 2024-12-05 | [[incident-ultralytics-pypi-compromise]] | supply-chain incident | ASI04, LLM03 |
| 2024-02-14 | [[incident-air-canada-chatbot-hallucination]] | судебно подтверждённое последствие | ASI09, LLM09 |
| 2023-11-08 | [[incident-openai-ddos-outage-2023]] | подтверждённый service incident | LLM10 |
| 2023-02-08 | [[incident-bing-sydney-prompt-leak]] | подтверждённое production-preview behavior | LLM01, LLM07 |
| 2016-03-24 | [[incident-microsoft-tay-poisoning]] | production incident | ASI06, LLM04 |

## Покрытие рисков и контроль лимита

| Риск | Связанные инциденты | Количество |
|------|---------------------|------------|
| [[ASI01-agent-goal-hijack]] | [[incident-echoleak-m365-copilot]] | 1 |
| [[ASI02-tool-misuse]] | [[incident-echoleak-m365-copilot]], [[incident-replit-production-database-deletion]] | 2 |
| [[ASI03-identity-privilege-abuse]] | [[incident-moltbook-agent-database-exposure]] | 1 |
| [[ASI04-agentic-supply-chain]] | [[incident-mcp-remote-rce-cve-2025-6514]], [[incident-ultralytics-pypi-compromise]] | 2 |
| [[ASI05-unexpected-code-execution]] | [[incident-mcp-remote-rce-cve-2025-6514]], [[incident-replit-production-database-deletion]] | 2 |
| [[ASI06-memory-context-poisoning]] | [[incident-echoleak-m365-copilot]], [[incident-microsoft-tay-poisoning]] | 2 |
| [[ASI07-insecure-inter-agent-communication]] | [[incident-moltbook-agent-database-exposure]] | 1 |
| [[ASI08-cascading-failures]] | [[incident-replit-production-database-deletion]] | 1 |
| [[ASI09-human-agent-trust-exploitation]] | [[incident-replit-production-database-deletion]], [[incident-air-canada-chatbot-hallucination]] | 2 |
| [[ASI10-rogue-agents]] | [[incident-replit-production-database-deletion]], [[incident-moltbook-agent-database-exposure]] | 2 |
| [[LLM01-prompt-injection]] | [[incident-echoleak-m365-copilot]], [[incident-bing-sydney-prompt-leak]] | 2 |
| [[LLM02-sensitive-information-disclosure]] | [[incident-echoleak-m365-copilot]], [[incident-moltbook-agent-database-exposure]] | 2 |
| [[LLM03-supply-chain]] | [[incident-mcp-remote-rce-cve-2025-6514]], [[incident-ultralytics-pypi-compromise]] | 2 |
| [[LLM04-data-model-poisoning]] | [[incident-microsoft-tay-poisoning]] | 1 |
| [[LLM05-improper-output-handling]] | [[incident-echoleak-m365-copilot]] | 1 |
| [[LLM06-excessive-agency]] | [[incident-echoleak-m365-copilot]], [[incident-replit-production-database-deletion]] | 2 |
| [[LLM07-system-prompt-leakage]] | [[incident-bing-sydney-prompt-leak]] | 1 |
| [[LLM08-vector-embedding-weaknesses]] | [[incident-echoleak-m365-copilot]] | 1 |
| [[LLM09-misinformation]] | [[incident-replit-production-database-deletion]], [[incident-air-canada-chatbot-hallucination]] | 2 |
| [[LLM10-unbounded-consumption]] | [[incident-openai-ddos-outage-2023]] | 1 |

**Итог:** 20/20 рисков покрыты; максимум — 2 инцидента на риск.
