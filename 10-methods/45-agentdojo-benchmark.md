---
type: method
id: 45
layer: tests
method-type: T
prod-viable: false
effectiveness: meta-tool
robustness: n/a
evidence-level: strong
status: reviewed
tags:
  - agent-security
  - odd-batch
  - benchmark
sources:
  - source-progent-paper
  - source-agentdojo-paper
covers:
  - ASI01
  - ASI02
  - ASI03
  - ASI04
  - ASI05
  - ASI06
  - ASI07
  - ASI08
  - ASI09
  - ASI10
  - LLM01
  - LLM02
  - LLM03
  - LLM04
  - LLM05
  - LLM06
  - LLM07
  - LLM08
  - LLM09
  - LLM10
---

# Эталонный бенчмарк AgentDojo (не защита)

## Определение

**AgentDojo** — среда **измерения**, не барьер в продакшене. 97 реалистичных задач (почта, банк, Slack…), 629 тестов безопасности, метрики:

- **ASR** — доля успешных атак (ниже = лучше защита).
- **Utility** — доля решённых легитимных задач (ниже = защита мешает работе).

## Как это работает

```
AgentDojo.run(агент, defense=progent) → отчёт: атаки прошли / нет, задачи решены / нет
```

Защита подключается как плагин; среда подставляет инъекции в сценарии.

## Опубликованные результаты (хаб доказательств)

| Защита | ASR на AgentDojo | Источник |
|--------|-------------------|----------|
| Без защиты (типично) | ~40% | `source-progent-paper` |
| Progent | ~40% → ~1% | `source-progent-paper` |
| CaMeL | существенное снижение indirect | статья CaMeL |

Использовать для **проверки claims** способов 1–43, не путать с prod-контролем.

## Реализации

> Реализации: поле `method-id` в frontmatter (`20-implementations/`), без wikilink.

```dataview
TABLE verdict AS "Вердикт", repo AS "Репозиторий"
FROM "20-implementations"
WHERE method-id = this.id
SORT file.name
```

## Покрытие рисков

Способ **не защищает** — измеряет. В матрице во всех строках стоит **мета**: бенчмарк даёт воспроизводимую оценку силы способов 1–43, но не является ячейкой защиты.

| Роль | Уровень | Почему |
|------|---------|--------|
| ASI01…ASI10, LLM01…LLM10 | **мета** | 97 задач, 629 security-тестов; метрики ASR и utility для сравнения защит (Progent ~1% ASR vs ~40% baseline). |

Коды в `covers:` означают «применим для **оценки** покрытия этого риска», не «закрывает риск».

## Дополняет

- способ №17 (формальные политики)
- способ №43 (indirect injection)
- способ №1 (ML-барьеры)

## Используется для оценки

- способ №17 (Progent), способ №43 (CaMeL) — см. `source-progent-paper`, `source-agentdojo-paper`

## Требует

- —

## Не заменяет

- любой runtime-способ — бенчмарк только измеряет, не защищает
