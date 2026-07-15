---
type: repo-catalog
catalog-id: 5
method-id: 14
also-method-ids:
  - 12
  - 21
repo: https://github.com/safe-agentic-world/nomos
language: Unknown
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-tool-firewall-yaml
  - cluster-tool-firewall-pdp
---

# safe-agentic-world/nomos — каталог №5

## Репозиторий

[safe-agentic-world/nomos](https://github.com/safe-agentic-world/nomos)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3 |
| Тип | Детерм. |
| Семейства | [[cluster-tool-firewall-yaml]], [[cluster-tool-firewall-pdp]] |

## Принцип работы

Политики ALLOW / DENY / REQUIRE_APPROVAL на уровне инструментов

## Алгоритм

Политики ALLOW / DENY / REQUIRE_APPROVAL на уровне инструментов.

Каталожная заметка: основной механизм — **способ №14**; дополнительно перекрывает: способ №12, способ №21.

## Вариант в семействе

Декларативные ALLOW/DENY/REQUIRE_APPROVAL на tools. Родственные реализации — только через семейства: YAML-файрволы tools, PDP-шлюзы.


## Детерминизм или машинное обучение

Тип из каталога: **Детерм.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Реализуемые способы

- [[14-default-deny-allowlists]] — основной
- [[12-tool-policies-yaml-rego]]
- [[21-одобрение-опасных-действий-человеком]]
