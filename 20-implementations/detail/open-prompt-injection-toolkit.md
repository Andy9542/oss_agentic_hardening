---
type: implementation-detail
parent-repo: repo-71-open-prompt-injection
method-id: 45
repo: https://github.com/liu00222/Open-Prompt-Injection
language: Python
license: MIT
verdict: experimental
commit-sha: 95290f7
commit-date: 2025-10-29
verified-date: 2026-07-15
tags:
  - agent-security
---

# Open-Prompt-Injection — toolkit attacks + defenses

## Репозиторий

- [liu00222/Open-Prompt-Injection](https://github.com/liu00222/Open-Prompt-Injection)
- Проверенный срез: `95290f7`; код проверен 2026-07-15.

## Что это за технология

**Research toolkit** PI: create attacker (`attack_strategy`), target app с `defense`, evaluate ASR. Модули apps/attackers/models/tasks. Способ №45 (+ изучение defenses).

## Где в коде

- `main.py` — `--attack_strategy`, `--defense`
- `OpenPromptInjection/` — attackers, apps, tasks
- `run.py` matrix experiments

## Алгоритм

1. Config model + datasets.
2. `PI.create_attacker(strategy, inject_task)`.
3. `PI.create_app(target_task, model, defense=…)`.
4. Inject data_prompt → query → score attack success.

## Примеры реализации

```python
attacker = PI.create_attacker(args.attack_strategy, inject_task)
target_app = PI.create_app(target_task, model, defense=args.defense)
data_prompt_after_attack = attacker.inject(data_prompt, i, target_task=…)
response = target_app.query(data_prompt_after_attack, …)
```

Default strategy often `combine`; defense `no` baseline.

## Пример: вход → решение

- Attack+no defense → high ASR.
- Same attack + instructional/paraphrase defense → ASR↓.

## Детерминизм или машинное обучение

Harness фиксирован; модели — нет.

## Внешние зависимости

conda env; provider API keys.

## Ограничения

- Academic setup; not drop-in prod firewall.
- Model configs dated.

## Сигналы качества

- Safer with Google slides; extensible modules.

## Вердикт

**экспериментально** — classic PI attack/defense lab.

## Связи

- Репозиторий: [[repo-71-open-prompt-injection]]
