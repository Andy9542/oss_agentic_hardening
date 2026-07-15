---
type: repo-catalog
catalog-id: 17
method-id: 12
also-method-ids:
  - 19
  - 27
  - 38
repo: https://github.com/GoPlusSecurity/agentguard
language: Unknown
license: ""
verdict: prod
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-runtime-hooks
  - cluster-tool-firewall-yaml
  - cluster-supply-chain-scanners
---

# GoPlusSecurity/agentguard — каталог №17

## Репозиторий

[GoPlusSecurity/agentguard](https://github.com/GoPlusSecurity/agentguard)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3 |
| Тип | Детерм. |
| Семейства | [[cluster-runtime-hooks]], [[cluster-tool-firewall-yaml]], [[cluster-supply-chain-scanners]] |

## Принцип работы

Хуки в рантайме: сканирование навыков, блокировка опасных действий

## Алгоритм

Хуки в рантайме: сканирование навыков, блокировка опасных действий.

Каталожная заметка: основной механизм — **способ №12**; дополнительно перекрывает: способ №27.

## Вариант в семействе

Runtime hooks: сканирование навыков, блок опасных действий. Родственные реализации — только через семейства: runtime hooks, YAML-файрволы tools, сканеры supply chain.


## Детерминизм или машинное обучение

Тип из каталога: **Детерм.**.

## Вердикт

**готово к продакшену** — каталожная оценка по зрелости репозитория в экосистеме.


## Детальные разборы

- [[agentguard-runtime-hooks]]
- [[impl-agentguard-goplus]]


## Реализуемые способы

- [[12-tool-policies-yaml-rego]] — основной
- [[19-правила-против-инъекций-в-аргументах-инструментов]]
- [[27-статическая-проверка-навыков-и-плагинов]]
- [[38-skill-attribution]]
