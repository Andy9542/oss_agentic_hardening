---
type: implementation-detail
parent-repo: repo-29-agentic-radar
method-id: 28
repo: https://github.com/splx-ai/agentic-radar
language: Python
license: Apache-2.0
verdict: experimental
commit-sha: 65a7e4b
commit-date: 2025-11-27
verified-date: 2026-07-15
tags:
  - agent-security
---

# Agentic Radar — граф потоков LangGraph/CrewAI/n8n

## Репозиторий

- [splx-ai/agentic-radar](https://github.com/splx-ai/agentic-radar)
- Проверенный срез: `65a7e4b`; код проверен 2026-07-15.

## Что это за технология

**Статический security scanner агентных workflow**: парсит код/графы LangGraph, CrewAI, n8n, OpenAI Agents, AutoGen → строит graph nodes/edges (agent→tool→MCP) и ищет опасные связи (toxic flows). Способ №28.

## Где в коде

- CLI: `agentic-radar scan langgraph|crewai|n8n|…`
- Analyzers under package; tests `tests/analysis/openai_agents/e2e.py`
- Examples: `examples/langgraph`, …

## Алгоритм

1. Выбрать framework analyzer.
2. Parse project → Graph(nodes, edges).
3. Detect MCP stdio/SSE attachments, tool edges.
4. Apply vulnerability patterns on topology.
5. Emit report/visualization.

## Примеры реализации

```python
# tests
runner.invoke(app, ["scan", "langgraph", "-i", i, "-o", o])
graph = analyzer.analyze(str(root))
# assert agent → mcp edges
```

Supported: langgraph, crewai, n8n, openai-agents, autogen.

## Пример: вход → решение

- Agent wired to unrestricted shell MCP → finding on edge.
- Read-only tools only → clean graph.

## Детерминизм или машинное обучение

**Детерминированный** static graph analysis.

## Внешние зависимости

Python CLI.

## Ограничения

- Framework-specific parsers; dynamic graphs хуже видны.

## Сигналы качества

- Multi-framework e2e tests.

## Вердикт

**экспериментально** — полезный workflow topology scanner.

## Связи

- Репозиторий: [[repo-29-agentic-radar]]
