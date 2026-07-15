---
type: repo-catalog
catalog-id: 25
method-id: 27
also-method-ids:
  - 2
repo: https://github.com/cisco-ai-defense/skill-scanner
language: Unknown
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-supply-chain-scanners
  - cluster-content-guardrails-ml
---

# cisco-ai-defense/skill-scanner — каталог №25

## Репозиторий

[cisco-ai-defense/skill-scanner](https://github.com/cisco-ai-defense/skill-scanner)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 2 |
| Тип | Смешан. |
| Семейства | [[cluster-supply-chain-scanners]], [[cluster-content-guardrails-ml]] |

## Принцип работы

YARA + LLM-судья + dataflow для навыков Codex/Cursor

## Алгоритм

YARA + LLM-судья + dataflow для навыков Codex/Cursor.

Каталожная заметка: основной механизм — **способ №27**; дополнительно перекрывает: способ №2.

## Вариант в семействе

YARA + LLM-судья для навыков Codex/Cursor. Родственные реализации — только через семейства: сканеры supply chain, ML content guardrails.


## Детерминизм или машинное обучение

Тип из каталога: **Смешан.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Реализуемые способы

- [[27-статическая-проверка-навыков-и-плагинов]] — основной
- [[02-cot-reasoning-audit]]
