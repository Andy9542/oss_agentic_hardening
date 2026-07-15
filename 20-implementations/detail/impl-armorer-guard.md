---
type: implementation-detail
parent-repo: repo-107-armorer-guard
method-id: 1
repo: https://github.com/ArmorerLabs/Armorer-Guard
language: Rust
license: MIT
verdict: экспериментально
commit-sha: 674eb1009a56b50a54bc28163ea99e55c57f9d2a
commit-date: 2026-06-22
verified-date: 2026-07-15
tags:
  - agent-security
---

# Armorer Guard — локальный TF-IDF classifier

## Проверенная ревизия

`674eb1009a56b50a54bc28163ea99e55c57f9d2a`, дата коммита 2026-06-22; код проверен 2026-07-15.

## Где в коде

- Код: `src/main.rs`, `src/semantic_classifier_native.tsv`, `src/semantic_classifier_profile_native.tsv`, `src/dev_exemplars.tsv`, `docs/ARCHITECTURE.md`.
- Тесты: inline-модуль `tests` в `src/main.rs`; проверяются semantic categories, native model scores, profiles, JSON/JSONL contracts и context-aware policy lane.

## Алгоритм

1. Вход очищается, декодируется в нескольких представлениях и превращается в нормализованные token features.
2. Детерминированные semantic rules выявляют прямые injection, exfiltration, bypass и destructive-command patterns.
3. Rust-native word TF-IDF linear classifier рассчитывает оценки категорий по встроенным weights.
4. Production-профиль объединяет rules и word model; high-recall jailbreak profile может подключить char-wb linear fallback.
5. Итог дополняется context fields, similarity и локальной feedback overlay и возвращается как структурированный список причин и confidence.

## Зависимости

Один Rust binary со встроенными TSV weights; Python и npm packages служат обёртками и не содержат scanner logic. Основной scanner path не требует облака или сетевой модели.

## Ограничения

Линейная bag-of-features модель ограниченно понимает длинный контекст и новые перефразировки. High-recall fallback не включён в production profile по умолчанию. Публичные quality metrics и training provenance описаны авторами, но не воспроизведены независимой стороной.

## Вердикт

**экспериментально** — практичная локальная реализация способа №1, однако устойчивость к адаптивным обходам и переносимость benchmark-результатов требуют внешней проверки.

## Связи

- Репозиторий: [[repo-107-armorer-guard]]
