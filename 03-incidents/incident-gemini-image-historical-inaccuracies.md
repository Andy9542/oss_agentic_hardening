---
type: incident
date: 2024-02-23
incident-kind: confirmed-production-behavior
status: feature-paused-and-retuned
affected: "Google Gemini image generation of people"
risk-ids:
  - ASI09
  - LLM09
tags:
  - agent-security
  - incident
  - image-generation
  - misinformation
---

# Gemini — пауза image generation после исторически неверных изображений

## Что произошло

После запуска image generation of people Gemini создавала неточные и иногда offensive изображения, в том числе неверно отражала конкретные historical contexts, а в других случаях чрезмерно отказывала на нейтральные prompts. Google связала это с переусиленной diversity tuning и избыточной осторожностью.

## Статус доказательств

Google официально признала проблему и временно отключила генерацию людей. Это production quality/safety incident, а не adversarial security exploit.

## Связь с рисками

- [[ASI09-human-agent-trust-exploitation]] — пользователь мог принять реалистичное изображение как правдоподобную историческую репрезентацию.
- [[LLM09-misinformation]] — система генерировала визуально убедительный, но фактически неверный historical content.

## Последствия и реакция

Google остановила feature для retuning и расширенного тестирования. Инженерный вывод — policy tuning нужно проверять на конфликтующих constraints, исторической точности и calibrated refusal до широкого rollout.

## Источники

- [Google: официальный разбор Gemini image generation](https://blog.google/products-and-platforms/products/gemini/gemini-image-generation-issue/)
- [Reuters: подтверждение паузы feature](https://www.reuters.com/technology/google-pause-gemini-ai-models-image-generation-people-2024-02-22/)
