---
type: implementation
method-id: 44
repo: "https://github.com/usestrix/strix"
language: "Python"
license: "Apache-2.0"
verdict: экспериментально
tags:
  - agent-security
  - savedtg
  - red-team
  - pentest
  - deferred
---

# Strix — автономное AI pentesting

## Репозиторий

https://github.com/usestrix/strix

## Где в коде

- `strix/` — CLI, orchestration и agent runtime.
- `containers/` — sandbox-образы и tooling.
- `benchmarks/` — тестовые сценарии.
- `tests/` — автоматические проверки.
- `docs/` — scan modes, providers и CI/CD.

## Алгоритм

1. Принимает локальный репозиторий, Git URL или black-box target.
2. Разворачивает Docker sandbox и подключает выбранного LLM provider.
3. Специализированные агенты выполняют recon, SAST/DAST, browser- и API-тесты.
4. Потенциальные уязвимости проверяются воспроизводимым PoC.
5. CLI формирует findings и remediation/report; non-interactive режим возвращает ненулевой exit code при найденных уязвимостях.

## Сигналы качества и ограничения

- Apache-2.0, тесты, CI-mode и активная разработка.
- Сильная зависимость от модели и корректного scope; offensive actions требуют изоляции и явного разрешения.
- Независимый benchmark полноты и false-positive rate в карточке не подтверждён.

## Вердикт

**экспериментально** — практичный AI-помощник пентестера для отдельного трека, но не самостоятельный механизм hardening агентной системы.

## Связи

- Способ: [[44-red-team-regression]]
- Источник: [[source-strix]]
