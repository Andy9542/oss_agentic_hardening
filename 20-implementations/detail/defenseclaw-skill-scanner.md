---
type: implementation-detail
parent-repo: repo-18-defenseclaw
method-id: 27
repo: https://github.com/cisco-ai-defense/defenseclaw
language: Python/Go/TypeScript
license: Apache-2.0
verdict: experimental
commit-sha: main-readme-2026-07
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# DefenseClaw — admission scan skills/MCP + runtime guardrail

## Репозиторий

- [cisco-ai-defense/defenseclaw](https://github.com/cisco-ai-defense/defenseclaw)
- Источник анализа: upstream README/docs (локальный clone был повреждён); проверено 2026-07-15.

## Что это за технология

**Admission control + runtime guardrail** для OpenClaw: до запуска навык/MCP/plugin сканируется (Cisco skill-scanner, CodeGuard, policy); в runtime sidecar (Go) инспектирует prompts/completions/tool calls regex-правилами, опциональным LLM-judge и Cisco AI Defense. Режимы: observe (только лог) / action (block HIGH/CRITICAL).

## Где в коде (по docs)

- CLI: `defenseclaw skill scan`, `mcp list`, `plugin scan`
- Gateway sidecar Go + OpenClaw TS plugin
- Политики: `policies/scanners/`, `policies/guardrail/`
- Docs: `docs/GUARDRAIL.md`, `docs/GUARDRAIL_RULE_PACKS.md`, `docs/ARCHITECTURE.md`

## Алгоритм

1. `defenseclaw init --enable-guardrail`.
2. Admission: scan skill/MCP/plugin → verdict → block install/use if policy says unsafe.
3. Runtime: agent → OpenClaw plugin → DefenseClaw gateway → rule packs (+ optional LLM/Cisco) → allow/block.
4. Audit: SQLite, JSONL, OTLP, Splunk, webhooks.
5. Опционально OpenShell sandbox для FS/network/syscall.

## Примеры реализации

Операторский контур:

```bash
defenseclaw skill scan all
defenseclaw setup guardrail --mode observe --restart
defenseclaw setup guardrail --mode action --restart
```

Поверхности: Skills → cisco-ai-skill-scanner + CodeGuard; MCP → mcp-scanner; prompts → guardrail proxy rule packs.

## Пример: вход → решение

- Skill с credential harvesting YARA hit CRITICAL в action mode → block admission.
- Prompt с jailbreak pattern в observe → log only; в action → block completion path.

## Детерминизм или машинное обучение

**Смешанный:** regex/YARA/CodeGuard детерминированы; LLM judge / Cisco cloud — вероятностны.

## Внешние зависимости

Python 3.10+, Go, Node 18+; опционально Docker, Cisco AI Defense, OpenShell.

## Ограничения

- Observe mode не блокирует.
- Не доказывает отсутствие риска — только снижает.

## Сигналы качества

- Обширная документация Cisco; make test/lint.

## Вердикт

**экспериментально** — богатый governance stack; сложность внедрения высокая.

## Связи

- Репозиторий: [[repo-18-defenseclaw]]
