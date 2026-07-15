---
type: implementation-detail
parent-repo: repo-103-openshell
method-id: 34
repo: https://github.com/NVIDIA/OpenShell
language: Rust/Python
license: Apache-2.0
verdict: experimental
commit-sha: 392ad63
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# OpenShell — OS sandbox с YAML FS/network policy

## Репозиторий

- [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell)
- Проверенный срез: `392ad63`, дата коммита 2026-07-15; код проверен 2026-07-15.

## Что это за технология

**Agent-first OS sandbox**: агент работает в контейнере/MicroVM под gateway; доступ к файлам и сети задаётся декларативной YAML-политикой. На Linux используется **Landlock** (LSM) для ограничения FS paths. Это способ №34 — изоляция на уровне ОС, а не regex в промпте.

## Где в коде

- Пример политики: `scripts/agents/gator/policy.yaml`
- Python SDK: `python/openshell/sandbox.py`
- Gateway/Helm: `deploy/helm/openshell/`
- README quickstart: `openshell sandbox create -- claude`

## Алгоритм

1. Установить gateway + runtime (Docker/Podman/MicroVM).
2. Загрузить policy: `filesystem_policy` (read_only / read_write paths), `network_policies`, `process.run_as_user`.
3. Создать sandbox; агент исполняется внутри.
4. Landlock/compatibility `best_effort` применяет FS bounds.
5. Egress вне allowlist сети блокируется gateway policy.
6. Смена policy version отражается в `SandboxStatus.current_policy_version`.

## Примеры реализации

```yaml
# scripts/agents/gator/policy.yaml
version: 1
filesystem_policy:
  include_workdir: true
  read_only: [/usr, /lib, /proc, /dev/urandom, /app, /etc, /var/log]
  read_write: [/sandbox, /tmp, /dev/null]
landlock:
  compatibility: best_effort
process:
  run_as_user: sandbox
  run_as_group: sandbox
network_policies: {}
```

## Пример: вход → решение

- Чтение `/etc/passwd` при read_only `/etc` → allow read; запись туда → deny.
- Запись в `/sandbox/out.txt` → allow.
- Произвольный egress при пустом/строгом network policy → deny.

## Детерминизм или машинное обучение

**Детерминированный** enforcement ядра/LSM/gateway.

## Внешние зависимости

Docker/Podman или виртуализация; бинарник/PyPI `openshell`. Alpha, single-player mode.

## Ограничения

- Alpha software; k8s path experimental.
- Политика должна быть полной — дырка в read_write = побег данных.

## Сигналы качества

- NVIDIA docs; sandbox_test.py обширный.

## Вердикт

**экспериментально** — перспективный OS-слой; пока alpha.

## Связи

- Репозиторий: [[repo-103-openshell]]
