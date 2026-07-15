---
type: implementation-detail
parent-repo: repo-108-parallax
method-id: 11
repo: https://github.com/agent-defense/parallax
language: Rust
license: Apache-2.0
verdict: экспериментально
commit-sha: c9c28face1e7426bb67ab03aa18f772ff7050fc5
commit-date: 2026-06-05
verified-date: 2026-07-15
tags:
  - agent-security
---

# Parallax — stateful SQL rate limits

## Проверенная ревизия

`c9c28face1e7426bb67ab03aa18f772ff7050fc5`, дата коммита 2026-06-05; код и GitHub tree проверены 2026-07-15.

## Где в коде

- Код: `src/evaluators/sql_eval.rs`, `rules/sql/rate-limits.yaml`, `src/engine/context.rs`, `docs/RULES.md`.
- Тесты: inline-модуль в `src/evaluators/sql_eval.rs`: condition operators и `test_sql_evaluator_rate_limit`.

## Алгоритм

1. Каждый применимый event записывается в in-memory SQLite с timestamp, stage, session, user, channel, tool и ограниченным tool result.
2. YAML rule содержит SELECT query, числовое условие и action; доступны параметры `session_id`, `user_id`, `channel`, `tool_name` и `now`.
3. После записи текущего события evaluator выполняет запрос и сравнивает числовое поле с порогом.
4. Shipped rules выявляют более 50 calls за минуту в session и более 20 вызовов одного tool за пять минут.
5. Каждые 100 событий удаляются записи старше часа; общий объём ограничен 10 000 строками.

## Зависимости

Встроенный `rusqlite` и синхронизация через mutex; отдельная база данных или внешний rate-limit service не нужны.

## Ограничения

Состояние живёт только в памяти одного процесса и теряется при рестарте; несколько replicas не разделяют counters. Shipped rules используют action `detect`, а не `block`, и не ограничивают токены или стоимость. SQL из policy доверенный и не sandboxed.

## Вердикт

**экспериментально** — полезный локальный механизм способа №11 для обнаружения bursts, но не распределённый и по умолчанию не enforcing.

## Связи

- Репозиторий: [[repo-108-parallax]]
