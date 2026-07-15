---
type: incident
date: 2024-12-05
incident-kind: confirmed-supply-chain-incident
status: confirmed-remediated
affected: "ultralytics PyPI package 8.3.41"
risk-ids:
  - ASI04
  - LLM03
tags:
  - agent-security
  - incident
  - supply-chain
  - pypi
---

# Ultralytics — вредоносный wheel в PyPI

## Что произошло

Пользователи обнаружили, что wheel ultralytics 8.3.41 в PyPI не соответствует исходникам одноимённого GitHub tag. Опубликованный пакет добавлял загрузку и запуск XMRig miner; отдельные пользователи наблюдали 100% CPU после установки. Таким образом, доверенный ML-пакет распространял код, отсутствовавший в проверяемом репозитории.

## Статус доказательств

Это подтверждённый supply-chain incident: различие wheel и tag воспроизводилось загрузкой артефакта из PyPI, а issue в официальном репозитории закрыт как исправленный.

## Связь с рисками

- [[ASI04-agentic-supply-chain]] — скомпрометированный ML dependency может попасть в образ или окружение агента.
- [[LLM03-supply-chain]] — подписанное имя популярного пакета не гарантировало соответствие опубликованного артефакта исходникам.

## Последствия и реакция

Опасная версия была заменена. Кейс обосновывает проверку provenance, hash pinning и сканирование именно release artifact, а не только исходного GitHub tag.

## Источники

- [Ultralytics issue #18027: несовпадение wheel и GitHub tag](https://github.com/ultralytics/ultralytics/issues/18027)
- [Ultralytics issue #18030: наблюдаемая загрузка CPU на версии 8.3.41](https://github.com/ultralytics/ultralytics/issues/18030)
