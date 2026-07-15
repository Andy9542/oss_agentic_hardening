---
type: repo-catalog
catalog-id: 94
method-id: 23
also-method-ids:
  - 12
repo: https://github.com/MukundaKatta/agentguard
language: Unknown
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-egress-proxy-dlp
  - cluster-tool-firewall-yaml
---

# MukundaKatta/agentguard — каталог №94

## Репозиторий

[MukundaKatta/agentguard](https://github.com/MukundaKatta/agentguard)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3 |
| Тип | Детерм. |
| Семейства | [[cluster-egress-proxy-dlp]], [[cluster-tool-firewall-yaml]] |

## Принцип работы

Контроль сетевого egress агента

## Алгоритм

Контроль сетевого egress агента.

Каталожная заметка: основной механизм — **способ №23**; дополнительно перекрывает: способ №12.

## Вариант в семействе

Контроль сетевого egress (не GoPlus agentguard). Родственные реализации — только через семейства: egress/DLP-прокси, YAML-файрволы tools.


## Детерминизм или машинное обучение

Тип из каталога: **Детерм.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Реализуемые способы

- [[23-единый-прокси-исходящих-запросов-и-защита-от-ssrf]] — основной
- [[12-tool-policies-yaml-rego]]
