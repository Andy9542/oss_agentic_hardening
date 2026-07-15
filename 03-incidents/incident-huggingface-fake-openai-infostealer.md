---
type: incident
date: 2026-05-11
incident-kind: confirmed-supply-chain-incident
status: malicious-repositories-removed
affected: "Hugging Face repository Open-OSS/privacy-filter"
risk-ids:
  - ASI04
  - ASI05
  - LLM02
  - LLM03
tags:
  - agent-security
  - incident
  - supply-chain
  - malware
---

# Hugging Face — поддельный OpenAI-репозиторий распространял infostealer

## Что произошло

Исследователи HiddenLayer обнаружили на Hugging Face репозиторий Open-OSS/privacy-filter, который копировал оформление легитимного OpenAI-релиза. Файл loader.py загружал последующие команды и разворачивал infostealer Sefirah, способный собирать browser credentials, crypto wallets, VPN/SSH-данные и локальные файлы. Репозиторий поднялся в рейтинге с примерно 244 тысячами downloads и сотнями искусственных likes.

## Статус доказательств

Наличие вредоносного loader и инфраструктуры подтверждено исследованием, после уведомления Hugging Face связанные репозитории удалили. Счётчик downloads не равен числу заражений и мог быть накручен; публичного подтверждённого количества успешных исполнений нет.

## Связь с рисками

- [[ASI04-agentic-supply-chain]] — злоумышленник использовал доверие к реестру AI-моделей и похожее имя издателя.
- [[ASI05-unexpected-code-execution]] — loader запускал PowerShell/batch-цепочку и вредоносный executable на host.
- [[LLM02-sensitive-information-disclosure]] — целью infostealer были credentials, ключи, кошельки и чувствительные файлы.
- [[LLM03-supply-chain]] — model hub и model card выступили каналом supply-chain подмены.

## Последствия и реакция

Случай обосновывает проверку publisher identity, pinning commit/hash, статический просмотр loader-кода и запуск моделей/демо только в изолированном окружении. Популярность и позиция в рейтинге не являются provenance.

## Источники

- [TechRadar: исследование HiddenLayer и удаление репозиториев](https://www.techradar.com/pro/security/a-fake-openai-repository-has-taken-top-spot-on-hugging-face-but-all-it-does-is-push-infostealer-malware)
