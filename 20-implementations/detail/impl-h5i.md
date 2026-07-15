---
type: implementation-detail
parent-repo: repo-111-h5i
method-id: 33
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

# h5i — fail-closed isolation tiers

## Проверенная ревизия

`c33cf7308169b95b6e68464e74b693bde7b60b9d`, дата коммита 2026-07-15; код проверен 2026-07-15.

## Где в коде

- Код: `crates/h5i-sandbox/src/sandbox.rs`, `crates/h5i-sandbox/src/sandbox_policy.rs`, `crates/h5i-sandbox/src/container.rs`, `crates/h5i-sandbox/src/supervisor.rs`, `crates/h5i-sandbox/src/seccomp_notify.rs`, `crates/h5i-sandbox/src/cgroup.rs`, `crates/h5i-core/src/env.rs`.
- Тесты: inline-модули в `crates/h5i-sandbox/src/*.rs`, `tests/env_integration.rs`, `tests/cli_integration.rs`, `tests/sandbox_api.rs`.

## Алгоритм

1. Profile из `.h5i/env.toml` задаёт minimum isolation claim, filesystem grants/denies, network mode/egress, resources, environment и container image.
2. Host probe проверяет Landlock ABI, unprivileged user namespaces, seccomp и rootless Podman.
3. Без pinned tier runtime выбирает strongest runnable tier: container, supervised, process или workspace; несоответствие заявленному claim завершает операцию.
4. Process tier применяет Landlock allowlist, seccomp denylist, `no_new_privs`, rlimits и network namespace для deny-all; container tier добавляет rootless Podman и DNS-pinned egress proxy.
5. Resolved policy и isolation claim сохраняются в manifest и captures, а agent config paths блокируются read-only внутри kernel tiers.

## Зависимости

Linux для Landlock, seccomp и namespaces; rootless Podman и image для container tier. Git обязателен для environment worktree и provenance. Возможности hardened-container и microVM в проверенном срезе заявлены как неподдерживаемые tiers.

## Ограничения

`workspace` обеспечивает разделение Git-деревьев, но не confinement процессов. Static process tier умеет deny-all network, но не domain allowlist. Доступность Landlock/userns зависит от kernel configuration; на неподходящем host сильный claim отвергается, а auto mode может выбрать более слабый, но runnable tier.

## Вердикт

**экспериментально** — серьёзная fail-closed реализация способа №33, однако фактическая сила зависит от выбранного tier, Linux kernel и rootless container runtime.

## Связи

- Репозиторий: [[repo-111-h5i]]
