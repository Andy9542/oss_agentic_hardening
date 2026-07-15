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

- В каталоге — не более 40 уникальных incident cards; текущий объём — 29.
- Ограничения числа cross-links на риск нет: один инцидент может показывать несколько рисков одной exploit chain.
- Подтверждённый operational incident отделён от vulnerability disclosure, configuration/design disclosure и случая без известной эксплуатации.
- Для каждого события дана первичная или официальная ссылка и, где возможно, независимое подтверждение.
- Лабораторные PoC без production-компонента не включены; PoC против production feature помечается как disclosure, а не как breach.
- Счётчики downloads, потенциально затронутых пользователей и exposed records не выдаются за подтверждённое число жертв.

## Инциденты

| Дата | Карточка | Тип доказательства | Риски |
|------|----------|--------------------|-------|
| 2026-07-06 | [[incident-jadepuffer-agentic-ransomware]] | active exploitation / агентно оркестрированное вымогательство | ASI02, ASI03, ASI05, ASI08, ASI10, LLM06 |
| 2026-05-11 | [[incident-huggingface-fake-openai-infostealer]] | malicious model repository, удалён | ASI04, ASI05, LLM02, LLM03 |
| 2026-02-04 | [[incident-clawhub-malicious-openclaw-skills]] | массовая публикация malicious skills | ASI04, ASI05, ASI10, LLM02, LLM03, LLM06 |
| 2026-01-31 | [[incident-moltbook-agent-database-exposure]] | раскрытие и подтверждённый доступ, исправлено | ASI03, ASI07, ASI10 |
| 2026-01-12 | [[incident-servicenow-bodysnatcher-cve-2025-12420]] | CVE, исправлено; exploitation none | ASI03, ASI10, LLM06 |
| 2025-11-19 | [[incident-servicenow-second-order-prompt-injection]] | воспроизводимый second-order prompt injection PoC | ASI01, ASI02, ASI03, ASI07, ASI10, LLM01, LLM02, LLM06 |
| 2025-07-23 | [[incident-amazon-q-vscode-extension-compromise]] | malicious release; payload не выполнился | ASI04, ASI05, LLM03 |
| 2025-07-18 | [[incident-replit-production-database-deletion]] | production incident, данные восстановлены | ASI02, ASI05, ASI08, ASI09, ASI10, LLM06, LLM09 |
| 2025-07-09 | [[incident-mcp-remote-rce-cve-2025-6514]] | CVE, нет известной эксплуатации | ASI04, ASI05, LLM03 |
| 2025-06-27 | [[incident-mcp-inspector-rce-cve-2025-49596]] | CVE/RCE PoC, исправлено | ASI04, ASI05, LLM03 |
| 2025-06-11 | [[incident-echoleak-m365-copilot]] | CVE/exploit chain, нет подтверждённого customer breach | ASI01, ASI02, ASI06, LLM01, LLM02, LLM05, LLM06, LLM08 |
| 2025-05-14 | [[incident-grok-unauthorized-system-prompt-change]] | unauthorized prompt change, production behavior | ASI06, ASI10, LLM09 |
| 2025-03-06 | [[incident-pravda-network-llm-grooming]] | documented influence campaign / observed retrieval contamination | LLM04, LLM09 |
| 2025-01-29 | [[incident-deepseek-clickhouse-exposure]] | публичная unauthenticated database exposure | ASI03 |
| 2024-12-05 | [[incident-ultralytics-pypi-compromise]] | supply-chain incident | ASI04, LLM03 |
| 2024-09-25 | [[incident-ftc-donotpay-ai-lawyer]] | FTC enforcement и settlement | ASI09, LLM09 |
| 2024-08-20 | [[incident-slack-ai-indirect-prompt-injection]] | воспроизводимый indirect prompt injection PoC | ASI01, ASI06, LLM01, LLM02, LLM05, LLM08 |
| 2024-05-30 | [[incident-google-ai-overviews-erroneous-advice]] | production misinformation, vendor response | ASI09, LLM09 |
| 2024-05-22 | [[incident-chatgpt-memory-prompt-injection]] | воспроизводимый persistent-memory PoC | ASI01, ASI02, ASI06, LLM01, LLM08, LLM09 |
| 2024-04-04 | [[incident-nyc-mycity-illegal-advice]] | production misinformation, признано городом | ASI09, LLM09 |
| 2024-02-23 | [[incident-gemini-image-historical-inaccuracies]] | production inaccuracies, feature paused | ASI09, LLM09 |
| 2024-02-14 | [[incident-air-canada-chatbot-hallucination]] | судебно подтверждённое последствие | ASI09, LLM09 |
| 2024-01-18 | [[incident-dpd-chatbot-prompt-manipulation]] | production prompt manipulation, vendor response | ASI01, LLM01, LLM09 |
| 2023-11-08 | [[incident-openai-ddos-outage-2023]] | подтверждённый service incident | LLM10 |
| 2023-06-22 | [[incident-mata-v-avianca-fake-citations]] | судебные санкции за fake citations | ASI09, LLM09 |
| 2023-03-20 | [[incident-chatgpt-redis-cross-user-exposure]] | cross-user data exposure, vendor postmortem | ASI03, ASI08 |
| 2023-02-08 | [[incident-bing-sydney-prompt-leak]] | подтверждённое production-preview behavior | LLM01, LLM07 |
| 2022-12-30 | [[incident-pytorch-torchtriton-supply-chain]] | malicious PyPI dependency executed on import | ASI04, ASI05, LLM02, LLM03 |
| 2016-03-24 | [[incident-microsoft-tay-poisoning]] | production incident; LLM04 — квалифицированная аналогия | ASI06, LLM04 |

