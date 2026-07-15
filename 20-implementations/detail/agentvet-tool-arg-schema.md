---
type: implementation-detail
parent-repo: repo-93-agentvet
method-id: 13
repo: https://github.com/MukundaKatta/agentvet
language: TypeScript/JavaScript
license: MIT
verdict: experimental
commit-sha: f1014a7
commit-date: 2026-05-16
verified-date: 2026-07-15
tags:
  - agent-security
---

# agentvet — schema-валидация args до tool side-effect

## Репозиторий

- [MukundaKatta/agentvet](https://github.com/MukundaKatta/agentvet)
- Проверенный срез: `f1014a7`; код проверен 2026-07-15.

## Что это за технология

**Zero-dep JS/TS wrapper** `vet({name, schema, fn})`: проверяет LLM tool args (zod adapter) **до** вызова; на fail — `ToolArgError` с `toLLMFeedback()` для retry. Способ №13.

## Где в коде

- `src/vet.js`, `errors.js`, `adapters.js`
- CLI `agentvet validate|lint`
- `examples/demo-reject.js`

## Алгоритм

1. Wrap tool with schema (zod/safeParse).
2. Agent emits tool_use input.
3. If invalid → throw ToolArgError (tool never runs).
4. Feed structured error back as tool_result; model retries.

## Примеры реализации

```js
const search = vet({
  name: 'search',
  schema: adapters.zod(z.object({ query: z.string(), limit: z.number() })),
  fn: async ({ query, limit }) => doSearch(query, limit),
});
// search({ query: 42 }) → ToolArgError before doSearch
```

## Пример: вход → решение

- `flight_id: 12345` instead of string → reject + LLM feedback.
- Valid args → tool executes.

## Детерминизм или машинное обучение

**Детерминированная** schema validation.

## Внешние зависимости

None runtime; optional zod.

## Ограничения

- Не semantic policy (только типы/shape).
- Node/TS ecosystem.

## Сигналы качества

- 30/30 tests; npm package; agent-stack.

## Вердикт

**экспериментально** — минимальный tool-arg gate.

## Связи

- Репозиторий: [[repo-93-agentvet]]
