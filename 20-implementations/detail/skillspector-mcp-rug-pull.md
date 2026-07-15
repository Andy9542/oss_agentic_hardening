---
type: implementation-detail
parent-repo: repo-109-nvidia-skillspector
method-id: 25
mechanism-id: skillspector-mcp-rug-pull-analysis
repo: https://github.com/NVIDIA/SkillSpector
language: Python
license: Apache-2.0
verdict: experimental
tags:
  - agent-security
---

# SkillSpector — анализ MCP rug pull

## Проверенный срез

Upstream [`8f534e2951e0b7d0b8fb8e84832cd3605f95c032`](https://github.com/NVIDIA/SkillSpector/commit/8f534e2951e0b7d0b8fb8e84832cd3605f95c032) от 2026-07-14.

## Кодовые пути

- `src/skillspector/nodes/analyzers/mcp_rug_pull.py` — правила RP1–RP3.
- `src/skillspector/state.py` — `manifest` и опциональный `previous_manifest`.
- `src/skillspector/suppression.py` — baseline findings.
- `tests/nodes/analyzers/test_mcp_rug_pull.py`, `tests/test_mcp_rug_pull.py`.

## Алгоритм

RP1 regex-проверками находит неприкреплённые версии в `npx`, `uvx`, `pip install` и Docker references. RP2 ищет pre-staging расширения permissions; RP3 — broad/unpinned skill version. Если передан `previous_manifest`, analyzer сравнивает normalized permissions, triggers и parameter schemas/defaults и выдаёт findings для расширения привилегий или изменения поведения.

## Зависимости

Python stdlib regex и manifest, подготовленный build-context node. Сеть и LLM не требуются.

## Тесты

Тесты проверяют unpinned commands, permission/trigger/parameter drift, severity/confidence и безопасные pinned references.

## Ограничения

Полноценное сравнение требует, чтобы caller передал `previous_manifest`; обычный одиночный scan ограничен эвристиками. Regex поддерживает только известные package runners и может не распознать wrappers или shell indirection; baseline не является криптографическим снимком MCP metadata.

## Вердикт

**экспериментально** — полезная pre-install проверка pinning и manifest drift, но weaker, чем независимый подписанный или хешированный inventory.

## Связи

- Репозиторий: [[repo-109-nvidia-skillspector]]
