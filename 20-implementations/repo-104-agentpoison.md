---
type: repo-catalog
catalog-id: 104
method-id: 46
repo: https://github.com/BillChan226/AgentPoison
language: Python
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-red-team
  - cluster-benchmarks
---

# BillChan226/AgentPoison — каталог №104

## Репозиторий

[BillChan226/AgentPoison](https://github.com/BillChan226/AgentPoison)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | — |
| Тип | Red team |
| Семейства | [[cluster-red-team]], [[cluster-benchmarks]] |

## Принцип работы

Red-team: backdoor через poisoning memory/RAG KB (NeurIPS 2024, arXiv:2407.12784)

## Алгоритм

Red-team: backdoor через poisoning memory/RAG KB (NeurIPS 2024, arXiv:2407.12784).

Каталожная заметка: основной механизм — **способ №46**.

## Вариант в семействе

Attack benchmark для memory poisoning; eval угрозы способа №46, не runtime-защита. Родственные реализации — только через семейства: red-team, benchmarks.

## Детерминизм или машинное обучение

Тип из каталога: **Red team**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Детальные разборы

- [[impl-agentpoison]]

## Реализуемые способы

- [[46-memory-protection]] — основной
