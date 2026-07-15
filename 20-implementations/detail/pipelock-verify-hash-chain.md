---
type: implementation-detail
parent-repo: repo-57-pipelock-verify-python
method-id: 39
repo: https://github.com/luckyPipewrench/pipelock-verify-python
language: Python
license: MIT
verdict: experimental
commit-sha: 5639739
commit-date: 2026-07-11
verified-date: 2026-07-15
tags:
  - agent-security
---

# pipelock-verify — проверка hash-chain evidence receipts

## Репозиторий

- [luckyPipewrench/pipelock-verify-python](https://github.com/luckyPipewrench/pipelock-verify-python)
- Проверенный срез: `5639739`; код проверен 2026-07-15.

## Что это за технология

**Верификатор** подписанных evidence receipts PipeLock: Ed25519 signatures, canonicalization, **hash chain** между событиями аудита агента. Trust anchors opt-in (`public_key_hex`). Способ №39.

## Где в коде

- `pipelock_verify/` — `verify`, `verify_evidence`, `evidence_receipt_hash`
- README — v0.2.0 chain mode rules; fuzz/

## Алгоритм

1. Загрузить receipt file / stream.
2. Canonicalize signing input; verify signature.
3. Chain mode: каждый next.hash связывается с previous; signer consistency.
4. Reject v2 in chain mode unless verify individually.

## Примеры реализации

```python
# Trust anchors opt-in
verify(..., public_key_hex=…)  # or trust embedded key
# chain mode enforces signer consistency across v1 receipts
# v0.2.0 rejects EvidenceReceipt v2 in chain mode
```

## Пример: вход → решение

- Tampered middle event → hash chain break → fail.
- Valid signed chain → verify OK.

## Детерминизм или машинное обучение

**Детерминированная** crypto verification.

## Внешние зависимости

Pure Python verify lib; keys from PipeLock emitters.

## Ограничения

- Нужен корректный emitter (PipeLock).
- Version skew v1/v2.

## Сигналы качества

- Fuzz targets; SECURITY.md; paired with PipeLock.

## Вердикт

**экспериментально** — audit integrity verifier.

## Связи

- Репозиторий: [[repo-57-pipelock-verify-python]]
