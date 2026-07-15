---
type: repo-catalog
catalog-id: 118
method-id: 32
repo: https://github.com/perplexityai/bumblebee
language: Go
license: Apache-2.0
verdict: experimental
tags:
  - agent-security
  - repo-catalog
  - savedtg
  - review-2026
clusters:
  - cluster-artifact-trust
  - cluster-supply-chain-scanners
---

# perplexityai/bumblebee — каталог №118

## Репозиторий

[perplexityai/bumblebee](https://github.com/perplexityai/bumblebee), проверенная ревизия `d753592` от 2026-06-25.

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 2 |
| Тип | Детерм. |
| Семейства | [[cluster-artifact-trust]], [[cluster-supply-chain-scanners]] |

## Принцип работы

Read-only сенсор инвентаризирует пакеты, расширения, agent skills и MCP-конфигурации на developer endpoints и может сопоставлять записи с внешним exposure catalog.

## Алгоритм

Профиль задаёт корни обхода, специализированные парсеры извлекают идентичность компонентов из локальных метаданных, нормализованные записи выводятся как NDJSON, а точные совпадения с каталогом превращаются в findings. Основной и единственный каталожный механизм — **способ №32**.

## Вариант в семействе

Bumblebee отражает фактическое состояние developer endpoint, а не состав выпущенного артефакта. Он не запускает package managers и не читает исходный код.

## Детерминизм или машинное обучение

Полностью детерминированный Go-сканер без моделей и LLM-анализа.

## Вердикт

**экспериментально** — качественно протестированный inventory sensor для incident response; не является preventive control.

## Детальные разборы

- [[impl-bumblebee]]
- [[bumblebee-exposure-catalog]]
- [[bumblebee-snapshot-state]]

## Реализуемые способы

- [[32-aibom-inventory]] — основной
