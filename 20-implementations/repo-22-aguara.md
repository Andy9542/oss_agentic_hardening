---
type: repo-catalog
catalog-id: 22
method-id: 27
also-method-ids:
  - 25
  - 26
  - 29
repo: https://github.com/garagon/aguara
language: Go
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-supply-chain-scanners
---

# garagon/aguara — каталог №22

## Репозиторий

[garagon/aguara](https://github.com/garagon/aguara)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 2 |
| Тип | Статич. |
| Семейства | [[cluster-supply-chain-scanners]] |

## Принцип работы

Go-сканер: паттерны, NLP, taint, rug-pull в навыках

## Алгоритм

Go-сканер: паттерны, NLP, taint, rug-pull в навыках.

Каталожная заметка: основной механизм — **способ №27**; дополнительно перекрывает: способ №26.

## Вариант в семействе

Go-сканер навыков: паттерны, NLP, rug-pull. Родственные реализации — только через семейства: сканеры supply chain.


## Детерминизм или машинное обучение

Тип из каталога: **Статич.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.


## Детальные разборы

- [[aguara-package-ci-scan]]
- [[aguara-rugpull]]
- [[aguara-skill-nlp-scan]]


## Реализуемые способы

- [[27-статическая-проверка-навыков-и-плагинов]] — основной
- [[25-контроль-целостности-описаний-инструментов]]
- [[26-tool-poisoning-scan]]
- [[29-проверка-зависимостей-ci-и-сценариев-установки]]
