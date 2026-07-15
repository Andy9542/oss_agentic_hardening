---
type: repo-catalog
catalog-id: 16
method-id: 16
also-method-ids:
  - 34
repo: https://github.com/eunomia-bpf/ActPlane
language: C/eBPF
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-os-isolation
---

# eunomia-bpf/ActPlane — каталог №16

## Репозиторий

[eunomia-bpf/ActPlane](https://github.com/eunomia-bpf/ActPlane)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 4 |
| Тип | Детерм. |
| Семейства | [[cluster-os-isolation]] |

## Принцип работы

eBPF-контроль потоков информации на уровне ОС

## Алгоритм

eBPF-контроль потоков информации на уровне ОС.

Каталожная заметка: основной механизм — **способ №16**; дополнительно перекрывает: способ №34.

## Вариант в семействе

eBPF-контроль потоков информации на уровне ОС. Родственные реализации — только через семейства: изоляция ОС (eBPF).


## Детерминизм или машинное обучение

Тип из каталога: **Детерм.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Реализуемые способы

- [[16-ifc-capability-taint]] — основной
- [[34-os-sandbox-openshell]]
