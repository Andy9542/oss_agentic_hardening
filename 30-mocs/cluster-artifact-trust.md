---
type: moc
tags:
  - cluster
  - repo-catalog
---

# cluster-artifact-trust

## Доверие к артефактам и AIBOM

> [!NOTE] Общая суть
> Подпись, верификация, SBOM/AIBOM, scan сериализованных моделей.

Несколько репозиториев реализуют **одну идею** разными способами (язык, точка встраивания, зрелость). Каждый вариант — отдельная заметка `repo-NN-*`; связь на графе: **кластер → реализация → способ**.

## Связанные способы

- способ №31 (31-допуск-артефактов-и-отзыв-по-чёрному-списку)
- способ №32 (32-aibom-inventory)
- способ №30 (30-static-analysis-code)

## Варианты реализации (6)

- [[repo-01-agent-governance-toolkit]] — microsoft/agent-governance-toolkit: Agent OS: ядро политик, идентичность агента, песочницы, адаптеры для LangGraph/CrewAI/ADK
- [[repo-21-agent-scan]] — snyk/agent-scan: Сканер агентов, MCP-серверов, навыков (преемник mcp-scan)
- [[repo-33-agentseal]] — getagentseal/agentseal: Подпись и верификация артефактов агентов
- [[repo-58-mcp-gateway-registry]] — agentic-community/mcp-gateway-registry: Реестр и шлюз MCP с контролем доступа
- [[repo-61-aibom-generator]] — GenAI-Security-Project/aibom-generator: SBOM для ИИ-компонентов агента
- [[repo-65-modelscan]] — protectai/modelscan: Сканирование сериализованных ML-файлов


## Навигация

- [[github-100-repo]] — полный каталог 100 репозиториев
- [[MOC — Кластеры репозиториев]] — все семейства
