---
type: implementation-detail
parent-repo: repo-60-asamm
method-id: 41
repo: https://github.com/scadastrangelove/asamm
language: Markdown
license: CC-BY-SA-4.0
verdict: experimental
commit-sha: 31c9d19
commit-date: 2026-06-28
verified-date: 2026-07-15
tags:
  - agent-security
---

# Agentic SAMM (ASAMM) — 21 контроля зрелости агентов

## Репозиторий

- [scadastrangelove/asamm](https://github.com/scadastrangelove/asamm)
- Проверенный срез: `31c9d19`; код проверен 2026-07-15.

## Что это за технология

**Фреймворк зрелости** (не runtime): расширение OWASP SAMM под agentic systems — taxonomy угроз по entry points, 21 control в 5 function families, maturity L1–L3, audit tracks. Способ №41 (сопоставление с требованиями стандартов).

## Где в коде

- `controls/*.md` — 21 контроль (AG/AI/AO/AV…)
- `part2-greenfield.md`, `audit/`, PDF assets

## Алгоритм

1. Выбрать adoption path (migrate / greenfield).
2. Оценить controls по L1/L2/L3 evidence.
3. Map gaps → roadmap.
4. Audit track по evidence (registry, approvals, …).

## Примеры реализации

`controls/AG-02.md` Tool Registry Governance:

```text
L1: enumerate tools/MCP + owner + access policy
L2: risk tiers always/conditional/prohibited + approval
L3: versioned registry; additions → threat model; remove unused
Evidence: registry; prohibited tools blocked without exception
```

Threat coverage tags C2, C4 на control.

## Пример: вход → решение

- Org без tool inventory → AG-02 = L0 → gap.
- Versioned MCP registry + risk tiers → L2/L3.

## Детерминизм или машинное обучение

Документный framework — **детерминированные** критерии evidence.

## Внешние зависимости

Нет runtime; human audit.

## Ограничения

- Не enforce сам по себе.
- Нужна интерпретация под org.

## Сигналы качества

- OWASP SAMM lineage; multi-language PDFs; structured controls.

## Вердикт

**экспериментально** — сильный governance map для agent programs.

## Связи

- Репозиторий: [[repo-60-asamm]]
