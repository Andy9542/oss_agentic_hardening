---
type: moc
tags:
  - cluster
  - repo-catalog
---

# cluster-capability-camel

## Capability-based контроль (CaMeL)

> [!NOTE] Общая суть
> Разделение доверенных/недоверенных данных и capability taint.

Несколько репозиториев реализуют **одну идею** разными способами (язык, точка встраивания, зрелость). Каждый вариант — отдельная заметка `repo-NN-*`; связь на графе: **кластер → реализация → способ**.

## Связанные способы

- способ №43 (43-две-модели-с-разделением-доверия-и-карантином)
- способ №16 (16-ifc-capability-taint)

## Варианты реализации (2)

- [[repo-56-camel-prompt-injection]] — google-research/camel-prompt-injection: CaMeL: capability-based контроль + разделение доверенных данных
- [[repo-89-autodefense]] — XHMY/AutoDefense: Мультиагентная защита от jailbreak


## Навигация

- [[github-100-repo]] — полный каталог 100 репозиториев
- [[MOC — Кластеры репозиториев]] — все семейства
