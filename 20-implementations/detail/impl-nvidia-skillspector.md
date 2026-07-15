---
type: implementation-detail
parent-repo: repo-109-nvidia-skillspector
method-id: 27
mechanism-id: skillspector-langgraph-scan-pipeline
repo: https://github.com/NVIDIA/SkillSpector
language: Python
license: Apache-2.0
verdict: experimental
tags:
  - agent-security
---

# SkillSpector — LangGraph-конвейер проверки skills

## Проверенный срез

Upstream [`8f534e2951e0b7d0b8fb8e84832cd3605f95c032`](https://github.com/NVIDIA/SkillSpector/commit/8f534e2951e0b7d0b8fb8e84832cd3605f95c032) от 2026-07-14.

## Кодовые пути

- `src/skillspector/nodes/resolve_input.py`, `build_context.py` — получение input и общий file cache.
- `src/skillspector/graph.py`, `state.py` — fan-out/fan-in граф и state reducers.
- `src/skillspector/nodes/analyzers/__init__.py` — реестр 22 анализаторов.
- `src/skillspector/nodes/meta_analyzer.py`, `report.py` — LLM-фильтрация, baseline, score и SARIF.

## Алгоритм

1. Input handler разрешает Git URL, file URL, ZIP, Markdown-файл или каталог во временный skill root.
2. Build context читает компоненты, manifest и executable flag.
3. LangGraph параллельно запускает static, AST, taint, YARA, MCP и semantic nodes; reducer объединяет findings.
4. При `use_llm=true` meta-analyzer фильтрует и обогащает findings по файлам; при `--no-llm` используется fallback.
5. Report применяет baseline до score, валидирует SARIF 2.1.0 и выдаёт terminal/JSON/Markdown/SARIF.

## Зависимости

Python 3.12–3.14, LangGraph/LangChain, Pydantic, YARA, HTTPX и выбранные LLM provider packages; для MCP server mode нужен optional extra `mcp`.

## Тесты

`tests/unit/`, `tests/nodes/` и `tests/nodes/analyzers/` запускаются публичным CI; `tests/integration/` проверяет полный граф, но в публичном GitHub workflow не запускается. Команды: `make test`, `make test-cov`.

## Ограничения

LLM-режим отправляет содержимое файлов настроенному provider и недетерминирован. Image, encrypted/binary и runtime behavior не анализируются; отсутствие OSV сети сужает coverage.

## Вердикт

**экспериментально** — широкий и расширяемый alpha pipeline, но эксплуатационный trust зависит от выбранного режима и внешних сервисов.

## Связи

- Репозиторий: [[repo-109-nvidia-skillspector]]
