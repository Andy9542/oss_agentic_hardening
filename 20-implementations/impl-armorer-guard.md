---
type: implementation
method-id: 19
repo: "https://github.com/ArmorerLabs/Armorer-Guard"
language: "Rust"
license: "MIT"
verdict: экспериментально
tags:
  - agent-security
  - review-2026
  - runtime-guard
---

# Armorer Guard — локальная проверка MCP до tool call

## Репозиторий

https://github.com/ArmorerLabs/Armorer-Guard

## Где в коде

- Rust core и CLI — scanner, policy lanes и MCP proxy.
- `docs/SECURITY_MODEL.md` — границы модели угроз.
- `docs/RESULTS.md` и `docs/BENCHMARKS.md` — метрики и методика.
- `docs/MCP_QUICKSTART.md` — обёртка stdio MCP.
- `examples/` — LangChain, CrewAI, Claude Code, Cursor и GitHub Actions.

## Алгоритм

1. MCP proxy перехватывает `tools/call` до выполнения.
2. Нормализует prompt, model output или аргументы инструмента.
3. Применяет быстрые правила для секретов, injection, эксфильтрации и опасных действий.
4. Локальный semantic classifier добавляет оценку для перефразированных инструкций.
5. Policy lane возвращает структурированную причину, которую runtime использует для allow/block/redact.
6. Learning Loop сохраняет локальную обратную связь и позволяет повторно проверить тот же ввод.

## Детерминизм или машинное обучение

Смешанный подход: детерминированные правила и локальный TF-IDF/semantic classifier. Production-профиль не делает сетевых запросов сканера; high-recall профили могут использовать дополнительную модель.

## Внешние зависимости

Rust binary; Python и Node wrappers опциональны. Модели и профили поставляются локально. Облако не требуется для основного scanner path.

## Сигналы качества

- Тесты в репозитории: `cargo test`, `pytest`, CI example.
- Документированные обходы: security model, attack fixtures и отдельные held-out metrics.
- Зрелость: опубликованы crates/PyPI/npm и benchmark docs; заявленная latency и качество требуют независимого воспроизведения.

## Вердикт

**экспериментально** — практичный hot-path guard с прозрачной смешанной архитектурой, но новый проект и собственные benchmark-данные пока не дают сильной внешней гарантии.

## Связи

- Способ: [[19-правила-против-инъекций-в-аргументах-инструментов]]
