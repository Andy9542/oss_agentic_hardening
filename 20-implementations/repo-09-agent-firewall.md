---
type: repo-catalog
catalog-id: 9
method-id: 14
also-method-ids:
  - 12
repo: https://github.com/0xrem/agent-firewall
language: Unknown
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-tool-firewall-yaml
---

# 0xrem/agent-firewall — каталог №9

## Репозиторий

[0xrem/agent-firewall](https://github.com/0xrem/agent-firewall)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3 |
| Тип | Детерм. |
| Семейства | [[cluster-tool-firewall-yaml]] |

## Принцип работы

Pre-execution firewall: блокировка до выполнения

## Алгоритм

Pre-execution firewall: блокировка до выполнения.

Каталожная заметка: основной механизм — **способ №14**; дополнительно перекрывает: способ №12.

## Вариант в семействе

Лёгкий pre-execution firewall до выполнения. Родственные реализации — только через семейства: YAML-файрволы tools.


## Детерминизм или машинное обучение

Тип из каталога: **Детерм.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Детальные разборы

- [[agent-firewall-builtin-rules]]

## Реализуемые способы

- [[14-default-deny-allowlists]] — основной
- [[12-tool-policies-yaml-rego]]
