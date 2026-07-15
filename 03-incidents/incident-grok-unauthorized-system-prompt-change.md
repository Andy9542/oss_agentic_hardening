---
type: incident
date: 2025-05-14
incident-kind: confirmed-production-configuration-incident
status: confirmed-remediated
affected: "xAI Grok on X"
risk-ids:
  - ASI06
  - ASI10
  - LLM09
tags:
  - agent-security
  - incident
  - system-prompt
  - misinformation
---

# Grok — неавторизованное изменение system prompt

## Что произошло

14 мая 2025 года Grok начал вставлять тему «white genocide» в ответы на несвязанные запросы. xAI сообщила, что причиной была неавторизованная модификация system prompt, которая обошла code review и нарушила внутренние политики.

## Статус доказательств

Production behavior подтверждено множеством публичных ответов и заявлением xAI. Карточка не делает вывод о мотивах конкретного сотрудника и не называет это poisoning base-model weights: скомпрометирован был operational instruction context.

## Связь с рисками

- [[ASI06-memory-context-poisoning]] — изменённый system prompt отравил общий контекст и влиял на несвязанные диалоги.
- [[ASI10-rogue-agents]] — сервис систематически действовал вопреки заявленным целям и политикам владельца.
- [[LLM09-misinformation]] — пользователи получали политизированные и нерелевантные утверждения как часть обычных ответов.

## Последствия и реакция

xAI объявила усиление review, публикацию system prompts в GitHub и круглосуточный monitoring. Кейс показывает, что prompt/configuration — production code: нужны change control, separation of duties, audit trail и rollback.

## Источники

- [Reuters: заявление xAI и меры после инцидента](https://www.reuters.com/business/musks-xai-updates-grok-chatbot-after-white-genocide-comments-2025-05-17/)
- [Associated Press: подтверждение поведения и реакции xAI](https://apnews.com/article/64ce5f240061ca0b88d5af4c424e1f3b)
