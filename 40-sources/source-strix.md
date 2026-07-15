---
type: source
tags:
  - docs
  - savedtg
  - red-team
  - pentest
---

# Strix

## URL

https://github.com/usestrix/strix

## Суть

Strix — open-source AI pentesting tool для white-box и black-box тестирования приложений. Агенты выполняют recon, динамическую эксплуатацию и проверку findings через PoC, а затем формируют remediation и отчёт.

## Ключевые выводы

- Сочетает multi-agent orchestration, SAST/DAST, browser и shell tooling, exploit runtime и CI/CD режим.
- Требует Docker и LLM provider либо локальную модель; результаты зависят от модели, target и rules of engagement.
- Заявления о «real exploit validation» исходят из README; независимая сравнительная оценка не приведена.
- Инструмент относится к авторизованному pentest/red-team треку и не является runtime-барьером agent-системы.

## Связи

- [[44-red-team-regression]]
- [[impl-strix]]
