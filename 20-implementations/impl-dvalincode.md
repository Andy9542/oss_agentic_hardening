---
type: implementation
method-id: 35
repo: "https://github.com/arthurpanhku/dvalincode"
language: "TypeScript"
license: "MIT"
verdict: экспериментально
tags:
  - agent-security
  - review-2026
  - sandbox
---

# DvalinCode — policy-bound runtime для coding-агента

## Репозиторий

https://github.com/arthurpanhku/dvalincode

## Где в коде

- `src/agent/session.ts` — общий turn-runner и агентный цикл.
- `docs/POLICY-REFERENCE.md` — организационные политики и правило сужения.
- `docs/AUDIT-TRAIL.md` — hash-chained JSONL журнал.
- `docs/DVALIN.md` — security scan → remediation → test → re-scan.
- `docs/security/` и `docs/governance/` — threat model и governance evidence.

## Алгоритм

1. Машинная политика задаёт допустимые режимы, модели, инструменты, shell-команды и пути.
2. Политика репозитория может только сузить машинную, но не расширить её.
3. Перед записью или командой runtime применяет approval mode и показывает diff.
4. Shell ограничивается рабочей областью; на macOS используется `sandbox-exec` с запретом сети и записью только в `cwd`/`/tmp`.
5. Каждый tool call, файловая операция, команда и approval попадает в хеш-цепочку аудита.
6. Режим Dvalin объединяет Semgrep/Trivy/OSV или импорт SARIF, изолированное исправление, тест и повторный scan.

## Детерминизм или машинное обучение

Границы политики, approvals, пути и проверка audit chain детерминированы. Поиск и исправление уязвимостей выполняет LLM и внешние сканеры; качество этой части вероятностное.

## Внешние зависимости

Bun/TypeScript runtime и выбранный OpenAI-compatible LLM. Semgrep CE, Trivy и OSV-Scanner опциональны. Сильная sandbox-реализация зависит от ОС; заявленная macOS-изоляция не равна microVM.

## Сигналы качества

- Тесты в репозитории: README заявляет 770 тестов; есть injection regression и проверки границ skills.
- Документированные обходы: malicious instructions, poisoned MCP, egress, audit tampering и sandbox escape перечислены в threat model.
- Зрелость: релизы и governance-документация есть, но продукт быстро меняется и часть desktop/runtime путей платформозависима.

## Вердикт

**экспериментально** — ценный пример controllable/transparent/auditable coding-агента, однако сила sandbox и полнота enforcement требуют отдельной проверки на каждой ОС.

## Связи

- Способ: [[35-уровни-исполнения-и-изоляция-рабочего-каталога]]
