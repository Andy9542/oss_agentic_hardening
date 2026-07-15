---
type: implementation-detail
parent-repo: repo-68-finbot-ctf
method-id: 44
repo: https://github.com/GenAI-Security-Project/finbot-ctf
language: Python
license: Apache-2.0
verdict: experimental
commit-sha: 1450fc4
commit-date: 2026-06-09
verified-date: 2026-07-15
tags:
  - agent-security
---

# OWASP FinBot CTF — Juice Shop для agentic AI

## Репозиторий

- [GenAI-Security-Project/finbot-ctf](https://github.com/GenAI-Security-Project/finbot-ctf)
- Проверенный срез: `1450fc4`; код проверен 2026-07-15.

## Что это за технология

**Intentionally vulnerable multi-agent fintech platform** (vendor onboarding, fraud, invoices, payments): portals Vendor/Admin/CTF; exploits via PI, policy bypass, tool poison, exfil, RCE; event-driven success detection (не static flags). Способ №44 (hands-on red team lab).

## Где в коде

- Platform app + challenge mappings to OWASP LLM/Agentic Top 10, CWE, ATLAS
- Live: owasp-finbot-ctf.org

## Алгоритм

1. Interact with FinBot agents via portals.
2. Craft injection/policy bypass payloads.
3. Platform detects successful exploit events.
4. Map challenge → OWASP IDs.

## Примеры реализации

Attack classes: prompt injection, policy bypass, tool poisoning, data exfiltration, RCE — auto-scored via event pipeline.

## Пример: вход → решение

- Inject into vendor chat → agent issues unauthorized payment → challenge solved event.
- Hardened policy → no event.

## Детерминизм или машинное обучение

Detection pipeline детерминирован; agent LLM — нет.

## Внешние зависимости

Hosted CTF or self-host; LLM backends.

## Ограничения

- Lab only — never expose secrets.
- Challenge set evolves.

## Сигналы качества

- OWASP GenAI; live site; multi-standard mapping.

## Вердикт

**экспериментально** — лучший hands-on agent CTF в каталоге.

## Связи

- Репозиторий: [[repo-68-finbot-ctf]]
