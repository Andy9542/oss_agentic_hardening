---
type: incident
date: 2025-01-29
incident-kind: confirmed-data-exposure
status: confirmed-remediated
affected: "DeepSeek public ClickHouse database"
risk-ids:
  - ASI03
tags:
  - agent-security
  - incident
  - data-exposure
  - cloud
---

# DeepSeek — открытая ClickHouse-база с chat history и secrets

## Что произошло

Wiz обнаружила два internet-facing ClickHouse endpoint DeepSeek без аутентификации. Интерфейс позволял выполнять SQL и давал доступ более чем к миллиону log records, включая plaintext chat history, API keys, backend details и operational metadata; доступ также давал полный контроль над database operations.

## Статус доказательств

Это подтверждённая exposure, проверенная минимальными безопасными запросами. Wiz не выполняла intrusive queries и не сообщала о сторонней эксплуатации; DeepSeek закрыла доступ вскоре после уведомления.

## Связь с рисками

- [[ASI03-identity-privilege-abuse]] — анонимный внешний субъект получал database privileges без identity check.

## Последствия и реакция

Случай подчёркивает необходимость deny-by-default для telemetry stores, authentication на нестандартных портах, secret redaction в логах и continuous external attack-surface monitoring.

## Источники

- [Wiz Research: первичный disclosure](https://www.wiz.io/blog/wiz-research-uncovers-exposed-deepseek-database-leak)
- [Reuters: независимое подтверждение и реакция DeepSeek](https://www.reuters.com/technology/artificial-intelligence/sensitive-deepseek-data-exposed-web-israeli-cyber-firm-says-2025-01-29/)
