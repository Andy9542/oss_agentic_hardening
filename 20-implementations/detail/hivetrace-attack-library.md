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

# HiveTraceRed — библиотека и композиция атак

## Проверенная ревизия

`975fd99`, дата коммита 2026-06-25; код проверен 2026-07-15.

## Где в коде

- Код: `src/hivetracered/attacks/base_attack.py`, `src/hivetracered/attacks/composed_attack.py`, `src/hivetracered/attacks/yaml_loader.py`, `src/hivetracered/attacks/types/single_turn/`, `src/hivetracered/attacks/types/multi_turn/conversational/crescendo_attack.py`, `src/hivetracered/pipeline/create_dataset.py`.
- Тесты: `tests/conformance/test_attack_conformance.py`, `tests/attacks/base/`, `tests/attacks/token_smuggling/`, `tests/attacks/text_structure/`, `tests/attacks/iterative/`, `tests/attacks/conversational/test_crescendo_attack.py`.

## Алгоритм

1. Конфигурация разрешает имя атаки через registry и создаёт static, model-based, iterative либо conversational объект.
2. Опциональный `inner_attack` соединяет преобразования в композицию.
3. Static-атаки применяют шаблоны, кодирование или структурные преобразования; PAIR/TAP и Crescendo используют attacker/target models и judge.
4. Streaming API применяет каждую атаку ко всем исходным промптам и сохраняет тип, параметры, metadata и ошибки.

## Зависимости

Статические преобразования работают локально. Model-based, iterative и conversational варианты требуют attacker model; часть вариантов также требует target model и evaluator.

## Ограничения

Большое число техник не означает полноту пространства атак. Категории в основном нацелены на jailbreak и prompt-level обходы, а вероятностные атаки чувствительны к модели и judge.

## Вердикт

**экспериментально** — самостоятельный генератор red-team случаев способа №44 с conformance- и category-specific тестами.

## Связи

- Репозиторий: [[repo-116-hivetrace-red]]
