---
type: implementation-detail
parent-repo: repo-02-pipelock
method-id: 7
repo: https://github.com/luckyPipewrench/pipelock
language: Go
license: Apache-2.0
verdict: prod
commit-sha: 7a6f866752605215d2ee820eb10132d464626d49
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# Pipelock — DLP-шаблоны секретов

## Репозиторий

- [luckyPipewrench/pipelock](https://github.com/luckyPipewrench/pipelock)
- Проверенный срез: `7a6f866`, дата коммита 2026-07-15; код проверен 2026-07-15.

## Что это за технология

**DLP (Data Loss Prevention) на регулярных выражениях** — поиск известных форматов секретов (API keys, токены, connection strings) в URL, заголовках, телах запросов и MCP-аргументах *до* утечки наружу. Это способ №7 (секреты в тексте): не ML, а словарь высокосигнатурных префиксов (`sk-ant-`, `AKIA`, `ghp_`).

Pipelock прогоняет текст через `normalize.ForDLP` (снять exotic whitespace внутри ключей) и сопоставляет с `defaultDLPPatternSet`.

## Где в коде

- Реестр паттернов: `internal/config/dlp_patterns.go`
- Сканер URL/тела: `internal/scanner/` (`ScannerDLP`, `text_dlp.go`)
- Нормализация для DLP: `internal/normalize/normalize.go` → `ForDLP`, `StripExoticWhitespace`
- Тесты/фикстуры: `sdk/conformance/testdata/corpus/golden/03-block-dlp-aws-key.json`

## Алгоритм

1. Извлечь сканируемый текст (URL query, body, header, MCP args).
2. `ForDLP`: убрать exotic whitespace (NBSP внутри `sk-pr\u00A0oj-…` → `sk-proj-…`), NFKC, control chars.
3. Keyword/pre-filter по литеральным префиксам (ускорение).
4. Полный regex match → severity (critical/high) → block/warn в зависимости от поверхности (URL enforce vs body action).
5. Исключения: `ExemptDomains` для легитимной отправки ключа провайдеру; SigV4 structural exemption для presigned URL.

## Примеры реализации

Из `dlp_patterns.go`:

| Имя | Regex | Severity |
|-----|-------|----------|
| Anthropic API Key | `sk-ant-[a-zA-Z0-9\-_]{20,}\b` | critical |
| OpenAI API Key | `sk-proj-[a-zA-Z0-9\-_]{20,}\b` | critical |
| AWS Access ID | `AWSAccessIDRegex` (AKIA/ASIA/… + 16+) | critical |
| GitHub Token | `gh[pousr]_[A-Za-z0-9_]{36,}` | critical |
| GitLab PAT | `glpat-[a-zA-Z0-9\-_]{20,}` | critical |
| Stripe Key | `[sr]k[-_](live\|test)[-_][a-zA-Z0-9]{20,}` | critical |
| PostgreSQL DSN | `postgres(?:ql)?://[^:/?#\s]*:[^@/?#\s]+@` | critical |
| Google API Key | `AIza[0-9A-Za-z\-_]{35}\b` | high |

## Пример: вход → решение

- URL с `?key=sk-ant-api03-…` → DLP hit Anthropic → **block** (типичный golden-тест).
- `postgres://user:s3cret@db.internal/app` → hit connection string → block.
- Presigned S3 URL с `AKIA…` внутри SigV4 credential → structural exemption (не long-lived leak).

## Детерминизм или машинное обучение

Полностью **детерминированный**.

## Внешние зависимости

Нет. Локальные regex в бинарнике.

## Ограничения

- Не ловит произвольные high-entropy секреты без префикса (частично компенсирует entropy scanner).
- Новые форматы ключей требуют обновления реестра.
- Обход: фрагментация секрета по чанкам / encoding вне decode-pass.

## Сигналы качества

- Conformance corpus с golden block-dlp; drift-тесты пресетов.
- Документированные exempt/structural carve-outs.

## Вердикт

**готово к продакшену** — плотный детерминированный DLP-слой для агентного egress.

## Связи

- Репозиторий: [[repo-02-pipelock]]
