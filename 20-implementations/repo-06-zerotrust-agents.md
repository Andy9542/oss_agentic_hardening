---
type: repo-catalog
catalog-id: 6
method-id: 12
also-method-ids:
  - 23
repo: https://github.com/lokeshsk/zerotrust-agents
language: Unknown
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-tool-firewall-pdp
  - cluster-tool-firewall-yaml
  - cluster-egress-proxy-dlp
---

# lokeshsk/zerotrust-agents — каталог №6

## Репозиторий

[lokeshsk/zerotrust-agents](https://github.com/lokeshsk/zerotrust-agents)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3 |
| Тип | Детерм. |
| Семейства | [[cluster-tool-firewall-pdp]], [[cluster-tool-firewall-yaml]], [[cluster-egress-proxy-dlp]] |

## Принцип работы

Zero-trust прокси между агентом и API

## Алгоритм

Zero-trust прокси между агентом и API.

Каталожная заметка: основной механизм — **способ №12**; дополнительно перекрывает: способ №23.

## Вариант в семействе

Zero-trust прокси между агентом и внешними API. Родственные реализации — только через семейства: PDP-шлюзы, YAML-файрволы tools, egress/DLP-прокси.


## Детерминизм или машинное обучение

Тип из каталога: **Детерм.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Детальные разборы

- [[zerotrust-agents-policy-dsl]]

## Реализуемые способы

- [[12-tool-policies-yaml-rego]] — основной
- [[23-единый-прокси-исходящих-запросов-и-защита-от-ssrf]]
