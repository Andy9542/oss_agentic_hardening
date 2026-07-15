---
type: repo-catalog
catalog-id: 37
method-id: 1
also-method-ids:
  - 2
  - 8
  - 9
  - 30
repo: https://github.com/meta-llama/PurpleLlama
language: Python
license: ""
verdict: prod
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-content-guardrails-ml
  - cluster-content-guardrails-mixed
---

# meta-llama/PurpleLlama — каталог №37

## Репозиторий

[meta-llama/PurpleLlama](https://github.com/meta-llama/PurpleLlama)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 1 |
| Тип | Вероятн. |
| Семейства | [[cluster-content-guardrails-ml]], [[cluster-content-guardrails-mixed]] |

## Принцип работы

LlamaFirewall, CodeShield, CyberSecEval

## Алгоритм

LlamaFirewall, CodeShield, CyberSecEval.

Каталожная заметка: основной механизм — **способ №1**; дополнительно перекрывает: способ №8, способ №9.

## Вариант в семействе

LlamaFirewall, CodeShield, CyberSecEval. Родственные реализации — только через семейства: ML content guardrails, смешанные guardrails.


## Детерминизм или машинное обучение

Тип из каталога: **Вероятн.**.

## Вердикт

**готово к продакшену** — каталожная оценка по зрелости репозитория в экосистеме.


## Детальные разборы

- [[impl-alignmentcheck-llamafirewall]]
- [[impl-codeshield]]
- [[promptguard2-prompt-injection]]


## Реализуемые способы

- [[01-классификация-инъекций-машинным-обучением]] — основной
- [[02-cot-reasoning-audit]]
- [[08-toxicity-moderation]]
- [[09-проверка-фактической-точности-и-галлюцинаций]]
- [[30-static-analysis-code]]
