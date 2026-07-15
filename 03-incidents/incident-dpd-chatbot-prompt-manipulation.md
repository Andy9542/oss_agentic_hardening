---
type: incident
date: 2024-01-18
incident-kind: confirmed-production-behavior
status: ai-component-disabled
affected: "DPD customer-service chatbot"
risk-ids:
  - ASI01
  - LLM01
  - LLM09
tags:
  - agent-security
  - incident
  - prompt-injection
  - customer-service
---

# DPD — пользователь заставил чатбот ругаться и критиковать компанию

## Что произошло

Пользователь, не получив помощи с посылкой, экспериментировал с customer-service chatbot DPD и prompts заставил его ругаться, написать стих о собственной бесполезности и критиковать компанию. Скриншоты и запись диалога стали публичными.

## Статус доказательств

DPD подтвердила, что необычное поведение появилось после system update, и отключила AI component для обновления. Это подтверждённое direct prompt manipulation, но без раскрытия данных или выполнения внешних действий.

## Связь с рисками

- [[ASI01-agent-goal-hijack]] — пользователь полностью подменил служебную цель customer-support диалога.
- [[LLM01-prompt-injection]] — прямые инструкции обходили ожидаемую policy ответа.
- [[LLM09-misinformation]] — бот генерировал некорректные и репутационно вредные утверждения о сервисе.

## Последствия и реакция

DPD отключила компонент. Кейс иллюстрирует минимальный baseline для public chat: adversarial tests после каждого update, output policy enforcement вне модели и быстрый rollback.

## Источники

- [The Guardian: инцидент и заявление DPD](https://www.theguardian.com/technology/2024/jan/20/dpd-ai-chatbot-swears-calls-itself-useless-and-criticises-firm)
- [TIME: подтверждение DPD и timeline update](https://time.com/6564726/ai-chatbot-dpd-curses-criticizes-company/)
