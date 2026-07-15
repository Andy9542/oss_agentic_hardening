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

# HiveTraceRed — evaluators и регрессионная отчётность

## Проверенная ревизия

`975fd99`, дата коммита 2026-06-25; код проверен 2026-07-15.

## Где в коде

- Код: `src/hivetracered/pipeline/evaluation.py`, `src/hivetracered/evaluators/base_evaluator.py`, `src/hivetracered/evaluators/wild_guard_evaluator.py`, `src/hivetracered/evaluators/system_prompt_detection_evaluator.py`, `src/hivetracered/evaluators/scoring_judge_evaluator.py`, `src/hivetracered/report.py`.
- Тесты: `tests/evaluators/test_evaluators_wild_guard_evaluator.py`, `tests/evaluators/test_evaluators_system_prompt_detection_evaluator.py`, `tests/evaluators/test_evaluators_scoring_judge_evaluator.py`, `tests/pipeline/test_pipeline_evaluation.py`, `tests/test_report.py`.

## Алгоритм

1. Заблокированные и ошибочные ответы исключаются из model-based scoring и получают отрицательный результат с причиной.
2. Остальные ответы evaluator обрабатывает batch-потоком с сохранением порядка.
3. Для каждого ответа сохраняются verdict, параметры evaluator и итоговый `success`.
4. Reporting агрегирует success rate по типам и именам атак, строит графики и таблицы, а для нескольких datasets разделяет метрики.
5. Сохранённые результаты образуют baseline для сравнения следующих запусков.

## Зависимости

Keyword-оценки локальны; WildGuard и scoring judges требуют соответствующую модель, GPU или API. HTML-отчёт зависит от табличного и графического стека проекта.

## Ограничения

Model-based evaluator может ошибаться и вносит вероятностность. Отчёт сравним только при зафиксированных datasets, моделях, evaluator, параметрах и версиях провайдеров.

## Вердикт

**экспериментально** — самостоятельный измерительный механизм способа №44 с хорошими unit- и pipeline-тестами, но без формальной гарантии корректности judge.

## Связи

- Репозиторий: [[repo-116-hivetrace-red]]
