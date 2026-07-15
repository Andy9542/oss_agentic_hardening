---
type: repo-catalog
catalog-id: 103
method-id: 34
repo: https://github.com/NVIDIA/OpenShell
language: Python/Go
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-sandbox-isolation
  - cluster-os-isolation
---

# NVIDIA/OpenShell — каталог №103

## Репозиторий

[NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 4 |
| Тип | Архит. |
| Семейства | [[cluster-sandbox-isolation]], [[cluster-os-isolation]] |

## Принцип работы

OS-level sandbox: YAML-политики на FS/сеть/syscall, gateway + k3s harness

## Алгоритм

OS-level sandbox: YAML-политики на FS/сеть/syscall, gateway + k3s harness.

Каталожная заметка: основной механизм — **способ №34**.

## Вариант в семействе

Runtime NVIDIA для coding-агентов; эталон способа №34 (OS sandbox). Родственные реализации — только через семейства: sandbox-isolation, os-isolation.

## Детерминизм или машинное обучение

Тип из каталога: **Архит.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Детальные разборы

- [[impl-openshell]]

## Реализуемые способы

- [[34-os-sandbox-openshell]] — основной
