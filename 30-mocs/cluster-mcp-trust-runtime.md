---
type: moc
tags:
  - cluster
  - repo-catalog
---

# cluster-mcp-trust-runtime

## Runtime trust для MCP

> [!NOTE] Общая суть
> Доверие и защита MCP-серверов в рантайме, не только static scan.

Несколько репозиториев реализуют **одну идею** разными способами (язык, точка встраивания, зрелость). Каждый вариант — отдельная заметка `repo-NN-*`; связь на графе: **кластер → реализация → способ**.

## Связанные способы

- способ №24 (24-mcp-gateway-rbac)
- способ №25 (25-контроль-целостности-описаний-инструментов)
- способ №14 (14-default-deny-allowlists)

## Варианты реализации (4)

- [[repo-14-interlock]] — MaazAhmed47/Interlock: Слой доверия MCP в рантайме
- [[repo-24-mcp-scanner]] — cisco-ai-defense/mcp-scanner: Анализ MCP: tools, prompts, malware, готовность к деплою
- [[repo-28-mcp-guardian]] — alexandriashai/mcp-guardian: Детекция инъекций в описаниях MCP-инструментов
- [[repo-36-mcp-guardian]] — mcp-guardian/mcp-guardian: Runtime-защита MCP-серверов


## Навигация

- [[github-100-repo]] — полный каталог 100 репозиториев
- [[MOC — Кластеры репозиториев]] — все семейства
