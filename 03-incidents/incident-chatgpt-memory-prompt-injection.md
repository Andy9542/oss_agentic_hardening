---
type: incident
date: 2024-05-22
incident-kind: vulnerability-disclosure
status: disclosed-as-model-safety-issue
affected: "ChatGPT Memory with connected apps, uploads and browsing"
risk-ids:
  - ASI01
  - ASI02
  - ASI06
  - LLM01
  - LLM08
  - LLM09
tags:
  - agent-security
  - incident
  - memory
  - prompt-injection
---

# ChatGPT Memory — persistent memory injection из недоверенных данных

## Что произошло

Johann Rehberger показал, что indirect prompt injection в connected Google Doc или загруженном image могла вызвать memory tool: записать ложные факты и инструкции либо удалить существующие memories. Новые записи сохранялись между чатами и влияли на последующие ответы; исследователь также добился менее стабильных вариантов через browsing/tool chaining.

## Статус доказательств

Это real-world PoC против production memory feature, но не подтверждённая массовая эксплуатация. OpenAI закрыла report как model-safety issue; исследователь отмечал частичные mitigations для browsing и отсутствие сопоставимой защиты для ряда других каналов на момент disclosure.

## Связь с рисками

- [[ASI01-agent-goal-hijack]] — внешний документ менял долгосрочную цель и поведение ассистента.
- [[ASI02-tool-misuse]] — prompt injection инициировала запись или удаление через memory tool.
- [[ASI06-memory-context-poisoning]] — ложная память сохранялась и повторно попадала в будущие context windows.
- [[LLM01-prompt-injection]] — недоверенный content интерпретировался как инструкция.
- [[LLM08-vector-embedding-weaknesses]] — connected-app retrieval переносил malicious document в доверенный контекст.
- [[LLM09-misinformation]] — записанные ложные факты могли систематически искажать будущие ответы.

## Последствия и реакция

Нужны запрет automatic memory writes после untrusted retrieval, явное подтверждение изменения памяти, provenance каждой записи, лимиты bulk operations и возможность audit/rollback.

## Источники

- [Embrace The Red: первичный PoC и disclosure](https://embracethered.com/blog/posts/2024/chatgpt-hacking-memories/)
