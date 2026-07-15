---
type: implementation-detail
parent-repo: repo-111-h5i
method-id: 7
repo: https://github.com/h5i-dev/h5i
language: Rust
license: Apache-2.0
verdict: экспериментально
commit-sha: c33cf7308169b95b6e68464e74b693bde7b60b9d
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# h5i — capability-scoped secrets broker

## Проверенная ревизия

`c33cf7308169b95b6e68464e74b693bde7b60b9d`, дата коммита 2026-07-15; код проверен 2026-07-15.

## Где в коде

- Код: `crates/h5i-sandbox/src/secrets_broker.rs`, `crates/h5i-sandbox/src/secrets.rs`, `crates/h5i-sandbox/src/sandbox_policy.rs`, `docs/credential-proxy-design.md`, `roadmap/secrets-broker-design.md`.
- Тесты: inline-модуль в `crates/h5i-sandbox/src/secrets_broker.rs`, включая fail-closed resolution, output caps, timeout, file mode `0600`, unlink on drop и value-free audit.

## Алгоритм

1. Pinned profile перечисляет `SecretGrant`; значения разрешаются на host только во время запуска из `env:`, `file:` или явно разрешённого `command:` source.
2. Отсутствующее, пустое, зависшее, чрезмерно длинное или завершившееся ошибкой значение останавливает весь запуск.
3. Secret инъецируется как environment variable либо временный файл вне `$WORK` с режимом `0600`; file injection разрешён только для поддерживаемого tier.
4. Точные значения добавляются в redaction set для captured output и удаляются вместе с временными файлами по завершении.
5. Audit хранит grant name, source, injection method, TTL и короткий SHA-256 fingerprint, но не значение.

## Зависимости

Rust, host environment/filesystem и SHA-256. `command:` extractor запускает host-side shell и поэтому выключен без `allow_command_extractors = true`; даже при включении действует timeout и лимит stdout 1 MiB.

## Ограничения

Механизм предотвращает запись выданных значений в policy и Git refs, но не мешает разрешённому agent process прочитать credential из своей среды. Redaction ищет точное значение и не гарантирует удаление преобразованных или частичных представлений. Короткий fingerprint раскрывает равенство секретов между запусками.

## Вердикт

**экспериментально** — самостоятельный fail-closed механизм способа №7 с сильной hygiene, но не полноценный DLP и не защита от злонамеренного разрешённого процесса.

## Связи

- Репозиторий: [[repo-111-h5i]]
