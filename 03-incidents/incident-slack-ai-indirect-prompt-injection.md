---
type: incident
date: 2024-08-20
incident-kind: vulnerability-disclosure
status: disclosed-no-known-exploitation
affected: "Slack AI search and answer generation"
risk-ids:
  - ASI01
  - ASI06
  - LLM01
  - LLM02
  - LLM05
  - LLM08
tags:
  - agent-security
  - incident
  - prompt-injection
  - data-exfiltration
---

# Slack AI — indirect prompt injection из public channel

## Что произошло

PromptArmor показала, что attacker мог разместить malicious instruction в public channel, где не состояла жертва. Когда пользователь запрашивал Slack AI о секрете из private channel, retrieval смешивал private data и attacker message; модель формировала Markdown link, содержащий секрет в URL. Эксфильтрация завершалась после клика жертвы.

## Статус доказательств

Это воспроизводимая exploit chain в production feature, responsibly disclosed Slack, но не подтверждённый customer breach. Slack не признала первоначальные доказательства достаточными и назвала поиск public-channel messages intended behavior; карточка сохраняет статус disclosure.

## Связь с рисками

- [[ASI01-agent-goal-hijack]] — инструкция из постороннего channel меняла цель ответа Slack AI.
- [[ASI06-memory-context-poisoning]] — недоверенное сообщение становилось частью общего retrieval context.
- [[LLM01-prompt-injection]] — основной механизм — indirect prompt injection.
- [[LLM02-sensitive-information-disclosure]] — целью была выдача секрета из private channel атакующему.
- [[LLM05-improper-output-handling]] — Markdown output превращал данные в кликабельный URL-параметр.
- [[LLM08-vector-embedding-weaknesses]] — retrieval смешивал public attacker content и private authorized data без достаточной provenance isolation.

## Последствия и реакция

Защита требует source-aware retrieval, полного citation trail, маркировки untrusted content, запрета секретов в external links и user confirmation для egress. Фильтрация только input prompt не закрывает цепочку.

## Источники

- [PromptArmor: первичный disclosure и timeline](https://promptarmor.substack.com/p/data-exfiltration-from-slack-ai-via)
