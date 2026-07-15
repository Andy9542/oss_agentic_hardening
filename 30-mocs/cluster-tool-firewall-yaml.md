---
type: moc
tags:
  - cluster
  - repo-catalog
---

# cluster-tool-firewall-yaml

## YAML/JSON файрволы на границе tool-call

> [!NOTE] Общая суть
> Default-deny политики на вызовах инструментов в декларативном YAML/JSON — разные точки встраивания (sidecar, decorator, standalone).

Несколько репозиториев реализуют **одну идею** разными способами (язык, точка встраивания, зрелость). Каждый вариант — отдельная заметка `repo-NN-*`; связь на графе: **кластер → реализация → способ**.

## Связанные способы

- способ №12 (12-tool-policies-yaml-rego)
- способ №14 (14-default-deny-allowlists)
- способ №21 (21-одобрение-опасных-действий-человеком)

## Варианты реализации (21)

- [[repo-01-agent-governance-toolkit]] — microsoft/agent-governance-toolkit: Agent OS: ядро политик, идентичность агента, песочницы, адаптеры для LangGraph/CrewAI/ADK
- [[repo-03-aegis]] — Justin0504/Aegis: Шлюз с PDP: перехват вызовов, RBAC, аудит, SDK на Go/Python
- [[repo-04-rampart]] — peg/rampart: Файрвол для coding-агентов: политики на файловые и сетевые действия
- [[repo-05-nomos]] — safe-agentic-world/nomos: Политики ALLOW / DENY / REQUIRE_APPROVAL на уровне инструментов
- [[repo-06-zerotrust-agents]] — lokeshsk/zerotrust-agents: Zero-trust прокси между агентом и API
- [[repo-07-agent-tool-firewall]] — SecAI-Hub/agent-tool-firewall: Default-deny YAML-политики на вызовах инструментов
- [[repo-08-agent-airlock]] — sattyamjjain/agent-airlock: Декоратор для LangChain/CrewAI: валидация аргументов, RBAC, E2B-песочница
- [[repo-09-agent-firewall]] — 0xrem/agent-firewall: Pre-execution firewall: блокировка до выполнения
- [[repo-10-progent]] — sunblaze-ucb/progent: Модульные политики привилегий + SMT-проверка
- [[repo-11-janus]] — Agentic-AI-Risk-Mitigation/Janus: Политики на границе вызова инструмента
- [[repo-13-avakill]] — log-bell/avakill: YAML-политики, три пути enforcement
- [[repo-15-agentgate-public]] — ElamOlame31/agentgate-public: PDP AgentGate: решение до выполнения действия
- [[repo-17-agentguard]] — GoPlusSecurity/agentguard: Хуки в рантайме: сканирование навыков, блокировка опасных действий
- [[repo-18-defenseclaw]] — cisco-ai-defense/defenseclaw: CodeGuard, песочница, SSRF-защита реестра, аудит
- [[repo-19-bifrost]] — maximhq/bifrost: AI-шлюз с встроенными барьерами и лимитами
- [[repo-32-clawsec]] — prompt-security/clawsec: Набор security-навыков для OpenClaw-семейства
- [[repo-36-mcp-guardian]] — mcp-guardian/mcp-guardian: Runtime-защита MCP-серверов
- [[repo-50-agentshield]] — AdityaBelhekar/AgentShield: Runtime SDK: перехват вызовов в приложении
- [[repo-63-opa]] — open-policy-agent/opa: Движок политик Rego для авторизации
- [[repo-94-agentguard]] — MukundaKatta/agentguard: Контроль сетевого egress агента
- [[repo-95-agent-bound]] — ElPaisano/agent-bound: Ограничение границ действий агента


## Навигация

- [[github-100-repo]] — полный каталог 100 репозиториев
- [[MOC — Кластеры репозиториев]] — все семейства
