---
type: implementation-detail
parent-repo: repo-99-presidio
method-id: 5
repo: https://github.com/microsoft/presidio
language: Python
license: MIT
verdict: prod
commit-sha: 0ac87d5
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# Presidio — выявление и анонимизация PII

## Репозиторий

- [microsoft/presidio](https://github.com/microsoft/presidio)
- Проверенный срез: `0ac87d5`, дата коммита 2026-07-15; код проверен 2026-07-15.

## Что это за технология

**PII detection + anonymization pipeline.** Presidio — набор сервисов Microsoft: **Analyzer** находит персональные данные в тексте, **Anonymizer** заменяет/маскирует их. Детекция комбинирует:

1. **Regex PatternRecognizer** — шаблоны для email, карт, телефонов и т.п.;
2. **Checksum / валидаторы** (например алгоритм Луна для карт);
3. **NER (spaCy / Transformers)** — именованные сущности (имена, локации);
4. **Контекстные слова** — повышают score, если рядом «visa», «email» и т.д.

Это не «магический LLM», а классический NLP+правила стек для DLP/PII (способ №5 / смежно №6).

## Где в коде

- Analyzer engine: `presidio-analyzer/presidio_analyzer/`
- Pattern base: `pattern_recognizer.py`, `pattern.py`
- Примеры recognizers: `predefined_recognizers/generic/credit_card_recognizer.py`, `email_recognizer.py`
- Anonymizer: `presidio-anonymizer/`
- Image redactor (отдельный пакет): `presidio-image-redactor/`

## Алгоритм

1. Текст попадает в `AnalyzerEngine.analyze(text, language, entities=…)`.
2. Каждый зарегистрированный recognizer возвращает `RecognizerResult` (entity_type, start, end, score).
3. PatternRecognizer: regex → кандидаты; опционально `validate_result` (Luhn и др.); контекст сдвигает score.
4. NLP recognizer добавляет сущности из модели.
5. Результаты дедуплицируются / ранжируются по score.
6. Anonymizer применяет операторы: `replace`, `mask`, `hash`, `encrypt`, `redact` по типу сущности.
7. На выходе — текст без (или с плейсхолдерами) PII и список найденных spans.

## Примеры реализации

Email (`email_recognizer.py`), score 0.5:

```text
\b((([!#$%&'*+\-/=?^_`{|}~\w])|… )[@]\w+(?:-+\w+)*(?:\.\w+(?:-+\w+)*)+)\b
```

Credit card (`credit_card_recognizer.py`), weak regex score 0.3 + **Luhn**:

```text
\b(?!1\d{12}(?!\d))((4\d{3})|(5[0-5]\d{2})|(6\d{3})|…)[- ]?(\d{3,4})[- ]?…
```

После матча `validate_result` снимает пробелы/дефисы и проверяет `checksum % 10 == 0`. Контекст: `credit`, `visa`, `mastercard`, `amex`…

## Пример: вход → решение

- Вход: `Contact jane.doe@contoso.com about invoice.` → entity `EMAIL_ADDRESS`, anonymize → `Contact <EMAIL_ADDRESS> about invoice.`
- Вход: `Card 4111-1111-1111-1111` → regex hit + Luhn OK → `CREDIT_CARD`; случайная 16-циферная без Luhn → отбрасывается валидатором.

## Детерминизм или машинное обучение

**Смешанный:** regex+checksum детерминированы; spaCy/transformer NER вероятностны.

## Внешние зависимости

- Python, spaCy models (локально)
- Опционально Transformers / Azure
- Отдельные контейнеры analyzer/anonymizer для сервиса

## Ограничения

- Языковое покрытие зависит от установленных моделей.
- Кастомные корпоративные ID нужно добавлять своими recognizers.
- Не защищает от tool-injection — только content DLP/PII слой.

## Сигналы качества

- Обширные unit-тесты recognizers; зрелый Microsoft OSS.
- Известные FN на нестандартных форматах и нелатинских именах без NLP-модели.

## Вердикт

**готово к продакшену** — де-факто стандарт open-source PII для LLM/агентных пайплайнов.

## Связи

- Репозиторий: [[repo-99-presidio]]
