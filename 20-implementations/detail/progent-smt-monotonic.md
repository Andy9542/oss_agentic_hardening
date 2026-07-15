---
type: implementation-detail
parent-repo: repo-10-progent
method-id: 17
repo: https://github.com/sunblaze-ucb/progent
language: Python
license: MIT
verdict: experimental
commit-sha: 8a8eb89
commit-date: 2026-05-13
verified-date: 2026-07-15
tags:
  - agent-security
---

# Progent — SMT-проверка монотонности политик (Z3)

## Репозиторий

- [sunblaze-ucb/progent](https://github.com/sunblaze-ucb/progent)
- Проверенный срез: `8a8eb89`, дата коммита 2026-05-13; код проверен 2026-07-15.

## Что это за технология

**SMT (Satisfiability Modulo Theories)** — автоматическое доказательство выполнимости логических формул с теориями (целые, строки, regex как автоматы). Здесь используется решатель **Z3** (Microsoft Research).

Progent хранит привилегии агента как JSON-schema-ограничения на аргументы tools. При **обновлении** политики система проверяет, что новое множество разрешений **не шире** старого (монотонное сужение). Если существует значение аргумента, разрешённое новой политикой, но запрещённое старой — Z3 находит **контрпример**, обновление отклоняется (нужно одобрение человека — см. expansion approval).

Это формальная проверка политик (способ №17), а не эвристический diff YAML.

## Где в коде

- SMT / subset: `secagent/policy_analysis.py` (`security_policy_subset_check`, `solve_schema`)
- Regex → Z3: `secagent/role_analyzer.py` (`regex_to_z3_expr`)
- Enforcement на tool call: `secagent/tool.py` (вызов subset check при обновлении)
- Бенчмарки: `agentdojo/`, `asb/`

## Алгоритм

1. Политика: словарь `tool_name → [(priority, …, {arg: json_schema}, …)]`. Фильтруются правила с приоритетом `100` (жёсткие allow).
2. Для каждой пары (старая, новая) ограничений на один аргумент строится формула:
   - `allOf: [ {"not": restriction_old}, restriction_new ]`
   - смысл: «существует x, запрещённый старым правилом, но разрешённый новым» = **расширение**.
3. `solve_schema` кодирует JSON Schema в Z3-ограничения (`String`/`Int`/`Real`/`Bool`/array wrappers), `Solver.check()` с timeout 5000 ms.
4. Если `sat` → найден контрпример `model[var]` → `security_policy_subset_check` возвращает `False` (не subset).
5. Если `unsat` (или нет контрпримера) → новая политика ⊆ старой → обновление допустимо без HITL.
6. Отдельно `security_policy_analysis` ищет **пересечения** правил (`allOf` двух restriction) — предупреждение о неоднозначности.

## Примеры реализации

Проверка расширения (`policy_analysis.py`):

```python
schema = {
    "allOf": [
        {"not": restriction_1},  # старое
        restriction_2,            # новое
    ]
}
model, var = solve_schema(schema)
if model:
    return False  # new allows something old forbids
```

Пример политик в `__main__`: `send_money.recipient` с IBAN-pattern; `send_email.recipient` с email regex vs конкретный `agent@example.com`.

Regex-ограничения переводятся в Z3 `ReRef` через `regex_to_z3_expr` (категории `\d`, `\w`, `Minus`/`Intersect` автоматов).

## Пример: вход → решение

- Старое: `recipient: {pattern: "agent@example.com"}`; новое: `{pattern: ".*@example.com"}` → Z3 находит e.g. другой ящик → **не subset** → reject без approval.
- Старое: широкий enum; новое: подмножество enum → **subset** → allow update.

## Детерминизм или машинное обучение

- SMT / check вызова — **детерминированные**.
- Генерация начальной политики LLM — **вероятностная** (качество старта критично).

## Внешние зависимости

- Python + пакет `z3-solver`
- LLM API для генерации политики (эксперименты)
- AgentDojo / ASB для оценки

## Ограничения

- Timeout 5 с: сложные schema могут не доказать subset (осторожный fail).
- Покрытие JSON Schema неполное (не все конструкции RFC).
- Исследовательский код; интеграция в прод требует обёртки HITL.

## Сигналы качества

- Paper arXiv:2504.11703; цифры ASR на AgentDojo в README/paper.
- Unit-логика в `policy_analysis.py`; бенчмарк-скрипты в `agentdojo/`.

## Вердикт

**экспериментально** — сильная идея формального сужения привилегий; зрелость ниже промышленных YAML-шлюзов.

## Связи

- Репозиторий: [[repo-10-progent]]
