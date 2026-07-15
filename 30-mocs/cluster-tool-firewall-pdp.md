---
type: moc
tags:
  - cluster
  - repo-catalog
---

# cluster-tool-firewall-pdp

## PDP-шлюзы и zero-trust прокси

> [!NOTE] Общая суть
> Policy Decision Point перехватывает вызов до исполнения: RBAC, аудит, иногда human approval.

Несколько репозиториев реализуют **одну идею** разными способами (язык, точка встраивания, зрелость). Каждый вариант — отдельная заметка `repo-NN-*`; связь на графе: **кластер → реализация → способ**.

## Связанные способы

- способ №12 (12-tool-policies-yaml-rego)
- способ №21 (21-одобрение-опасных-действий-человеком)
- способ №39 (39-неизменяемый-журнал-с-цепочкой-хешей-и-подписями)
- способ №37 (37-выявление-поведенческих-отклонений)

## Варианты реализации (8)

- [[repo-01-agent-governance-toolkit]] — microsoft/agent-governance-toolkit: Agent OS: ядро политик, идентичность агента, песочницы, адаптеры для LangGraph/CrewAI/ADK
- [[repo-03-aegis]] — Justin0504/Aegis: Шлюз с PDP: перехват вызовов, RBAC, аудит, SDK на Go/Python
- [[repo-05-nomos]] — safe-agentic-world/nomos: Политики ALLOW / DENY / REQUIRE_APPROVAL на уровне инструментов
- [[repo-06-zerotrust-agents]] — lokeshsk/zerotrust-agents: Zero-trust прокси между агентом и API
- [[repo-102-spicedb]] — authzed/spicedb: Google Zanzibar-style ReBAC: CheckPermission на графе user→agent→tool
- [[repo-15-agentgate-public]] — ElamOlame31/agentgate-public: PDP AgentGate: решение до выполнения действия
- [[repo-50-agentshield]] — AdityaBelhekar/AgentShield: Runtime SDK: перехват вызовов в приложении
- [[repo-95-agent-bound]] — ElPaisano/agent-bound: Ограничение границ действий агента


## Навигация

- [[github-100-repo]] — полный каталог 100 репозиториев
- [[MOC — Кластеры репозиториев]] — все семейства
