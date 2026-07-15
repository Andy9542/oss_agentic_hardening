---
type: repo-catalog
catalog-id: 11
method-id: 12
also-method-ids:
  - 13
  - 18
  - 35
repo: https://github.com/Agentic-AI-Risk-Mitigation/Janus
language: Python
license: ""
verdict: prod
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-formal-policies
  - cluster-tool-firewall-yaml
---

# Agentic-AI-Risk-Mitigation/Janus — каталог №11

## Репозиторий

[Agentic-AI-Risk-Mitigation/Janus](https://github.com/Agentic-AI-Risk-Mitigation/Janus)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3 |
| Тип | Детерм. |
| Семейства | [[cluster-formal-policies]], [[cluster-tool-firewall-yaml]] |

## Принцип работы

Политики на границе вызова инструмента

## Алгоритм

Политики на границе вызова инструмента.

Каталожная заметка: основной механизм — **способ №12**; дополнительно перекрывает: способ №13, способ №18.

## Вариант в семействе

Политики и JSON Schema на границе tool-call. Родственные реализации — только через семейства: формальные политики, YAML-файрволы tools.


## Детерминизм или машинное обучение

Тип из каталога: **Детерм.**.

## Вердикт

**готово к продакшену** — каталожная оценка по зрелости репозитория в экосистеме.


## Детальные разборы

- [[janus-json-schema]]
- [[janus-workspace-jail]]


## Реализуемые способы

- [[12-tool-policies-yaml-rego]] — основной
- [[13-проверка-аргументов-по-json-схеме]]
- [[18-rebac-spicedb]]
- [[35-уровни-исполнения-и-изоляция-рабочего-каталога]]
