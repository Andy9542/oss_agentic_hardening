---
type: implementation-detail
parent-repo: repo-22-aguara
method-id: 27
repo: https://github.com/garagon/aguara
language: Go
license: Apache-2.0
verdict: experimental
commit-sha: f9283ce
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# Aguara — сканер навыков: patterns, decode, rug-pull

## Репозиторий

- [garagon/aguara](https://github.com/garagon/aguara)
- Проверенный срез: `f9283ce`; код проверен 2026-07-15.

## Что это за технология

**Статический Go-сканер** skill/MCP артефактов: regex/pattern engine с prefilter, multi-codec decode (base64/hex/url/unicode), NLP-сигналы и **rug-pull** (сравнение хеша содержимого между сканами). Способ №27 + №26.

## Где в коде

- `internal/engine/pattern/` — matcher, prefilter, decoder
- `internal/scanner/` — target walk, exemptions
- CLI: `cmd/aguara/commands/scan.go`
- Tests: `aguara_test.go` (RUGPULL_001)

## Алгоритм

1. Walk skill files; apply ignore globs.
2. Decode obfuscated spans (`base64Re`, `hexRe`, `unicodeEscapeRe`, …).
3. Pattern match compiled rules (strong vs weak patterns).
4. Если есть stateDir: сравнить previous hash → content change + dangerous patterns → RUGPULL_001.
5. Emit findings + optional redaction.

## Примеры реализации

Decoder (`decoder.go`):

```text
base64Re = [A-Za-z0-9+/]{40,}={0,2}
unicodeEscapeRe = (\\u[0-9a-fA-F]{4}){3,}
urlEncodedRe = (%[0-9a-fA-F]{2}){3,}
```

Secret-ish pattern (tests):

```text
(?i)["'][A-Z_]*(API[_-]?KEY|SECRET|TOKEN|PASSWORD|CREDENTIAL)[A-Z_]*["']\s*:\s*["'][a-zA-Z0-9_\-]{20,}["']
```

## Пример: вход → решение

- Skill добавил `exfiltrate` + curl после baseline → RUGPULL_001.
- Unchanged content → no rug-pull.

## Детерминизм или машинное обучение

Patterns/rug-pull **детерминированные**; NLP слой может быть смешанным.

## Внешние зависимости

Go binary; опциональный intel feed.

## Ограничения

- Нужен stateDir для rug-pull.
- Regex FP на легитимных config patterns (есть exemptions).

## Сигналы качества

- Fuzz + coverage CI; redaction tests.

## Вердикт

**экспериментально** — сильный skill supply-chain scanner.

## Связи

- Репозиторий: [[repo-22-aguara]]
