---
type: repo-catalog
catalog-id: 2
method-id: 23
also-method-ids:
  - 3
  - 6
  - 7
  - 19
  - 25
  - 39
repo: https://github.com/luckyPipewrench/pipelock
language: Go
license: ""
verdict: prod
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-egress-proxy-dlp
  - cluster-content-guardrails-ml
  - cluster-governance-platform
---

# luckyPipewrench/pipelock — каталог №2

## Репозиторий

[luckyPipewrench/pipelock](https://github.com/luckyPipewrench/pipelock)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3+4 |
| Тип | Детерм. |
| Семейства | [[cluster-egress-proxy-dlp]], [[cluster-content-guardrails-ml]], [[cluster-governance-platform]] |

## Принцип работы

Прокси исходящего трафика: MCP, DLP, криптографические квитанции аудита

## Алгоритм

Прокси исходящего трафика: MCP, DLP, криптографические квитанции аудита.

Каталожная заметка: основной механизм — **способ №23**; дополнительно перекрывает: способ №6, способ №7, способ №19, способ №3, способ №39.

## Вариант в семействе

Эталон egress/DLP-прокси для MCP/HTTP/A2A. Родственные реализации — только через семейства: egress/DLP-прокси, ML content guardrails, платформы governance.


## Детерминизм или машинное обучение

Тип из каталога: **Детерм.**.

## Вердикт

**готово к продакшену** — каталожная оценка по зрелости репозитория в экосистеме.


## Детальные разборы

- [[pipelock-audit-receipts]]
- [[pipelock-dlp-secrets]]
- [[pipelock-egress-proxy]]
- [[pipelock-injection-heuristics]]
- [[pipelock-rugpull-hash]]
- [[pipelock-shell-rules]]


## Реализуемые способы

- [[23-единый-прокси-исходящих-запросов-и-защита-от-ssrf]] — основной
- [[03-правила-и-шаблоны-для-выявления-инъекций]]
- [[06-content-dlp-inspection]]
- [[07-выявление-секретов-в-тексте]]
- [[19-правила-против-инъекций-в-аргументах-инструментов]]
- [[25-контроль-целостности-описаний-инструментов]]
- [[39-неизменяемый-журнал-с-цепочкой-хешей-и-подписями]]
