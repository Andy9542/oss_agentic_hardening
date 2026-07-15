---
type: repo-catalog
catalog-id: 18
method-id: 12
also-method-ids:
  - 23
  - 26
  - 27
  - 31
  - 33
repo: https://github.com/cisco-ai-defense/defenseclaw
language: Unknown
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-governance-platform
  - cluster-tool-firewall-yaml
  - cluster-supply-chain-scanners
  - cluster-sandbox-isolation
  - cluster-egress-proxy-dlp
---

# cisco-ai-defense/defenseclaw — каталог №18

## Репозиторий

[cisco-ai-defense/defenseclaw](https://github.com/cisco-ai-defense/defenseclaw)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3+4 |
| Тип | Смешан. |
| Семейства | [[cluster-governance-platform]], [[cluster-tool-firewall-yaml]], [[cluster-supply-chain-scanners]], [[cluster-sandbox-isolation]], [[cluster-egress-proxy-dlp]] |

## Принцип работы

CodeGuard, песочница, SSRF-защита реестра, аудит

## Алгоритм

CodeGuard, песочница, SSRF-защита реестра, аудит.

Каталожная заметка: основной механизм — **способ №12**; дополнительно перекрывает: способ №27, способ №33, способ №23.

## Вариант в семействе

OpenClaw-стек: CodeGuard, sandbox, SSRF-защита. Родственные реализации — только через семейства: платформы governance, YAML-файрволы tools, сканеры supply chain, песочницы, egress/DLP-прокси.


## Детерминизм или машинное обучение

Тип из каталога: **Смешан.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.


## Детальные разборы

- [[defenseclaw-admission-enforcement]]
- [[defenseclaw-skill-scanner]]
- [[impl-defenseclaw]]


## Реализуемые способы

- [[12-tool-policies-yaml-rego]] — основной
- [[23-единый-прокси-исходящих-запросов-и-защита-от-ssrf]]
- [[26-tool-poisoning-scan]]
- [[27-статическая-проверка-навыков-и-плагинов]]
- [[31-допуск-артефактов-и-отзыв-по-чёрному-списку]]
- [[33-изоляция-агента-в-микровиртуальных-машинах-и-контейнерах]]
