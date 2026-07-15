---
type: incident
date: 2024-09-25
incident-kind: regulatory-enforcement
status: settled-final-order
affected: "DoNotPay legal AI services"
risk-ids:
  - ASI09
  - LLM09
tags:
  - agent-security
  - incident
  - legal
  - human-trust
---

# DoNotPay — FTC action за недоказанные claims об «AI lawyer»

## Что произошло

FTC обвинила DoNotPay в том, что сервис рекламировался как замена человеческому юристу и обещал быстро создавать валидные legal documents, не имея тестов на эквивалентность работе адвоката и не привлекая attorneys для проверки. Отдельный feature для поиска нарушений на сайтах малого бизнеса также, по complaint, не работал как заявлено.

## Статус доказательств

Это regulatory enforcement, а не единичная hallucination transcript. DoNotPay согласилась на settlement с выплатой 193 тысяч долларов, уведомлением части подписчиков и запретом делать claims о замене профессионалов без доказательств.

## Связь с рисками

- [[ASI09-human-agent-trust-exploitation]] — маркетинг и интерфейс побуждали пользователей доверять системе как профессиональному представителю.
- [[LLM09-misinformation]] — качество и юридическая валидность outputs заявлялись без достаточной проверки и evidence.

## Последствия и реакция

Кейс переводит evaluation и disclosure limitations из best practice в измеримое регуляторное последствие. Для high-impact ассистентов нужны task-specific benchmarks, expert review, traceable sources и запрет на unsupported capability claims.

## Источники

- [FTC: Operation AI Comply и DoNotPay action](https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes)
- [FTC case page: DoNotPay](https://www.ftc.gov/legal-library/browse/cases-proceedings/donotpay)
