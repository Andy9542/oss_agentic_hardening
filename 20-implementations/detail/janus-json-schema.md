---
type: implementation-detail
parent-repo: repo-11-janus
method-id: 13
repo: https://github.com/Agentic-AI-Risk-Mitigation/Janus
language: Python
license: Apache-2.0
verdict: experimental
commit-sha: cd14442
commit-date: 2026-07-14
verified-date: 2026-07-15
tags:
  - agent-security
---

# Janus — PolicyEnforcer и условия на аргументы

## Репозиторий

- [Agentic-AI-Risk-Mitigation/Janus](https://github.com/Agentic-AI-Risk-Mitigation/Janus)
- Проверенный срез: `cd14442`, дата коммита 2026-07-14; код проверен 2026-07-15.

## Что это за технология

**Policy enforcement на границе tool call**: перед исполнением инструмента `PolicyEnforcer.enforce(tool, args)` сверяет вызов с правилами вида `(priority, effect, conditions, fallback)`. Effect: allow=0 / deny=1. Conditions — dict ограничений на аргументы (JSON-schema-подобно), валидируемые `validate_argument`. Это способ №13 на уровне агентного runtime.

## Где в коде

- `janus/policy/enforcer.py` — `PolicyEnforcer`
- `janus/policy/validator.py` — `validate_argument`
- `janus/policy/loader.py` — парсинг JSON/YAML политик
- Примеры: `examples/config.yaml`, `examples/run.py`

## Алгоритм

1. Загрузить политику (`load` path или dict); отсортировать правила по priority.
2. На tool call: найти правила для `tool_name`.
3. Для каждого правила по возрастанию priority: проверить conditions на args.
4. Первое сработавшее: effect allow → продолжить; deny → `PolicyViolation` / exit / ask user (fallback).
5. Нет правила / нет политики — поведение по умолчанию (violation для неизвестных tools в типичной конфигурации).

## Примеры реализации

Формат правила (из docstring enforcer):

```python
{
  "tool_name": [
    (priority: int, effect: int, conditions: dict, fallback: int),
  ]
}
# effect: 0=allow, 1=deny
# fallback: 0=raise, 1=sys.exit, 2=ask user
```

```python
enforcer.enforce("read_file", {"file_path": "data.csv"})  # OK
enforcer.enforce("run_command", {"command": "rm -rf /"})  # PolicyViolation
```

## Пример: вход → решение

- `read_file` в allow-list без жёстких path constraints → allow.
- `run_command` отсутствует / deny rule → PolicyViolation.

## Детерминизм или машинное обучение

Enforcement **детерминированный**; generator политик LLM (отдельный модуль) — вероятностный.

## Внешние зависимости

Python; опционально LLM для generator.

## Ограничения

- Качество = полнота policy file.
- Workspace jail — отдельный механизм (см. janus-workspace-jail).

## Сигналы качества

- Документированный API enforcer; examples/scenarios.

## Вердикт

**экспериментально** — чистый pedagogical PDP для tool boundary.

## Связи

- Репозиторий: [[repo-11-janus]]
