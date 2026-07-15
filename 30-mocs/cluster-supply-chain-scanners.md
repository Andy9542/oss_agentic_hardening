---
type: moc
tags:
  - cluster
  - repo-catalog
---

# cluster-supply-chain-scanners

## Сканеры цепочки поставки агентов

> [!NOTE] Общая суть
> Static analysis навыков, MCP-манифестов, tool poisoning, toxic flows.

Несколько репозиториев реализуют **одну идею** разными способами (язык, точка встраивания, зрелость). Каждый вариант — отдельная заметка `repo-NN-*`; связь на графе: **кластер → реализация → способ**.

## Связанные способы

- способ №26 (26-tool-poisoning-scan)
- способ №27 (27-статическая-проверка-навыков-и-плагинов)
- способ №28 (28-toxic-flow-analysis)
- способ №25 (25-контроль-целостности-описаний-инструментов)

## Варианты реализации (20)

- [[repo-01-agent-governance-toolkit]] — microsoft/agent-governance-toolkit: Agent OS: ядро политик, идентичность агента, песочницы, адаптеры для LangGraph/CrewAI/ADK
- [[repo-17-agentguard]] — GoPlusSecurity/agentguard: Хуки в рантайме: сканирование навыков, блокировка опасных действий
- [[repo-18-defenseclaw]] — cisco-ai-defense/defenseclaw: CodeGuard, песочница, SSRF-защита реестра, аудит
- [[repo-21-agent-scan]] — snyk/agent-scan: Сканер агентов, MCP-серверов, навыков (преемник mcp-scan)
- [[repo-22-aguara]] — garagon/aguara: Go-сканер: паттерны, NLP, taint, rug-pull в навыках
- [[repo-23-aguara-mcp]] — garagon/aguara-mcp: Aguara как MCP-инструмент для CI
- [[repo-24-mcp-scanner]] — cisco-ai-defense/mcp-scanner: Анализ MCP: tools, prompts, malware, готовность к деплою
- [[repo-25-skill-scanner]] — cisco-ai-defense/skill-scanner: YARA + LLM-судья + dataflow для навыков Codex/Cursor
- [[repo-26-agent-audit]] — scadastrangelove/agent-audit: 296 правил для coding-агентов и MCP-манифестов
- [[repo-27-agentshield]] — affaan-m/agentshield: Сканер конфигураций агентов, GitHub Action
- [[repo-28-mcp-guardian]] — alexandriashai/mcp-guardian: Детекция инъекций в описаниях MCP-инструментов
- [[repo-29-agentic-radar]] — splx-ai/agentic-radar: Карта потоков данных в LangGraph/CrewAI/n8n
- [[repo-30-inkog]] — inkog-io/inkog: Статический анализ LangChain/CrewAI/AutoGen
- [[repo-31-medusa]] — Pantheon-Security/medusa: Сканер репозиториев агентов и MCP
- [[repo-32-clawsec]] — prompt-security/clawsec: Набор security-навыков для OpenClaw-семейства
- [[repo-34-repo-forensics]] — alexgreensh/repo-forensics: Офлайн-сканер навыков, плагинов, MCP
- [[repo-35-skillguard]] — obielin/skillguard: Защита навыков агентов от компрометации
- [[repo-46-invariant]] — invariantlabs-ai/invariant: Анализ трасс агентов, политики на цепочках вызовов
- [[repo-79-agentic-security]] — msoedov/agentic_security: Сканер агентных систем: hijack, tool abuse
- [[repo-93-agentvet]] — MukundaKatta/agentvet: Веттинг конфигураций агентов


## Навигация

- [[github-100-repo]] — полный каталог 100 репозиториев
- [[MOC — Кластеры репозиториев]] — все семейства
