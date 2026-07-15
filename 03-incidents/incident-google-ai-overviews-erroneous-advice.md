---
type: incident
date: 2024-05-30
incident-kind: confirmed-production-behavior
status: confirmed-mitigated
affected: "Google Search AI Overviews"
risk-ids:
  - ASI09
  - LLM09
tags:
  - agent-security
  - incident
  - misinformation
  - search
---

# Google AI Overviews — ошибочные и потенциально вредные ответы

## Что произошло

После широкого запуска AI Overviews пользователи получили ряд странных и неверных сводок. Google подтвердила реальные случаи, включая совет использовать glue для фиксации сыра на pizza и ответ на запрос о поедании rocks, объяснив часть ошибок data voids, satire и forum content.

## Статус доказательств

Google отдельно отметила, что многие viral screenshots были поддельными, но признала существование реальных inaccurate or unhelpful overviews. Поэтому карточка опирается только на примеры, подтверждённые vendor post, и не повторяет непроверенные screenshots.

## Связь с рисками

- [[ASI09-human-agent-trust-exploitation]] — формат Search summary создавал высокий уровень доверия к автоматически синтезированному совету.
- [[LLM09-misinformation]] — система представляла сатиру и нерелевантный user-generated content как фактический ответ.

## Последствия и реакция

Google внесла более десятка изменений: detection nonsensical queries, ограничения satire/UGC и дополнительные triggering restrictions. Кейс показывает необходимость provenance display, abstention при data void и отдельной политики для health/safety queries.

## Источники

- [Google: официальный postmortem AI Overviews](https://blog.google/products-and-platforms/products/search/ai-overviews-update-may-2024/)
