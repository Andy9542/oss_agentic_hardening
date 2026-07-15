---
type: moc
tags:
  - cluster
  - repo-catalog
---

# cluster-governance-platform

## Платформы governance агентов

> [!NOTE] Общая суть
> Комплексные платформы: политики, идентичность, sandbox, supply-chain scan и compliance в одном дистрибутиве.

Несколько репозиториев реализуют **одну идею** разными способами (язык, точка встраивания, зрелость). Каждый вариант — отдельная заметка `repo-NN-*`; связь на графе: **кластер → реализация → способ**.

## Связанные способы

- способ №12 (12-tool-policies-yaml-rego)
- способ №21 (21-одобрение-опасных-действий-человеком)
- способ №26 (26-tool-poisoning-scan)
- способ №32 (32-aibom-inventory)
- способ №36 (36-crypto-agent-identity)
- способ №39 (39-неизменяемый-журнал-с-цепочкой-хешей-и-подписями)

## Варианты реализации (7)

- [[repo-01-agent-governance-toolkit]] — microsoft/agent-governance-toolkit: Agent OS: ядро политик, идентичность агента, песочницы, адаптеры для LangGraph/CrewAI/ADK
- [[repo-02-pipelock]] — luckyPipewrench/pipelock: Прокси исходящего трафика: MCP, DLP, криптографические квитанции аудита
- [[repo-03-aegis]] — Justin0504/Aegis: Шлюз с PDP: перехват вызовов, RBAC, аудит, SDK на Go/Python
- [[repo-100-obot]] — obot-platform/obot: MCP-шлюз с контролем доступа и аудитом
- [[repo-18-defenseclaw]] — cisco-ai-defense/defenseclaw: CodeGuard, песочница, SSRF-защита реестра, аудит
- [[repo-57-pipelock-verify-python]] — luckyPipewrench/pipelock-verify-python: Верификатор криптографических квитанций Pipelock


- [[repo-111-h5i]] — h5i-dev/h5i: Rust CLI создаёт Git-addressed environments для агентов, выбирает наиболее сильный доступный isolation tier, фиксирует p

## Навигация

- [[github-100-repo]] — полный каталог 118 репозиториев
- [[MOC — Кластеры репозиториев]] — все семейства
