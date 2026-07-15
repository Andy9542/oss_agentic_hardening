---
type: incident
date: 2023-03-20
incident-kind: confirmed-data-exposure
status: confirmed-remediated
affected: "ChatGPT web service and Plus billing views"
risk-ids:
  - ASI03
  - ASI08
  - LLM02
tags:
  - agent-security
  - incident
  - data-exposure
  - shared-state
---

# ChatGPT — cross-user утечка через redis-py

## Что произошло

Bug в async Redis Cluster client приводил к тому, что после отменённого request следующий unrelated request иногда получал данные предыдущего пользователя. Некоторые пользователи видели чужие chat titles и, возможно, первое сообщение нового диалога. В девятичасовом окне могли отображаться отдельные billing details 1,2% активных Plus subscribers; полные card numbers не раскрывались.

## Статус доказательств

OpenAI опубликовала технический postmortem, исправила redis-py и уведомила потенциально затронутых пользователей. Формулировка 1,2% относится к потенциальной видимости payment data, а не к подтверждённому просмотру данных каждого такого пользователя.

## Связь с рисками

- [[ASI03-identity-privilege-abuse]] — shared connection pool нарушил изоляцию identity между активными sessions.
- [[ASI08-cascading-failures]] — редкий сбой общего cache layer распространился на chat history, billing view и email delivery.
- [[LLM02-sensitive-information-disclosure]] — в другой user context могли попасть названия диалогов, сообщение и payment metadata.

## Последствия и реакция

OpenAI добавила redundant user-matching checks, лог-анализ и улучшила Redis cluster. Общий вывод — shared state должен иметь tenant binding и fail-closed validation на каждом read.

## Источники

- [OpenAI: официальный postmortem 20 марта](https://openai.com/index/march-20-chatgpt-outage/)
