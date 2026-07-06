---
type: implementation
method-id: 31
repo: https://github.com/cisco-ai-defense/defenseclaw
language: Python/Go/TS
license: Apache-2.0
verdict: prod
tags: [agent-security]
---

# defenseclaw — admission enforcement

## Где в коде

Scan → quarantine → revoke sandbox (<2s); directory watcher rescan; OPA/Rego.

## Вердикт

**готово к продакшену** — rare full enforcement loop.

## Связи

- Способ: [[31-admission-blocklist]]
