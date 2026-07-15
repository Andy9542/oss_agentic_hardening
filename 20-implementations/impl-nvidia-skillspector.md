---
type: implementation
method-id: 27
repo: "https://github.com/NVIDIA/SkillSpector"
language: "Python"
license: "Apache-2.0"
verdict: экспериментально
tags:
  - agent-security
  - review-2026
  - supply-chain
---

# NVIDIA SkillSpector — сканер безопасности agent skills

## Репозиторий

https://github.com/NVIDIA/SkillSpector

## Где в коде

- `src/skillspector/` — модели findings, providers и analyzer pipeline.
- `src/skillspector/models.py` — сериализация finding.
- `docs/DEVELOPMENT.md` — архитектура и расширение pipeline.
- `docs/SUPPRESSION.md` — baseline и подавление false positives.
- `contrib/batch_scan/` — пакетное сканирование.

## Алгоритм

1. Принимает Git repo, URL, ZIP, каталог или файл skill.
2. Выполняет статический анализ по 68 паттернам в 17 категориях.
3. Проверяет prompt injection, exfiltration, privilege escalation, supply chain, memory poisoning, tool misuse и MCP least privilege.
4. AST/taint/YARA анализируют код и данные; OSV lookup добавляет сведения об уязвимостях.
5. Опциональный LLM semantic evaluation рассматривает неоднозначные инструкции.
6. Формирует risk score и terminal/JSON/Markdown/SARIF отчёт; baseline выделяет только новые findings.

## Детерминизм или машинное обучение

Основной статический pipeline детерминирован. Семантическая стадия опциональна и зависит от выбранной модели; OSV может работать с offline fallback.

## Внешние зависимости

Python 3.12+. Для основной статики облако не требуется. LLM endpoint нужен только для semantic evaluation; live CVE lookup использует OSV.dev.

## Сигналы качества

- Тесты в репозитории: `make test`, coverage target, fixtures и batch scanner.
- Документированные обходы: README выделяет limitations и variability локальных/внешних моделей.
- Зрелость: официальный репозиторий NVIDIA, широкий набор правил и форматов, но проект новый и заявленные проценты риска skills требуют проверки первичного исследования.

## Вердикт

**экспериментально** — один из наиболее полных новых skill scanners; полезен уже сейчас для CI/admission, но не заменяет ручной review и runtime containment.

## Связи

- Способ: [[27-статическая-проверка-навыков-и-плагинов]]
