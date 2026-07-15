---
type: moc
tags:
  - cluster
  - repo-catalog
---

# cluster-formal-policies

## Формальные и enterprise политики

> [!NOTE] Общая суть
> Rego/Cedar/DSL + (опционально) SMT-проверка монотонности привилегий.

Несколько репозиториев реализуют **одну идею** разными способами (язык, точка встраивания, зрелость). Каждый вариант — отдельная заметка `repo-NN-*`; связь на графе: **кластер → реализация → способ**.

## Связанные способы

- способ №12 (12-tool-policies-yaml-rego)
- способ №17 (17-формальная-проверка-политик-и-сужение-привилегий)
- способ №13 (13-проверка-аргументов-по-json-схеме)

## Варианты реализации (6)

- [[repo-08-agent-airlock]] — sattyamjjain/agent-airlock: Декоратор для LangChain/CrewAI: валидация аргументов, RBAC, E2B-песочница
- [[repo-10-progent]] — sunblaze-ucb/progent: Модульные политики привилегий + SMT-проверка
- [[repo-102-spicedb]] — authzed/spicedb: Google Zanzibar-style ReBAC: CheckPermission на графе user→agent→tool
- [[repo-11-janus]] — Agentic-AI-Risk-Mitigation/Janus: Политики на границе вызова инструмента
- [[repo-50-agentshield]] — AdityaBelhekar/AgentShield: Runtime SDK: перехват вызовов в приложении
- [[repo-63-opa]] — open-policy-agent/opa: Движок политик Rego для авторизации


## Навигация

- [[github-100-repo]] — полный каталог 118 репозиториев
- [[MOC — Кластеры репозиториев]] — все семейства
