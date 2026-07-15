---
type: implementation-detail
parent-repo: repo-95-agent-bound
method-id: 12
repo: https://github.com/ElPaisano/agent-bound
language: Unknown
license: Unknown
verdict: unknown
commit-sha: unavailable
commit-date: ""
verified-date: 2026-07-16
tags:
  - agent-security
---

# agent-bound — исходники недоступны (каталог №95)

## Репозиторий

- [ElPaisano/agent-bound](https://github.com/ElPaisano/agent-bound) — на 2026-07-16 **HTTP 404** (clone требует auth / removed).
- Wayback / PyPI / GitHub search по «agent-bound» + «Agentic Entropy» зеркал с кодом не дали.
- Проверенный срез кода: **нет** (разбор без commit SHA).

## Что это за технология

По вторичным описаниям в awesome-листах (Jamie-Cui / ProjectRecon *awesome-ai-agents-security*): **design-time** анализ архитектуры агента, метрика **Agentic Entropy** — количественная оценка непредсказуемости / риска бесконечных циклов и неограниченных действий. Это не runtime firewall и не YAML-PDP в привычном смысле каталожной карточки (№12/№14), а скорее статический risk score на этапе проектирования.

Без репозитория нельзя подтвердить API, формулы энтропии, формат входа/выхода.

## Где в коде

Недоступно. Пути модулей, тесты, конфиги политики — неизвестны.

## Алгоритм (по публичному описанию, не верифицирован)

1. На вход — описание/граф агентной архитектуры (инструменты, циклы, права).
2. Вычисление «Agentic Entropy» как меры unconstrained / loop risk.
3. Выход — числовой риск / отчёт для design review.

Шаги 1–3 — реконструкция из blurb, не из исходников.

## Примеры реализации

Артефактов из кода нет. Не воспроизводить вымышленные regex/YAML.

## Пример: вход → решение

Не верифицируется без бинарника/репо.

## Детерминизм или машинное обучение

Неизвестно.

## Внешние зависимости

Неизвестно.

## Ограничения

- Каталожная ссылка мёртвая — углубление невозможно.
- Соседние живые проекты с похожей ролью (egress/policy): agentguard (MukundaKatta), eqtylab MCP Guardian proxy — см. соответствующие detail в каталоге.

## Сигналы качества

- Упоминания только во вторичных awesome-листах; stars/CI/license не проверить.

## Вердикт

**неизвестно** — репозиторий удалён; карточка оставлена как заглушка каталога №95.

## Связи

- Репозиторий: [[repo-95-agent-bound]]
