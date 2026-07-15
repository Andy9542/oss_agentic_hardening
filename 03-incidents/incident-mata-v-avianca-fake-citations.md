---
type: incident
date: 2023-06-22
incident-kind: legal-decision
status: confirmed-sanctions
affected: "Legal filing prepared with ChatGPT"
risk-ids:
  - ASI09
  - LLM09
tags:
  - agent-security
  - incident
  - legal
  - hallucination
---

# Mata v. Avianca — вымышленные судебные решения из ChatGPT

## Что произошло

Юристы включили в brief шесть фиктивных case citations, сгенерированных ChatGPT. После того как opposing counsel и суд не нашли решения, команда продолжила на них ссылаться; суд установил conscious avoidance и misleading statements.

## Статус доказательств

Факты и последствие закреплены sanctions order федерального суда: два юриста и фирма получили общий штраф 5 000 долларов. Суд отдельно отметил, что использование AI само по себе не запрещено, но адвокат сохраняет gatekeeping responsibility.

## Связь с рисками

- [[ASI09-human-agent-trust-exploitation]] — уверенный conversational output и повторное заверение модели заменили профессиональную проверку.
- [[LLM09-misinformation]] — ChatGPT создал несуществующие precedents и правдоподобные, но ложные цитаты.

## Последствия и реакция

Кейс обосновывает обязательную проверку каждой citation по первичному источнику, запрет включать unverifiable references и ответственность человека за финальный high-impact output.

## Источники

- [Reuters: sanctions и позиция суда](https://www.reuters.com/legal/new-york-lawyers-sanctioned-using-fake-chatgpt-cases-legal-brief-2023-06-22/)
- [CourtListener: docket Mata v. Avianca](https://www.courtlistener.com/docket/63107798/mata-v-avianca-inc/)
