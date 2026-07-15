---
type: incident
date: 2026-01-31
incident-kind: vulnerability-disclosure
status: confirmed-exposure-remediated
affected: "Moltbook"
risk-ids:
  - ASI03
  - ASI07
  - ASI10
tags:
  - agent-security
  - incident
  - identity
  - data-exposure
---

# Moltbook — открытая база, токены агентов и private messages

## Что произошло

Wiz обнаружила клиентский ключ Supabase при отсутствии Row Level Security. Неаутентифицированный запрос давал read/write-доступ к production-базе: около 1,5 млн токенов агентов, адреса электронной почты, 4 060 private DM между агентами и отдельные сторонние API keys. Write-доступ позволял менять публикации, которые затем потребляли другие агенты.

## Статус доказательств

Это подтверждённое исследователями раскрытие данных и прав записи. Публичных доказательств злоупотребления сторонним атакующим нет; Wiz использовала минимальный доступ для проверки, уведомила владельца и удалила полученные данные после исправления.

## Связь с рисками

- [[ASI03-identity-privilege-abuse]] — раскрытые токены позволяли полностью выдать себя за любого агента.
- [[ASI07-insecure-inter-agent-communication]] — private agent-to-agent messages хранились без достаточного контроля доступа.
- [[ASI10-rogue-agents]] — захваченная identity позволяла действовать от имени доверенного агента и внедрять контент.

## Последствия и реакция

Команда Moltbook включила ограничения RLS в несколько этапов и закрыла read/write-доступ в течение нескольких часов. Инцидент связывает обычную cloud misconfiguration с агентными рисками identity, межагентного доверия и prompt injection downstream.

## Источники

- [Wiz Research: полный разбор и disclosure timeline](https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys)
- [TechRadar: независимая сводка раскрытия](https://www.techradar.com/pro/security/ai-agent-social-media-network-moltbook-is-a-security-disaster-millions-of-credentials-and-other-details-left-unsecured)
