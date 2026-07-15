---
type: implementation-detail
parent-repo: repo-35-skillguard
method-id: 27
repo: https://github.com/obielin/skillguard
language: Python
license: MIT
verdict: experimental
commit-sha: 3825721
commit-date: 2026-07-11
verified-date: 2026-07-15
tags:
  - agent-security
---

# SkillGuard — 12 regex-правил для SKILL.md

## Репозиторий

- [obielin/skillguard](https://github.com/obielin/skillguard)
- Проверенный срез: `3825721`; код проверен 2026-07-15.

## Что это за технология

**Zero-dependency Python scanner** навыков агента: чистые regex-правила (SG-001…SG-012) на prompt injection, exfil, lethal trifecta и др. CLI + SARIF. Способ №27.

## Где в коде

- `src/skillguard/rules.py` — все правила
- `src/skillguard/scanner.py`, `cli.py`
- Tests: `tests/test_skillguard.py`

## Алгоритм

1. `skillguard scan SKILL.md` / directory / stdin.
2. Каждое Rule.match(text) → snippets.
3. Фильтр `--min-severity`.
4. Вывод human / JSON / SARIF.

## Примеры реализации

SG-001 (`rules.py`):

```python
_PROMPT_INJECTION_PATTERNS = [
  r"ignore\s+(?:all\s+)?(?:previous|prior|above|earlier)\s+instructions?",
  r"disregard\s+(?:all\s+)?(?:previous|prior|above|earlier)\s+instructions?",
  r"jailbreak", r"DAN\s+mode",
  r"(?:bypass|override|disable)\s+(?:your\s+)?(?:safety|…)\s+(?:filter|…)",
]
# Rule id SG-001 severity CRITICAL
```

SG-002 exfil: `send|post|upload|exfiltrate` + secrets/env; curl/wget/socket.

## Пример: вход → решение

- `"Ignore all previous instructions"` → SG-001.
- `requests.post('http://…/exfil', …)` → SG-002/SG-003.

## Детерминизм или машинное обучение

**Детерминированный** regex.

## Внешние зависимости

Только stdlib.

## Ограничения

- Нет NLP/семантики; обход paraphrasing.
- 12 правил — узкий, но понятный baseline.

## Сигналы качества

- Тесты на каждый rule_id; SARIF.

## Вердикт

**экспериментально** — лёгкий pre-install skill gate.

## Связи

- Репозиторий: [[repo-35-skillguard]]
