---
type: implementation-detail
parent-repo: repo-116-hivetrace-red
method-id: 44
repo: https://github.com/HiveTrace/HiveTraceRed
language: Python
license: Apache-2.0
verdict: экспериментально
commit-sha: 975fd99
commit-date: 2026-06-25
verified-date: 2026-07-15
tags:
  - agent-security
---

# HiveTraceRed — четырёхстадийный red-team pipeline

## Проверенная ревизия

`975fd99`, дата коммита 2026-06-25; код проверен 2026-07-15.

## Где в коде

- Код: `src/hivetracered/runner.py`, `src/hivetracered/pipeline/create_dataset.py`, `src/hivetracered/pipeline/model_responses.py`, `src/hivetracered/pipeline/evaluation.py`, `src/hivetracered/pipeline/utils/data_io.py`.
- Тесты: `tests/pipeline/test_runner.py`, `tests/pipeline/test_multi_dataset_pipeline.py`, `tests/pipeline/test_pipeline_model_responses.py`, `tests/pipeline/test_pipeline_evaluation.py`, `tests/pipeline/test_pipeline_data_io.py`.

## Алгоритм

1. Конфигурация проходит preflight-проверку моделей, datasets и evaluators.
2. Для каждого исходного промпта создаётся кросс-произведение настроенных атак.
3. Асинхронный поток отправляет изменённые промпты целевой модели и помечает ошибки или блокировки.
4. Evaluator присваивает результату признак успешности атаки.
5. Pipeline сохраняет промежуточные наборы, объединяет оценки и формирует HTML-отчёт; превышение допустимой доли ошибок делает запуск degraded.

## Зависимости

Python 3.10+, конфигурация provider adapters и API keys либо локальные endpoints. Форматы вывода и отчёты используют зависимости, объявленные Python-пакетом проекта.

## Ограничения

Red-team pipeline измеряет ответы LLM, но не исполняет и не проверяет реальные side effects tool-using агента. Результаты зависят от evaluator и целевой модели.

## Вердикт

**экспериментально** — основной механизм способа №44 имеет хорошее тестовое покрытие pipeline и пригоден для повторяемых pre-release проверок.

## Связи

- Репозиторий: [[repo-116-hivetrace-red]]
