---
type: implementation-detail
parent-repo: repo-113-mcp-armor
method-id: 1
mechanism-id: mcp-armor-local-prompt-classifier
repo: https://github.com/aira-security/mcp-armor
language: Python
license: Apache-2.0
verdict: experimental
tags:
  - agent-security
---

# MCP Armor — локальный классификатор prompt injection

## Проверенный срез

Upstream [`6af4cee4665ab6242f02a88952f9127b6a04922a`](https://github.com/aira-security/mcp-armor/commit/6af4cee4665ab6242f02a88952f9127b6a04922a) от 2026-03-27.

## Кодовые пути

- `src/mcp_armor/scan_checks/prompt_injection.py` — lazy model load, chunking и classification.
- `src/mcp_armor/security_utils.py` — извлечение текста из MCP entities.
- `src/mcp_armor/run_checks.py` — параллельный запуск checks.

## Алгоритм

Hugging Face pipeline загружает `Aira-security/FT-Llama-Prompt-Guard-2` один раз под lock. Текст tool/resource/prompt/template токенизируется блоками до 512 tokens с overlap 64; блоки классифицируются batch size 8. Любой лучший результат с label `malicious` и score не ниже 0,8 создаёт critical finding; entities обрабатываются пакетами по 16.

## Зависимости

`transformers~=4.57.1`, `torch~=2.9.0` и первоначальная загрузка модели из Hugging Face; после кэширования inference выполняется локально.

## Тесты

Автоматических тестов classifier, threshold, chunk overlap или model failure в проверенном срезе нет; доступен только ручной demo flow.

## Ограничения

При ошибке загрузки или inference код логирует проблему и фактически пропускает detection; неожиданный label трактуется как benign. Качество модели и threshold не подкреплены репозиторным benchmark, а overlapping chunks не восстанавливают весь межблочный контекст.

## Вердикт

**экспериментально** — приватный локальный ML-check, но fail-open поведение и отсутствие regression tests требуют дополнительного deterministic слоя.

## Связи

- Репозиторий: [[repo-113-mcp-armor]]
