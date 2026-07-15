---
type: repo-catalog
catalog-id: 110
method-id: 44
also-method-ids:
  - 45
repo: https://github.com/sleeepeer/PIArena
language: Python
license: MIT
verdict: experimental
tags:
  - agent-security
  - repo-catalog
  - review-2026
clusters:
  - cluster-benchmarks
  - cluster-red-team
---

# sleeepeer/PIArena — каталог №110

## Репозиторий

[sleeepeer/PIArena](https://github.com/sleeepeer/PIArena), проверенная ревизия `c39fd88` от 2026-04-20.

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | — |
| Тип | Бенчмарк |
| Семейства | [[cluster-benchmarks]], [[cluster-red-team]] |

## Принцип работы

Платформа сравнивает prompt-injection атаки и защиты на общих наборах данных, а также запускает агентные сценарии AgentDojo, AgentDyn и InjecAgent.

## Алгоритм

Раннер выбирает набор данных, модель, атаку и защиту, строит инъецированный контекст, измеряет attack success rate и полезность ответа, затем сохраняет результаты для сопоставления конфигураций. Основной механизм — **способ №44**; агентные наборы испытаний дополнительно реализуют способ №45.

## Вариант в семействе

PIArena объединяет обычные, поисковые и агентные эксперименты в одном исследовательском стенде. Это измерительный контур, а не runtime-барьер.

## Детерминизм или машинное обучение

Оркестрация и часть метрик детерминированы при фиксированном seed; ответы моделей, LLM-judge и генеративные атаки вероятностны.

## Вердикт

**экспериментально** — полезно для сравнительной и регрессионной оценки, но у основной платформы нет собственного test suite.

## Детальные разборы

- [[impl-piarena]]
- [[piarena-search-attacks]]
- [[piarena-agent-benchmarks]]

## Реализуемые способы

- [[44-red-team-regression]] — основной
- [[45-agentdojo-как-эталонный-набор-испытаний]]