## Покрытие рисков

| Риск | Связанные инциденты | Количество |
|------|---------------------|------------|
| [[ASI01-agent-goal-hijack]] | [[incident-servicenow-second-order-prompt-injection]], [[incident-echoleak-m365-copilot]], [[incident-slack-ai-indirect-prompt-injection]], [[incident-chatgpt-memory-prompt-injection]], [[incident-dpd-chatbot-prompt-manipulation]] | 5 |
| [[ASI02-tool-misuse]] | [[incident-jadepuffer-agentic-ransomware]], [[incident-servicenow-second-order-prompt-injection]], [[incident-replit-production-database-deletion]], [[incident-echoleak-m365-copilot]], [[incident-chatgpt-memory-prompt-injection]] | 5 |
| [[ASI03-identity-privilege-abuse]] | [[incident-jadepuffer-agentic-ransomware]], [[incident-moltbook-agent-database-exposure]], [[incident-servicenow-bodysnatcher-cve-2025-12420]], [[incident-servicenow-second-order-prompt-injection]], [[incident-deepseek-clickhouse-exposure]], [[incident-chatgpt-redis-cross-user-exposure]] | 6 |
| [[ASI04-agentic-supply-chain]] | [[incident-huggingface-fake-openai-infostealer]], [[incident-clawhub-malicious-openclaw-skills]], [[incident-amazon-q-vscode-extension-compromise]], [[incident-mcp-remote-rce-cve-2025-6514]], [[incident-mcp-inspector-rce-cve-2025-49596]], [[incident-ultralytics-pypi-compromise]], [[incident-pytorch-torchtriton-supply-chain]] | 7 |
| [[ASI05-unexpected-code-execution]] | [[incident-jadepuffer-agentic-ransomware]], [[incident-huggingface-fake-openai-infostealer]], [[incident-clawhub-malicious-openclaw-skills]], [[incident-amazon-q-vscode-extension-compromise]], [[incident-replit-production-database-deletion]], [[incident-mcp-remote-rce-cve-2025-6514]], [[incident-mcp-inspector-rce-cve-2025-49596]], [[incident-pytorch-torchtriton-supply-chain]] | 8 |
| [[ASI06-memory-context-poisoning]] | [[incident-echoleak-m365-copilot]], [[incident-grok-unauthorized-system-prompt-change]], [[incident-slack-ai-indirect-prompt-injection]], [[incident-chatgpt-memory-prompt-injection]], [[incident-microsoft-tay-poisoning]] | 5 |
| [[ASI07-insecure-inter-agent-communication]] | [[incident-moltbook-agent-database-exposure]], [[incident-servicenow-second-order-prompt-injection]] | 2 |
| [[ASI08-cascading-failures]] | [[incident-jadepuffer-agentic-ransomware]], [[incident-replit-production-database-deletion]], [[incident-chatgpt-redis-cross-user-exposure]] | 3 |
| [[ASI09-human-agent-trust-exploitation]] | [[incident-replit-production-database-deletion]], [[incident-ftc-donotpay-ai-lawyer]], [[incident-google-ai-overviews-erroneous-advice]], [[incident-nyc-mycity-illegal-advice]], [[incident-gemini-image-historical-inaccuracies]], [[incident-air-canada-chatbot-hallucination]], [[incident-mata-v-avianca-fake-citations]] | 7 |
| [[ASI10-rogue-agents]] | [[incident-jadepuffer-agentic-ransomware]], [[incident-clawhub-malicious-openclaw-skills]], [[incident-moltbook-agent-database-exposure]], [[incident-servicenow-bodysnatcher-cve-2025-12420]], [[incident-servicenow-second-order-prompt-injection]], [[incident-replit-production-database-deletion]], [[incident-grok-unauthorized-system-prompt-change]] | 7 |
| [[LLM01-prompt-injection]] | [[incident-servicenow-second-order-prompt-injection]], [[incident-echoleak-m365-copilot]], [[incident-slack-ai-indirect-prompt-injection]], [[incident-chatgpt-memory-prompt-injection]], [[incident-dpd-chatbot-prompt-manipulation]], [[incident-bing-sydney-prompt-leak]] | 6 |
| [[LLM02-sensitive-information-disclosure]] | [[incident-huggingface-fake-openai-infostealer]], [[incident-clawhub-malicious-openclaw-skills]], [[incident-servicenow-second-order-prompt-injection]], [[incident-echoleak-m365-copilot]], [[incident-slack-ai-indirect-prompt-injection]], [[incident-pytorch-torchtriton-supply-chain]] | 6 |
| [[LLM03-supply-chain]] | [[incident-huggingface-fake-openai-infostealer]], [[incident-clawhub-malicious-openclaw-skills]], [[incident-amazon-q-vscode-extension-compromise]], [[incident-mcp-remote-rce-cve-2025-6514]], [[incident-mcp-inspector-rce-cve-2025-49596]], [[incident-ultralytics-pypi-compromise]], [[incident-pytorch-torchtriton-supply-chain]] | 7 |
| [[LLM04-data-model-poisoning]] | [[incident-pravda-network-llm-grooming]], [[incident-microsoft-tay-poisoning]] *(для Tay — квалифицированная историческая аналогия, не доказательство poisoning весов/индекса)* | 2 |
| [[LLM05-improper-output-handling]] | [[incident-echoleak-m365-copilot]], [[incident-slack-ai-indirect-prompt-injection]] | 2 |
| [[LLM06-excessive-agency]] | [[incident-jadepuffer-agentic-ransomware]], [[incident-clawhub-malicious-openclaw-skills]], [[incident-servicenow-bodysnatcher-cve-2025-12420]], [[incident-servicenow-second-order-prompt-injection]], [[incident-replit-production-database-deletion]], [[incident-echoleak-m365-copilot]] | 6 |
| [[LLM07-system-prompt-leakage]] | [[incident-bing-sydney-prompt-leak]] | 1 |
| [[LLM08-vector-embedding-weaknesses]] | [[incident-echoleak-m365-copilot]], [[incident-slack-ai-indirect-prompt-injection]], [[incident-chatgpt-memory-prompt-injection]] | 3 |
| [[LLM09-misinformation]] | [[incident-replit-production-database-deletion]], [[incident-grok-unauthorized-system-prompt-change]], [[incident-pravda-network-llm-grooming]], [[incident-ftc-donotpay-ai-lawyer]], [[incident-google-ai-overviews-erroneous-advice]], [[incident-chatgpt-memory-prompt-injection]], [[incident-nyc-mycity-illegal-advice]], [[incident-gemini-image-historical-inaccuracies]], [[incident-air-canada-chatbot-hallucination]], [[incident-dpd-chatbot-prompt-manipulation]], [[incident-mata-v-avianca-fake-citations]] | 11 |
| [[LLM10-unbounded-consumption]] | [[incident-openai-ddos-outage-2023]] | 1 |

**Итог:** 20/20 рисков покрыты; 29/40 уникальных карточек. Cross-links не считаются отдельными инцидентами.
