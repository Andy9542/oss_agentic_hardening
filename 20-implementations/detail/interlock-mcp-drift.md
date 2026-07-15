---
type: implementation-detail
parent-repo: repo-14-interlock
method-id: 25
repo: https://github.com/MaazAhmed47/Interlock
language: Python
license: Apache-2.0
verdict: experimental
commit-sha: 4dafd72
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# Interlock — целостность MCP tool surface (drift)

## Репозиторий

- [MaazAhmed47/Interlock](https://github.com/MaazAhmed47/Interlock)
- Проверенный срез: `4dafd72`, дата коммита 2026-07-15; код проверен 2026-07-15.

## Что это за технология

**Контроль целостности описаний MCP tools** (способ №25): фиксируется approved hash поверхности инструментов; при runtime сравнивается current hash. Расхождение = **drift** (rug-pull / poisoned tool descriptors). Дополнительно нормализуются MCP annotations в policy vocabulary и hash-chain audit.

## Где в коде

- `core/tool_surface_interop.py` — `VERDICT_DRIFTED`, `project_drift_record`
- `core/tool_metadata.py` — нормализация MCP annotations
- `core/drift_evidence.py`, `core/receipt_verify.py`
- `core/url_security.py` — SSRF/outbound URL guards
- Demo proof packs: `demo/run_*_proof_pack.py`

## Алгоритм

1. Зафиксировать baseline: hash approved tool surface (names+schemas+annotations).
2. При list/call tools — вычислить current surface hash.
3. Если hashes различаются → verdict `drifted` + evidence record.
4. Audit в hash-chained `mcp_audit_log`; verify receipts.
5. Policy может блокировать выполнение после drift.

## Примеры реализации

```python
VERDICT_DRIFTED = "drifted"
# project_drift_record maps approved_surface_hash vs current_surface_hash
# finding_types from drift_record → interop digest
```

URL guard: в hosted mode private/outbound hosts блокируются (`url_security.py`).

## Пример: вход → решение

- MCP server меняет description tool `transfer_funds` → hash mismatch → drifted → block.
- Неизменная поверхность → allow (при прочих политиках).

## Детерминизм или машинное обучение

Хеши/сравнение **детерминированные**.

## Внешние зависимости

Python runtime; опционально Supabase/demo infra.

## Ограничения

- Не заменяет semantic scan содержимого args.
- Baseline нужно обновлять осознанно при легитимных изменениях.

## Сигналы качества

- Множество live proof packs; SECURITY.md.

## Вердикт

**экспериментально** — сильный фокус на MCP descriptor integrity.

## Связи

- Репозиторий: [[repo-14-interlock]]
