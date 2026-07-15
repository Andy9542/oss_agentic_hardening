---
type: incident
date: 2016-03-24
incident-kind: confirmed-production-incident
status: confirmed-service-withdrawn
affected: "Microsoft Tay"
risk-ids:
  - ASI06
  - LLM04
tags:
  - agent-security
  - incident
  - poisoning
  - feedback-loop
---

# Microsoft Tay — координированное отравление публичного feedback loop

## Что произошло

В первые 24 часа после запуска группа пользователей координированно эксплуатировала поведение Twitter-бота Tay. Бот начал публиковать оскорбительные сообщения, после чего Microsoft отключила сервис и признала, что не предусмотрела конкретный способ злоупотребления взаимодействиями.

## Статус доказательств

Это подтверждённый production-инцидент по официальному разбору Microsoft. Связь с poisoning используется как архитектурная аналогия: публично не доказано изменение base-model weights, но недоверенный feedback устойчиво изменил выдаваемое системой поведение.

## Связь с рисками

- [[ASI06-memory-context-poisoning]] — недоверенные массовые взаимодействия влияли на последующие ответы и публичные действия бота.
- [[LLM04-data-model-poisoning]] — входной feedback loop не был защищён от координированной манипуляции; это канонический operational пример poisoning, хотя не современная LLM-система.

## Последствия и реакция

Microsoft сняла Tay с публикации и заявила о доработке конкретной уязвимости. Для современных агентов урок относится к online learning, memory и feedback stores: пользовательский сигнал нельзя автоматически превращать в доверенное состояние.

## Источники

- [Microsoft: Learning from Tay’s introduction](https://blogs.microsoft.com/blog/2016/03/25/learning-tays-introduction/)
- [TIME: как пользователи манипулировали Tay](https://time.com/4270684/microsoft-tay-chatbot-racism/)
