---
type: implementation-detail
parent-repo: repo-34-repo-forensics
method-id: 27
repo: https://github.com/alexgreensh/repo-forensics
language: Python/Shell
license: Apache-2.0
verdict: experimental
commit-sha: f3e5fc0
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# repo-forensics — IOC + skill-scan (26 scanners)

## Репозиторий

- [alexgreensh/repo-forensics](https://github.com/alexgreensh/repo-forensics)
- Проверенный срез: `f3e5fc0`; код проверен 2026-07-15.

## Что это за технология

**Глубокий forensics-сканер** репозиториев, AI skills и MCP: набор из ~26 статических сканеров (IOC DB, archive/bytecode decode-and-rescan, dead_anchors / SkillJacking). Режим `--skill-scan` сужает до skill-поверхности. Хуки PreToolUse/PostToolUse для coding-агентов (pip/npm/git pull). Способ №27.

## Где в коде

- `action.yml` — GitHub Action (`full` / `skill-scan`)
- `skills/repo-forensics/scripts/run_forensics.sh`
- `data/rulepacks/dead_anchors.json`
- `iocs/`, `hooks/`

## Алгоритм

1. Выбрать mode: full audit или `--skill-scan`.
2. Опционально обновить IOC/rulepack cache.
3. Пройти сканеры (текст, архивы, bytecode, decode-and-rescan, dead anchors).
4. PreToolUse: IOC gate до install; PostToolUse: auto-scan после install/pull.
5. Fail CI / block agent tool при severity.

## Примеры реализации

Action flags (`action.yml`):

```yaml
mode: full | skill-scan
# skill-scan → ARGS+=("--skill-scan")
```

Обходы, закрытые в CHANGELOG: content-based archives, bytecode poisoning, decode-and-rescan.

## Пример: вход → решение

- Skill ссылается на claimable npm package (dead_anchors) → finding.
- `uv sync` после pull → PostToolUse scan на working dir.

## Детерминизм или машинное обучение

**Детерминированный** signature/IOC scan.

## Внешние зависимости

Python 3; optional IOC feed update; GitHub Action.

## Ограничения

- Signature freshness зависит от IOC updates.
- Не runtime sandbox.

## Сигналы качества

- Обширный CHANGELOG по scanner-bypass; Action + hooks.

## Вердикт

**экспериментально** — сильный skill/repo forensics toolkit.

## Связи

- Репозиторий: [[repo-34-repo-forensics]]
