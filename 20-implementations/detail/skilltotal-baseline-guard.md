---
type: implementation-detail
parent-repo: repo-105-skilltotal
method-id: 29
mechanism-id: skilltotal-baseline-diff-guard
repo: https://github.com/pezhik/skilltotal
language: Python
license: Apache-2.0
verdict: experimental
tags:
  - agent-security
---

# SkillTotal — baseline, diff и install guard

## Проверенный срез

Upstream [`7905d363ef9bb525ebb119cbc008e961c4517a5f`](https://github.com/pezhik/skilltotal/commit/7905d363ef9bb525ebb119cbc008e961c4517a5f) от 2026-07-09.

## Кодовые пути

- `skilltotal/baseline.py` — стабильные fingerprints и suppression.
- `skilltotal/diff.py` — сравнение двух источников или сохранённых отчётов.
- `skilltotal/guard.py`, `skilltotal/policy.py`, `skilltotal/cli.py` — allow/block, rule policy и exit codes.
- `tests/test_baseline.py`, `tests/test_diff.py`, `tests/test_guard.py`, `tests/test_policy.py`.

## Алгоритм

Baseline вычисляет 16 hex-символов SHA-1 от `(rule_id, file, normalized snippet)` без номера строки и удаляет совпавшие evidence до score. Diff тем же fingerprint сопоставляет новые, закрытые и изменённые findings и может завершиться кодом 2 только для нового риска. Guard всегда блокирует malicious indicators и, в зависимости от `--block-on`, агрегированные bands `medium/high/critical`; одни capabilities не блокируют установку.

## Зависимости

Python stdlib; для Git URL нужен `git`, для `npm:`/`pypi:` — сетевой доступ на этапе получения пакета. SHA-1 здесь идентификатор дедупликации, а не security hash.

## Тесты

Unit tests проверяют устойчивость fingerprint к сдвигу строк, частичное suppression evidence, diff-классификацию, пороги guard и rule actions `block/warn/ignore`.

## Ограничения

Baseline может скрыть всё ещё опасный, но ранее принятый snippet; изменение форматирования snippet способно создать новый fingerprint. Guard доверяет качеству upstream scanners и не перехватывает установку сам — его exit code должен вызвать интегратор.

## Вердикт

**экспериментально** — практичный CI/admission primitive с ясной семантикой, но не криптографическая аттестация артефакта и не runtime enforcement.

## Связи

- Репозиторий: [[repo-105-skilltotal]]
