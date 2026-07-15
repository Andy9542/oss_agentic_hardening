---
type: implementation-detail
parent-repo: repo-32-clawsec
method-id: 27
repo: https://github.com/prompt-security/clawsec
language: TypeScript
license: Apache-2.0
verdict: experimental
commit-sha: 77fe4c8
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# ClawSec — suite security-навыков для OpenClaw

## Репозиторий

- [prompt-security/clawsec](https://github.com/prompt-security/clawsec)
- Проверенный срез: `77fe4c8`; код проверен 2026-07-15.

## Что это за технология

**Набор security skills** (не классический library firewall): навыки сканирования deps/SAST/DAST, advisories, signing — подключаются к OpenClaw/NanoClaw/Hermes как agent skills. CVE polling из NVD. Способ №27 в форме skill suite + политики.

## Где в коде

- Skills tree (scanner, advisories) per CONTRIBUTING layout `skills/*/skill.json`
- `clawsec-signing-public.pem`
- Site/app: `App.tsx`, advisories/
- CI: poll-nvd-cves workflow

## Алгоритм

1. Install ClawSec skills into OpenClaw skill dir.
2. Agent invokes scanner skill on project/MCP.
3. Rules from skill `config/rules.json` + advisories DB.
4. Optional signature verification of skill packages.
5. Report to operator / block via agent policy.

## Примеры реализации

Skill layout (CONTRIBUTING):

```text
skills/simple-scanner/
  skill.json
  config/rules.json
```

Scanner skill: deps + SAST + OpenClaw DAST.

## Пример: вход → решение

- Agent runs clawsec-scanner on MCP server → vulnerability findings in chat.
- Unsigned skill → signature check fail.

## Детерминизм или машинное обучение

Сканерные skills в основном детерминированы; агентная оркестрация — нет.

## Внешние зависимости

OpenClaw-compatible runtime; Node for site/skills tooling.

## Ограничения

- Зависит от корректной установки skills в агент.
- Не заменяет OS sandbox.

## Сигналы качества

- Prompt Security; multi-language docs; NVD poll CI.

## Вердикт

**экспериментально** — security-as-skills модель для OpenClaw family.

## Связи

- Репозиторий: [[repo-32-clawsec]]
