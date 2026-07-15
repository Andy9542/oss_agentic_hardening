---
type: implementation-detail
parent-repo: repo-64-genai-agent-security-initiative
method-id: 41
repo: https://github.com/GenAI-Security-Project/GenAI-Agent-Security-Initiative
language: Python
license: Apache-2.0
verdict: experimental
commit-sha: e1deaca
commit-date: 2026-04-03
verified-date: 2026-07-15
tags:
  - agent-security
---

# OWASP ASI — insecure agent samples (GASI)

## Репозиторий

- [GenAI-Security-Project/GenAI-Agent-Security-Initiative](https://github.com/GenAI-Security-Project/GenAI-Agent-Security-Initiative)
- Проверенный срез: `e1deaca`; код проверен 2026-07-15.

## Что это за технология

**Учебные intentionally insecure agents** на LangChain/LangGraph/CrewAI/AutoGen/Swarm/Bedrock — демонстрация misconfig → OWASP GenAI/Agentic Top 10. Не защита, а lab для №41/обучения.

## Где в коде

- Framework folders с vulnerable examples + descriptions
- CONTRIBUTING / ASI landing

## Алгоритм

1. Выбрать framework example.
2. Запустить vulnerable agent (осторожно).
3. Reproduce described vuln (injection, excessive agency…).
4. Сопоставить с OWASP IDs; harden locally.

## Примеры реализации

Frameworks covered: LangChain, LangGraph, CrewAI, AutoGen, OpenAI Swarm, Amazon Bedrock Agents — каждый с описанием vulnerability.

## Пример: вход → решение

- Example with unrestricted tools → ASI02-style tool misuse demo.
- Student patches allowlist → exploit fails.

## Детерминизм или машинное обучение

Примеры кода детерминированы; LLM behavior — нет.

## Внешние зависимости

Framework + LLM keys; **не деплоить в prod**.

## Ограничения

- Deliberately insecure — isolation required.
- Coverage per framework varies.

## Сигналы качества

- OWASP ASI branding; multi-framework.

## Вердикт

**экспериментально** — training corpus, не control.

## Связи

- Репозиторий: [[repo-64-genai-agent-security-initiative]]
