---
type: implementation-detail
parent-repo: repo-105-skilltotal
method-id: 27
mechanism-id: skilltotal-static-evidence-engine
repo: https://github.com/pezhik/skilltotal
language: Python
license: Apache-2.0
verdict: experimental
tags:
  - agent-security
---

# SkillTotal — статический evidence-движок

## Проверенный срез

Upstream [`7905d363ef9bb525ebb119cbc008e961c4517a5f`](https://github.com/pezhik/skilltotal/commit/7905d363ef9bb525ebb119cbc008e961c4517a5f) от 2026-07-09.

## Кодовые пути

- `skilltotal/collector.py`, `skilltotal/file_index.py` — получение и однократная индексация компонента.
- `skilltotal/scanners/`, `skilltotal/scanners/python_ast.py` — реестр regex/custom scanners и Python AST.
- `skilltotal/engine.py`, `skilltotal/models.py`, `skilltotal/scoring.py` — нормализация, evidence-инвариант и score.

## Алгоритм

1. Коллектор переводит path, Git URL, архив или registry package во временный локальный каталог, не импортируя и не запуская его.
2. File index отбрасывает VCS, dependencies и binaries, кэширует текст и переводит offsets в строки.
3. Scanners создают один finding на rule и прикрепляют ограниченный набор evidence: путь, диапазон строк и snippet; неоднозначные сигналы уходят в `needs_review`.
4. До score baseline подавляет принятые evidence, а тестовый код понижается до `needs_review`.
5. Severity weights суммируются только для risk-bearing findings; capabilities дают нулевой вклад.

## Зависимости

Python 3.10+ и стандартная библиотека; `git` нужен только для удалённых репозиториев. Runtime dependencies в `pyproject.toml` отсутствуют.

## Тесты

`pytest` охватывает collectors, AST/regex scanners, evidence, scoring, SARIF и fixtures в `tests/`; `.github/workflows/ci.yml` запускает CI. `tests/manual_eval/` исключён из обычного pytest и служит ручной калибровкой.

## Ограничения

Не видит runtime-поведение и неизвестные high-level API; Node/config анализ преимущественно regex. Capability означает наличие возможности, а не доказанную эксплуатацию; независимого benchmark в срезе нет.

## Вердикт

**экспериментально** — воспроизводимый и хорошо тестируемый pre-install SAST, но не замена ручному review, sandbox или runtime policy.

## Связи

- Репозиторий: [[repo-105-skilltotal]]
