---
type: implementation
method-id: 44
repo: "https://github.com/HiveTrace/HiveTraceRed"
language: "Python"
license: "Apache-2.0"
verdict: экспериментально
tags:
  - agent-security
  - review-2026
  - red-team
---

# HiveTrace Red — регрессионное red-team тестирование LLM

## Репозиторий

https://github.com/HiveTrace/HiveTraceRed

## Где в коде

- Attack library — 80+ техник в 10 категориях.
- Async evaluation pipeline — массовый запуск prompts.
- Provider adapters — OpenAI, GigaChat, YandexGPT, Gemini и другие.
- Evaluators, включая WildGuard и system-prompt detection.
- Dataset outputs `attack_prompts_*` и `model_responses_*`.

## Алгоритм

1. Загружает один или несколько attack datasets.
2. Применяет статические и динамические преобразования: roleplay, persuasion, encoding, context switching и token smuggling.
3. Отправляет атаки выбранным моделям асинхронно.
4. Evaluator классифицирует успешность обхода и сохраняет ответы.
5. Кросс-произведение model × attack × dataset позволяет сравнивать версии.
6. Сохранённые результаты используются как regression baseline перед релизом.

## Детерминизм или машинное обучение

Оркестрация, datasets и агрегация детерминированы; ответы моделей, адаптивные преобразования и model-based evaluators вероятностны.

## Внешние зависимости

Python 3.10+, API keys или локальные endpoints тестируемых моделей. WildGuard и другие evaluators могут требовать отдельную модель/GPU или внешний API.

## Сигналы качества

- Тесты в репозитории: публичный pipeline и конфигурация нескольких datasets/providers; независимый benchmark не указан.
- Документированные обходы: широкий multilingual набор, включая русский, но акцент преимущественно на LLM jailbreak, а не на tool-using agent side effects.
- Зрелость: Apache-2.0 и документация есть; новый исследовательский framework.

## Вердикт

**экспериментально** — полезен как CI/regression harness для content guardrails, но не является runtime barrier и слабее покрывает действия агента.

## Связи

- Способ: [[44-red-team-regression]]
