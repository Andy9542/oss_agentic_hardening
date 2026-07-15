---
type: implementation-detail
parent-repo: repo-16-actplane
method-id: 16
repo: https://github.com/eunomia-bpf/ActPlane
language: Rust/C
license: Apache-2.0
verdict: experimental
commit-sha: a62e5d9
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# ActPlane — eBPF information-flow control для агентов

## Репозиторий

- [eunomia-bpf/ActPlane](https://github.com/eunomia-bpf/ActPlane)
- Проверенный срез: `a62e5d9`; код проверен 2026-07-15.

## Что это за технология

**Runtime IFC (information-flow control) на eBPF/LSM**: policy DSL компилируется в `taint_config`, загружается в ядро; на syscall (`exec`/`open`/`write`/`connect`) метки (labels) распространяются между процессами/файлами/endpoints. Sink-правила `block`/`kill`/`notify` останавливают утечку секретов до commit операции. Это способ №16 на уровне ОС — не анализ AST, а живой поток данных агента.

## Где в коде

- Docs: `docs/rule-language.md`, `docs/security_model.md`, `CLAUDE.md`
- ABI: `bpf/taint.h` (`taint_rule`, `taint_match` EXACT/PREFIX/SUFFIX)
- Compiler: `actplane-ifc-compiler` (Rust)
- Engine: BPF maps `ts_proc`, hooks LSM/tracepoints

## Алгоритм

1. Написать DSL: `source SECRET = file ~/.ssh/**` + sink `block connect` если process имеет SECRET.
2. `actplane compile` → binary `taint_config`.
3. Запуск агента под `actplane --policy … run claude`.
4. На событиях: fork наследует labels; read файла-source taints process; connect к внешнему host с tainted label → block (-EPERM) / kill / notify.
5. Агент получает feedback о нарушении.

## Примеры реализации

Операции: `fork`, `exec`, `read`, `write`, `unlink`, `connect`, `recv`.

Effects: `block` (BPF-LSM deny), `kill`, `notify`.

Matchers: EXACT / PREFIX / SUFFIX / ANY на path/host/argv.

Pipeline: `policy.dsl → compiler → taint_config → eBPF → TAINT_VIOLATION`.

## Пример: вход → решение

- Процесс прочитал `~/.ssh/id_rsa` (source SECRET) → пытается `connect evil.com:443` → **block**.
- `git status` без taint → allow (если политика разрешает).

## Детерминизм или машинное обучение

**Детерминированный** kernel enforcement.

## Внешние зависимости

Linux + BPF LSM; Rust toolchain; sudo для load.

## Ограничения

- Без BPF LSM `block` unsupported.
- Сложность DSL и privilege для установки.

## Сигналы качества

- Formal rule-language doc; e2e examples E1–E12; unit tests BPF/compiler.

## Вердикт

**экспериментально** — редкий OS-level IFC harness для агентов.

## Связи

- Репозиторий: [[repo-16-actplane]]
