---
type: repo-catalog
catalog-id: 32
method-id: 27
also-method-ids:
  - 12
repo: https://github.com/prompt-security/clawsec
language: Unknown
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-tool-firewall-yaml
  - cluster-supply-chain-scanners
---

# prompt-security/clawsec — каталог №32

## Репозиторий

[prompt-security/clawsec](https://github.com/prompt-security/clawsec)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3 |
| Тип | Смешан. |
| Семейства | [[cluster-tool-firewall-yaml]], [[cluster-supply-chain-scanners]] |

## Принцип работы

Набор security-навыков для OpenClaw-семейства

## Алгоритм

Набор security-навыков для OpenClaw-семейства.

Каталожная заметка: основной механизм — **способ №27**; дополнительно перекрывает: способ №12.

## Вариант в семействе

Security-навыки для OpenClaw (policy-as-skill). Родственные реализации — только через семейства: YAML-файрволы tools, сканеры supply chain.


## Детерминизм или машинное обучение

Тип из каталога: **Смешан.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Реализуемые способы

- [[27-статическая-проверка-навыков-и-плагинов]] — основной
- [[12-tool-policies-yaml-rego]]
