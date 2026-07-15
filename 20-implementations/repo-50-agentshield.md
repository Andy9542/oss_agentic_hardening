---
type: repo-catalog
catalog-id: 50
method-id: 12
also-method-ids:
  - 13
repo: https://github.com/AdityaBelhekar/AgentShield
language: Unknown
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-tool-firewall-pdp
  - cluster-tool-firewall-yaml
  - cluster-formal-policies
---

# AdityaBelhekar/AgentShield — каталог №50

## Репозиторий

[AdityaBelhekar/AgentShield](https://github.com/AdityaBelhekar/AgentShield)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3 |
| Тип | Детерм. |
| Семейства | [[cluster-tool-firewall-pdp]], [[cluster-tool-firewall-yaml]], [[cluster-formal-policies]] |

## Принцип работы

Runtime SDK: перехват вызовов в приложении

## Алгоритм

Runtime SDK: перехват вызовов в приложении.

Каталожная заметка: основной механизм — **способ №12**; дополнительно перекрывает: способ №13.

## Вариант в семействе

Runtime SDK: перехват вызовов (не путать с affaan-m/agentshield). Родственные реализации — только через семейства: PDP-шлюзы, YAML-файрволы tools, формальные политики.


## Детерминизм или машинное обучение

Тип из каталога: **Детерм.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Детальные разборы

- [[agentshield-belhekar-policy]]

## Реализуемые способы

- [[12-tool-policies-yaml-rego]] — основной
- [[13-проверка-аргументов-по-json-схеме]]
