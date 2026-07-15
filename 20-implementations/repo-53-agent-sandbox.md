---
type: repo-catalog
catalog-id: 53
method-id: 33
also-method-ids:
  - 35
repo: https://github.com/kubernetes-sigs/agent-sandbox
language: Unknown
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-sandbox-isolation
---

# kubernetes-sigs/agent-sandbox — каталог №53

## Репозиторий

[kubernetes-sigs/agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 4 |
| Тип | Архит. |
| Семейства | [[cluster-sandbox-isolation]] |

## Принцип работы

K8s CRD для изоляции агентов

## Алгоритм

K8s CRD для изоляции агентов.

Каталожная заметка: основной механизм — **способ №33**; дополнительно перекрывает: способ №35.

## Вариант в семействе

K8s CRD для изоляции агентов. Родственные реализации — только через семейства: песочницы.


## Детерминизм или машинное обучение

Тип из каталога: **Архит.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Реализуемые способы

- [[33-изоляция-агента-в-микровиртуальных-машинах-и-контейнерах]] — основной
- [[35-уровни-исполнения-и-изоляция-рабочего-каталога]]
