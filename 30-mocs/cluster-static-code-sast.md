---
type: moc
tags:
  - cluster
  - repo-catalog
---

# cluster-static-code-sast

## SAST кода агентов

> [!NOTE] Общая суть
> Статический анализ исходного/генерируемого кода: Semgrep, rule-based паттерны опасных конструкций.

Репозитории связаны **только через это семейство** (без прямых связей repo↔repo). На графе: **кластер → repo-NN → detail → способ**.

## Связанные способы

- способ №30
- способ №26

## Варианты реализации (6)

- [[repo-101-semgrep]] — semgrep/semgrep: Rule-based SAST для кода, генерируемого coding-агентами


- [[repo-105-skilltotal]] — pezhik/skilltotal: Локально и без исполнения исследуемого компонента индексирует skills, MCP-серверы, npm/PyPI-пакеты и проекты, затем объе
- [[repo-106-dvalincode]] — arthurpanhku/dvalincode: Coding-agent runtime сводит машинную и репозиторную политики сужением разрешений, проверяет операции в единой точке вызо
- [[repo-109-nvidia-skillspector]] — NVIDIA/SkillSpector: LangGraph-конвейер разрешает Git/URL/ZIP/файл, строит общий контекст, параллельно запускает 22 анализатора и передаёт fi
- [[repo-114-claude-code-security-review]] — anthropics/claude-code-security-review: GitHub Action передаёт Claude Code diff и ограниченный контекст pull request, получает security findings, выполняет отде
- [[repo-117-destructive-command-guard]] — Dicklesworthstone/destructive_command_guard: `dcg` перехватывает shell-команду coding-агента до исполнения, нормализует и классифицирует контекст, применяет allowlis

## Навигация

- [[github-100-repo]] — полный каталог репозиториев
- [[MOC — Кластеры репозиториев]] — все семейства
