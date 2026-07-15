---
type: moc
tags:
  - cluster
  - repo-catalog
---

# cluster-runtime-hooks

## Runtime hooks coding-агентов

> [!NOTE] Общая суть
> Перехват на уровне IDE/agent runtime: skills scan, block dangerous ops.

Несколько репозиториев реализуют **одну идею** разными способами (язык, точка встраивания, зрелость). Каждый вариант — отдельная заметка `repo-NN-*`; связь на графе: **кластер → реализация → способ**.

## Связанные способы

- способ №12 (12-tool-policies-yaml-rego)
- способ №27 (27-статическая-проверка-навыков-и-плагинов)

## Варианты реализации (3)

- [[repo-17-agentguard]] — GoPlusSecurity/agentguard: Хуки в рантайме: сканирование навыков, блокировка опасных действий


- [[repo-108-parallax]] — agent-defense/parallax: Внешний Rust service принимает lifecycle events агента и прогоняет их через cost-ordered chain из regex, keyword, Sigma,
- [[repo-117-destructive-command-guard]] — Dicklesworthstone/destructive_command_guard: `dcg` перехватывает shell-команду coding-агента до исполнения, нормализует и классифицирует контекст, применяет allowlis

## Навигация

- [[github-100-repo]] — полный каталог 118 репозиториев
- [[MOC — Кластеры репозиториев]] — все семейства
