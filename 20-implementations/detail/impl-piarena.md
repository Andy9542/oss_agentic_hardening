---
type: implementation-detail
parent-repo: repo-110-piarena
method-id: 44
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

# PIArena — сравнительный pipeline атак и защит

## Проверенная ревизия

`c39fd88`, дата коммита 2026-04-20; код проверен 2026-07-15.

## Где в коде

- Код: `main.py`, `piarena/registry.py`, `piarena/attacks/base.py`, `piarena/defenses/base.py`, `piarena/evaluations/__init__.py`, `piarena/evaluations/llm_judge.py`, `scripts/run.py`.
- Тесты: собственного каталога `tests/`, `pytest.ini` или test target для основной PIArena на этой ревизии нет; `agents/agentdojo/tests/` относится к включённому AgentDojo.

## Алгоритм

1. Раннер загружает локальный или Hugging Face dataset и фиксирует seed.
2. Реестры по имени создают одну атаку и одну защиту.
3. Атака строит инъецированный контекст; защита получает целевую инструкцию, контекст и модель.
4. Dataset-specific evaluator вычисляет attack success и utility.
5. Промежуточные атаки и итоговые записи сохраняются в JSON, а `scripts/run.py` перебирает матрицу dataset × model × attack × defense.

## Зависимости

Python 3.10, PyTorch, Transformers, Hugging Face Datasets и зависимости выбранных атак и защит; `main.py` требует доступный GPU. Для API-моделей нужны учётные данные соответствующего провайдера.

## Ограничения

Нет собственного test suite для core pipeline. Широкие `except` при загрузке данных и результатов могут скрывать причину ошибки. Фиксированный seed не делает ответы модели и LLM-judge детерминированными.

## Вердикт

**экспериментально** — основной механизм PIArena пригоден для сравнительной и регрессионной оценки по способу №44, но не является runtime-защитой.

## Связи

- Репозиторий: [[repo-110-piarena]]
