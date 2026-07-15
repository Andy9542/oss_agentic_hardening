---
type: implementation
method-id: 44
repo: "https://github.com/sleeepeer/PIArena"
language: "Python"
license: "MIT"
verdict: экспериментально
tags:
  - agent-security
  - review-2026
  - benchmark
---

# PIArena — benchmark атак и защит от prompt injection

## Репозиторий

https://github.com/sleeepeer/PIArena

## Где в коде

- `main.py` — общий benchmark runner.
- `main_agentdojo.py` — AgentDojo/AgentDyn runner.
- Модули attacks/defenses — plug-and-play стратегии.
- Интеграции InjecAgent, AgentDojo и AgentDyn — agentic evaluation.

## Алгоритм

1. Выбирает dataset, целевую модель, атаку и защиту.
2. Генерирует или преобразует prompt-injection payload.
3. Применяет выбранную defense до/вокруг вызова модели.
4. Запускает кросс-произведение атак, защит и наборов данных.
5. Оценивает attack success и utility, сохраняя воспроизводимый конфиг.
6. Для agentic режима запускает benchmark-native защиты через общий AgentDojo/AgentDyn entrypoint.

## Детерминизм или машинное обучение

Оркестрация и метрики детерминированы при фиксированных данных и seed; генеративные атаки, ответы модели и LLM-based защиты вероятностны.

## Внешние зависимости

Python и API/локальные endpoints тестируемых моделей. Для agentic eval нужны зависимости соответствующего benchmark. Облако не обязательно при локальных моделях.

## Сигналы качества

- Тесты в репозитории: воспроизводимые benchmark runners и публичный dataset/leaderboard.
- Документированные обходы: включает search-based attacks и PISmith для адаптивного red team.
- Зрелость: paper принят на ACL 2026; это исследовательская платформа, не runtime barrier.

## Вердикт

**экспериментально** — сильная платформа для сравнительной и регрессионной оценки prompt-injection защит на нескольких benchmark-наборах; использовать как измеритель, а не как production-защиту.

## Связи

- Способ: [[44-red-team-regression]]
