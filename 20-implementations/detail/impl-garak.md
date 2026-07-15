---
type: implementation-detail
parent-repo: repo-76-garak
method-id: 44
repo: https://github.com/NVIDIA/garak
language: Python
license: Apache-2.0
verdict: prod
commit-sha: 17de5f8
commit-date: 2026-07-14
verified-date: 2026-07-15
tags:
  - agent-security
---

# garak — red-team probes и измерение ASR

## Репозиторий

- [NVIDIA/garak](https://github.com/NVIDIA/garak)
- Проверенный срез: `17de5f8`, дата коммита 2026-07-14; код проверен 2026-07-15.

## Что это за технология

**LLM vulnerability scanner**: библиотека **probes** (атак) генерирует prompts (DAN, encoding, prompt inject, …), гоняет их на целевую модель/агента, **detectors** решают success/fail, агрегатор считает **ASR (Attack Success Rate)**. Это способ №44 — регрессионный red team, не runtime firewall.

## Где в коде

- Probes: `garak/probes/` (`dan.py`, `promptinject`, `encoding`, `goodside`, `agent_breaker.py`, …)
- Detectors / harness / CLI в пакете `garak`
- README/FAQ — как запускать сканы

## Алгоритм

1. Выбрать generator (OpenAI, HF, REST, …) и список probes.
2. Для каждого probe: сгенерировать попытки → отправить в модель.
3. Detector классифицирует ответ (jailbreak success? leak?).
4. Записать hits; посчитать ASR / hit log.
5. Сравнивать ASR между версиями защит (regression).

## Примеры реализации

Каталог probes включает: `dan`, `ansiescape`, `atkgen`, `continuation`, `divergence`, `malwaregen`, `agent_breaker`, `apikey`, …

Типичный запуск (документация NVIDIA):

```bash
garak --model_type openai --model_name gpt-4o-mini --probes dan
```

## Пример: вход → решение

- Probe DAN → модель отвечает в роли DAN → detector hit → ASR↑.
- С включённым guardrail → hit↓ → регрессия защиты измерима.

## Детерминизм или машинное обучение

Оркестрация детерминирована; ответы модели и часть detectors — вероятностны.

## Внешние зависимости

Python; API ключи целевых моделей; опционально GPU для local models.

## Ограничения

- Не блокирует прод-трафик — только оценка.
- ASR зависит от judge/detector quality.

## Сигналы качества

- Широко цитируемый NVIDIA OSS; активные probes.

## Вердикт

**готово к продакшену** как CI/red-team harness (не как PEP).

## Связи

- Репозиторий: [[repo-76-garak]]
