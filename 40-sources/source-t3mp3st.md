---
type: source
tags:
  - docs
  - savedtg
  - red-team
---

# T3MP3ST

## URL

https://github.com/elder-plinius/T3MP3ST

## Суть

T3MP3ST — self-hosted multi-agent offensive-security framework, который использует уже установленный coding agent или локальную модель как «мозг» для цепочки recon → exploit → report.

## Ключевые выводы

- Поддерживает web/CTF, white-box анализ и экспериментальные треки для cloud, mobile и binary/RE.
- Авторы публикуют fixtures и `verify-claims`, но headline-метрики остаются self-reported и требуют независимого прогона.
- Инструмент предназначен только для авторизованных целей; это test/red-team контур, а не runtime-защита.
- В основной каталог agent-hardening сейчас не включается.

## Связи

- [[44-red-team-regression]]
- [[impl-t3mp3st]]
