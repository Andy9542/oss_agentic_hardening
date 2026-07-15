---
type: incident
date: 2023-11-08
incident-kind: confirmed-service-incident
status: resolved
affected: "ChatGPT and OpenAI API"
risk-ids:
  - LLM10
tags:
  - agent-security
  - incident
  - availability
  - resource-exhaustion
---

# OpenAI — DDoS и периодические сбои ChatGPT/API

## Что произошло

8–9 ноября 2023 года ChatGPT и OpenAI API испытывали периодические полные сбои. В status update OpenAI связала их с аномальным трафиком, характерным для DDoS-атаки. Были затронуты API и несколько компонентов ChatGPT.

## Статус доказательств

Это подтверждённый service incident с официальной status page. Он не был вызван внутренним agent loop и используется только для ветки риска, связанной с внешним неограниченным потреблением ресурсов и отказом в обслуживании.

## Связь с рисками

- [[LLM10-unbounded-consumption]] — массовый неконтролируемый поток запросов исчерпал доступную способность сервиса и нарушил доступность.

## Последствия и реакция

OpenAI применила меры mitigation и закрыла инцидент 9 ноября. В agentic deployment такой outage может дополнительно вызвать retry storms, поэтому нужны quotas, backoff, circuit breakers и ограничение параллелизма.

## Источники

- [OpenAI Status: Periodic outages across ChatGPT and API](https://status.openai.com/incidents/21vl32gvx3hb)
- [BleepingComputer: подтверждение DDoS и влияние на сервисы](https://www.bleepingcomputer.com/news/security/openai-confirms-ddos-attacks-behind-ongoing-chatgpt-outages/)
