---
type: moc
tags:
  - cluster
  - repo-catalog
---

# cluster-observability

## Наблюдаемость и SIEM для агентов

> [!NOTE] Общая суть
> Трассировка, стоимость, compliance — обнаружение, не блокировка.

Несколько репозиториев реализуют **одну идею** разными способами (язык, точка встраивания, зрелость). Каждый вариант — отдельная заметка `repo-NN-*`; связь на графе: **кластер → реализация → способ**.

## Связанные способы

- способ №40 (40-opentelemetry-siem)
- способ №37 (37-выявление-поведенческих-отклонений)
- способ №9 (09-проверка-фактической-точности-и-галлюцинаций)

## Варианты реализации (8)

- [[repo-03-aegis]] — Justin0504/Aegis: Шлюз с PDP: перехват вызовов, RBAC, аудит, SDK на Go/Python
- [[repo-20-litellm]] — BerriAI/litellm: Прокси LLM с guardrails, бюджетами, логированием
- [[repo-43-langkit]] — whylabs/langkit: Мониторинг инъекций, дрейфа, токсичности
- [[repo-96-agentops]] — AgentOps-AI/agentops: Сессии, стоимость, ошибки, compliance
- [[repo-97-openllmetry]] — traceloop/openllmetry: OpenTelemetry для LLM/агентов
- [[repo-98-phoenix]] — Arize-AI/phoenix: Трассировка, eval RAG, галлюцинации


- [[repo-106-dvalincode]] — arthurpanhku/dvalincode: Coding-agent runtime сводит машинную и репозиторную политики сужением разрешений, проверяет операции в единой точке вызо
- [[repo-108-parallax]] — agent-defense/parallax: Внешний Rust service принимает lifecycle events агента и прогоняет их через cost-ordered chain из regex, keyword, Sigma,

## Навигация

- [[github-100-repo]] — полный каталог 118 репозиториев
- [[MOC — Кластеры репозиториев]] — все семейства
