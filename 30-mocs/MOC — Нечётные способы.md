# Карта нечётных способов

Правила связей и фильтры графа: `30-mocs/Правила связей.md` (мета-документ, без wikilink — иначе хаб на графе).

23 способа из сводной таблицы [[all-methods-top-20#Сводка полный перечень способов (уникальные классы)]].

## Таблица (Dataview)

```dataview
TABLE layer AS "Слой", method-type AS "Тип", effectiveness AS "Эффект.", robustness AS "Прочн.", evidence-level AS "Доказат.", status AS "Статус"
FROM "10-methods"
WHERE contains(tags, "odd-batch")
SORT id asc
```

**Расшифровка полей:** эффект. = эффективность; прочн. = прочность; доказат. = уровень доказательств.

## Навигация по способам

| № | Способ | Слой | Заметка |
|---|--------|------|---------|
| 1 | ML-классификация инъекций | Текст | [[01-ml-injection-classifier]] |
| 3 | Эвристики и regex | Текст | [[03-heuristics-regex-injection]] |
| 5 | Маскирование ПДн | Текст | [[05-pii-masking-detection]] |
| 7 | Детекция секретов | Текст | [[07-secrets-detection-text]] |
| 9 | Проверка фактов / галлюцинации | Текст | [[09-factcheck-hallucination]] |
| 11 | Лимиты токенов и стоимости | Действие | [[11-rate-cost-token-limits]] |
| 13 | Схема JSON / типизация | Действие | [[13-json-schema-args]] |
| 15 | Правила потоков | Действие | [[15-flow-rules]] |
| 17 | SMT / монотонные привилегии | Действие | [[17-smt-monotonic-privilege]] |
| 19 | SQL/shell/path инъекции | Действие | [[19-injection-rules-args]] |
| 21 | Человек в контуре | Действие | [[21-human-in-the-loop]] |
| 23 | Прокси и SSRF | Сеть | [[23-egress-proxy-ssrf]] |
| 25 | Rug-pull / хеш baseline | Цепочка поставок | [[25-rugpull-hash-baseline]] |
| 27 | Статическое сканирование навыков | Цепочка поставок | [[27-skill-static-scan]] |
| 29 | Пакеты и CI | Цепочка поставок | [[29-package-ci-hooks]] |
| 31 | Admission и blocklist | Цепочка поставок | [[31-admission-blocklist]] |
| 33 | microVM / контейнер | Инфра | [[33-microvm-container]] |
| 35 | Кольца / тюрьма каталога | Инфра | [[35-execution-rings-jail]] |
| 37 | Поведенческая аномалия | Поведение | [[37-behavioral-anomaly]] |
| 39 | Цепочка хешей / подписи | Аудит | [[39-hash-chained-audit]] |
| 41 | Compliance mapping | Аудит | [[41-compliance-mapping]] |
| 43 | Две LLM + карантин | Архитектура | [[43-dual-llm-quarantine]] |
| 45 | Бенчмарк AgentDojo | Тесты | [[45-agentdojo-benchmark]] |

## Легенда типов (в frontmatter: method-type)

| Код | Значение |
|-----|----------|
| D | Детерминированный |
| V | Вероятностный (ML) |
| S | Смешанный |
| A | Архитектурный |
| T | Тестирование |
