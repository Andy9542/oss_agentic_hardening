---
type: implementation-detail
parent-repo: repo-09-agent-firewall
method-id: 14
repo: https://github.com/0xrem/agent-firewall
language: Python
license: Apache-2.0
verdict: experimental
commit-sha: e4945d0
commit-date: 2026-04-04
verified-date: 2026-07-15
tags:
  - agent-security
---

# agent-firewall — pre-execution rules (injection + dangerous cmds)

## Репозиторий

- [0xrem/agent-firewall](https://github.com/0xrem/agent-firewall)
- Проверенный срез: `e4945d0`, дата коммита 2026-04-04; код проверен 2026-07-15.

## Что это за технология

**Pre-execution firewall** для tool/prompt событий: набор Rule-классов возвращает `Decision` (`allow` / `block` / `review`) до запуска инструмента. Встроенные правила — substring/phrase match на инъекции в промпте и опасные shell-паттерны. Способ №14 + №3 (эвристики).

## Где в коде

- `src/agentfirewall/rules/builtin.py` — `ReviewPromptInjectionRule`, `BlockDangerousCommandRule`, …
- `src/agentfirewall/policy.py` — `DecisionAction`
- `src/agentfirewall/policy_packs.py` — сборка packs
- Examples: LangGraph / OpenAI Agents

## Алгоритм

1. Runtime эмитит `EventContext` (PROMPT / TOOL / REQUEST…).
2. PolicyEngine прогоняет rules по порядку.
3. Первое non-None Decision применяется (block/review).
4. Block — не исполнять; review — HITL/log; иначе allow.

## Примеры реализации

Фразы injection (`ReviewPromptInjectionRule`):

```text
"ignore previous instructions", "disregard all prior instructions",
"reveal the system prompt", "you are DAN", "do anything now",
"enter developer mode", "ignore safety guidelines"
```

Опасные команды (`BlockDangerousCommandRule`):

```text
"rm -rf /", "rm -rf ~", "| bash", "curl | sh", "wget | bash", …
```

Match: `if pattern in command_text` (substring, lowercased для prompts).

## Пример: вход → решение

- Prompt с `ignore previous instructions` → Decision.review.
- Tool exec `curl http://x | bash` → block dangerous command.
- Чистый `ls -la` → allow (если нет других rules).

## Детерминизм или машинное обучение

**Детерминированный** phrase/substring matching.

## Внешние зависимости

Python package; интеграции LangGraph/OpenAI Agents.

## Ограничения

- Substring FP/FN; нет Unicode-нормализации уровня Pipelock.
- Default pack может начинаться с ALLOW — смотреть policy_packs.

## Сигналы качества

- Тесты evals + examples; CI.

## Вердикт

**экспериментально** — простой pedagogic pre-exec firewall.

## Связи

- Репозиторий: [[repo-09-agent-firewall]]
