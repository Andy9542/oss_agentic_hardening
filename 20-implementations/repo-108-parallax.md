---
type: repo-catalog
catalog-id: 108
method-id: 12
also-method-ids:
  - 3
  - 7
  - 11
  - 15
  - 19
  - 40
repo: https://github.com/agent-defense/parallax
language: Rust
license: Apache-2.0
verdict: experimental
tags:
  - agent-security
  - repo-catalog
  - review-2026
clusters:
  - cluster-tool-firewall-yaml
  - cluster-content-guardrails-mixed
  - cluster-runtime-hooks
  - cluster-observability
---

# agent-defense/parallax — каталог №108

## Репозиторий

- [agent-defense/parallax](https://github.com/agent-defense/parallax)
- Проверенный срез: [`c9c28face1e7426bb67ab03aa18f772ff7050fc5`](https://github.com/agent-defense/parallax/commit/c9c28face1e7426bb67ab03aa18f772ff7050fc5), 2026-06-05.
- Лицензия: [Apache-2.0](https://github.com/agent-defense/parallax/blob/c9c28face1e7426bb67ab03aa18f772ff7050fc5/LICENSE).

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 4 |
| Тип | Детерминированный PDP |
| Семейства | [[cluster-tool-firewall-yaml]], [[cluster-content-guardrails-mixed]], [[cluster-runtime-hooks]], [[cluster-observability]] |

## Принцип работы

Внешний Rust service принимает lifecycle events агента и прогоняет их через cost-ordered chain из regex, keyword, Sigma, CEL и stateful SQL evaluators, возвращая `allow`, `detect`, `redact` или `block`.

## Алгоритм

Интеграция отправляет `message.before`, `params.before`, `tool.before` и `tool.after` на `/evaluate`. Config loader собирает inline и auto-discovered YAML rules; evaluators исполняются от дешёвых к дорогим и останавливаются при `block`. Остальные результаты агрегируются по приоритету, пишутся в JSONL и при настройке отправляются webhook. Основной механизм — **способ №12**; дополнительно реализуются способы №3, №7, №11, №15, №19 и №40.

## Вариант в семействе

Parallax не встраивает модель и не требует Python/JVM: policy engine работает отдельным binary и подключается через HTTP, proxy или lifecycle hooks. Надёжность enforcement зависит от полноты событий и невозможности обойти интеграционный hook.

## Детерминизм или машинное обучение

Проверенный срез полностью детерминирован: regex, substring patterns, Sigma conditions, CEL-like expressions и SQLite queries. ML и LLM evaluators присутствуют только в cost taxonomy и roadmap.

## Вердикт

**экспериментально** — сильная reference-monitor архитектура и модульные rules, но ранняя версия, ограниченный Sigma/CEL dialect и hook-dependent coverage не дают production-гарантии.

## Детальные разборы

- [[impl-parallax]]
- [[parallax-secret-redaction]]
- [[parallax-sql-rate-limits]]

## Реализуемые способы

- [[12-tool-policies-yaml-rego]] — основной
- [[03-правила-и-шаблоны-для-выявления-инъекций]]
- [[07-выявление-секретов-в-тексте]]
- [[11-ограничение-токенов-расходов-и-частоты-вызовов]]
- [[15-правила-последовательности-вызовов-и-потоков-данных]]
- [[19-правила-против-инъекций-в-аргументах-инструментов]]
- [[40-opentelemetry-siem]]
