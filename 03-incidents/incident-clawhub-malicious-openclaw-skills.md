---
type: incident
date: 2026-02-04
incident-kind: confirmed-supply-chain-incident
status: confirmed-malware-and-mitigations
affected: "ClawHub / OpenClaw skills ecosystem"
risk-ids:
  - ASI04
  - ASI05
  - ASI10
  - LLM02
  - LLM03
  - LLM06
tags:
  - agent-security
  - incident
  - skills
  - supply-chain
---

# ClawHub — вредоносные skills для OpenClaw

## Что произошло

Исследователи обнаружили в ClawHub серии skills, маскировавшихся под crypto, wallet и social-инструменты. По сводке The Verge, 28 malicious skills появились 27–29 января 2026 года, ещё 386 — 31 января–2 февраля. Часть payloads пряталась в Markdown-инструкциях, убеждая пользователя или агента запустить скрипт, который крал wallet keys, SSH credentials и browser passwords.

## Статус доказательств

Это реальная публикация вредоносных расширений в production marketplace, а не лабораторный PoC. Однако публичные отчёты подтверждают наличие malware и распространение skills, а не точное число успешно заражённых машин.

## Связь с рисками

- [[ASI04-agentic-supply-chain]] — marketplace расширений стал каналом доставки недоверенных инструкций и кода агенту.
- [[ASI05-unexpected-code-execution]] — skills добивались исполнения shell-команд и установки infostealer на host.
- [[ASI10-rogue-agents]] — скомпрометированный skill мог заставить локального агента действовать против владельца.
- [[LLM02-sensitive-information-disclosure]] — payloads нацеливались на credentials, wallets и локальные секреты.
- [[LLM03-supply-chain]] — доверие к community skill и его рейтингу заменяло проверку provenance.
- [[LLM06-excessive-agency]] — широкий доступ OpenClaw к файлам, shell и сети увеличивал blast radius установки.

## Последствия и реакция

В ClawHub добавили ограничения для новых publisher accounts и reporting; позднее экосистема усилила сканирование. Архитектурный вывод — skill нужно считать исполняемой зависимостью: review, подпись, allowlist capabilities, sandbox и запрет неявной установки.

## Источники

- [The Verge: сводка массовых malicious skills и реакция OpenClaw](https://www.theverge.com/news/874011/openclaw-ai-skill-clawhub-extensions-security-nightmare)
- [Tom's Hardware: разбор ранней серии crypto-themed skills](https://www.tomshardware.com/tech-industry/cyber-security/malicious-moltbot-skill-targets-crypto-users-on-clawhub)
