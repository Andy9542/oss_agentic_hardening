---
type: repo-catalog
catalog-id: 38
method-id: 42
also-method-ids:
  - 1
  - 3
  - 5
  - 9
repo: https://github.com/NVIDIA-NeMo/Guardrails
language: Python
license: ""
verdict: prod
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-content-guardrails-mixed
  - cluster-content-guardrails-ml
---

# NVIDIA-NeMo/Guardrails — каталог №38

## Репозиторий

[NVIDIA-NeMo/Guardrails](https://github.com/NVIDIA-NeMo/Guardrails)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 1 |
| Тип | Смешан. |
| Семейства | [[cluster-content-guardrails-mixed]], [[cluster-content-guardrails-ml]] |

## Принцип работы

Программируемые рельсы на Colang

## Алгоритм

Программируемые рельсы на Colang.

Каталожная заметка: основной механизм — **способ №42**; дополнительно перекрывает: способ №1, способ №5.

## Вариант в семействе

Программируемые рельсы на Colang (NeMo). Родственные реализации — только через семейства: смешанные guardrails, ML content guardrails.


## Детерминизм или машинное обучение

Тип из каталога: **Смешан.**.

## Вердикт

**готово к продакшену** — каталожная оценка по зрелости репозитория в экосистеме.


## Детальные разборы

- [[impl-nemo-guardrails]]
- [[nemo-fact-hallucination-rails]]
- [[nemo-jailbreak-heuristics]]
- [[nemo-mask-pii]]


## Реализуемые способы

- [[42-colang-dialog-rails]] — основной
- [[01-классификация-инъекций-машинным-обучением]]
- [[03-правила-и-шаблоны-для-выявления-инъекций]]
- [[05-выявление-и-маскирование-персональных-данных]]
- [[09-проверка-фактической-точности-и-галлюцинаций]]
