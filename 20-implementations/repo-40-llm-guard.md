---
type: repo-catalog
catalog-id: 40
method-id: 1
also-method-ids:
  - 5
  - 6
  - 7
  - 8
  - 9
  - 10
repo: https://github.com/protectai/llm-guard
language: Python
license: ""
verdict: prod
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-content-guardrails-ml
---

# protectai/llm-guard — каталог №40

## Репозиторий

[protectai/llm-guard](https://github.com/protectai/llm-guard)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 1 |
| Тип | Вероятн. |
| Семейства | [[cluster-content-guardrails-ml]] |

## Принцип работы

Сканеры prompt injection, токсичности, секретов

## Алгоритм

Сканеры prompt injection, токсичности, секретов.

Каталожная заметка: основной механизм — **способ №1**; дополнительно перекрывает: способ №7, способ №8.

## Вариант в семействе

Эталон ML content guard от Protect AI. Родственные реализации — только через семейства: ML content guardrails.


## Детерминизм или машинное обучение

Тип из каталога: **Вероятн.**.

## Вердикт

**готово к продакшену** — каталожная оценка по зрелости репозитория в экосистеме.


## Детальные разборы

- [[impl-llm-guard-dlp]]
- [[impl-llm-guard-json]]
- [[impl-llm-guard-moderation]]
- [[llm-guard-anonymize]]
- [[llm-guard-factual-consistency]]
- [[llm-guard-prompt-injection]]
- [[llm-guard-secrets]]


## Реализуемые способы

- [[01-классификация-инъекций-машинным-обучением]] — основной
- [[05-выявление-и-маскирование-персональных-данных]]
- [[06-content-dlp-inspection]]
- [[07-выявление-секретов-в-тексте]]
- [[08-toxicity-moderation]]
- [[09-проверка-фактической-точности-и-галлюцинаций]]
- [[10-json-schema-constrained]]
