---
type: implementation-detail
parent-repo: repo-17-agentguard
method-id: 21
repo: https://github.com/GoPlusSecurity/agentguard
language: TypeScript
license: Apache-2.0
verdict: experimental
commit-sha: d18e142
commit-date: 2026-06-25
verified-date: 2026-07-15
tags:
  - agent-security
---

# AgentGuard — runtime hooks и default policies

## Репозиторий

- [GoPlusSecurity/agentguard](https://github.com/GoPlusSecurity/agentguard)
- Проверенный срез: `d18e142`, дата коммита 2026-06-25; код проверен 2026-07-15.

## Что это за технология

**Runtime hook interceptor** для OpenClaw/Hermes: на `before_tool_call` движок решает `allow` / `deny` / `confirm` по политике секретов, exec, сети и capability model навыка. Блокировка возвращает `{ block: true, blockReason }` в хук хоста. Это способ №21 (human approval) + default-deny exec.

## Где в коде

- `src/adapters/engine.ts` — решения deny по sensitive path / untrusted skill / capability
- `src/adapters/openclaw.ts` — мост `before_tool_call` / `after_tool_call`
- `src/policy/default.ts` — `DEFAULT_POLICIES`, `RESTRICTIVE_CAPABILITY`
- `src/utils/system-paths.ts` — block/require_approval для system paths
- `hooks/hooks.json` — регистрация хуков

## Алгоритм

1. Хук pre-tool получает tool name + args + initiating skill.
2. Проверка sensitive paths → deny critical.
3. Проверка trust/capabilities skill (network/fs/exec allowlists).
4. Применение `DEFAULT_POLICIES`: private_key/mnemonic → deny; exec_command → deny; body_contains_secret → deny; untrusted_domain → confirm.
5. Audit log; вернуть block или пропустить.

## Примеры реализации

```typescript
export const DEFAULT_POLICIES: PolicyConfig = {
  secret_exfil: { private_key: 'deny', mnemonic: 'deny', api_secret: 'confirm' },
  exec_command: 'deny',
  network: { untrusted_domain: 'confirm', body_contains_secret: 'deny' },
  web3: { unlimited_approval: 'confirm', unknown_spender: 'confirm', user_not_present: 'confirm' },
};

export const RESTRICTIVE_CAPABILITY = {
  network_allowlist: [],
  filesystem_allowlist: [],
  exec: 'deny',
  secrets_allowlist: [],
};
```

OpenClaw: blocking via `{ block: true, blockReason: "..." }` from `before_tool_call`.

## Пример: вход → решение

- Write to `~/.ssh/id_rsa` → deny `SENSITIVE_PATH`.
- `exec` без allow → deny.
- Network to untrusted domain → confirm (HITL).

## Детерминизм или машинное обучение

Политики **детерминированные**; сканер skills может быть смешанным (отдельный контур).

## Внешние зависимости

Node/TypeScript plugin в хост-агенте; без обязательного облака.

## Ограничения

- Работает только если хост вызывает hooks.
- Web3-акцент в default policy — не универсален для всех агентов.

## Сигналы качества

- Тесты Hermes plugin (`plugins/hermes/tests/`); skill docs.

## Вердикт

**экспериментально** — практичный hook-layer с жёстким default на exec/secrets.

## Связи

- Репозиторий: [[repo-17-agentguard]]
