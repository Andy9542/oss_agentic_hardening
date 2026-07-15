---
type: incident
date: 2024-04-04
incident-kind: confirmed-production-behavior
status: confirmed-remained-online-with-mitigations
affected: "New York City MyCity chatbot"
risk-ids:
  - ASI09
  - LLM09
tags:
  - agent-security
  - incident
  - government
  - misinformation
---

# NYC MyCity — чатбот давал бизнесу незаконные советы

## Что произошло

Официальный городской MyCity chatbot выдавал владельцам бизнеса неверные ответы: разрешал удерживать tips работников, не учитывать требования о schedule notice и принимать решения, противоречащие labor и consumer rules. После публикаций сервис продолжал работать; город признал, что ответы ошибочны, и усилил disclaimer.

## Статус доказательств

Неверные ответы многократно воспроизводили журналисты, а мэр и Office of Technology and Innovation публично признали проблемы. Публично не доказано, что конкретный бизнес понёс санкции, следуя этим советам.

## Связь с рисками

- [[ASI09-human-agent-trust-exploitation]] — государственный домен и обещание trusted information усиливали доверие к ответам.
- [[LLM09-misinformation]] — чатбот уверенно сообщал правила, противоречащие действующему праву и официальным policy.

## Последствия и реакция

Кейс показывает, что disclaimer не компенсирует authoritative presentation. Для public-sector advice нужны ответы только из канонических источников, citations, abstention, human escalation и регулярные legal regression tests.

## Источники

- [Reuters: признание ошибок городом и примеры неверных ответов](https://www.reuters.com/technology/new-york-city-defends-ai-chatbot-that-advised-entrepreneurs-break-laws-2024-04-04/)
- [Associated Press: независимое воспроизведение](https://apnews.com/article/6ebc71db5b770b9969c906a7ee4fae21)
