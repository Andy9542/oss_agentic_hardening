---
type: repo-catalog
catalog-id: 99
method-id: 5
also-method-ids:
  - 6
repo: https://github.com/microsoft/presidio
language: Python
license: ""
verdict: prod
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-content-guardrails-mixed
  - cluster-egress-proxy-dlp
---

# microsoft/presidio — каталог №99

## Репозиторий

[microsoft/presidio](https://github.com/microsoft/presidio)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 1 |
| Тип | Детерм. |
| Семейства | [[cluster-content-guardrails-mixed]], [[cluster-egress-proxy-dlp]] |

## Принцип работы

Детекция и анонимизация ПДн в потоках агента

## Алгоритм

Детекция и анонимизация ПДн в потоках агента.

Каталожная заметка: основной механизм — **способ №5**; дополнительно перекрывает: способ №6.

## Вариант в семействе

Детекция и анонимизация ПДн. Родственные реализации — только через семейства: смешанные guardrails, egress/DLP-прокси.


## Детерминизм или машинное обучение

Тип из каталога: **Детерм.**.

## Вердикт

**готово к продакшену** — каталожная оценка по зрелости репозитория в экосистеме.


## Детальные разборы

- [[impl-presidio]]


## Реализуемые способы

- [[05-выявление-и-маскирование-персональных-данных]] — основной
- [[06-content-dlp-inspection]]
