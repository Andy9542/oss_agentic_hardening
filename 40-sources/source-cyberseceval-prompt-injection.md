---
type: source
tags:
  - benchmark
  - meta
---

# CyberSecEval — инъекции в промпт

## Суть

Набор бенчмарков безопасности **PurpleLlama** от Meta: в том числе тесты на инъекции в промпт и обход ограничений.

## URL

https://github.com/meta-llama/PurpleLlama/tree/main/CybersecurityBenchmarks

## Ключевые выводы

- Количественные метрики по **семействам** атак для PromptGuard и других сканеров
- Подтверждает: атаки с **кодированием** и **многоязычностью** остаются сложными для нейросетевых классификаторов
- Используется для оценки способ №01

## Связи

- [[01-ml-injection-classifier]]
