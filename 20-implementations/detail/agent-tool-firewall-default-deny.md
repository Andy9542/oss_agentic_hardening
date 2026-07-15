---
type: implementation-detail
parent-repo: repo-07-agent-tool-firewall
method-id: 14
repo: https://github.com/SecAI-Hub/agent-tool-firewall
language: Go
license: Apache-2.0
verdict: experimental
commit-sha: 3373b1f
commit-date: 2026-04-28
verified-date: 2026-07-15
tags:
  - agent-security
---

# agent-tool-firewall — YAML default-deny на tool calls

## Репозиторий

- [SecAI-Hub/agent-tool-firewall](https://github.com/SecAI-Hub/agent-tool-firewall)
- Проверенный срез: `3373b1f`, дата коммита 2026-04-28; код проверен 2026-07-15.

## Что это за технология

**Default-deny tool gateway** — HTTP-сервис между агентом и инструментами. Любой `tool_call`, которого нет в allowlist, отклоняется. Это способ №14 (default-deny / allowlists): политика в YAML, enforcement в Go, без ML.

Дополнительно: path allow/deny, blocklist подстрок в аргументах, sliding-window rate limit, JSONL audit.

## Где в коде

- Весь сервис: `main.go` (`evaluateTool`, `handleEvaluate`, загрузка YAML)
- Пример политики: `examples/policy.yaml`
- API: `POST /v1/evaluate`, `POST /v1/reload`, health/metrics

## Алгоритм

1. Загрузить `policy.yaml` → структура `Tools{Default, Allow, Deny, RateLimit}`.
2. На `POST /v1/evaluate` с `{tool, params}`:
   1. Проверить rate limit (RPM + burst) → иначе deny.
   2. Если tool в `deny` → deny («deny always wins»).
   3. Если `default != "allow"` (рекомендуемый режим):
      - найти tool в `allow`; иначе deny «not in allowlist»;
      - `validateArgs` (длина, `args_blocklist`);
      - `checkPathConstraints` (glob allowlist / denylist, `../`).
   4. Иначе default-allow (не рекомендуется).
3. Записать audit JSONL; вернуть `{allowed, reason}`.

## Примеры реализации

Из `examples/policy.yaml`:

```yaml
tools:
  default: "deny"
  rate_limit:
    requests_per_minute: 120
    burst_size: 20
  allow:
    - name: "filesystem.read"
      paths_allowlist: ["/home/user/documents/**"]
      paths_denylist: ["/etc/shadow", "/etc/passwd"]
      max_arg_length: 4096
    - name: "web.search"
      args_blocklist: ["password", "secret", "api_key"]
  deny:
    - name: "shell.exec"
    - name: "process.spawn"
    - name: "network.fetch"
```

Порядок в `evaluateTool` (`main.go`): rate → deny list → allowlist match → args → paths.

## Пример: вход → решение

- `{tool: "shell.exec"}` → deny (explicit deny / not allowlisted).
- `{tool: "filesystem.read", params: {path: "/home/user/documents/a.txt"}}` → allow.
- `{tool: "filesystem.read", params: {path: "/etc/passwd"}}` → deny (denylist).
- `{tool: "web.search", params: {query: "leak api_key"}}` → deny (args_blocklist).

## Детерминизм или машинное обучение

Полностью **детерминированный**.

## Внешние зависимости

Один статический Go-бинарник + файл политики. Без GPU/облака.

## Ограничения

- Агент обязан ходить только через `/v1/evaluate`; прямой вызов tool обходит PEP.
- Blocklist подстрок легко обойти синонимами (`passwd` vs `password`).
- Нет SMT/формальной верификации обновлений политики.

## Сигналы качества

- CI workflow в репозитории; threat model в `THREAT_MODEL.md`.
- Зрелость ниже Pipelock/AGT, но педагогически ясный эталон default-deny.

## Вердикт

**экспериментально** — чистый учебный/лёгкий prod-candidate для tool allowlists.

## Связи

- Репозиторий: [[repo-07-agent-tool-firewall]]
