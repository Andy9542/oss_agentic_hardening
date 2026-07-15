---
type: implementation-detail
parent-repo: repo-13-avakill
method-id: 7
repo: https://github.com/log-bell/avakill
language: Go
license: Apache-2.0
verdict: experimental
commit-sha: 6b3d5d6
commit-date: 2026-03-10
verified-date: 2026-07-15
tags:
  - agent-security
---

# AvaKill — сканер секретов/PII/инъекций в shim

## Репозиторий

- [log-bell/avakill](https://github.com/log-bell/avakill)
- Проверенный срез: `6b3d5d6`, дата коммита 2026-03-10; код проверен 2026-07-15.

## Что это за технология

**YAML-политический shim** перед tools/MCP: Go-бинарник `avakill-shim` оценивает вызовы и **сканирует контент** regex-наборами secrets / PII / injection. Pre-filter (`strings.Contains`) ускоряет перед полным regex. Есть kill switch (глобальный deny). Способ №7 + №12.

## Где в коде

- `cmd/avakill-shim/scanner.go` — pattern defs + ScanContent
- `cmd/avakill-shim/evaluator.go` — policy decisions
- `cmd/avakill-shim/killswitch.go`
- `cmd/avakill-shim/shell_analysis.go`

## Алгоритм

1. Загрузить YAML policy (`default_action`, rules, custom_patterns).
2. На tool/response: Scanner.ScanContent(text).
3. Для каждой category: preFilter → regex → finding + action.
4. Kill switch engaged → deny независимо от rules.
5. Fail-closed на ошибках конфигурации/сканера.

## Примеры реализации

Secrets (`scanner.go`):

```text
AKIA[0-9A-Z]{16}                          # aws_access_key
gh[pos]_[A-Za-z0-9_]{36,}                 # github_token
sk-ant-[A-Za-z0-9_-]{90,}                 # anthropic_key
(?i)ignore\s+(?:all\s+)?(?:previous|prior|above)\s+instructions
(?i)<\s*IMPORTANT\s*>                     # important_tag
!\[[^\]]*\]\(https?://[^)\s]*            # markdown_exfil
```

PII: email, us_phone, ssn, credit_card.

## Пример: вход → решение

- Response содержит `AKIA…` → finding aws_access_key → deny/redact по action.
- Kill switch on → любой tool deny.
- Текст без паттернов + default allow → allow.

## Детерминизм или машинное обучение

**Детерминированный**.

## Внешние зависимости

Go shim; Python packaging wrappers в репозитории.

## Ограничения

- Regex FP на UUID-like heroku pattern и phone numbers.
- Нужна обязательная вставка shim в путь агента.

## Сигналы качества

- Обширные scanner_test.go / killswitch_test.go.

## Вердикт

**экспериментально** — крепкий regex scanner внутри policy shim.

## Связи

- Репозиторий: [[repo-13-avakill]]
