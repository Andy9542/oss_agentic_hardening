---
type: implementation
method-id: 26
repo: "https://github.com/highflame-ai/ramparts"
language: "Rust"
license: "Apache-2.0"
verdict: экспериментально
tags:
  - agent-security
  - review-2026
  - supply-chain
---

# Ramparts — единый scanner MCP и agent skills

## Репозиторий

https://github.com/highflame-ai/ramparts

## Где в коде

- Rust CLI `ramparts scan` / skill scan.
- `docs/security-features.md` — детекторы и attack vectors.
- YARA rules — сигнатуры содержимого и bundled scripts.
- MCP server mode — запуск scanner как stdio tool.
- GitHub Actions workflow — tests и lint.

## Алгоритм

1. Auto-discovery находит MCP-конфигурации и skills в поддерживаемых IDE/CLI.
2. Для MCP запрашивает tools/resources/prompts и анализирует metadata.
3. Для skills читает `SKILL.md`, frontmatter, `allowed-tools`, ссылки и sibling scripts/references.
4. YARA и structural checks ищут poisoning, secret leakage, traversal, command injection, shadowing и опасные grants.
5. OSV добавляет supply-chain CVE, опциональный LLM анализирует неоднозначный текст.
6. Выход: terminal, JSON, SARIF или Markdown; scanner можно вызвать из самого агента через MCP.

## Детерминизм или машинное обучение

YARA, metadata/config и OSV checks детерминированы; LLM stage вероятностна. Сканер статический и не обеспечивает runtime enforcement.

## Внешние зависимости

Rust binary; OSV.dev для актуальных CVE и LLM provider для опционального semantic анализа. Базовые проверки работают локально.

## Сигналы качества

- Тесты в репозитории: CI tests/clippy и публичная документация detector coverage.
- Документированные обходы: README прямо требует layered runtime guardrails и допускает inaccuracies.
- Зрелость: releases и SARIF есть; проект молодой и функционально пересекается с SkillSpector/MCP Armor.

## Вердикт

**экспериментально** — сильный объединённый pre-install scanner двух доверенных поверхностей, но не блокирует последующее поведение установленного компонента.

## Связи

- Способ: [[26-tool-poisoning-scan]]
