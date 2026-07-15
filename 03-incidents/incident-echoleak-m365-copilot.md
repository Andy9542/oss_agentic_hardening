---
type: incident
date: 2025-06-11
incident-kind: vulnerability-disclosure
status: disclosed-no-known-exploitation
affected: "Microsoft 365 Copilot"
risk-ids:
  - ASI01
  - ASI02
  - ASI06
  - LLM01
  - LLM05
  - LLM06
  - LLM08
tags:
  - agent-security
  - incident
  - prompt-injection
  - data-exfiltration
---

# EchoLeak — zero-click prompt injection в Microsoft 365 Copilot

## Что произошло

Исследователи описали CVE-2025-32711: специально подготовленное письмо могло попасть в контекст Microsoft 365 Copilot и заставить его извлечь доступные пользователю корпоративные данные. Цепочка обходила проверку cross-prompt injection, использовала reference-style Markdown, автоматическую загрузку изображения и разрешённый прокси Microsoft Teams для вывода данных без дополнительного клика пользователя.

## Статус доказательств

Это подтверждённая уязвимость production-продукта и воспроизводимая exploit chain, а не публично подтверждённый взлом клиента. В карточке не предполагается эксплуатация в реальной атаке сверх раскрытия исследователями.

## Связь с рисками

- [[ASI01-agent-goal-hijack]] — инструкция из письма подменяла цель ответа Copilot.
- [[ASI02-tool-misuse]] — цепочка злоупотребляла автоматической загрузкой ресурса и доверенным прокси.
- [[ASI06-memory-context-poisoning]] — вредоносное письмо становилось устойчивым недоверенным элементом рабочего контекста.
- [[LLM01-prompt-injection]] — основной механизм атаки: indirect prompt injection.
- [[LLM05-improper-output-handling]] — Markdown-вывод превращался клиентом в исходящий сетевой запрос.
- [[LLM06-excessive-agency]] — ассистент одновременно имел доступ к данным и канал действия без отдельного подтверждения.
- [[LLM08-vector-embedding-weaknesses]] — опасный документ попадал в retrieval-контур и смешивался с доверенным контекстом.

## Последствия и реакция

Microsoft присвоила CVE и исправила уязвимость. Для обзора ключевой вывод — фильтра входа недостаточно, если retrieval, renderer и разрешённый egress образуют единую цепочку.

## Источники

- [MSRC: CVE-2025-32711](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-32711)
- [EchoLeak: paper и описание exploit chain](https://arxiv.org/abs/2509.10540)
