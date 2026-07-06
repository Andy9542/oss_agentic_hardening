---
type: method
id: 29
layer: supply-chain
method-type: D
prod-viable: true
effectiveness: medium
robustness: medium
evidence-level: moderate
status: reviewed
tags:
  - agent-security
  - odd-batch
  - supply-chain
covers:
  - ASI04
  - LLM03
  - LLM04
---

# Сканирование пакетов, CI и install-хуков

## Определение

Анализ **зависимостей** репозитория агента и **скриптов жизненного цикла** пакетов (postinstall npm, setup.py) и **GitHub Actions** до деплоя.

## Как это работает пошагово

1. Парсинг **lockfile** (package-lock.json, poetry.lock, go.sum…).
2. Поиск **install hooks** — `postinstall`, `preinstall` с подозрительным кодом.
3. **ci-trust** — опасные триггеры (`pull_request_target`), злоупотребление OIDC.
4. **Flow-sensitive** анализ `build.rs`, `setup.py` на exfil.
5. Отчёт в CI → fail merge при критических находках.

## От чего защищает

- Компрометация npm/PyPI пакета, typosquatting.
- Вредоносный postinstall при `npm install` на машине разработчика.
- Supply chain через CI.

## От чего НЕ защищает

- Рантайм агента после чистой установки.
- `pip install` **внутри** песочницы агента.

## Реализации

> Реализации: поле `method-id` в frontmatter (`20-implementations/`), без wikilink.

```dataview
TABLE verdict AS "Вердикт", repo AS "Репозиторий"
FROM "20-implementations"
WHERE method-id = this.id
SORT file.name
```


## Покрытие рисков

| Риск | Сценарий в матрице | Уровень | Почему такая оценка |
|------|--------------------|---------|---------------------|
| ASI04 | ↳ вредонос в пакетах и CI | **выс.** | install-хуки, typosquatting, опасные GitHub Actions — основной сценарий aguara/snyk в CI. |
| ASI04 | Отравление обучения / артефактов | **выс.** | Контроль артефактов в репозитории и lockfile до попадания в среду обучения/деплоя. |
| ASI04 | ↳ rug-pull MCP | **—** | CI не видит смену `tools/list` после деплоя — зона №25/№31. |
| LLM03 / LLM04 | Supply chain / poisoning | **выс.** | Прямое соответствие OWASP; shift-left до рантайма. |

## Оценка эффективности

**Уровень:** средний

**Обоснование:** Стандарт DevSecOps для agent repos; силён до деплоя, слаб после.

## Оценка прочности

**Уровень:** средний — не покрывает рантайм и `pip install` внутри песочницы агента.

## Дополняет

- способ №27 (CI-скан)
- способ №25 (хеш baseline)

## Требует

- —

## Не заменяет

- способ №31 (блок admission и revoke в рантайме)
