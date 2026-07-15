---
type: implementation-detail
parent-repo: repo-65-modelscan
method-id: 30
repo: https://github.com/protectai/modelscan
language: Python
license: Apache-2.0
verdict: prod
commit-sha: 61fcec9
commit-date: 2026-02-18
verified-date: 2026-07-15
tags:
  - agent-security
---

# ModelScan — unsafe pickle/TF ops в весах моделей

## Репозиторий

- [protectai/modelscan](https://github.com/protectai/modelscan)
- Проверенный срез: `61fcec9`; код проверен 2026-07-15.

## Что это за технология

**Статический сканер ML-артефактов** (pickle, PyTorch, Keras/H5, TF SavedModel, numpy): ищет dangerous globals/opcodes до загрузки модели агентом. Способ №30 (статический анализ артефактов).

## Где в коде

- `modelscan/settings.py` — `DEFAULT_SETTINGS`, `unsafe_globals`
- `modelscan/tools/picklescanner.py`
- Scanners: `scanners/pickle/`, `saved_model/`, `h5/`

## Алгоритм

1. `modelscan -p model.pkl` → выбрать scanners по extension.
2. Для pickle: разобрать opcodes, сопоставить GLOBAL с `unsafe_globals` severity.
3. Для TF: флаг `ReadFile`/`WriteFile` (HIGH), Keras `Lambda` (MEDIUM).
4. Issues по severity → console/JSON.

## Примеры реализации

```python
# settings.py unsafe_globals CRITICAL
"builtins": ["eval", "exec", "open", "__import__", …],
"os": "*", "subprocess": "*", "posix": "*", "nt": "*",
# TF ops
"ReadFile": "HIGH", "WriteFile": "HIGH",
"Lambda": "MEDIUM",
```

Extensions: `.pkl/.pickle/.joblib/.pt/.pth/.pb/.h5/.keras/.npy`.

## Пример: вход → решение

- Pickle с `os.system` GLOBAL → CRITICAL issue.
- Чистый state_dict без code → pass.

## Детерминизм или машинное обучение

**Детерминированный** opcode/operator scan.

## Внешние зависимости

Python CLI; без GPU.

## Ограничения

- Не динамический sandbox load.
- Новые unsafe APIs нужно добавлять в settings.

## Сигналы качества

- Protect AI; PyPI; широкие форматы.

## Вердикт

**готово к продакшену** для CI gate на model files.

## Связи

- Репозиторий: [[repo-65-modelscan]]
