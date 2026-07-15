---
type: implementation-detail
parent-repo: repo-110-piarena
method-id: 45
repo: https://github.com/sleeepeer/PIArena
language: Python
license: MIT
verdict: экспериментально
commit-sha: c39fd88
commit-date: 2026-04-20
verified-date: 2026-07-15
tags:
  - agent-security
---

# PIArena — агентные наборы испытаний

## Проверенная ревизия

`c39fd88`, дата коммита 2026-04-20; код проверен 2026-07-15.

## Где в коде

- Код: `main_agentdojo.py`, `main_injecagent.py`, `scripts/run_agentdojo.py`, `scripts/run_injecagent.py`, `agents/agentdojo/src/agentdojo/agent_pipeline/piarena_defense_adapter.py`, `agents/agentdojo/src/agentdojo/task_suite/load_suites.py`.
- Тесты: `agents/agentdojo/tests/test_benchmark.py`, `agents/agentdojo/tests/test_workspace_user_tasks.py`; это тесты включённого AgentDojo, отдельного integration-теста для `main_agentdojo.py`, `main_injecagent.py` и PIArena adapter нет.

## Алгоритм

1. Раннер выбирает AgentDojo/AgentDyn suite либо InjecAgent и тип атаки.
2. API-модель вызывается напрямую, а локальная Hugging Face модель поднимается через vLLM.
3. Выбранная PIArena defense подключается к AgentDojo через adapter и переменную `PIARENA_DEFENSE`.
4. Benchmark выполняет benign user tasks и injection tasks с инструментами, затем сохраняет результаты по suite и конфигурации.

## Зависимости

Включённое дерево AgentDojo, наборы AgentDyn, API провайдера либо GPU и vLLM; для InjecAgent нужен его dataset и соответствующий runner.

## Ограничения

Покрытие определяется фиксированными suites и задачами. Тесты vendored AgentDojo не подтверждают PIArena-specific wiring целиком; запуск локальных моделей требует длительного GPU-процесса.

## Вердикт

**экспериментально** — самостоятельный benchmark harness способа №45, полезный для оценки атак с последствиями в tool-using сценариях.

## Связи

- Репозиторий: [[repo-110-piarena]]
