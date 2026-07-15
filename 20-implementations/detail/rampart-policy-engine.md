---
type: implementation-detail
parent-repo: repo-04-rampart
method-id: 12
repo: https://github.com/peg/rampart
language: Go
license: Apache-2.0
verdict: experimental
commit-sha: cb2e54f
commit-date: 2026-06-08
verified-date: 2026-07-15
tags:
  - agent-security
---

# Rampart — политики filesystem/network/exec для coding-агентов

## Репозиторий

- [peg/rampart](https://github.com/peg/rampart)
- Проверенный срез: `cb2e54f`, дата коммита 2026-06-08; код проверен 2026-07-15.

## Что это за технология

**Policy engine для coding agents** (Claude Code, OpenClaw, shell-wrap): каждый `exec` / `read` / `fetch` оценивается по YAML-правилам до исполнения. Действия: `deny`, `ask`, `watch`, `allow`. Deny всегда побеждает. Это способ №12/№14 в нише desktop coding agents.

## Где в коде

- Документация и примеры политик: `README.md` (секции policy YAML)
- CLI: `rampart serve`, `rampart wrap`, `rampart mcp`, `rampart allow`
- Project-local: `.rampart/policy.yaml`

## Алгоритм

1. Загрузить user + project policies (project можно отключить `RAMPART_NO_PROJECT_POLICY=1`).
2. Сопоставить tool (`exec`/`read`/`fetch`) и условия (`command_matches`, `command_contains`, `path_matches`, `domain_matches`).
3. Выбрать действие с учётом priority; **deny wins**.
4. `ask` → native approval UI агента; `watch` → log only; `allow` → execute.
5. Audit log строк вида `DENY … [block-destructive]`.

## Примеры реализации

```yaml
policies:
  - name: block-destructive
    match: { tool: ["exec"] }
    rules:
      - action: deny
        when:
          command_matches: ["rm -rf *", "mkfs.*", "dd if=*", ":(){ :|:& };:"]
  - name: block-credential-reads
    priority: 1
    match: { tool: ["read"] }
    rules:
      - action: deny
        when:
          path_matches: ["**/.ssh/id_*", "**/.aws/credentials", "**/.env"]
  - name: block-exfil
    match: { tool: ["fetch"] }
    rules:
      - action: deny
        when:
          domain_matches: ["*.ngrok-free.app", "*.requestbin.com", "webhook.site"]
```

`command_contains: ["DROP TABLE", "rm -rf"]` — substring match (case-insensitive).

## Пример: вход → решение

- `exec "rm -rf /tmp/*"` → DENY `[block-destructive]`.
- `read ~/.env` → DENY `[block-credential-reads]`.
- `exec "npm test"` при allow-dev → ALLOW.

## Детерминизм или машинное обучение

**Детерминированный**.

## Внешние зависимости

Локальный Rampart service/binary; интеграции через hooks агента.

## Ограничения

- Default action может быть `allow` — опасный default, если мало deny-rules.
- Обход: агент, игнорирующий `$SHELL`/hooks.

## Сигналы качества

- Практичный UX (`rampart allow "npm install *"`); SECURITY.md с threat model.

## Вердикт

**экспериментально** — сильный fit для coding agents; проверять default_action.

## Связи

- Репозиторий: [[repo-04-rampart]]
