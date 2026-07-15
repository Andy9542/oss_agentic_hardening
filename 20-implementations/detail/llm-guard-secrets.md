---
type: implementation-detail
parent-repo: repo-40-llm-guard
method-id: 7
repo: https://github.com/protectai/llm-guard
language: Python
license: Apache-2.0
verdict: prod
commit-sha: 168c1034ffdb33837e7ae6fd6a16b80567c1be03
commit-date: 2026-07-09
verified-date: 2026-07-15
tags:
  - agent-security
---

# llm-guard — сканер секретов (detect-secrets)

## Репозиторий

- [protectai/llm-guard](https://github.com/protectai/llm-guard)
- Проверенный срез: `168c103`, дата коммита 2026-07-09; код проверен 2026-07-15.

## Что это за технология

Обёртка над **Yelp detect-secrets**: набор плагинов-детекторов (regex + эвристики), каждый ищет свой тип секрета в тексте. llm-guard подключает десятки детекторов (AWS, Stripe, JWT, кастомные в `secrets_plugins/`) и при нахождении может **реджектить** или **редактировать** (redact) промпт/ответ через Presidio `TextReplaceBuilder`.

Это способ №7 на стороне LLM gateway, дополняющий ML injection scanner.

## Где в коде

- `llm_guard/input_scanners/secrets.py` (и зеркало в output scanners)
- Плагины: `llm_guard/input_scanners/secrets_plugins/*.py`
- Зависимость: `detect_secrets` + опционально presidio anonymizer helpers

## Алгоритм

1. Сконфигурировать `SecretsCollection` с `transient_settings` и списком `plugins_used` (Softlayer, Stripe, AWSKey, JwtToken, PrivateKey, … + custom path `file://…/secrets_plugins`).
2. Записать текст во временный файл / scan string API detect-secrets.
3. Собрать найденные секреты (тип, значение, позиции).
4. Если секреты есть и режим redact — заменить spans на плейсхолдеры; иначе вернуть `is_valid=False`.
5. Risk score по факту наличия находок.

## Примеры реализации

Фрагмент конфига плагинов (`secrets.py`):

```python
_default_detect_secrets_config = {
    "plugins_used": [
        {"name": "AWSKeyDetector"},
        {"name": "StripeDetector"},
        {"name": "JwtTokenDetector"},
        {"name": "PrivateKeyDetector"},
        {"name": "DiscordBotTokenDetector"},
        {"name": "AdafruitKeyDetector", "path": _custom_plugins_path + "/adafruit.py"},
        # … десятки других
    ]
}
```

Кастомные плагины — отдельные regex-детекторы в `secrets_plugins/` (Airtable, Algolia, Age secret key и т.д.).

## Пример: вход → решение

- Вход: `My key is AKIA…` → AWSKeyDetector hit → invalid или redact `******`.
- Вход: обычный текст без токенов → valid.

## Детерминизм или машинное обучение

**Детерминированный** (regex/plugins); не нейросеть.

## Внешние зависимости

- Python пакеты `detect-secrets`, опционально `presidio-anonymizer`
- Без GPU

## Ограничения

- Те же, что у signature DLP: новые форматы ключей, фрагментация, encoding.
- False positives на тестовых/примерах ключей в документации.

## Сигналы качества

- Зрелая экосистема detect-secrets; llm-guard добавляет LLM-oriented API scan_prompt/scan_output.

## Вердикт

**готово к продакшену** — практичный secrets pre/post-filter рядом с PromptInjection scanner.

## Связи

- Репозиторий: [[repo-40-llm-guard]]
