---
type: implementation-detail
parent-repo: repo-85-ps-fuzz
method-id: 44
repo: https://github.com/prompt-security/ps-fuzz
language: Python
license: MIT
verdict: experimental
commit-sha: a04982f
commit-date: 2026-02-16
verified-date: 2026-07-15
tags:
  - agent-security
---

# Prompt Fuzzer (ps-fuzz) — registry атак на system prompts

## Репозиторий

- [prompt-security/ps-fuzz](https://github.com/prompt-security/ps-fuzz)
- Проверенный срез: `a04982f`; код проверен 2026-07-15.

## Что это за технология

**Open-source fuzzer** от Prompt Security: подаёт зарегистрированные атаки (`@register_test`) на target LLM с вашими system prompts, оценивает jailbreak/injection resilience. Способ №44.

## Где в коде

- `ps_fuzz/attacks/*.py` — dan, base64_injection, typoglycemia, rag_poisoning, …
- `ps_fuzz/attack_registry.py`, `prompt_injection_fuzzer.py`
- CLI / interactive mode

## Алгоритм

1. Задать target client + system prompts.
2. Loader регистрирует tests из `attacks/`.
3. Fuzzer прогоняет каждую атаку через chat session.
4. Report successes / failures.

## Примеры реализации

Атаки (файлы): `dan.py`, `base64_injection.py`, `typoglycemia.py`, `translation.py`, `self_refine.py`, `rag_poisoning.py`, `harmful_behavior.py`, `ucar.py`, `aim.py`.

```python
@register_test
class …Attack:  # каждая атака в attacks/*.py
```

## Пример: вход → решение

- DAN payload ломает policy → finding.
- Model refuses all registered tests → hardened.

## Детерминизм или машинное обучение

Payloads фиксированы; исход зависит от LLM.

## Внешние зависимости

Python; LangChain clients; target API keys.

## Ограничения

- Фокус GenAI apps/prompts, не MCP egress.
- Attack set finite.

## Сигналы качества

- Prompt Security; CI; Colab.

## Вердикт

**экспериментально** — практичный prompt fuzzer.

## Связи

- Репозиторий: [[repo-85-ps-fuzz]]
