---
type: implementation-detail
parent-repo: repo-105-skilltotal
method-id: 28
mechanism-id: skilltotal-exfiltration-correlation
repo: https://github.com/pezhik/skilltotal
language: Python
license: Apache-2.0
verdict: experimental
tags:
  - agent-security
---

# SkillTotal — корреляция доступа к данным и egress

## Проверенный срез

Upstream [`7905d363ef9bb525ebb119cbc008e961c4517a5f`](https://github.com/pezhik/skilltotal/commit/7905d363ef9bb525ebb119cbc008e961c4517a5f) от 2026-07-09.

## Кодовые пути

- `skilltotal/scanners/taint.py` — source-to-sink проверки.
- `skilltotal/scanners/secrets.py`, `skilltotal/scanners/sensitive_paths.py` — источники чувствительных данных.
- `skilltotal/scanners/network.py`, `skilltotal/scoring.py` — egress-сигналы и синтез `ST-COMBO-EXFIL`.
- `tests/test_taint.py`, `tests/test_flow_and_convergence.py`, `tests/test_combinations.py` — проверки механизма.

## Алгоритм

Сканеры сначала фиксируют evidence доступа к credential path, embedded secret и network egress. Taint-анализ распознаёт прямой или переменно-опосредованный поток из внешнего ввода к shell/exec sink. Если чувствительные данные и egress сосуществуют, scoring добавляет отдельный critical `risky_construct` `ST-COMBO-EXFIL`; повторы одного правила не увеличивают score по числу совпадений.

## Зависимости

Только Python 3.10+ stdlib и предварительно построенный file index; сеть и LLM не требуются.

## Тесты

Unit tests проверяют прямые и опосредованные потоки, convergence нескольких scanners, exfil-комбинации и отрицательные fixtures в `tests/eval_corpus/negative/`.

## Ограничения

Анализ внутрипроцедурный и эвристический: не строит полный interprocedural call graph и может пропустить поток через неизвестную библиотеку или динамическую диспетчеризацию. Сосуществование secret access и egress сильнее одиночного сигнала, но не доказывает фактическую передачу.

## Вердикт

**экспериментально** — полезная evidence-корреляция для triage, но не полноценный формальный taint engine.

## Связи

- Репозиторий: [[repo-105-skilltotal]]
