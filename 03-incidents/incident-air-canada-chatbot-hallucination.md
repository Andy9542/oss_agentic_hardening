---
type: incident
date: 2024-02-14
incident-kind: legal-decision
status: confirmed-liability
affected: "Air Canada support chatbot"
risk-ids:
  - ASI09
  - LLM09
tags:
  - agent-security
  - incident
  - hallucination
  - human-trust
---

# Air Canada — неверная политика возврата в ответе чатбота

## Что произошло

Чатбот Air Canada сообщил пассажиру, что он сможет оформить bereavement fare задним числом. После поездки авиакомпания отказала, потому что опубликованные правила не допускали такой порядок. Civil Resolution Tribunal Британской Колумбии признал, что компания отвечает за информацию своего чатбота, и присудил компенсацию.

## Статус доказательств

Факт неверного ответа и ответственность подтверждены решением Moffatt v. Air Canada, 2024 BCCRT 149. Это не security exploit, а operational incident доверия и misinformation с измеримым юридическим последствием.

## Связь с рисками

- [[ASI09-human-agent-trust-exploitation]] — пользователь обоснованно воспринял уверенный ответ агента как официальное обещание компании.
- [[LLM09-misinformation]] — chatbot сгенерировал неверное правило, противоречившее канонической политике.

## Последствия и реакция

Air Canada обязали компенсировать разницу и расходы. Кейс показывает, что disclaimer не заменяет grounding в каноническом источнике, контроль high-impact advice и возможность проверить цитируемое правило.

## Источники

- [CanLII: Moffatt v. Air Canada, 2024 BCCRT 149](https://www.canlii.org/en/bc/bccrt/doc/2024/2024bccrt149/2024bccrt149.html)
- [The Guardian: сводка решения и позиции сторон](https://www.theguardian.com/world/2024/feb/16/air-canada-chatbot-lawsuit)
