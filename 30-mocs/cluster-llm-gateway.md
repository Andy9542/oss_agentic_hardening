---
type: moc
tags:
  - cluster
  - repo-catalog
---

# cluster-llm-gateway

## LLM-шлюзы с guardrails

> [!NOTE] Общая суть
> Прокси к моделям с budgets, logging и встроенными барьерами.

Несколько репозиториев реализуют **одну идею** разными способами (язык, точка встраивания, зрелость). Каждый вариант — отдельная заметка `repo-NN-*`; связь на графе: **кластер → реализация → способ**.

## Связанные способы

- способ №11 (11-ограничение-токенов-расходов-и-частоты-вызовов)
- способ №1 (01-классификация-инъекций-машинным-обучением)
- способ №40 (40-opentelemetry-siem)

## Варианты реализации (5)

- [[repo-01-agent-governance-toolkit]] — microsoft/agent-governance-toolkit: Agent OS: ядро политик, идентичность агента, песочницы, адаптеры для LangGraph/CrewAI/ADK
- [[repo-08-agent-airlock]] — sattyamjjain/agent-airlock: Декоратор для LangChain/CrewAI: валидация аргументов, RBAC, E2B-песочница
- [[repo-12-agentgateway]] — agentgateway/agentgateway: Шлюз MCP/A2A: маршрутизация, аутентификация, ограничение поверхностей
- [[repo-19-bifrost]] — maximhq/bifrost: AI-шлюз с встроенными барьерами и лимитами
- [[repo-20-litellm]] — BerriAI/litellm: Прокси LLM с guardrails, бюджетами, логированием


## Навигация

- [[github-100-repo]] — полный каталог 100 репозиториев
- [[MOC — Кластеры репозиториев]] — все семейства
