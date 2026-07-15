---
type: implementation-detail
parent-repo: repo-94-agentguard
method-id: 23
repo: https://github.com/MukundaKatta/agentguard
language: TypeScript/JavaScript
license: MIT
verdict: experimental
commit-sha: b42366e
commit-date: 2026-05-16
verified-date: 2026-07-15
tags:
  - agent-security
---

# agentguard (MukundaKatta) — fetch allowlist firewall

## Репозиторий

- [MukundaKatta/agentguard](https://github.com/MukundaKatta/agentguard)
- Проверенный срез: `b42366e`; код проверен 2026-07-15.

## Что это за технология

**Egress firewall** для агентов: `policy({network:{allow,deny,methods}, budget})` + `firewall(policy, fn)` патчит `globalThis.fetch` (или `wrapFetch` для SDK). Deny > allow; `PolicyViolation` / 403. Не путать с GoPlus agentguard. Способ №23.

## Где в коде

- `src/index.js` / `index.d.ts` — policy, firewall, wrapFetch, check
- `examples/demo-block.js`

## Алгоритм

1. Declare allowlist hosts (`api.openai.com`, `*.example.com`).
2. `await firewall(safe, () => agent.run(…))`.
3. Each fetch checked; budget maxRequests enforced.
4. Outside allowlist → throw or 403.

## Примеры реализации

```js
const safe = policy({
  network: {
    allow: ['api.openai.com', 'api.anthropic.com', '*.example.com'],
    methods: ['GET', 'POST'],
  },
  budget: { maxRequests: 50 },
  violations: 'throw', // or 'block'
});
await firewall(safe, async () => { await myAgent.run('…'); });
// codes: not_in_allowlist, denylist_match, budget_exceeded
```

## Пример: вход → решение

- PI-driven fetch to evil.com → PolicyViolation.
- Allowlisted OpenAI → pass.

## Детерминизм или машинное обучение

**Детерминированный** host/method policy.

## Внешние зависимости

Zero runtime deps.

## Ограничения

- Только fetch-based egress (не raw sockets).
- Must wrap agent entrypoint.

## Сигналы качества

- 47/47 tests; npm; clear API.

## Вердикт

**экспериментально** — отличный минимальный egress gate.

## Связи

- Репозиторий: [[repo-94-agentguard]]
