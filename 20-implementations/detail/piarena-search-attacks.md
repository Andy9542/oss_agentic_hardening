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

# PIArena — адаптивные поисковые атаки

## Проверенная ревизия

`c39fd88`, дата коммита 2026-04-20; код проверен 2026-07-15.

## Где в коде

- Код: `main_search.py`, `scripts/run_search.py`, `piarena/attacks/strategy_search/attack_strategy_search.py`, `piarena/attacks/strategy_search/init_strategies.py`, `piarena/attacks/pair/attack_pair.py`, `piarena/attacks/tap/attack_tap.py`.
- Тесты: собственного тестового пути для этих модулей нет; root-каталог `tests/` и pytest-конфигурация отсутствуют.

## Алгоритм

1. PAIR или TAP поручает attacker LLM итеративно уточнять payload; strategy search начинает с набора стратегий.
2. Текущая защита оценивается внутри цикла и передаёт обратную связь поиску.
3. Кандидаты изменяются или отбрасываются, пока не найден успешный вариант либо не исчерпан бюджет.
4. Лучший инъецированный контекст проходит через тот же расчёт attack success и utility, что и обычные атаки.

## Зависимости

Backend LLM, отдельная attacker LLM для PAIR/TAP, выбранная защита, PyTorch и vLLM-зависимости отдельных batch-реализаций. Поисковые запуски рассчитаны на GPU.

## Ограничения

Стоимость и результат зависят от моделей, бюджета и stochastic generation. Отсутствие unit- и integration-тестов затрудняет отделение регрессии алгоритма от вариативности модели.

## Вердикт

**экспериментально** — самостоятельный red-team механизм способа №44 для поиска обходов конкретной защиты, а не гарантия полноты атаки.

## Связи

- Репозиторий: [[repo-110-piarena]]
