---
type: implementation
method-id: 44
repo: "https://github.com/elder-plinius/T3MP3ST"
language: "TypeScript"
license: "AGPL-3.0"
verdict: экспериментально
tags:
  - agent-security
  - savedtg
  - red-team
  - deferred
---

# T3MP3ST — multi-agent offensive-security harness

## Репозиторий

https://github.com/elder-plinius/T3MP3ST

## Алгоритм

1. Оператор задаёт авторизованный target через War Room или CLI.
2. Оркестратор декомпозирует миссию по фазам recon, exploitation, verification и report.
3. Coding agent, API-модель или локальная OpenAI-compatible модель планирует шаги.
4. Arsenal предоставляет специализированные offensive tools и sandboxed task paths.
5. Findings и benchmark claims сохраняются в воспроизводимых артефактах; `verify-claims` пересчитывает метрики.

## Сигналы качества и ограничения

- Есть committed benchmark data и скрипт повторного расчёта claims.
- Зрелость подсистем неодинакова: web/CTF заявлены stable, часть white-box/cloud/mobile/binary функций ограничена или остаётся scaffolding.
- Независимая проверка headline-результатов в карточке не выполнялась.
- Высокорисковый offensive tool; применять только к системам, на тестирование которых есть явное разрешение.

## Вердикт

**экспериментально** — перспективный red-team harness для отдельного pentest-трека; не включён в основной каталог защитных OSS.

## Связи

- Способ: [[44-red-team-regression]]
- Источник: [[source-t3mp3st]]
