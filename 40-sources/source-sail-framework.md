---
type: source
tags:
  - framework
  - savedtg
  - lifecycle
---

# SAIL (Secure AI Lifecycle) Framework V2

## URL

https://www.pillar.security/sail

## Суть

SAIL — framework Pillar Security для сквозной безопасности AI-систем: от разработки и threat modeling до тестирования, deployment и непрерывных runtime controls. Он объединяет язык для разработчиков, MLOps, security и governance.

## Ключевые выводы

- В test-фазе отдельно рассматриваются goal hijacking, prompt injection через tool chains, privilege escalation, memory poisoning, inter-agent smuggling и cascading failures.
- В deploy-фазе требуются action-level authorization, least privilege для каждого вызова, input/output filtering, behavioral baselines и возможность остановить агента.
- Каталог охватывает более 90 рисков и может использоваться для roadmap, RFP, risk assessment и compliance mapping.
- Это отраслевой framework и продуктовый материал, не OSS-реализация и не измерение эффективности конкретного control.

## Применение в обзоре

Использовать как контроль полноты lifecycle и источник терминов; конкретные механизмы подтверждать отдельными реализациями и исследованиями.

## Связи

- [[MOC — Выводы]]
- [[sources-savedtg]]
