---
type: incident
date: 2025-11-19
incident-kind: configuration-vulnerability-disclosure
status: disclosed-intended-behavior-no-known-exploitation
affected: "ServiceNow Now Assist agent discovery"
risk-ids:
  - ASI01
  - ASI02
  - ASI03
  - ASI07
  - ASI10
  - LLM01
  - LLM02
  - LLM06
tags:
  - agent-security
  - incident
  - prompt-injection
  - multi-agent
---

# ServiceNow Now Assist — second-order prompt injection между агентами

## Что произошло

AppOmni показала, как low-privileged пользователь помещает malicious prompt в поле ticket. Когда привилегированный пользователь запускает benign categorization agent, тот читает поле и через agent discovery привлекает более мощный Record Management agent. В PoC содержимое недоступного тикета копировалось в доступную атакующему запись; другие варианты позволяли назначать роли или отправлять данные по email.

## Статус доказательств

Это воспроизводимое раскрытие поведения конфигурации, а не подтверждённая атака клиента. ServiceNow сообщила исследователю, что механизмы работают как задумано, и уточнила документацию. Prompt-injection protection была включена во время теста; реальный impact зависит от состава discoverable agents, их tools и execution mode.

## Связь с рисками

- [[ASI01-agent-goal-hijack]] — инструкция из ticket подменяла исходную цель benign categorization task.
- [[ASI02-tool-misuse]] — скомпрометированный агент рекрутировал CRUD/email tools другого агента.
- [[ASI03-identity-privilege-abuse]] — цепочка пересекала ACL: действие выполнялось с правами пользователя, запустившего benign task.
- [[ASI07-insecure-inter-agent-communication]] — доверие между discoverable agents позволило передать вредоносную цель без проверки provenance.
- [[ASI10-rogue-agents]] — комбинация агентов автономно выполняла действия, не соответствующие намерению оператора.
- [[LLM01-prompt-injection]] — первичный механизм — indirect/second-order prompt injection из поля записи.
- [[LLM02-sensitive-information-disclosure]] — PoC раскрывал содержимое защищённой записи и допускал email-exfiltration.
- [[LLM06-excessive-agency]] — автономное исполнение privileged tools превращало prompt manipulation в изменение данных и ролей.

## Последствия и реакция

Рекомендации AppOmni: supervised mode для privileged tools, отключённый autonomous override, сегментация агентов по teams и мониторинг отклонения от исходной цели. Важен authorization check на каждом hop, а не только у первого агента.

## Источники

- [AppOmni AO Labs: первичный технический разбор](https://appomni.com/ao-labs/ai-agent-to-agent-discovery-prompt-injection/)
- [TechRadar: независимая сводка disclosure](https://www.techradar.com/pro/security/second-order-prompt-injection-can-turn-ai-into-a-malicious-insider)
