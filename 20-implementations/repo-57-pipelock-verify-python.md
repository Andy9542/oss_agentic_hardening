---
type: repo-catalog
catalog-id: 57
method-id: 39
also-method-ids:
  - 23
repo: https://github.com/luckyPipewrench/pipelock-verify-python
language: Python
license: ""
verdict: experimental
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-egress-proxy-dlp
  - cluster-governance-platform
---

# luckyPipewrench/pipelock-verify-python — каталог №57

## Репозиторий

[luckyPipewrench/pipelock-verify-python](https://github.com/luckyPipewrench/pipelock-verify-python)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 2 |
| Тип | Детерм. |
| Семейства | [[cluster-egress-proxy-dlp]], [[cluster-governance-platform]] |

## Принцип работы

Верификатор криптографических квитанций Pipelock

## Алгоритм

Верификатор криптографических квитанций Pipelock.

Каталожная заметка: основной механизм — **способ №39**; дополнительно перекрывает: способ №23.

## Вариант в семействе

Верификатор криптографических квитанций Pipelock. Родственные реализации — только через семейства: egress/DLP-прокси, платформы governance.


## Детерминизм или машинное обучение

Тип из каталога: **Детерм.**.

## Вердикт

**экспериментально** — каталожная оценка по зрелости репозитория в экосистеме.

## Реализуемые способы

- [[39-неизменяемый-журнал-с-цепочкой-хешей-и-подписями]] — основной
- [[23-единый-прокси-исходящих-запросов-и-защита-от-ssrf]]
