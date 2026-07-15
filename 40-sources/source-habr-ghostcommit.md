---
type: source
tags:
  - research
  - savedtg
  - prompt-injection
  - multimodal
---

# GhostCommit: prompt injection в PNG и утечка .env

## Источники

- Habr: https://habr.com/ru/articles/1058368/
- Раскрытие ASSET Research Group: https://asset-group.github.io/disclosures/ghostcommit/
- PoC: https://github.com/asset-group/ghostcommit

## Суть

В контролируемой демонстрации вредоносная инструкция находилась внутри PNG, на который ссылался безобидно выглядящий `AGENTS.md`. Текстовые PR-reviewers не анализировали изображение, после merge vision-capable coding agent прочитал инструкцию, открыл canary-`.env` и записал секреты в код как tuple целых чисел.

## Ключевые выводы

- Это лабораторный PoC с фиктивными секретами, не подтверждённый production-инцидент.
- Blind spot двойной: review не читает изображение, а secret scanner не декодирует список чисел обратно в строку.
- Результат зависел прежде всего от agent harness: одинаковая модель в разных coding tools могла выполнить или отклонить инструкцию.
- Нужна многослойная защита: multimodal review недоверенных артефактов, ограничение чтения секретов, runtime policy/telemetry и регрессионные тесты.
- Показатели защитного reviewer приведены авторами исследования и требуют независимого воспроизведения.

## Связи

- [[43-две-модели-с-разделением-доверия-и-карантином]]
- [[44-red-team-regression]]
